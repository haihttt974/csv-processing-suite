import os
import csv

def chuc_nang_17_gop_nhieu_file():
    folder = input("📁 Nhập thư mục chứa các file CSV cần gộp: ").strip()

    if not os.path.exists(folder) or not os.path.isdir(folder):
        print("❌ Thư mục không hợp lệ.")
        return []

    files = [f for f in os.listdir(folder) if f.lower().endswith(".csv")]
    if not files:
        print("❌ Không tìm thấy file CSV nào trong thư mục.")
        return []

    print(f"🔍 Tìm thấy {len(files)} file:")
    for f in files:
        print(f" - {f}")

    merged_data = []
    header = None
    for filename in files:
        path = os.path.join(folder, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = list(reader)
                if not rows:
                    continue
                if header is None:
                    header = rows[0]
                    merged_data.append(header)
                elif rows[0] != header:
                    print(f"⚠️ File {filename} có tiêu đề không khớp. Bỏ qua.")
                    continue
                merged_data.extend(rows[1:])
        except Exception as e:
            print(f"❌ Lỗi đọc file {filename}: {e}")

    print(f"✅ Đã gộp {len(merged_data)-1} dòng dữ liệu từ {len(files)} file.")

    # Hỏi người dùng có muốn lưu file kết quả
    save = input("💾 Bạn có muốn lưu kết quả vào file mới không? (y/n): ").strip().lower()
    if save == "y":
        name = input("📄 Nhập tên file (mặc định: GopFile.csv): ").strip()
        if not name:
            name = "GopFile.csv"
        with open(name, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(merged_data)
        print(f"✅ Đã lưu vào {name}")

    return merged_data
