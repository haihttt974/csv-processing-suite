import csv
import os
import json
from utils import get_column_index

def chuc_nang_12_kiem_tra_loi(lines, file_path):
    header = lines[0]
    header_len = len(header)
    loi = 0
    loi_rong = []
    loi_ket_cau = []

    for i, row in enumerate(lines[1:], start=2):
        if not row or all(cell.strip() == '' for cell in row):
            loi_rong.append(i)
        elif len(row) != header_len:
            loi_ket_cau.append((i, row))

    # Xử lý dòng rỗng
    if loi_rong:
        print(f"\n⚠️ Có {len(loi_rong)} dòng rỗng: {loi_rong}")
        chon = input("\n🧹 Bạn có muốn xóa các dòng rỗng này và lưu lại file gốc không? (y/n): ").strip().lower()
        if chon == 'y':
            new_lines = [lines[0]] + [row for i, row in enumerate(lines[1:], start=2) if i not in loi_rong]
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(new_lines)
            print("✅ Đã xóa và lưu lại file gốc.")

    # Xử lý dòng lỗi thiếu/thừa cột
    if loi_ket_cau:
        print(f"\n⚠️ Có {len(loi_ket_cau)} dòng lỗi cấu trúc (thiếu/thừa cột):")
        for i, row in loi_ket_cau:
            print(f"- Dòng {i}: {row}")

        chon = input("\n🛠️ Bạn có muốn sửa trực tiếp tại đây không? (y/n): ").strip().lower()
        if chon == 'y':
            for i, row in loi_ket_cau:
                print(f"\n📝 Dòng {i} hiện tại:")
                data = {header[j]: row[j] if j < len(row) else '' for j in range(header_len)}
                print(json.dumps(data, indent=2, ensure_ascii=False))
                for j in range(header_len):
                    old = data[header[j]]
                    new = input(f"🔄 {header[j]} (hiện: '{old}'): ").strip()
                    data[header[j]] = new if new else old
                lines[i - 1] = [data[col] for col in header]
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(lines)
            print("✅ Đã cập nhật và lưu lại file gốc.")

    if not loi_rong and not loi_ket_cau:
        print("\n✅ Không phát hiện lỗi dữ liệu.")
    else:
        print(f"\n📊 Tổng cộng {len(loi_rong) + len(loi_ket_cau)} lỗi được phát hiện.")
