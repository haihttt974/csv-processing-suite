import csv
import os
from utils import get_column_index

def chuc_nang_18_tach_file_csv(lines):
    if not lines or len(lines) < 2:
        print("❌ File không đủ dữ liệu để tách.")
        return

    print("📂 Bạn muốn tách theo:")
    print("1. Số dòng mỗi file")
    print("2. Giá trị trong một cột cụ thể")

    chon = input("👉 Nhập lựa chọn (1 hoặc 2): ").strip()

    if chon == "1":
        try:
            so_dong = int(input("🔢 Nhập số dòng mỗi file (không tính header): "))
            if so_dong <= 0:
                print("❌ Số dòng phải > 0")
                return

            header = lines[0]
            data = lines[1:]
            for i in range(0, len(data), so_dong):
                part = data[i:i+so_dong]
                ten_file = f"tach_{i//so_dong + 1}.csv"
                with open(ten_file, "w", encoding="utf-8", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(part)
                print(f"✅ Đã tạo file: {ten_file}")

        except:
            print("❌ Số dòng không hợp lệ.")

    elif chon == "2":
        col = input("📌 Nhập cột cần chia (A, B...): ").strip().upper()
        col_idx = get_column_index(lines[0], col)
        if col_idx is None:
            print("❌ Cột không hợp lệ.")
            return

        header = lines[0]
        groups = {}
        for row in lines[1:]:
            key = row[col_idx] if col_idx < len(row) else "Khac"
            groups.setdefault(key, []).append(row)

        for key, group in groups.items():
            safe_key = "".join(c for c in key if c.isalnum() or c in (' ', '_')).strip().replace(" ", "_") or "Khac"
            ten_file = f"tach_{safe_key}.csv"
            with open(ten_file, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(group)
            print(f"✅ Đã tạo file: {ten_file}")

    else:
        print("❌ Lựa chọn không hợp lệ.")
