#Bài 6-20
char = input("Nhập vào một ký tự chữ cái bất kỳ: ")

char = char.lower() # Chuyển đổi ký tự sang chữ thường

if len(char) != 1 or not 'a' <= char <= 'z':
    print("Vui lòng nhập một ký tự chữ cái hợp lệ.")
else:
    if char in "ueoai":
        print(char, "là nguyên âm.")
    else:
        print(char, "là phụ âm.")
#Bài7-20
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

if chieu_cao <= 0 or can_nang <= 0:
    print("Chiều cao và cân nặng phải là số dương.")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print("Chỉ số BMI của bạn là:", bmi)

    if bmi < 18.5:
        print("Bạn đang bị thiếu cân.")
    elif 18.5 <= bmi <= 24.9:
        print("Bạn có cân nặng bình thường.")
    elif 25 <= bmi <= 29.9:
        print("Bạn đang bị thừa cân.")
    else:
        print("Bạn đang bị béo phì.")
#Bài 8-21
thang_sinh = int(input("Nhập tháng sinh của bạn (1-12): "))

if thang_sinh < 1 or thang_sinh > 12:
    print("Tháng sinh nhập vào không đúng")
elif thang_sinh in (1, 2, 3):
    print("Bạn sinh vào Mùa xuân")
elif thang_sinh in (4, 5, 6):
    print("Bạn sinh vào Mùa hạ")
elif thang_sinh in (7, 8, 9):
    print("Bạn sinh vào Mùa thu")
else:  # thang_sinh in (10, 11, 12)
    print("Bạn sinh vào Mùa đông")       
#Bài 9-35
bang_cuu_chuong = int(input("Nhập bảng cửu chương muốn in (1-10): "))

if 1 <= bang_cuu_chuong <= 10:
    print(f"Bảng cửu chương {bang_cuu_chuong}:")
    for i in range(1, 11):
        print(f"{bang_cuu_chuong} x {i} = {bang_cuu_chuong * i}")
else:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số từ 1 đến 10.")
#Bài 10-36
diem_he_10 = [9.5, 7.8, 6.2, 4.5, 8.9, 5.2, 9.1, 7.0, 3.5, 8.2]  # Danh sách điểm hệ 10 (ví dụ)

diem_chu = []
diem_he_4 = []

for diem in diem_he_10:
    if 9.0 <= diem <= 10:
        diem_chu.append("A+")
        diem_he_4.append(4.0)
    elif 8.5 <= diem <= 8.9:
        diem_chu.append("A")
        diem_he_4.append(3.7)
    elif 8.0 <= diem <= 8.4:
        diem_chu.append("B+")
        diem_he_4.append(3.5)
    elif 7.0 <= diem <= 7.9:
        diem_chu.append("B")
        diem_he_4.append(3.0)
    elif 6.5 <= diem <= 6.9:
        diem_chu.append("C+")
        diem_he_4.append(2.5)
    elif 5.5 <= diem <= 6.4:
        diem_chu.append("C")
        diem_he_4.append(2.0)
    elif 5.0 <= diem <= 5.4:
        diem_chu.append("D+")
        diem_he_4.append(1.5)
    elif 4.0 <= diem <= 4.9:
        diem_chu.append("D")
        diem_he_4.append(1.0)
    else:  # diem < 4.0
        diem_chu.append("F")
        diem_he_4.append(0.0)

# Tính điểm trung bình
trung_binh_he_10 = sum(diem_he_10) / len(diem_he_10)
trung_binh_he_4 = sum(diem_he_4) / len(diem_he_4)

print("Điểm hệ 10:", diem_he_10)
print("Điểm chữ:", diem_chu)
print("Điểm hệ 4:", diem_he_4)
print(f"Điểm trung bình hệ 10: {trung_binh_he_10:.2f}") # Định dạng 2 chữ số thập phân
print(f"Điểm trung bình hệ 4: {trung_binh_he_4:.2f}") # Định dạng 2 chữ số thập phân     
#Bài 11-38
def la_so_nguyen_to_co_ban(n):
    if n <= 1:  # Số nhỏ hơn hoặc bằng 1 không phải số nguyên tố
        return False
    for i in range(2, n):  # Duyệt từ 2 đến n-1
        if n % i == 0:  
            return False  
    return True  

n = int(input("Nhập số tự nhiên n: "))
if la_so_nguyen_to_co_ban(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")
#Bài 12-38
import math
try:
    N = int(input("Nhập vào một số N: "))

    if N < 2:
        print("Không có số nguyên tố nào trong khoảng này.")
    else:
        print(f"Các số nguyên tố từ 2 đến {N}:")

        for num in range(2, N + 1):
            is_prime = True  # Giả sử ban đầu num là số nguyên tố

            if num <= 1:
                is_prime = False
            elif num <= 3:
                is_prime = True
            elif num % 2 == 0 or num % 3 == 0:
                is_prime = False
            else: # Chỉ kiểm tra các số có dạng 6k ± 1 (tối ưu)
                for i in range(5, int(math.sqrt(num)) + 1, 6):
                    if num % i == 0 or num % (i + 2) == 0:
                        is_prime = False
                        break # Thoát vòng lặp ngay khi tìm thấy ước số

            if is_prime: # Nếu num vẫn là số nguyên tố
                print(num, end=" ")

        print() 
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
#Bài 13-40
try:
    N = int(input("Nhập vào một số tự nhiên N (N > 0): "))
    if N <= 0:
        print("Vui lòng nhập số tự nhiên lớn hơn 0.")
    else:
        binary = ""
        temp_N = N  # Tạo biến tạm để không thay đổi giá trị N ban đầu

        while temp_N > 0:
            remainder = temp_N % 2  # Lấy số dư khi chia cho 2
            binary = str(remainder) + binary  # Thêm số dư vào *đầu* chuỗi
            temp_N //= 2  # Chia nguyên cho 2

        print(f"{N} (hệ 10) = {binary} (hệ 2)")
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
#Bài 14-40
import numpy as np # type: ignore

try:
    nhap_chieu_cao = input("Nhập chiều cao của sinh viên, cách nhau bởi dấu phẩy: ")
    chieu_cao = [float(x.strip()) for x in nhap_chieu_cao.split(",")]

    if not chieu_cao:
        print("Danh sách chiều cao rỗng.")
    else:
        chieu_cao_np = np.array(chieu_cao)

        cao_nhat = chieu_cao_np[0] # Khởi tạo giá trị cao nhất
        thap_nhat = chieu_cao_np[0] # Khởi tạo giá trị thấp nhất
        tong_chieu_cao = 0
        so_luong_cao_hon_tb = 0

        # Vòng lặp để tính toán
        for h in chieu_cao_np:
            if h > cao_nhat:
                cao_nhat = h
            if h < thap_nhat:
                thap_nhat = h
            tong_chieu_cao += h

        trung_binh = tong_chieu_cao / len(chieu_cao_np)

        for h in chieu_cao_np: #Duyệt lại để đếm số người cao hơn trung bình
            if h >= trung_binh:
                so_luong_cao_hon_tb +=1

        print(f"Chiều cao sinh viên cao nhất: {cao_nhat} m")
        print(f"Chiều cao sinh viên thấp nhất: {thap_nhat} m")
        print(f"Chiều cao trung bình của lớp: {trung_binh:.2f} m")
        print(f"Số lượng sinh viên cao hơn hoặc bằng chiều cao trung bình: {so_luong_cao_hon_tb}")

except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập số hợp lệ.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
         