import curses
import sys
from utils import clear

def nhap_mat_khau(stdscr, show=False):
    curses.curs_set(1)
    mat_khau = ""
    stdscr.clear()
    stdscr.addstr(1, 2, "🔐 Nhập mật khẩu (ấn F2 để ẩn/hiện):")
    stdscr.refresh()

    while True:
        stdscr.move(3, 4)
        stdscr.clrtoeol()
        stdscr.addstr(3, 4, "*" * len(mat_khau) if not show else mat_khau)
        stdscr.refresh()

        key = stdscr.getch()
        if key in (curses.KEY_ENTER, 10, 13):
            break
        elif key in (curses.KEY_BACKSPACE, 127):
            if mat_khau:
                mat_khau = mat_khau[:-1]
        elif key == curses.KEY_F2:
            show = not show
        elif 32 <= key <= 126:
            mat_khau += chr(key)

    return mat_khau

def dang_nhap():
    so_lan_thu = 0
    while so_lan_thu < 3:
        def get_input(stdscr):
            return nhap_mat_khau(stdscr)

        mk = curses.wrapper(get_input)
        clear()
        if mk == "haine":
            print("\n✅ Đăng nhập thành công!\n")
            return
        else:
            so_lan_thu += 1
            print(f"\n❌ Sai mật khẩu. Thử lại... ({so_lan_thu}/3)\n")
            if so_lan_thu < 3:
                input("Nhấn Enter để thử lại...")

    print("🚫 Đã vượt quá số lần thử. Thoát.")
    sys.exit()