import re
from datetime import datetime

def is_number(value):
    try:
        float(value)
        return True
    except:
        return False

def is_date(value):
    formats = ['%d/%m/%Y', '%Y-%m-%d', '%m/%d/%Y']
    for fmt in formats:
        try:
            datetime.strptime(value, fmt)
            return True
        except:
            continue
    return False

def chuc_nang_22_nhan_dien_kieu_du_lieu(lines):
    if not lines or len(lines) < 2:
        print("⚠️ File không có đủ dữ liệu.")
        return

    headers = lines[0]
    columns = list(zip(*lines[1:]))

    print("\n📊 Loại dữ liệu của từng cột:\n")

    for i, col in enumerate(columns):
        sample = [val for val in col if val.strip() != ""]
        sample = sample[:30]

        num_count = sum(1 for val in sample if is_number(val))
        date_count = sum(1 for val in sample if is_date(val))
        total = len(sample)

        if total == 0:
            col_type = "Rỗng"
        elif num_count / total > 0.9:
            col_type = "Số"
        elif date_count / total > 0.9:
            col_type = "Ngày tháng"
        else:
            col_type = "Chuỗi"

        print(f"🧩 Cột {headers[i]} → {col_type}")
