# 1_remove_string.py

from utils import get_column_index

def chuc_nang_1_xoa_chuoi(lines):
    text = input("🔤 Nhập chuỗi cần xóa: ")
    col = input("📌 Nhập cột muốn áp dụng (A, B...) hoặc Enter để áp dụng toàn bộ: ").strip().upper()
    count = 0
    if col:
        col_idx = get_column_index(lines[0], col)
        if col_idx is None:
            print("❌ Cột không hợp lệ.")
            return lines
        for row in lines[1:]:
            if col_idx < len(row):
                count += row[col_idx].count(text)
                row[col_idx] = row[col_idx].replace(text, "")
    else:
        for row in lines[1:]:
            for i in range(len(row)):
                count += row[i].count(text)
                row[i] = row[i].replace(text, "")
    print(f"✅ Đã xóa {count} lần xuất hiện của chuỗi '{text}'.")
    return lines
