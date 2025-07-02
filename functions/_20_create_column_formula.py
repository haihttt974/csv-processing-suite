import re
from load_save import save_csv

def chuc_nang_20_tao_cot_cong_thuc(lines, file_path):
    headers = lines[0]
    rows = lines[1:]

    print("\n📌 Bạn muốn tạo cột mới bằng công thức từ các cột hiện tại.")
    print("📚 Các cột hiện có:")
    col_map = {}
    for idx, col in enumerate(headers):
        key = chr(ord('a') + idx)
        col_map[key] = idx
        print(f"   {key}: {col}")

    print("\n📘 Ví dụ công thức: (a + b) * 2 hoặc (c / d) + a")
    formula = input("✍️  Nhập công thức (dùng ký hiệu a, b,...): ").strip()
    new_col = input("📌 Nhập tên cột mới: ").strip()

    new_lines = [headers + [new_col]]
    error_count = 0

    for row in rows:
        try:
            local_vars = {k: convert_to_number(row[v]) for k, v in col_map.items() if v < len(row)}
            result = eval(formula, {}, local_vars)
        except Exception:
            result = "ERR"
            error_count += 1
        new_lines.append(row + [result])

    print(f"\n✅ Đã tạo cột '{new_col}'. Có {error_count} dòng lỗi (ghi là 'ERR').")

    save_option = input("📁 Bạn có muốn lưu kết quả này ra file mới không? (y/n): ").strip().lower()
    if save_option == 'y':
        save_name = file_path.replace(".csv", f"_{new_col}_formula.csv")
        save_csv(save_name, new_lines)
        print(f"✅ Đã lưu file: {save_name}")

    return new_lines

def convert_to_number(val):
    try:
        return float(val)
    except:
        return 0  # fallback nếu không convert được
