from utils import get_column_index

def chuc_nang_16_xoa_trung_lap(lines):
    print("🔍 Bạn muốn xóa trùng theo:")
    print("1. Toàn bộ dòng")
    print("2. Một hoặc nhiều cột chỉ định")

    choice = input("👉 Chọn (1/2): ").strip()
    if choice == "1":
        seen = set()
        new_lines = [lines[0]]
        for row in lines[1:]:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                new_lines.append(row)
        print(f"✅ Đã xóa {len(lines) - len(new_lines)} dòng trùng hoàn toàn.")
        lines = new_lines

    elif choice == "2":
        headers = lines[0]
        print("📋 Các cột hiện có:")
        for i, h in enumerate(headers):
            print(f"{chr(65+i)}. {h}")

        cols = input("📌 Nhập các cột cần xét trùng (VD: A,C,E): ").strip().upper().split(",")
        col_indices = [get_column_index(headers, c) for c in cols if get_column_index(headers, c) is not None]

        if not col_indices:
            print("❌ Không có cột hợp lệ.")
            return lines

        seen = set()
        new_lines = [headers]
        for row in lines[1:]:
            key = tuple(row[i] for i in col_indices if i < len(row))
            if key not in seen:
                seen.add(key)
                new_lines.append(row)
        print(f"✅ Đã xóa {len(lines) - len(new_lines)} dòng trùng theo cột {cols}.")
        lines = new_lines

    else:
        print("❌ Lựa chọn không hợp lệ.")
        return lines

    # Hỏi lưu
    save = input("💾 Bạn có muốn lưu vào file mới không? (y/n): ").strip().lower()
    if save == "y":
        name = input("📁 Nhập tên file muốn lưu (mặc định: XoaTrungLap.csv): ").strip()
        if not name:
            name = "XoaTrungLap.csv"

        with open(name, "w", encoding="utf-8") as f:
            for row in lines:
                f.write(",".join(row) + "\n")
        print(f"✅ Đã lưu file: {name}")

    return lines
