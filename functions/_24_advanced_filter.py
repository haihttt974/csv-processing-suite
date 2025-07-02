from utils import get_column_index
import csv


def chuc_nang_24_loc_nang_cao(lines):
    header = lines[0]
    data = lines[1:]

    # Gợi ý thông tin cột
    print("\n📌 Gợi ý các cột và giá trị:")
    for i, col in enumerate(header):
        values = [row[i] for row in data if i < len(row)]
        try:
            numeric_values = [float(v) for v in values if v.replace('.', '', 1).isdigit()]
            if numeric_values:
                min_val = int(min(numeric_values)) if min(numeric_values).is_integer() else min(numeric_values)
                max_val = int(max(numeric_values)) if max(numeric_values).is_integer() else max(numeric_values)
                print(f" 🔹 {col}: {min_val} - {max_val}")
            else:
                unique_vals = sorted(set(values))
                print(f" 🔹 {col}: {', '.join(unique_vals[:10])} {'...' if len(unique_vals) > 10 else ''}")
        except:
            unique_vals = sorted(set(values))
            print(f" 🔹 {col}: {', '.join(unique_vals[:10])} {'...' if len(unique_vals) > 10 else ''}")

    print("\n📝 Gợi ý cú pháp:")
    print(" - Tên cột phải đúng như trong file (phân biệt chữ hoa/thường)")
    print(" - Có thể dùng các toán tử: >, <, >=, <=, ==, !=, and, or, in, not in")
    print(" - Ví dụ: Age > 25 and City == 'Hanoi'")

    dieu_kien = input("\n✏️ Nhập điều kiện lọc nâng cao (ví dụ: Age > 30 and City == 'Hanoi'):\n👉 ").strip()

    def eval_row(row):
        try:
            local_vars = {}
            for i, col in enumerate(header):
                cell = row[i] if i < len(row) else ""
                if cell.replace('.', '', 1).isdigit():
                    try:
                        val = float(cell)
                        if val.is_integer():
                            val = int(val)
                    except:
                        val = cell
                else:
                    val = cell
                local_vars[col] = val
            return eval(dieu_kien, {}, local_vars)
        except Exception as e:
            print(f"❌ Lỗi cú pháp hoặc tên cột: {e}")
            return False

    ket_qua = [row for row in data if eval_row(row)]

    print("\n📄 Kết quả lọc:")
    if ket_qua:
        col_widths = [max(len(str(row[i])) for row in [header] + ket_qua) for i in range(len(header))]

        def print_row(row):
            print(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))

        print_row(header)
        print("-" * (sum(col_widths) + 3 * (len(header) - 1)))
        for row in ket_qua:
            print_row(row)
        print(f"\n✅ Lọc được {len(ket_qua)} dòng.")

        # 💾 Gợi ý lưu file mới
        save = input("\n📁 Bạn có muốn lưu kết quả lọc vào file mới? (y/n): ").strip().lower()
        if save == 'y':
            import re
            clean_name = re.sub(r"[^a-zA-Z0-9]+", "_", dieu_kien)
            filename = f"loc_{clean_name}.csv"
            try:
                with open(filename, mode='w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(ket_qua)
                print(f"✅ Đã lưu vào file: {filename}")
            except Exception as e:
                print(f"❌ Lỗi khi lưu file: {e}")
    else:
        print("⚠️ Không có dòng nào khớp.")

    return lines  # Trả lại dữ liệu gốc để không bị thay đổi
