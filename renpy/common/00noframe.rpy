# remove_titlebar.rpy
init -999 python:
    def noframewindow():

        if renpy.windows:
            import ctypes, pygame, time
            from threading import Thread, Event
            from ctypes import wintypes

            # ---------- Windows 常量 ----------
            WS_CAPTION       = 0x00C00000
            WS_SYSMENU       = 0x00080000
            WS_THICKFRAME    = 0x00040000
            WS_MINIMIZEBOX   = 0x00020000
            WS_MAXIMIZEBOX   = 0x00010000
            #WS_OVERLAPPEDWINDOW = WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX
            GWL_STYLE = -16
            SWP_FRAMECHANGED = 0x0020
            SWP_NOMOVE = 0x0002
            SWP_NOSIZE = 0x0001
            SWP_NOZORDER = 0x0004

            user32 = ctypes.windll.user32

            def get_hwnd_by_title():
                # 获取当前 Ren'Py 窗口标题（通过 config 或默认）
                import renpy.config
                target_title = renpy.config.name
                # 若标题为空，尝试使用项目名称
                if not target_title:
                    try:
                        target_title = renpy.config.name
                    except:
                        pass

                # 枚举窗口回调
                found_hwnd = None
                def enum_windows_proc(hwnd, lParam):
                    nonlocal found_hwnd
                    length = user32.GetWindowTextLengthW(hwnd)
                    if length > 0:
                        buffer = ctypes.create_unicode_buffer(length + 1)
                        user32.GetWindowTextW(hwnd, buffer, length + 1)
                        if target_title in buffer.value:
                            found_hwnd = hwnd
                            return False  # 停止枚举
                    return True

                EnumWindows = user32.EnumWindows
                EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
                proc = EnumWindowsProc(enum_windows_proc)
                user32.EnumWindows(proc, 0)

                return found_hwnd

            # ---------- 统一获取句柄（自动降级）----------
            def get_hwnd():
                return get_hwnd_by_title()

            # ---------- 移除标题栏核心函数 ----------
            def remove_titlebar_impl(hwnd):
                try:
                    style = user32.GetWindowLongW(hwnd, GWL_STYLE)
                    old_style = style
                    style = style & ~(WS_SYSMENU | WS_CAPTION | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX )
                    user32.SetWindowLongW(hwnd, GWL_STYLE, style)
                    user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0,
                        SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED)
                    # 验证
                    new_style = user32.GetWindowLongW(hwnd, GWL_STYLE)
                    if (new_style & WS_CAPTION) == 0:
                        return True
                    else:
                        return False
                except Exception as e:
                    return False

            # ---------- 带重试的任务（保证最终成功）----------
            def retry_remove_titlebar(attempts=20, interval=0.3):
                for i in range(attempts):
                    if Event().is_set():
                        return
                    hwnd = get_hwnd()
                    if hwnd:
                        remove_titlebar_impl(hwnd)
                    time.sleep(interval)
                renpy.notify("无法去除标题栏，请检查窗口标题")

            # ---------- 启动重试线程 ----------
            Thread(target=retry_remove_titlebar, daemon=True).start()


    if renpy.config.borderless_window:
        if renpy.windows:
            noframewindow()