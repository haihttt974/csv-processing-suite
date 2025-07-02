import csv

def load_csv(file_path, silent=False):
    import os
    if not os.path.exists(file_path):
        if not silent:
            print("❌ File không tồn tại.")
        return None
    if not os.path.isfile(file_path):
        if not silent:
            print("❌ Đường dẫn không phải là file.")
        return None
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            lines = list(reader)
        return lines
    except Exception as e:
        if not silent:
            print(f"❌ Lỗi khi đọc file: {e}")
        return None

def save_csv(file_path, data):
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print("✅ Đã lưu file thành công.")
    except Exception as e:
        print(f"❌ Lỗi khi lưu file: {e}")

def doi_duong_dan_file():
    import os
    new_path = input("🔁 Nhập đường dẫn file CSV mới: ").strip()
    if os.path.exists(new_path):
        print("✅ Đã cập nhật đường dẫn.")
        return new_path
    else:
        print("❌ Đường dẫn không tồn tại.")
        return None
