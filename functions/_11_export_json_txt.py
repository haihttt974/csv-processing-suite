# 11_export_json_txt.py

import json

def chuc_nang_11_xuat(lines):
    fmt = input("💾 Xuất sang định dạng nào? (json/txt): ").strip().lower()
    name = input("📄 Nhập tên file (không cần đuôi): ").strip()

    if fmt == "json":
        try:
            with open(name + ".json", "w", encoding="utf-8") as f:
                keys = lines[0]
                json.dump([dict(zip(keys, row)) for row in lines[1:]], f, ensure_ascii=False, indent=2)
            print(f"✅ Đã lưu file {name}.json")
        except Exception as e:
            print(f"❌ Lỗi khi lưu JSON: {e}")

    elif fmt == "txt":
        try:
            with open(name + ".txt", "w", encoding="utf-8") as f:
                for row in lines:
                    f.write(" | ".join(row) + "\n")
            print(f"✅ Đã lưu file {name}.txt")
        except Exception as e:
            print(f"❌ Lỗi khi lưu TXT: {e}")

    else:
        print("❌ Định dạng không hợp lệ.")
