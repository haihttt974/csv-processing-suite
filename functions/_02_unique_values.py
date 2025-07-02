# 2_unique_values.py

from utils import get_column_index

def chuc_nang_2_thong_ke(lines):
    col = input("📌 Nhập cột cần thống kê (A, B, ...): ").strip().upper()
    col_idx = ord(col) - ord('A')
    if col_idx < 0 or col_idx >= len(lines[0]):
        print("❌ Cột không hợp lệ.")
        return

    values = {}
    for row in lines[1:]:
        if col_idx < len(row):
            val = row[col_idx]
            values[val] = values.get(val, 0) + 1

    for val, count in values.items():
        print(f"{val}: {count} lần")
