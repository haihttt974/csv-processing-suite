# 5_remove_rows.py

def chuc_nang_5_xoa_dong_rong(lines):
    key = input("🔤 Nhập chuỗi (Enter nếu muốn xóa dòng rỗng): ").strip()
    new_lines = [lines[0]]  # giữ lại header

    for row in lines[1:]:
        if key:
            if not any(key in cell for cell in row):
                new_lines.append(row)
        else:
            if any(cell.strip() for cell in row):
                new_lines.append(row)

    so_dong_xoa = len(lines) - len(new_lines)
    print(f"✅ Đã xóa {so_dong_xoa} dòng.")
    return new_lines
