from utils import clear
from auth import dang_nhap
from menu import print_menu
from global_data import global_data
from load_save import load_csv

from functions._01_remove_string import chuc_nang_1_xoa_chuoi
from functions._02_unique_values import chuc_nang_2_thong_ke
from functions._03_find_replace import chuc_nang_3_tim_thay
from functions._04_case_convert import chuc_nang_4_chuyen_hoa_thuong
from functions._05_remove_rows import chuc_nang_5_xoa_dong_rong
from functions._06_merge_split_columns import chuc_nang_6_gop_tach
from functions._07_filter_data import chuc_nang_7_loc
from functions._08_statistical_summary import chuc_nang_8_thong_ke_so
from functions._09_sort_column import chuc_nang_9_sap_xep
from functions._10_datetime_process import chuc_nang_10_thoi_gian
from functions._11_export_json_txt import chuc_nang_11_xuat
from functions._12_validate_data import chuc_nang_12_kiem_tra_loi
from functions._13_preview_rows import chuc_nang_13_preview
from functions._14_change_path import chuc_nang_14_doi_duong_dan
from functions._15_plot_chart import chuc_nang_15_ve_bieu_do
from functions._16_remove_duplicates import chuc_nang_16_xoa_trung_lap
from functions._17_merge_multiple_csv import chuc_nang_17_gop_nhieu_file
from functions._18_split_csv import chuc_nang_18_tach_file_csv
from functions._19_auto_summary import chuc_nang_19_tao_bao_cao
from functions._20_create_column_formula import chuc_nang_20_tao_cot_cong_thuc
from functions._21_standardize_column import chuc_nang_21_chuan_hoa
from functions._22_detect_column_type import chuc_nang_22_nhan_dien_kieu_du_lieu
from functions._23_extract_from_excel_pdf import chuc_nang_23_extract_from_excel_pdf
from functions._24_advanced_filter import chuc_nang_24_loc_nang_cao

import os

def main():
    dang_nhap()

    file_path = input("📁 Nhập đường dẫn tới file CSV: ").strip()
    while not os.path.exists(file_path) or not os.path.isfile(file_path) or not file_path.lower().endswith(".csv"):
        print("❌ Đường dẫn không hợp lệ hoặc không phải file CSV.")
        file_path = input("📁 Nhập lại đường dẫn tới file CSV: ").strip()

    print("✅ Đã xác nhận file hợp lệ.")
    lines = load_csv(file_path)
    global_data["lines"] = lines
    global_data["file_path"] = file_path

    while True:
        clear()
        print(f"📂 File đang làm việc: {global_data['file_path']}")
        print_menu()

        choice = input("👉 Chọn chức năng (0-24): ").strip()
        if choice == "0":
            break
        elif choice == "1":
            global_data["lines"] = chuc_nang_1_xoa_chuoi(global_data["lines"])
        elif choice == "2":
            chuc_nang_2_thong_ke(global_data["lines"])
        elif choice == "3":
            global_data["lines"] = chuc_nang_3_tim_thay(global_data["lines"])
        elif choice == "4":
            global_data["lines"] = chuc_nang_4_chuyen_hoa_thuong(global_data["lines"])
        elif choice == "5":
            global_data["lines"] = chuc_nang_5_xoa_dong_rong(global_data["lines"])
        elif choice == "6":
            global_data["lines"] = chuc_nang_6_gop_tach(global_data["lines"], global_data["file_path"])
        elif choice == "7":
            global_data["lines"] = chuc_nang_7_loc(global_data["lines"])
        elif choice == "8":
            chuc_nang_8_thong_ke_so(global_data["lines"])
        elif choice == "9":
            global_data["lines"] = chuc_nang_9_sap_xep(global_data["lines"])
        elif choice == "10":
            global_data["lines"] = chuc_nang_10_thoi_gian(global_data["lines"])
        elif choice == "11":
            chuc_nang_11_xuat(global_data["lines"])
        elif choice == "12":
            chuc_nang_12_kiem_tra_loi(global_data["lines"], global_data["file_path"])
        elif choice == "13":
            chuc_nang_13_preview(global_data["lines"])
        elif choice == "14":
            temp, new_path = chuc_nang_14_doi_duong_dan()
            if temp:
                global_data["lines"] = temp
                global_data["file_path"] = new_path
        elif choice == "15":
            chuc_nang_15_ve_bieu_do(global_data["lines"])
        elif choice == "16":
            global_data["lines"] = chuc_nang_16_xoa_trung_lap(global_data["lines"])
        elif choice == "17":
            global_data["lines"] = chuc_nang_17_gop_nhieu_file()
        elif choice == "18":
            global_data["lines"] = chuc_nang_18_tach_file_csv(global_data["lines"])
        elif choice == "19":
            chuc_nang_19_tao_bao_cao(global_data["lines"])
        elif choice == "20":
            global_data["lines"] = chuc_nang_20_tao_cot_cong_thuc(global_data["lines"], global_data["file_path"])
        elif choice == "21":
            global_data["lines"] = chuc_nang_21_chuan_hoa(global_data["lines"], global_data["file_path"])
        elif choice == "22":
            chuc_nang_22_nhan_dien_kieu_du_lieu(global_data["lines"])
        elif choice == "23":
            chuc_nang_23_extract_from_excel_pdf()
        elif choice == "24":
            lines = chuc_nang_24_loc_nang_cao(lines)

        input("\nNhấn Enter để quay lại menu...")

if __name__ == "__main__":
    main()
