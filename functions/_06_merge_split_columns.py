from utils import get_column_index
from load_save import save_csv

def chuc_nang_6_gop_tach(lines, filename):
    action = input("📦 Gõ 'gop' để gộp hoặc 'tach' để tách cột: ").strip().lower()

    if action == 'gop':
        cols = input("📌 Nhập các cột muốn gộp (VD: A,B,C): ").strip().split(',')
        sep = input("🔗 Nhập ký tự phân tách: ")

        indices = []
        for c in cols:
            idx = get_column_index(lines[0], c.strip())
            if idx is None:
                print(f"❌ Cột '{c}' không hợp lệ.")
                return lines
            indices.append(idx)

        for row in lines[1:]:
            values = [row[i] if i < len(row) else "" for i in indices]
            row.append(sep.join(values))

        lines[0].append("GopCot")
        print("✅ Đã gộp cột.")

    elif action == 'tach':
        col = input("📌 Cột muốn tách (A, B...): ").strip().upper()
        sep = input("🔗 Ký tự phân tách: ")
        idx = get_column_index(lines[0], col)

        if idx is None:
            print("❌ Cột không hợp lệ.")
            return lines

        new_col_names = input("📌 Nhập tên các cột mới (phân cách bởi dấu phẩy): ").split(",")
        lines[0].extend(new_col_names)

        for row in lines[1:]:
            if idx < len(row):
                parts = row[idx].split(sep)
                row.extend(parts)
        print("✅ Đã tách cột.")

    else:
        print("❌ Hành động không hợp lệ.")
        return lines

    # ✅ Gợi ý lưu vào đúng file đang dùng
    luu = input(f"💾 Bạn có muốn ghi đè vào file `{filename}`? (y/n): ").strip().lower()
    if luu == 'y':
        save_csv(filename, lines)
        print(f"✅ Đã lưu vào file `{filename}`.")
    else:
        print("📌 Bạn đã chọn không lưu.")

    return lines
