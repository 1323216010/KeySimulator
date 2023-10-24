import win32gui

def print_window_title(hwnd, extra):
    title = win32gui.GetWindowText(hwnd)
    if title:
        print(title)