# 3_find_replace.py

from utils import get_column_index

def chuc_nang_3_tim_thay(lines):
    target = input("🔍 Chuỗi cần tìm: ")
    replace = input("✏️ Chuỗi thay thế: ")
    col = input("📌 Nhập cột áp dụng hoặc Enter để toàn bộ: ").strip().upper()
    count = 0

    if col:
        col_idx = get_column_index(lines[0], col)
        if col_idx is None:
            print("❌ Cột không hợp lệ.")
            return lines
        for row in lines[1:]:
            if col_idx < len(row):
                count += row[col_idx].count(target)
                row[col_idx] = row[col_idx].replace(target, replace)
    else:
        for row in lines[1:]:
            for i in range(len(row)):
                count += row[i].count(target)
                row[i] = row[i].replace(target, replace)

    print(f"✅ Đã thay thế {count} lần.")
    return lines
