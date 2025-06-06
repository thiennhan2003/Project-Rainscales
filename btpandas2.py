import pandas as pd

# Tạo DataFrame với thông tin sinh viên
sinh_vien = {
    'Name': ['An', 'Bình', 'Chi', 'Dũng', 'Em', 'Hà', 'Hùng', 'Lan', 'Mai', 'Nam'],
    'Age': [20, 21, 19, 22, 20, 23, 21, 20, 19, 22],
    'Gender': ['M', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'F', 'M'],
    'Score': [7.5, 8.0, 6.5, 5.0, 4.5, 9.0, 6.0, 8.5, 3.5, 7.0]
}

df = pd.DataFrame(sinh_vien)

# In toàn bộ dữ liệu
print("Danh sách sinh viên:")
print(df)

# In 3 dòng đầu tiên
print("\nBa sinh viên đầu tiên:")
print(df.head(3))

# In tên sinh viên ở dòng có index = 2
print("\nSinh viên ở dòng thứ 3 (index=2):")
print("Tên:", df.loc[2, 'Name'])

# Kiểm tra nếu tồn tại index = 10, thì in tuổi; ngược lại thông báo
print("\nThông tin sinh viên ở index=10:")
if 10 in df.index:
    print("Tuổi:", df.loc[10, 'Age'])
else:
    print("Không có sinh viên ở index=10.")

# In cột Name và Score
print("\nTên và điểm của tất cả sinh viên:")
print(df[['Name', 'Score']])

# Thêm cột Pass: True nếu Score >= 5, ngược lại False
df['Pass'] = df['Score'] >= 5
print("\nDanh sách có thêm cột Pass (qua môn):")
print(df)

# Sắp xếp theo điểm giảm dần
df_sorted = df.sort_values(by='Score', ascending=False)
print("\nSinh viên sắp xếp theo điểm từ cao xuống thấp:")
print(df_sorted)
