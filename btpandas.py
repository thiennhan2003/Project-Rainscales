import pandas as pd

data = {
    'Name': ['Nhân', 'Thành', 'Diện', 'Tứ', 'Hà', 'Hùng', 'Lan', 'Mai', 'Nam', 'Tú'],
    'Age': [20, 21, 20, 22, 23, 21, 19, 20, 22, 20],
    'Gender': ['Nam', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nữ', 'Nam', 'Nữ'],
    'Score': [6.5, 8.0, 4.5, 7.0, 5.5, 3.0, 9.0, 6.0, 4.0, 8.5]
}

df_students = pd.DataFrame(data)

# Hiển thị toàn bộ dữ liệu
print("Toàn bộ dữ liệu:")
print(df_students)

# 3 dòng đầu
print("\n3 dòng đầu:")
print(df_students.head(3))

# Index=2 và cột Name
print("\nIndex 2, cột Name:", df_students.loc[2, 'Name'])

# Index=10 và cột Age
if 10 in df_students.index:
    print("Index 10, cột Age:", df_students.loc[10, 'Age'])
else:
    print("Index 10 không tồn tại trong DataFrame.")

# Cột Name và Score
print("\nCột Name và Score:")
print(df_students[['Name', 'Score']])

# Thêm cột Pass
df_students['Pass'] = df_students['Score'] >= 5

# Sắp xếp theo Score giảm dần
df_sorted = df_students.sort_values(by='Score', ascending=False)
print("\nDữ liệu sau khi thêm cột Pass và sắp xếp giảm dần theo Score:")
print(df_sorted)
