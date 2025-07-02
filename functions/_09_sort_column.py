from utils import get_column_index
import csv

def chuc_nang_9_sap_xep(lines):
    col = input("📌 Cột cần sắp xếp (A, B...): ").strip().upper()
    idx = get_column_index(lines[0], col)

    if idx is None:
        print("❌ Cột không hợp lệ.")
        return lines

    desc = input("🔽 Sắp xếp giảm dần? (y/n): ").strip().lower() == 'y'

    try:
        def parse_value(value):
            try:
                return float(value)
            except:
                return value

        lines[1:] = sorted(lines[1:], key=lambda x: parse_value(x[idx]), reverse=desc)
        print("✅ Đã sắp xếp.")

        # Lấy dữ liệu để hiển thị
        header = lines[0]
        preview_rows = lines[1:6]

        # Tính độ dài tối đa của từng cột
        col_widths = [max(len(str(row[i])) for row in [header] + preview_rows) for i in range(len(header))]

        # In bảng
        print("\n📋 5 dòng đầu sau khi sắp xếp:")
        print(" | ".join(header[i].ljust(col_widths[i]) for i in range(len(header))))
        print("-" * (sum(col_widths) + 3 * (len(header) - 1)))

        for row in preview_rows:
            print(" | ".join(row[i].ljust(col_widths[i]) for i in range(len(row))))

        # Gợi ý lưu file
        save = input("\n💾 Bạn có muốn lưu kết quả ra file mới không? (y/n): ").strip().lower()
        if save == 'y':
            col_name = header[idx].replace(" ", "_")
            default_name = f"SapXep_{col_name}_{'Giam' if desc else 'Tang'}.csv"
            file_name = input(f"📄 Nhập tên file muốn lưu (mặc định: {default_name}): ").strip()
            if not file_name:
                file_name = default_name

            with open(file_name, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(lines)
            print(f"✅ Đã lưu vào file: {file_name}")

    except Exception as e:
        print(f"❌ Lỗi khi sắp xếp: {e}")

    return lines
