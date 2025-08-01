﻿# Copyright 2004-2025 Tom Rothamel <pytom@bishoujo.us>
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

init python:
    import platform
    pc_os=platform.system() + " " + platform.release()
    arch=platform.machine()

screen about:

    $ version = renpy.version()

    frame:
        style_group "l"
        style "l_root"

        window:
            xfill True

            has vbox xfill True

            add "images/logo.png" xalign 0.5 yoffset -5

            null height 15

            text _("[version!q]") xalign 0.5 bold True
            text _("OS: [pc_os]") xalign 0.5 bold False
            text _("CPU Architecture: [arch]") xalign 0.5 bold False

            null height 20

            textbutton _("View license") action interface.OpenLicense() xalign 0.5

    textbutton _("Return") action Jump("front_page") style "l_left_button"

label about:
    call screen about

