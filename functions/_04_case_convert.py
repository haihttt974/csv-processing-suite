# 4_case_convert.py

from utils import get_column_index

def chuc_nang_4_chuyen_hoa_thuong(lines):
    mode = input("🔁 Chọn chế độ (upper/lower): ").strip().lower()
    col = input("📌 Nhập cột áp dụng (A, B,...): ").strip().upper()
    col_idx = get_column_index(lines[0], col)

    if col_idx is None:
        print("❌ Cột không hợp lệ.")
        return lines

    for row in lines[1:]:
        if col_idx < len(row):
            row[col_idx] = row[col_idx].upper() if mode == 'upper' else row[col_idx].lower()

    print("✅ Đã chuyển đổi.")
    return lines
