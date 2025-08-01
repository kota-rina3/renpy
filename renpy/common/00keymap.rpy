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

init -1600 python:

    class _keymap_list(_list):

        def remove(self, a):
            try:
                _list.remove(self, a)
            except ValueError:
                if config.developer:
                    raise
                pass


    config.keymap = dict(

        # Bindings present almost everywhere, unless explicitly
        # disabled.
        rollback = [ 'anyrepeat_K_PAGEUP', 'anyrepeat_KP_PAGEUP', 'K_AC_BACK'],
        screenshot = [ 'K_s' ],
        toggle_afm = [ ],
        toggle_fullscreen = [ 'K_F11', 'noshift_K_f' ],
        game_menu = [ 'K_MENU', 'K_PAUSE','K_ESCAPE' ],
        hide_windows = [ 'mouseup_3', 'noshift_K_h','K_ESCAPE' ],
        launch_editor = [ ],
        dump_styles = [ ],
        reload_game = [ 'shift_K_r' ],
        inspector = [ 'alt_noshift_K_i', 'shift_K_i' ],
        full_inspector = [ 'alt_shift_K_i' ],
        developer = [ 'shift_K_d' ],
        quit = ['K_q' ],
        iconify = [ 'K_END' ],
        help = [ ],
        choose_renderer = ['alt_K_g', 'shift_K_g' ],
        progress_screen = [ 'alt_shift_K_p', 'meta_shift_K_p' ],
        bubble_editor = [ 'alt_K_b', 'shift_K_b' ],

        # Accessibility.
        accessibility = [ 'shift_K_a' ],
        self_voicing = [ 'alt_K_v', 'K_v' ],
        clipboard_voicing = [ 'alt_shift_K_c', 'shift_K_c' ],
        debug_voicing = [ 'alt_shift_K_v', 'meta_shift_K_v' ],
        extra_voicing = [ '?' ],

        # Say.
        rollforward = [ 'anyrepeat_K_PAGEDOWN', 'anyrepeat_KP_PAGEDOWN', 'mousedown_5' ],
        dismiss = [ 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1' , 'mousedown_5'],
        dismiss_unfocused = [ ],

        # Pause.
        dismiss_hard_pause = [ ],

        # Focus.
        focus_left = [ 'anyrepeat_K_LEFT', 'anyrepeat_KP_LEFT' ],
        focus_right = [ 'anyrepeat_K_RIGHT', 'anyrepeat_KP_RIGHT' ],
        focus_up = [ 'anyrepeat_K_UP', 'anyrepeat_KP_UP' ],
        focus_down = [ 'anyrepeat_K_DOWN', 'anyrepeat_KP_DOWN' ],

        # Button.
        button_ignore = [ 'mousedown_1' ],
        button_select = [ 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1',  ],
        button_alternate = [ 'mouseup_3' ],
        button_alternate_ignore = [ 'mousedown_3' ],

        # Input.
        input_backspace = [ 'anyrepeat_K_BACKSPACE' ],
        input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
        input_next_line = [ 'shift_K_RETURN', 'shift_K_KP_ENTER' ],
        input_left = [ 'anyrepeat_K_LEFT', 'anyrepeat_KP_LEFT' ],
        input_right = [ 'anyrepeat_K_RIGHT', 'anyrepeat_KP_RIGHT' ],
        input_up = [ 'anyrepeat_K_UP', 'anyrepeat_KP_UP' ],
        input_down = [ 'anyrepeat_K_DOWN', 'anyrepeat_KP_DOWN' ],
        input_delete = [ 'anyrepeat_K_DELETE', 'anyrepeat_KP_DELETE' ],
        input_home = [ 'K_HOME', 'KP_HOME', 'meta_K_LEFT' ],
        input_end = [ 'K_END', 'KP_END', 'meta_K_RIGHT' ],
        input_copy = [ 'ctrl_noshift_K_INSERT', 'ctrl_noshift_K_c', 'meta_noshift_K_c' ],
        input_paste = [ 'shift_K_INSERT', 'ctrl_noshift_K_v', 'meta_noshift_K_v' ],
        input_jump_word_left = [ 'osctrl_K_LEFT', 'osctrl_KP_LEFT' ],
        input_jump_word_right = [ 'osctrl_K_RIGHT', 'osctrl_KP_RIGHT' ],
        input_delete_word = [ 'osctrl_K_BACKSPACE' ],
        input_delete_full = [ 'meta_K_BACKSPACE' ],

        # Viewport.
        viewport_leftarrow = [ 'anyrepeat_K_LEFT', 'anyrepeat_KP_LEFT' ],
        viewport_rightarrow = [ 'anyrepeat_K_RIGHT', 'anyrepeat_KP_RIGHT' ],
        viewport_uparrow = [ 'anyrepeat_K_UP', 'anyrepeat_KP_UP' ],
        viewport_downarrow = [ 'anyrepeat_K_DOWN', 'anyrepeat_KP_DOWN' ],
        viewport_wheelup = [ 'mousedown_4' ],
        viewport_wheeldown = [ 'mousedown_5' ],
        viewport_drag_start = [ 'mousedown_1' ],
        viewport_drag_end = [ 'mouseup_1' ],
        viewport_pageup = [ 'anyrepeat_K_PAGEUP', 'anyrepeat_KP_PAGEUP'],
        viewport_pagedown = [ 'anyrepeat_K_PAGEDOWN', 'anyrepeat_KP_PAGEDOWN' ],

        # These keys control skipping.
        skip = [ 'anymod_K_LCTRL', 'anymod_K_RCTRL' ],
        stop_skipping = [ ],
        toggle_skip = [ 'K_TAB' ],
        fast_skip = [ '>', 'shift_K_PERIOD' ],

        # Bar.
        bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
        bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
        bar_left = [ 'anyrepeat_K_LEFT', 'anyrepeat_KP_LEFT' ],
        bar_right = [ 'anyrepeat_K_RIGHT', 'anyrepeat_KP_RIGHT' ],
        bar_up = [ 'anyrepeat_K_UP', 'anyrepeat_KP_UP' ],
        bar_down = [ 'anyrepeat_K_DOWN', 'anyrepeat_KP_DOWN' ],

        # Delete a save.
        save_delete = [ 'K_DELETE', 'KP_DELETE' ],

        # Save/load screen pagination.
        save_page_prev = ['mousedown_4'],
        save_page_next = ['mousedown_5'],

        # Draggable.
        drag_activate = [ 'mousedown_1' ],
        drag_deactivate = [ 'mouseup_1' ],

        # Debug console.
        console = [ 'shift_K_o' ],
        console_exit = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3' ],
        console_older = [ 'anyrepeat_K_UP', 'anyrepeat_KP_UP' ],
        console_newer = [ 'anyrepeat_K_DOWN', 'anyrepeat_KP_DOWN' ],

        # Director
        director = [ 'noshift_K_d' ],

        # Ignored (kept for backwards compatibility).
        toggle_music = [ ],
        viewport_up = [ ],
        viewport_down = [ ],

        # Profile commands.
        performance = [ 'K_F3' ],
        image_load_log = [ 'K_F1' ],
        profile_once = [ 'K_F8' ],
        memory_profile = [ 'K_F7' ],
    )

    config.default_keymap = { k : _list(v) for k, v in config.keymap.items() }
    config.keymap = { k : _keymap_list(v) for k, v in config.keymap.items() }

    config.pad_bindings = {
        "pad_leftshoulder_press" : [ "rollback", ],
        "pad_lefttrigger_pos" : [ "rollback", ],
        "pad_back_press" : [ "rollback", ],

        "repeat_pad_leftshoulder_press" : [ "rollback", ],
        "repeat_pad_lefttrigger_pos" : [ "rollback", ],
        "repeat_pad_back_press" : [ "rollback", ],

        "pad_guide_press" : [ "game_menu", ],
        "pad_start_press" : [ "game_menu", ],

        "pad_y_press" : [ "hide_windows", ],
        "pad_x_press" : [ "button_alternate" ],

        "pad_rightshoulder_press" : [ "rollforward", ],
        "repeat_pad_rightshoulder_press" : [ "rollforward", ],

        "pad_righttrigger_pos" : [ "dismiss", "button_select", "bar_activate", "bar_deactivate" ],
        "pad_a_press" : [ "dismiss", "button_select", "bar_activate", "bar_deactivate"],
        "pad_b_press" : [ "game_menu" ],

        "pad_dpleft_press" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
        "pad_leftx_neg" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
        "pad_rightx_neg" : [ "focus_left", "bar_left", "viewport_leftarrow" ],

        "pad_dpright_press" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
        "pad_leftx_pos" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
        "pad_rightx_pos" : [ "focus_right", "bar_right", "viewport_rightarrow" ],

        "pad_dpup_press" : [ "focus_up", "bar_up", "viewport_uparrow" ],
        "pad_lefty_neg" : [ "focus_up", "bar_up", "viewport_uparrow" ],
        "pad_righty_neg" : [ "focus_up", "bar_up", "viewport_uparrow" ],

        "pad_dpdown_press" : [ "focus_down", "bar_down", "viewport_downarrow" ],
        "pad_lefty_pos" : [ "focus_down", "bar_down", "viewport_downarrow" ],
        "pad_righty_pos" : [ "focus_down", "bar_down", "viewport_downarrow" ],

        "repeat_pad_dpleft_press" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
        "repeat_pad_leftx_neg" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
        "repeat_pad_rightx_neg" : [ "focus_left", "bar_left", "viewport_leftarrow" ],

        "repeat_pad_dpright_press" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
        "repeat_pad_leftx_pos" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
        "repeat_pad_rightx_pos" : [ "focus_right", "bar_right", "viewport_rightarrow" ],

        "repeat_pad_dpup_press" : [ "focus_up", "bar_up", "viewport_uparrow" ],
        "repeat_pad_lefty_neg" : [ "focus_up", "bar_up", "viewport_uparrow" ],
        "repeat_pad_righty_neg" : [ "focus_up", "bar_up", "viewport_uparrow" ],

        "repeat_pad_dpdown_press" : [ "focus_down", "bar_down", "viewport_downarrow" ],
        "repeat_pad_lefty_pos" : [ "focus_down", "bar_down", "viewport_downarrow" ],
        "repeat_pad_righty_pos" : [ "focus_down", "bar_down", "viewport_downarrow" ],
    }

    # Should we use the autoreload system?
    config.autoreload = True

init -1600 python:

    # Are the windows currently hidden?
    _windows_hidden = False

    def _keymap_toggle_afm():
        if renpy.context()._menu:
            return

        renpy.run(Preference("auto-forward", "toggle"))

    def _toggle_skipping():

        if not renpy.config.allow_skipping:
            return

        if not renpy.store._skipping:
            return

        if not config.skipping:
            config.skipping = "slow"
        else:
            config.skipping = None

        if renpy.context()._menu:
            renpy.jump("_noisy_return")
        else:
            renpy.restart_interaction()

    toggle_skipping = _toggle_skipping

    def _keymap_toggle_skipping():
        if renpy.context()._menu:
            return

        _toggle_skipping()

    config.help = None

    config.help_screen = "help"

    def _help(help=None):

        if help is None:
            help = config.help

        if help is None:
            if config.help_screen and renpy.has_screen(config.help_screen):
                renpy.run(ShowMenu(config.help_screen))

            return

        if renpy.has_label(help):
            renpy.call_in_new_context(help)
            return

        try:
            import os

            if help.startswith('http://') or help.startswith('https://'):
                renpy.open_url(help)
                return

            file_path = os.path.join(config.basedir, help)
            if not os.path.isfile(file_path):
                return

            renpy.open_url("file:///" + file_path)
        except Exception:
            pass

    config.screenshot_pattern = os.environ.get("RENPY_SCREENSHOT_PATTERN", "screenshot%04d.png")

    # Called to make a screenshot happen.
    def _screenshot_core():
        import os.path
        import os

        dest = config.renpy_base

        if renpy.macapp:
            dest = os.path.expanduser("~/Desktop")

        pattern = renpy.store._screenshot_pattern or config.screenshot_pattern

        # Try to pick a filename.
        i = 1
        while True:
            fn = os.path.join(dest, pattern % i)
            if not os.path.exists(fn):
                break
            i += 1

        try:
            dn = os.path.dirname(fn)
            if not os.path.exists(dn):
                os.makedirs(dn)
        except Exception:
            pass


        try:
            if not renpy.screenshot(fn):
                renpy.notify(__("Failed to save screenshot as %s.") % fn)
                return
        except Exception:
            import traceback
            traceback.print_exc()
            renpy.notify(__("Failed to save screenshot as %s.") % fn)
            return

        if config.screenshot_callback is not None:
            config.screenshot_callback(fn)

    config.pre_screenshot_actions = [ ]


    def _screenshot():
        renpy.run(config.pre_screenshot_actions)
        renpy.invoke_in_main_thread(_screenshot_core)
        renpy.restart_interaction()


    def _screenshot_callback(fn):
        renpy.notify(__("Saved screenshot as %s.") % fn)

    config.screenshot_callback = _screenshot_callback


    def _fast_skip():
        if not config.fast_skipping and not config.developer:
            return

        Skip(fast=True, confirm=not config.developer)()

    def _reload_game():
        if not config.developer:
            return

        if not config.autoreload:
            renpy.exports.reload_script()
            return

        if renpy.get_autoreload():
            renpy.set_autoreload(False)
            renpy.restart_interaction()
        else:
            renpy.set_autoreload(True)
            renpy.exports.reload_script()

    def _launch_editor():
        if not config.developer:
            return

        filename, line = renpy.get_filename_line()
        renpy.launch_editor([ filename ], line)

    def _developer():

        if not config.developer:
            return

        renpy.show_screen("_developer")
        renpy.restart_interaction()

    def _profile_once():

        if not config.profile:
            config.profile_time = 10.0
            config.profile = True

        renpy.display.interface.profile_once = True

    def _memory_profile():
        import os

        if not renpy.experimental:
            return

        renpy.memory.diff_memory()

    def _progress_screen():
        if renpy.context_nesting_level():
            return

        if renpy.get_screen("_progress"):
            renpy.hide_screen("_progress")
        else:
            renpy.show_screen("_progress")

        renpy.restart_interaction()

screen _progress:
    layer config.interface_layer

    $ new = renpy.count_newly_seen_dialogue_blocks()
    $ seen = renpy.count_seen_dialogue_blocks()
    $ total = renpy.count_dialogue_blocks()

    drag:
        draggable True
        focus_mask None
        xpos 0
        ypos 0

        text "[new] [seen]/[total]":
            size gui._scale(18)
            color "#fff"
            outlines [ (1, "#000", 0, 0) ]
            alt ""

init -1100 python:

    # The default keymap.
    _default_keymap = renpy.Keymap(
        rollback = renpy.rollback,
        screenshot = _screenshot,
        toggle_fullscreen = renpy.toggle_fullscreen,
        toggle_afm = _keymap_toggle_afm,
        toggle_skip = _keymap_toggle_skipping,
        fast_skip = _fast_skip,
        game_menu = _invoke_game_menu,
        hide_windows = renpy.curried_call_in_new_context("_hide_windows"),
        launch_editor = _launch_editor,
        reload_game = _reload_game,
        developer = _developer,
        quit = renpy.quit_event,
        iconify = renpy.iconify,
        help = _help,
        choose_renderer = renpy.curried_call_in_new_context("_choose_renderer"),
        console = _console.enter,
        profile_once = _profile_once,
        memory_profile = _memory_profile,
        self_voicing = Preference("self voicing", "toggle"),
        clipboard_voicing = Preference("clipboard voicing", "toggle"),
        debug_voicing = Preference("debug voicing", "toggle"),
        extra_voicing = renpy.exports.speak_extra_alt,
        progress_screen = _progress_screen,
        director = director.Start(),
        performance = ToggleScreen("_performance"),
        accessibility = ToggleScreen("_accessibility"),
        bubble_editor = bubble.ToggleShown(),
        )

    config.underlay = [ _default_keymap ]

    config.pre_screenshot_actions = [ Hide("notify", immediately=True) ]


init 1100 python hide:

    import os

    if "RENPY_DEFAULT_KEYMAP" in os.environ:
        renpy.config.keymap = renpy.config.default_keymap
        config.underlay.insert(0, _default_keymap)


label _hide_windows:

    if renpy.context()._menu:
        return

    if _windows_hidden:
        return

    if renpy.has_label("hide_windows"):
        call hide_windows
        if _return:
            return

    python:
        _windows_hidden = True
        voice_sustain()
        ui.saybehavior(dismiss=['dismiss', 'hide_windows'])
        ui.interact(suppress_overlay=True, suppress_window=True)
        _windows_hidden = False

    return


label _save_reload_game:
    python hide:

        renpy.music.stop()

        if renpy.session.get("_reload_slot", None) and renpy.can_load(renpy.session["_reload_slot"]):
            renpy.utter_restart()

        if (renpy.game.log is None) or (renpy.game.log.current is None):
            renpy.utter_restart()

        renpy.session["_reload_slot"] = "_reload-1"

        import time
        renpy.session["_reload_time"] = time.time()

        renpy.take_screenshot((config.thumbnail_width, config.thumbnail_height))

        for i in config.bottom_layers + config.layers + config.top_layers:
            renpy.scene(layer=i)

        ui.add(Solid((0, 0, 0, 255)))
        ui.text("Saving game...",
                size=32, xalign=0.5, yalign=0.5, color="#fff", style="_text")

        ui.pausebehavior(0)
        ui.interact(suppress_overlay=True, suppress_underlay=True)

        renpy.save("_reload-1", "reload save game")

        ui.add(Solid((0, 0, 0, 255)))
        ui.text("Reloading script...",
                size=32, xalign=0.5, yalign=0.5, color="#fff", style="_text")

        ui.pausebehavior(0)
        ui.interact(suppress_overlay=True, suppress_underlay=True)

        renpy.utter_restart()

label _load_reload_game:

    if not renpy.session.get("_reload_slot", None):
        return

    if not renpy.can_load(renpy.session["_reload_slot"]):
        $ del renpy.session["_reload_slot"]
        return

    python hide:

        try:

            for i in config.bottom_layers + config.layers + config.top_layers:
                renpy.scene(layer=i)

            ui.add(Solid((0, 0, 0, 255)))
            ui.text("Reloading game...",
                    size=32, xalign=0.5, yalign=0.5, color="#fff", style="_text")

            ui.pausebehavior(0)
            ui.interact(suppress_underlay=True, suppress_overlay=True)

            renpy.load(renpy.session["_reload_slot"])

        except (renpy.game.RestartTopContext, renpy.game.RestartContext):

            renpy.rename_save(renpy.session["_reload_slot"], "_reload-2")
            del renpy.session["_reload_slot"]
            raise


    return
