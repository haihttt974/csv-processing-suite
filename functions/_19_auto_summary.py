import csv
from utils import get_column_index

def chuc_nang_19_tao_bao_cao(lines):
    if not lines or len(lines) < 2:
        print("❌ File không đủ dữ liệu để tạo báo cáo.")
        return

    header = lines[0]
    data = lines[1:]
    num_rows = len(data)
    num_cols = len(header)

    print("\n📄 TỔNG QUAN DỮ LIỆU")
    print(f"✅ Tổng số dòng: {num_rows}")
    print(f"✅ Tổng số cột: {num_cols}")

    print("\n📊 PHÂN TÍCH TỪNG CỘT:\n")

    for idx, col_name in enumerate(header):
        col_values = [row[idx] if idx < len(row) else "" for row in data]
        empty_count = sum(1 for val in col_values if not val.strip())
        unique_values = set(col_values)
        numeric_values = []

        for val in col_values:
            try:
                numeric_values.append(float(val))
            except:
                pass

        print(f"📌 Cột {idx} ({col_name}):")
        print(f"   - Rỗng: {empty_count} / {num_rows}")
        print(f"   - Giá trị duy nhất: {len(unique_values)}")
        if numeric_values:
            print(f"   - Dữ liệu số:")
            print(f"     • Tổng: {sum(numeric_values)}")
            print(f"     • Trung bình: {sum(numeric_values)/len(numeric_values):.2f}")
            print(f"     • Nhỏ nhất: {min(numeric_values)}")
            print(f"     • Lớn nhất: {max(numeric_values)}")
        else:
            print(f"   - Không phải dữ liệu số.")
        print()

    print("🧠 Bạn có thể dùng chức năng vẽ biểu đồ để trực quan hóa thêm nếu cần.")
