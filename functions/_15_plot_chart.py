import matplotlib.pyplot as plt
from utils import get_column_index

def chuc_nang_15_ve_bieu_do(lines):
    if len(lines) < 2:
        print("❌ File không có đủ dữ liệu để vẽ.")
        return

    headers = lines[0]
    print("📊 Các cột hiện có:")
    for idx, col in enumerate(headers):
        print(f"{chr(65+idx)}. {col}")

    col_x = input("🔹 Cột trục hoành (X) (A, B, ...): ").strip().upper()
    col_y = input("🔹 Cột trục tung (Y) (A, B, ...): ").strip().upper()
    chart_type = input("📈 Loại biểu đồ (line/bar/pie): ").strip().lower()

    idx_x = get_column_index(headers, col_x)
    idx_y = get_column_index(headers, col_y)

    if idx_x is None or idx_y is None:
        print("❌ Cột không hợp lệ.")
        return

    x = [row[idx_x] for row in lines[1:] if len(row) > max(idx_x, idx_y)]
    y = [row[idx_y] for row in lines[1:] if len(row) > max(idx_x, idx_y)]

    try:
        y = list(map(float, y))
    except:
        print("❌ Trục Y phải là số để vẽ line/bar.")
        return

    plt.figure(figsize=(10, 5))
    if chart_type == 'line':
        plt.plot(x, y, marker='o')
    elif chart_type == 'bar':
        plt.bar(x, y)
    elif chart_type == 'pie':
        if len(x) != len(y):
            print("❌ Số nhãn và số giá trị không khớp.")
            return
        plt.pie(y, labels=x, autopct='%1.1f%%')
    else:
        print("❌ Loại biểu đồ không hỗ trợ.")
        return

    plt.title(f"{chart_type.upper()} Chart: {headers[idx_x]} vs {headers[idx_y]}")
    if chart_type != 'pie':
        plt.xlabel(headers[idx_x])
        plt.ylabel(headers[idx_y])
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
