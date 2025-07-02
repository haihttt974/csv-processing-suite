import os
import pdfplumber
import pandas as pd
from load_save import save_csv
from functions._14_change_path import chuc_nang_14_doi_duong_dan_auto
from global_data import global_data  # Đúng dạng dict toàn cục

def chuc_nang_23_extract_from_excel_pdf():
    print("\n📥 Nhập đường dẫn file Excel hoặc PDF (đuôi .xlsx hoặc .pdf):")
    path = input("📂 ").strip()

    if not os.path.isfile(path):
        print("❌ File không tồn tại.")
        return

    base_name = os.path.splitext(os.path.basename(path))[0]
    ext = os.path.splitext(path)[1].lower()

    try:
        # Trích xuất từ Excel
        if ext == '.xlsx':
            xls = pd.ExcelFile(path, engine='openpyxl')
            print("📄 Danh sách sheet trong file:")
            for i, sheet in enumerate(xls.sheet_names):
                print(f"  {i+1}. {sheet}")
            chon = input("🔢 Nhập số thứ tự sheet muốn trích xuất: ").strip()
            if not chon.isdigit() or int(chon) < 1 or int(chon) > len(xls.sheet_names):
                print("❌ Lựa chọn không hợp lệ.")
                return
            sheet_name = xls.sheet_names[int(chon) - 1]
            df = pd.read_excel(xls, sheet_name=sheet_name)
            default_name = f"{base_name}_{sheet_name}.csv"

        # Trích xuất từ PDF
        elif ext == '.pdf':
            print("🔍 Đang trích xuất bảng từ PDF (sử dụng pdfplumber)...")
            tables = []

            with pdfplumber.open(path) as pdf:
                for i, page in enumerate(pdf.pages):
                    extracted = page.extract_tables()
                    for table in extracted:
                        tables.append(pd.DataFrame(table[1:], columns=table[0]))

            if not tables:
                print("❌ Không tìm thấy bảng nào trong file PDF.")
                return

            print("📑 Số bảng tìm thấy:", len(tables))
            for i, table in enumerate(tables):
                print(f"  {i+1}. Bảng {i+1} - {table.shape[0]} dòng, {table.shape[1]} cột")

            chon = input("🔢 Nhập số thứ tự bảng muốn lưu: ").strip()
            if not chon.isdigit() or int(chon) < 1 or int(chon) > len(tables):
                print("❌ Lựa chọn không hợp lệ.")
                return

            df = tables[int(chon) - 1]
            default_name = f"{base_name}_table{chon}.csv"

        else:
            print("❌ Chỉ hỗ trợ file .xlsx hoặc .pdf.")
            return

        # Xem trước dữ liệu
        print("\n📋 Xem trước dữ liệu (5 dòng đầu):")
        print(df.head())

        # Tạo tên file CSV
        file_name = input(f"\n💾 Nhập tên file CSV muốn lưu (mặc định: {default_name}): ").strip()
        if not file_name:
            file_name = default_name
        if not file_name.lower().endswith(".csv"):
            file_name += ".csv"

        save_path = os.path.join(os.getcwd(), file_name)
        df.to_csv(save_path, index=False)
        print(f"✅ Đã lưu dữ liệu ra file: {save_path}")

        # Đổi file đang làm việc nếu người dùng chọn
        doi = input("🔁 Bạn có muốn đổi sang file này để thực hiện tiếp các chức năng? (y/n): ").strip().lower()
        if doi == 'y':
            new_lines, new_path = chuc_nang_14_doi_duong_dan_auto(save_path)
            if new_lines:
                global_data["lines"] = new_lines
                global_data["file_path"] = new_path
                print(f"🔄 Đã cập nhật đường dẫn tới file mới: {new_path}")
            else:
                print("❌ Không thể đổi file.")

    except Exception as e:
        print(f"❌ Lỗi: {e}")
