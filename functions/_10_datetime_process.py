from utils import get_column_index
from datetime import datetime
from load_save import save_csv

def print_table(lines, num_rows=5):
    # Tính chiều rộng tối đa cho từng cột
    col_widths = [len(col) for col in lines[0]]
    for row in lines[1:num_rows+1]:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    def print_row(row):
        print(" | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row)))

    print(f"\n📋 {num_rows} dòng đầu sau khi xử lý:")
    print_row(lines[0])
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    for row in lines[1:num_rows+1]:
        print_row(row)

def chuc_nang_10_thoi_gian(lines):
    print("📌 Ví dụ định dạng: %Y-%m-%d | %d/%m/%Y | %Y/%m/%d %H:%M:%S")
    col = input("📅 Nhập cột thời gian (A, B...): ").strip().upper()
    fmt = input("⏰ Nhập định dạng thời gian: ").strip()

    col_idx = get_column_index(lines[0], col)
    if col_idx is None:
        print("❌ Cột không hợp lệ.")
        return lines

    count_ok = 0
    count_err = 0
    error_rows = []

    for i, row in enumerate(lines[1:], start=2):  # start=2 tính cả header
        try:
            dt = datetime.strptime(row[col_idx], fmt)
            row[col_idx] = dt.strftime("%Y-%m-%d %H:%M:%S")  # chuẩn hóa format
            count_ok += 1
        except Exception:
            error_rows.append((i, row[col_idx]))
            count_err += 1

    # Kết quả
    print(f"\n✅ Đã chuyển đổi thành công {count_ok} giá trị thời gian.")
    if count_err:
        print(f"⚠️ Có {count_err} dòng lỗi (không đúng định dạng):")
        for dong, val in error_rows[:5]:  # hiển thị tối đa 5 lỗi đầu
            print(f" - Dòng {dong}: {val}")
        if count_err > 5:
            print("...")

    # Hiển thị bảng mẫu
    print_table(lines, 3)

    # Lưu ra file mới
    yn = input("\n💾 Bạn có muốn lưu ra file mới không? (y/n): ").strip().lower()
    if yn == "y":
        col_name = lines[0][col_idx].replace(" ", "_")
        default_name = f"ThoiGian_{col_name}.csv"
        file_name = input(f"📂 Nhập tên file (mặc định: {default_name}): ").strip()
        if not file_name:
            file_name = default_name
        save_csv(file_name, lines)
        print(f"✅ Đã lưu file: {file_name}")

    return lines
