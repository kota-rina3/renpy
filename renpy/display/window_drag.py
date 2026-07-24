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

import time,
import renpy.pygame as pygame


class WindowDragManager:
    """
    Manages long-press-to-drag for borderless windows.

    When the left mouse button is held down for `threshold` seconds (default
    0.3s) without being released, subsequent mouse movement moves the window
    instead of being delivered to the game as normal mouse events.

    Short clicks (press and release within the threshold) pass through to the
    game normally, so interactive elements like buttons continue to work.
    """

    def __init__(self, threshold=0.3):
        """
        `threshold` is the number of seconds the left button must be held
        before dragging begins.
        """
        self.threshold = threshold
        self.reset()

    def reset(self):
        """Reset all drag state to idle."""
        self.state = 'idle'            # 'idle', 'holding', 'dragging'
        self.hold_start_time = 0.0
        self.drag_start_win_pos = (0, 0)
        self.drag_start_mouse_pos = (0, 0)
        self.drag_start_screen_pos = (0, 0)
        self.dpi_scale_x = 1.0
        self.dpi_scale_y = 1.0

    def handle_event(self, ev, window):
        """
        Process a mouse event for potential window dragging.

        `ev` is a raw pygame event (with unscaled screen coordinates).
        `window` is the pygame display Window object, or None.

        Returns True if the event was consumed (should *not* be dispatched
        to the game), False otherwise.
        """

        if window is None:
            self.reset()
            return False

        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            self.state = 'holding'
            self.hold_start_time = time.time()
            return False

        elif ev.type == pygame.MOUSEMOTION and self.state == 'holding':
            if time.time() - self.hold_start_time >= self.threshold:
                self.state = 'dragging'
                self.drag_start_win_pos = window.get_position()

                # 计算 DPI 缩放系数（不变）
                pw, ph = window.get_drawable_size()
                sw, sh = window.get_size()
                self.dpi_scale_x = pw / sw if sw > 0 else 1.0
                self.dpi_scale_y = ph / sh if sh > 0 else 1.0

                # 记录鼠标屏幕绝对位置（物理像素）
                win_x, win_y = self.drag_start_win_pos
                mouse_rel_x, mouse_rel_y = ev.pos  # 逻辑坐标
                self.drag_start_screen_pos = (
                    win_x + mouse_rel_x * self.dpi_scale_x,
                    win_y + mouse_rel_y * self.dpi_scale_y
                )

                return True   # 消费本次事件
            return False

        elif ev.type == pygame.MOUSEMOTION and self.state == 'dragging':
            # 计算当前鼠标屏幕绝对位置
            win_x, win_y = window.get_position()
            mouse_rel_x, mouse_rel_y = ev.pos
            current_screen_pos = (
                win_x + mouse_rel_x * self.dpi_scale_x,
                win_y + mouse_rel_y * self.dpi_scale_y
            )

            # 计算位移
            dx = current_screen_pos[0] - self.drag_start_screen_pos[0]
            dy = current_screen_pos[1] - self.drag_start_screen_pos[1]

            new_x = self.drag_start_win_pos[0] + dx
            new_y = self.drag_start_win_pos[1] + dy
            try:
                window.set_position((new_x, new_y))
            except Exception:
                pass
            return True

        elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
            was_dragging = self.state == 'dragging'
            self.state = 'idle'
            if was_dragging:
                return True   # consume the button-up after drag
            return False      # normal click, let it through

        return False
