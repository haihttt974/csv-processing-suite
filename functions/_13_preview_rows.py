# 13_preview_rows.py

def chuc_nang_13_preview(lines):
    print("🔍 5 dòng đầu:")
    for row in lines[:6]:
        print(row)

    print("\n🔍 5 dòng cuối:")
    for row in lines[-5:]:
        print(row)
