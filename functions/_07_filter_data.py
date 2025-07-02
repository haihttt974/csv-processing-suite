from utils import get_column_index
import csv

def chuc_nang_7_loc(lines):
    col = input("🔍 Nhập cột cần lọc (A, B...): ").strip().upper()
    value = input("🔹 Giá trị cần lọc (từ khóa hoặc số): ").strip()

    col_idx = get_column_index(lines[0], col)
    if col_idx is None:
        print("❌ Cột không hợp lệ.")
        return lines

    header = lines[0]
    filtered = []

    for row in lines[1:]:
        if col_idx < len(row):
            cell = row[col_idx]
            # Nếu là số thì cho phép lọc theo tiền tố (starts with)
            try:
                float(cell)  # nếu chuyển được là số
                if cell.startswith(value):
                    filtered.append(row)
            except ValueError:
                # Nếu là chuỗi thì kiểm tra chứa từ khóa
                if value.lower() in cell.lower():
                    filtered.append(row)

    print("\n📄 Kết quả lọc:")
    if filtered:
        col_widths = [max(len(str(row[i])) for row in [header] + filtered) for i in range(len(header))]

        def print_row(row):
            print(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))

        print_row(header)
        print("-" * (sum(col_widths) + 3 * (len(header) - 1)))
        for row in filtered:
            print_row(row)
        print(f"\n✅ Lọc được {len(filtered)} dòng.")

        # 💾 Gợi ý lưu file mới
        save = input("\n📁 Bạn có muốn lưu kết quả lọc vào file mới? (y/n): ").strip().lower()
        if save == 'y':
            col_name = header[col_idx].replace(" ", "_")
            filename = f"{col_name}-{value}.csv"
            try:
                with open(filename, mode='w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(filtered)
                print(f"✅ Đã lưu vào file: {filename}")
            except Exception as e:
                print(f"❌ Lỗi khi lưu file: {e}")
    else:
        print("⚠️ Không có dòng nào khớp.")

    return lines  # Không thay đổi dữ liệu gốc
