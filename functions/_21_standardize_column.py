# 📄 functions/_21_standardize_column.py

from datetime import datetime
from load_save import save_csv

def chuc_nang_21_chuan_hoa(lines, file_path):
    if not lines:
        print("⚠️ File rỗng.")
        return lines

    headers = lines[0]
    print("\n📦 Danh sách cột:")
    for idx, col in enumerate(headers):
        print(f"  {chr(97 + idx)}: {col}")

    col_letter = input("🔠 Nhập ký hiệu cột (a, b, c, ...): ").strip().lower()
    col_idx = ord(col_letter) - 97

    if col_idx < 0 or col_idx >= len(headers):
        print("❌ Ký hiệu cột không hợp lệ.")
        return lines

    print("""
    📘 Chọn kiểu chuẩn hóa:
    1. Viết hoa chữ cái đầu
    2. Viết thường toàn bộ
    3. Viết HOA TOÀN BỘ
    4. Xóa khoảng trắng đầu/cuối
    5. Chuẩn hóa ngày (dd/mm/yyyy → yyyy-mm-dd)
    """)

    choice = input("➡️ Lựa chọn của bạn (1-5): ").strip()

    def convert(val):
        if choice == "1":
            return val.title()
        elif choice == "2":
            return val.lower()
        elif choice == "3":
            return val.upper()
        elif choice == "4":
            return val.strip()
        elif choice == "5":
            try:
                return datetime.strptime(val.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
            except:
                return val
        return val

    count = 0
    for i in range(1, len(lines)):
        try:
            old = lines[i][col_idx]
            new = convert(old)
            if new != old:
                lines[i][col_idx] = new
                count += 1
        except:
            continue

    print(f"✅ Đã chuẩn hóa {count} dòng trong cột '{headers[col_idx]}'.")

    save = input("💾 Lưu kết quả ra file mới? (y/n): ").strip().lower()
    if save == "y":
        new_name = file_path.replace(".csv", f"_chuanhoa_{headers[col_idx]}.csv")
        save_csv(new_name, lines)
        print(f"📁 File đã lưu: {new_name}")

    return lines
