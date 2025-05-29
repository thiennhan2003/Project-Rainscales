# 1. Viết chương trình đổi các từ ở đầu câu sang chữ hoa và những từ không phải đầu câu sang chữ thường.
def chuan_hoa_ho_ten(ten):
    return ' '.join(word.capitalize() for word in ten.split())

print(chuan_hoa_ho_ten("hoang nhan"))  

# 2. Viết chương trình đảo ngược thứ tự các từ có trong chuỗi.
def dao_nguoc_cau(s):
    return ' '.join(s.split()[::-1])

print(dao_nguoc_cau("ngon ngu bị dao nguoc"))

# 3. Viết chương trình tìm kiếm ký tự xuất hiện nhiều nhất trong chuỗi.
from collections import Counter

def ki_tu_pho_bien(s):
    s = s.replace(" ", "")
    counts = Counter(s)
    return counts.most_common(1)[0]

print(ki_tu_pho_bien("toi ten la nhan"))

# 4. Viết chương trình nhập một chuỗi bất kỳ, liệt kê số lần xuất hiện của mỗi ký tự.
def dem_tan_suat(s):
    from collections import Counter
    return dict(Counter(s))

print(dem_tan_suat("nhan hoang"))

# 5. Viết hàm kiểm tra xem trong chuỗi có ký tự số hay không. Nếu có, tách các số đó ra thành một mảng riêng.
def tach_so(s):
    so = [ch for ch in s if ch.isdigit()]
    return so if so else "Không có số"

print(tach_so("number1245"))

# 6. Viết hàm cắt chuỗi họ tên thành chuỗi họ lót và chuỗi tên.
def tach_ho_ten(ho_ten):
    parts = ho_ten.strip().split()
    ho_lot = ' '.join(parts[:-1])
    ten = parts[-1]
    return ho_lot, ten

print(tach_ho_ten("Hoang Thien Nhan"))

# 7. Viết chương trình chuyển ký tự đầu tiên của mỗi từ trong chuỗi thành chữ in hoa.
def viet_hoa_tu(s):
    return s.title()

print(viet_hoa_tu("nhan hoang"))

# 8. Viết chương trình đổi chữ xen kẽ: một chữ hoa và một chữ thường.
def chu_xen_ke(s):
    ket_qua = ""
    for i, ch in enumerate(s):
        ket_qua += ch.upper() if i % 2 == 0 else ch.lower()
    return ket_qua

print(chu_xen_ke("ThienNhan"))

# 9. Viết chương trình nhập vào một chuỗi ký tự, kiểm tra xem chuỗi đó có đối xứng không.
def la_doi_xung(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(la_doi_xung("no lemon no melon"))

# 10. Viết chương trình nhập vào một số có 3 chữ số, xuất ra dòng chữ mô tả giá trị con số đó.
def so_thanh_chu(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    tram = n // 100
    chuc_so = (n % 100) // 10
    donvi_so = n % 10

    ket_qua = f"{don_vi[tram]} trăm"
    if chuc_so == 0 and donvi_so != 0:
        ket_qua += f" lẻ {don_vi[donvi_so]}"
    elif chuc_so != 0:
        ket_qua += f" {chuc[chuc_so]}"
        if donvi_so != 0:
            ket_qua += f" {don_vi[donvi_so]}"
    return ket_qua.strip()

print(so_thanh_chu(123))

