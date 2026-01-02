# Copyright 2004-2026 Tom Rothamel <pytom@bishoujo.us>
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

# Editor Support.
#
# This contains code for scanning for editors, and for allowing the user to
# select an editor.

init 1 python in editor:

    from store import Action, renpy, config, persistent
    import store.project as project
    import store.updater as updater
    import store.interface as interface
    import store.util as util
    import store

    import glob
    import re
    import traceback
    import os
    import os.path

    # Should we set up the editor?
    set_editor = "RENPY_EDIT_PY" not in os.environ

    # A map from editor name to EditorInfo object.
    editors = { }

    class EditorInfo(object):
        def __init__(self, filename):
            # The path to the editor info file.
            self.filename = filename

            # The name of the editor.
            self.name = os.path.basename(filename)[:-len(".edit.py")]

            # The time the editor file was last modified. We use this
            # to decide if we should update the editors mat when we
            # have multiple versions of an editor in contention.
            self.mtime = os.path.getmtime(filename)

    def scan_editor(filename):
        """
        Inserts an editor into editors if there isn't a newer
        editor there already.
        """

        ei = EditorInfo(filename)

        if ei.name in editors:
            if editors[ei.name].mtime >= ei.mtime:
                return

        editors[ei.name] = ei

    def scan_all():
        """
        Finds all *.edit.py files, and uses them to populate the list
        of editors.
        """

        editors.clear()

        for d in [ config.renpy_base, persistent.projects_directory ]:
            if d is None:
                continue

            if not os.path.isdir(d):
                continue

            for i in util.listdir(d):
                i = os.path.join(d, i)
                if not os.path.isdir(d):
                    continue

                for j in util.listdir(i):
                    j = os.path.join(i, j)

                    if j.endswith(".edit.py"):
                        scan_editor(j)

    ########################################################################

    # A list of fancy_editor_info objects.
    fancy_editors = [ ]

    # The error message to display if an editor failed to start.
    error_message = None

    class FancyEditorInfo(object):
        """
        Represents an editor in the selection screen. A FEI knows if the
        editor is installed or not.
        """

        def __init__(self, priority, name, description=None, dlc=None, dldescription=None, error_message=None, deprecated=False):
            # The priority of the editor. Lower priorities will come later
            # in the list.
            self.priority = priority

            # The name of the editor.
            self.name = name

            # Is the editor installed?
            self.installed = name in editors

            # The dlc needed to install the editor.
            self.dlc = dlc

            # A description of the editor.
            self.description = description

            # A description of the download.
            self.dldescription = dldescription

            # An error message to display if the editor failed to start.
            self.error_message = error_message

            # If the editor is considered deprecated for use with Ren'Py.
            self.deprecated = deprecated


    def vscode_path():
        """
        Gets the path to VS Code for this platform.
        """

        if renpy.windows:
            return os.path.join(config.renpy_base, "vscode/VSCode-win32-x64")
        elif renpy.macintosh:
            return os.path.join(config.renpy_base, "vscode/Visual Studio Code.app")
        else:
            if renpy.arch == "aarch64":
                arch = "arm64"
            else:
                arch = "x64"

            return os.path.join(config.renpy_base, "vscode/VSCode-linux-" + arch)

    def fancy_scan_editors():
        """
        Creates the list of FancyEditorInfo objects.
        """

        import platform

        global fancy_editors

        scan_all()

        fei = fancy_editors = [ ]

        # Visual Studio Code
        AD1 = _("A modern editor with many extensions including advanced Ren'Py integration.")
        AD2 = _("A modern editor with many extensions including advanced Ren'Py integration.\n{a=jump:reinstall_vscode}Upgrade Visual Studio Code to the latest version.{/a}")

        installed = os.path.exists(vscode_path())

        e = FancyEditorInfo(
            0,
            _("Visual Studio Code"),
            AD2 if installed else AD2,
            "extension:vscode",
            _("Up to 110 MB download required."),
            None)

        e.installed = e.installed and installed

        fei.append(e)


        fei.append(FancyEditorInfo(
            1,
            _("Visual Studio Code (System)"),
            _("Uses a copy of Visual Studio Code that you have installed outside of Ren'Py. It's recommended you install the language-renpy extension to add support for Ren'Py files."),
            ))

        fei.append(FancyEditorInfo(
            1,
            _("System Editor"),
            _("Invokes the editor your operating system has associated with .rpy files."),
            None))

        for k in editors:
            if k in [ "Visual Studio Code", "Visual Studio Code (System)", "System Editor", "None" ]:
                continue

            fei.append(FancyEditorInfo(
                2,
                k,
                None,
                None))

        fei.append(FancyEditorInfo(
            3,
            _("None"),
            _("Prevents Ren'Py from opening a text editor."),
            None))

        fei.sort(key=lambda e : (e.priority, e.name.lower()))

        # If we're in a linux distro or something, assume all editors work.
        if not updater.can_update():
            for i in fei:
                if i.dlc and not i.dlc.startswith("extension:") and not i.deprecated:
                    i.installed = True

    def fancy_activate_editor(default=False):
        """
        Activates the editor in persistent.editor, if it's installed.

        `default`

        """

        global error_message

        fancy_scan_editors()

        if default and not set_editor:
            renpy.editor.init()
            return

        for i in fancy_editors:

            if i.name == persistent.editor:
                if i.installed and i.name in editors:
                    ei = editors[i.name]
                    os.environ["RENPY_EDIT_PY"] = renpy.fsencode(os.path.abspath(ei.filename))
                    error_message = i.error_message
                    break

        else:
            persistent.editor = None
            os.environ.pop("RENPY_EDIT_PY", None)

        renpy.editor.init()

    def fancy_select_editor(name):
        """
        Selects the editor with the given name, installing it if it
        doesn't already exist.
        """

        for fe in fancy_editors:
            if fe.name == name:
                break
        else:
            return

        if not fe.installed:

            if fe.dlc.startswith("extension:"):
                import installer
                manifest = fe.dlc.partition(":")[2]
                renpy.invoke_in_new_context(installer.manifest, "https://www.renpy.org/extensions/{}/{}.py".format(manifest, manifest), renpy=True)
            else:
                store.add_dlc(fe.dlc)

        persistent.editor = fe.name
        fancy_activate_editor()

        return persistent.editor is not None

    # Call fancy_activate_editor on startup.
    fancy_activate_editor(True)

    class SelectEditor(Action):
        def __init__(self, name):
            self.name = name

        def get_selected(self):
            return persistent.editor == self.name

        def __call__(self):
            return fancy_select_editor(self.name)


    def check_editor():
        """
        Checks to see if an editor is set. If one isn't asks the user to
        select one.

        Returns True if the editor is set and editing can proceed, and
        False otherwise.
        """

        if not set_editor:
            return True

        if persistent.editor and persistent.editor != "None":
            return True

        return renpy.invoke_in_new_context(renpy.call_screen, "editor")

    ##########################################################################
    # Editing actions.


    class Edit(Action):
        alt = _("Edit [text].")

        def __init__(self, filename, line=None, check=False):
            """
            An action that opens the given line of the given file in a
            text editor.

            `filename`
                The filename to open.

            `line`
                The line in the file to jump to.

            `check`
                If true, we will check to see if the file exists, and gray
                out the box if it does not.
            """

            self.filename = filename
            self.line = line
            self.check = check

        def get_sensitive(self):
            if not self.check:
                return True

            fn = project.current.unelide_filename(self.filename)
            return os.path.exists(renpy.fsencode(fn))

        def __call__(self):

            if not self.get_sensitive():
                return

            if not check_editor():
                return

            fn = project.current.unelide_filename(self.filename)

            try:

                e = renpy.editor.editor

                e.begin()
                e.open(fn, line=self.line)
                e.end()

            except Exception as e:
                exception = traceback.format_exception_only(type(e), e)[-1][:-1]
                renpy.invoke_in_new_context(interface.error, _("An exception occurred while launching the text editor:\n[exception!q]"), error_message, exception=exception)

    class EditAbsolute(Action):
        def __init__(self, filename, line=None, check=False):
            """
            An action that lets us edit an absolutely-specified filename.

            `filename`
                The filename to open.

            `line`
                The line in the file to jump to.

            `check`
                If true, we will check to see if the file exists, and gray
                out the box if it does not.
            """

            self.filename = filename
            self.line = line
            self.check = check

        def get_sensitive(self):
            if not self.check:
                return True

            return os.path.exists(renpy.fsencode(self.filename))

        def __call__(self):

            if not self.get_sensitive():
                return

            if not check_editor():
                return

            try:

                e = renpy.editor.editor

                e.begin()
                e.open(self.filename, line=self.line)
                e.end()

            except Exception as e:
                exception = traceback.format_exception_only(type(e), e)[-1][:-1]
                renpy.invoke_in_new_context(interface.error, _("An exception occurred while launching the text editor:\n[exception!q]"), error_message, exception=exception)


    class EditAll(Action):
        """
        Opens all scripts that are part of the current project in a web browser.
        """

        def __init__(self):
            return

        def __call__(self):

            if not check_editor():
                return

            scripts = project.current.script_files()
            scripts = [ i for i in scripts if not i.startswith("game/tl/") ]
            scripts.sort(key=lambda fn : fn.lower())

            for fn in [ "game/screens.rpy", "game/options.rpy", "game/script.rpy" ]:
                if fn in scripts:
                    scripts.remove(fn)
                    scripts.insert(0, fn)

            try:

                e = renpy.editor.editor
                e.begin()

                for fn in scripts:
                    fn = project.current.unelide_filename(fn)
                    e.open(fn)

                e.end()

            except Exception as e:
                exception = traceback.format_exception_only(type(e), e)[-1][:-1]
                renpy.invoke_in_new_context(interface.error, _("An exception occurred while launching the text editor:\n[exception!q]"), error_message, exception=exception)


    class EditProject(Action):
        """
        Opens the project's base directory in an editor.
        """

        def __call__(self):

            if not check_editor():
                return

            try:

                e = renpy.editor.editor

                e.begin()
                e.open_project(project.current.path)
                e.end()

            except Exception as e:
                exception = traceback.format_exception_only(type(e), e)[-1][:-1]
                renpy.invoke_in_new_context(interface.error, _("An exception occurred while launching the text editor:\n[exception!q]"), error_message, exception=exception)


    def CanEditProject():
        """
        Returns True if EditProject can be used.
        """

        try:
            e = renpy.editor.editor
            return e.has_projects
        except Exception:
            return False


    def check_old_vscode_extension():
        """
        Check to see if the old version of the Ren'Py vscode extension is installed.
        """

        extensions = os.path.join(vscode_path(), "data", "extensions")

        if not os.path.isdir(extensions):
            return False

        for i in util.listdir(extensions):
            if i.lower().startswith("renpy.language-renpy-"):
                return False

        for i in util.listdir(extensions):
            if i.lower().startswith("luquedaniel.languague-renpy-"):
                return True

        return False


