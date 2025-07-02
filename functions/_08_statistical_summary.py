# 8_statistical_summary.py

from utils import get_column_index

def chuc_nang_8_thong_ke_so(lines):
    col = input("📌 Nhập cột số (A, B...): ").strip().upper()
    col_idx = get_column_index(lines[0], col)

    if col_idx is None:
        print("❌ Cột không hợp lệ.")
        return

    values = []
    for row in lines[1:]:
        try:
            values.append(float(row[col_idx]))
        except:
            continue

    if not values:
        print("❌ Không có giá trị số hợp lệ trong cột.")
        return

    tong = sum(values)
    trung_binh = tong / len(values)
    print(f"🔢 Tổng: {tong}")
    print(f"📊 Trung bình: {trung_binh:.2f}")
    print(f"🔽 Min: {min(values)}")
    print(f"🔼 Max: {max(values)}")
