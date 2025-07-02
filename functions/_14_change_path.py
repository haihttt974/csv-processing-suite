from load_save import load_csv

def chuc_nang_14_doi_duong_dan():
    new_path = input("📁 Nhập đường dẫn file CSV mới: ").strip()
    temp = load_csv(new_path, silent=True)

    if temp:
        print("✅ Đã cập nhật đường dẫn.")
        return temp, new_path
    else:
        print("❌ File không hợp lệ hoặc lỗi khi đọc.")
        return None, None

def chuc_nang_14_doi_duong_dan_auto(new_path):
    temp = load_csv(new_path, silent=True)
    if temp:
        print(f"✅ Đã cập nhật đường dẫn tới file mới: {new_path}")
        return temp, new_path
    else:
        print("❌ File không hợp lệ hoặc lỗi khi đọc.")
        return None, None