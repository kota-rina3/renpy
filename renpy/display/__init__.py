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

import renpy

import renpy.log

# The draw object through which all drawing is routed. This object
# contains all of the distinction between the software and GL
# renderers.
draw = None  # type: renpy.display.core.Renderer | None

# The interface object.
interface = None  # type: renpy.display.core.Interface | None

# Should we disable imagedissolve-type transitions?
less_imagedissolve = False

# Are we on a touchscreen?
touch = False

# The pygame.display.Info object, which we want to survive a reload.
info = None

# True if the platform can go fullscreen. (Right now, this is true for
# all platforms.)
can_fullscreen = True


def get_info():
    global info

    if info is None:
        import pygame_sdl2 as pygame

        pygame.display.init()
        info = pygame.display.Info()

    return info


# Logs we use.
log = renpy.log.open("log", developer=False, append=False)
ic_log = renpy.log.open("image_cache", developer=True, append=False)
to_log = renpy.log.open("text_overflow", developer=True, append=True)


# Generated by scripts/relative_imports.py, do not edit below this line.
import typing

if typing.TYPE_CHECKING:
    from . import accelerator as accelerator
    from . import anim as anim
    from . import behavior as behavior
    from . import controller as controller
    from . import core as core
    from . import displayable as displayable
    from . import dragdrop as dragdrop
    from . import emulator as emulator
    from . import error as error
    from . import focus as focus
    from . import gesture as gesture
    from . import im as im
    from . import image as image
    from . import imagelike as imagelike
    from . import imagemap as imagemap
    from . import joystick as joystick
    from . import layout as layout
    from . import matrix as matrix
    from . import minigame as minigame
    from . import model as model
    from . import module as module
    from . import motion as motion
    from . import movetransition as movetransition
    from . import particle as particle
    from . import pgrender as pgrender
    from . import predict as predict
    from . import presplash as presplash
    from . import quaternion as quaternion
    from . import render as render
    from . import scale as scale
    from . import scenelists as scenelists
    from . import screen as screen
    from . import swdraw as swdraw
    from . import transform as transform
    from . import transition as transition
    from . import tts as tts
    from . import video as video
    from . import viewport as viewport