screen editor:

    frame:
        style_group "l"
        style "l_root"

        window:

            has vbox

            label _("Select Editor")

            add HALF_SPACER

            hbox:
                frame:
                    style "l_indent"
                    xfill True

                    viewport:
                        scrollbars "vertical"
                        mousewheel True

                        has vbox

                        text _("A text editor is the program you'll use to edit Ren'Py script files. Here, you can select the editor Ren'Py will use. If not already present, the editor will be automatically downloaded and installed.") style "l_small_text"

                        for fe in editor.fancy_editors:

                            if fe.deprecated and not fe.installed:
                                continue

                            add SPACER

                            textbutton fe.name action editor.SelectEditor(fe.name)

                            add HALF_SPACER

                            frame:
                                style "l_indent"
                                has vbox

                                if fe.description:
                                    text fe.description:
                                        style "l_small_text"
                                        if fe.deprecated:
                                            color ERROR_COLOR

                                if not fe.installed:
                                    add HALF_SPACER
                                    text fe.dldescription style "l_small_text"


    textbutton _("Cancel") action Return(False) style "l_left_button"

label reinstall_vscode:
    python hide:
        manifest = "vscode"
        renpy.invoke_in_new_context(installer.manifest, "https://www.renpy.org/extensions/{}/{}.py".format(manifest, manifest), renpy=True)

    jump editor_preference

label upgrade_vscode_extension:
    python hide:
        manifest = "vscode"
        renpy.invoke_in_new_context(installer.manifest, "https://www.renpy.org/extensions/vscode/upgrade_extension.py", renpy=True)

    jump post_extension_check

label editor_preference:
    call screen editor
    jump preferences

default persistent.ignore_obsolete_editor = set()

# This label is called when the launcher starts, to check if the editor
# is obsolete, and let them change it.
label editor_check:

    if persistent.editor in persistent.ignore_obsolete_editor:
        jump post_editor_check


label post_extension_check:
    jump post_editor_check
