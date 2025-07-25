# Copyright 2004-2025 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This module handles the logging of messages to a file.

from __future__ import division, absolute_import, with_statement, print_function, unicode_literals
from renpy.compat import PY2, basestring, bchr, bord, chr, open, pystr, range, round, str, tobytes, unicode  # type: ignore


import os
import traceback
import platform
import time
import tempfile
import sys
import io
import re

import encodings.latin_1  # @UnusedImport

import renpy

real_stdout = sys.stdout
real_stderr = sys.stderr

# The file events are logged to.
log_file = None


class LogFile(object):
    """
    This manages one of our logfiles.
    """

    def __init__(self, name, append=False, developer=False, flush=True):
        """
        `name`
            The name of the logfile, without the .txt extension.
        `append`
            If true, we will append to the logfile. If false, we will truncate
            it to an empty file the first time we write to it.
        `developer`
            If true, nothing happens if config.developer is not set to True.
        `flush`
            Determines if the file is flushed after each write.
        """

        self.name = name
        self.append = append
        self.developer = developer
        self.flush = flush
        self.file = None

        # File-like attributes.
        self.softspace = 0
        self.newlines = None

        # Should we emulate file's write method? We do so if this is True.
        self.raw_write = False

        if renpy.ios:
            self.file = real_stdout

    def open(self):  # @ReservedAssignment
        if renpy.config.log_to_stdout:
            self.file = real_stdout
            return True

        if self.file:
            return True

        if self.file is False:
            return False

        if renpy.macapp:
            return False

        if self.developer and not renpy.config.developer:
            return False

        if not renpy.config.log_enable:
            return False

        if renpy.config.logdir is None:
            return

        try:
            base = os.environ.get("RENPY_LOG_BASE", renpy.config.logdir)

            if base is None:
                return False

            fn = os.path.join(base, self.name + ".txt")

            altfn = os.path.join(tempfile.gettempdir(), "renpy-" + self.name + ".txt")

            if self.append:
                mode = "a"
            else:
                mode = "w"

            try:
                self.file = io.open(fn, mode, encoding="utf-8")

                try:
                    renpy.util.expose_file(fn)
                except Exception:
                    pass
            except Exception:
                self.file = io.open(altfn, mode, encoding="utf-8")
                try:
                    renpy.util.expose_file(altfn)
                except Exception:
                    pass

            if self.append:
                self.write("")
                self.write("=" * 78)
                self.write("")

            self.write("%s UTC", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
            try:
                self.write("%s", platform.platform())
            except Exception:
                self.write("Unknown platform.")
            self.write("%s", renpy.version)
            self.write("")

            if "name" in renpy.game.build_info:
                self.write("%s", renpy.game.build_info["name"])
                self.write("%s", renpy.game.build_info["version"])
                self.write(
                    "Built at %s UTC", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(renpy.game.build_info["time"]))
                )
                self.write("")

            return True

        except Exception:
            self.file = False
            traceback.print_exc(file=real_stderr)
            return False

    def write(self, s, *args):
        """
        Formats `s` with args, and writes it to the logfile.
        """

        if self.open():
            if not isinstance(s, str):
                s = s.decode("latin-1")

            if not self.raw_write:
                try:
                    s = s % args
                    s = re.sub(r"\x1b[^a-zA-Z]*[a-zA-Z]", "", s)
                except Exception:
                    s = repr((s,) + args)

                s += "\n"

            self.file.write(s)  # type: ignore

            if self.flush:
                try:
                    self.file.flush()  # type: ignore
                except Exception:
                    self.flush = False

    def exception(self):
        """
        Writes the exception to the logfile.
        """

        self.raw_write = True
        traceback.print_exc(None, self)  # type: ignore
        self.raw_write = False


# A map from the log name to a log object.
log_cache = {}


def open(name, append=False, developer=False, flush=False):  # @ReservedAssignment
    rv = log_cache.get(name, None)

    if rv is None:
        rv = LogFile(name, append=append, developer=developer, flush=flush)
        log_cache[name] = rv

    return rv


################################################################################
# Timed event log.


class TimeLog(list):
    """
    This represents a log that is limited to the last `duration` seconds.
    """

    def __init__(self, duration):
        self.duration = duration

    def append(self, v):
        now = time.time()

        list.append(self, (now, v))
        self.prune(now)

    def prune(self, now=None):
        if now is None:
            now = time.time()

        while self[0][0] < (now - self.duration):
            self.pop(0)


################################################################################
# Stdout / Stderr Redirection


class StdioRedirector(object):
    real_file = sys.stderr

    def __init__(self):
        self.buffer = ""
        self.log = open("log", developer=False, append=False, flush=True)
        self.encoding = "utf-8"

    def write(self, s):
        if not isinstance(s, str):
            s = str(s, "utf-8", "replace")

        if not renpy.config.log_to_stdout:
            self.real_file.write(s)
            self.real_file.flush()

        if renpy.ios:
            return

        s = self.buffer + s

        lines = s.split("\n")

        try:
            callbacks = self.get_callbacks()
        except Exception:
            callbacks = []

        for l in lines[:-1]:
            self.log.write("%s", l)

            for i in callbacks:
                try:
                    i(l)
                except Exception:
                    pass

        self.buffer = lines[-1]

    def fileno(self):
        return self.real_file.fileno()

    def isatty(self):
        return self.real_file.isatty()

    def writelines(self, lines):
        for i in lines:
            self.write(i)

    def flush(self):
        try:
            self.real_file.flush()
        except Exception:
            pass

    def close(self):
        pass

    def get_callbacks(self):
        return []


if not "RENPY_NO_REDIRECT_STDIO" in os.environ:

    class StdoutRedirector(StdioRedirector):
        real_file = real_stdout

        def get_callbacks(self):
            return renpy.config.stdout_callbacks

    sys.stdout = sys_stdout = StdoutRedirector()

    class StderrRedirector(StdioRedirector):
        real_file = real_stderr

        def get_callbacks(self):
            return renpy.config.stderr_callbacks

    sys.stderr = sys_stderr = StderrRedirector()

else:
    sys_stdout = sys.stdout
    sys_stderr = sys.stderr


def post_init():
    sys.stdout = sys_stdout
    sys.stderr = sys_stderr
