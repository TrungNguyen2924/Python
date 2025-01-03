#Bài1
n = int(input("Nhập vào số kẹo của cô: "))
m = int(input("Nhập vào số học sinh trong lớp: "))
kẹo_mỗi_học_sinh = n // m
kẹo_còn_lại = n % m
print(f"Mỗi học sinh nhận được {kẹo_mỗi_học_sinh} cái kẹo.")
print(f"Số kẹo còn lại là {kẹo_còn_lại}.")

#Bài2
ho_ten = input("Nhập vào họ tên: ").strip().upper()
nam_sinh = int(input("Nhập vào năm sinh: "))
#.. Tính tuổi
from datetime import date
nam_hien_tai = date.today().year
tuoi = nam_hien_tai - nam_sinh
#..In kết quả
print(f"Bạn \"{ho_ten}\" năm nay {tuoi} tuổi!")

#Bài3
# Nhập số tháng
x = int(input("Nhập vào số tháng: "))
# Tính số thỏ (tăng gấp đôi sau mỗi tháng)
so_tho = 2 ** x
# Hiển thị kết quả
print(f"Trong rừng có: {so_tho} con thỏ")

#Bài4
# Chuỗi văn bản
van_ban = """Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"""
# 1. Đếm số ký tự trong đoạn văn
so_ky_tu = len(van_ban)
print(f"Số ký tự trong đoạn văn: {so_ky_tu}")
# 2. Kiểm tra sự xuất hiện của các từ
tu_ho_chi_minh = "hồ chí minh" in van_ban.lower()
tu_non_song = "non sông" in van_ban.lower()
print(f"Có chứa 'hồ chí minh': {tu_ho_chi_minh}")
print(f"Có chứa 'non sông': {tu_non_song}")
# 3. Tách đoạn văn thành các câu bởi dấu chấm
cau = [c.strip() for c in van_ban.split('.') if c.strip()]
print("Các câu trong đoạn văn:")
for idx, c in enumerate(cau, 1):
    print(f"- Câu {idx}: {c}")
# 4. Đếm số ký tự không phải chữ và số
so_ky_tu_dac_biet = sum(1 for c in van_ban if not c.isalnum() and not c.isspace())
print(f"Số ký tự đặc biệt trong đoạn văn: {so_ky_tu_dac_biet}")
# 5. Thay thế 'Việt Nam' bằng 'VIỆT NAM'
van_ban_moi = van_ban.replace("Việt Nam", "VIỆT NAM")
print("Đoạn văn sau khi thay thế:")
print(van_ban_moi)

#Bài5
# Khởi tạo danh sách điểm
bang_diem = ['C', 'B', 'D', 'A', 'F', 'A', 'B', 'F', 'B', 'C', 'A', 'D', 'F', 'B']
# 1. Số học sinh trong lớp
so_hoc_sinh = len(bang_diem)
print(f"Tổng số học sinh trong lớp: {so_hoc_sinh}")
# 2. Số sinh viên phải học lại môn này (điểm F)
so_hoc_lai = bang_diem.count('F')
print(f"Số sinh viên phải học lại (điểm F): {so_hoc_lai}")
# 3. Số sinh viên có điểm từ B trở lên (A hoặc B)
so_diem_cao = sum(1 for diem in bang_diem if diem in ['A', 'B'])
print(f"Số sinh viên có điểm từ B trở lên: {so_diem_cao}")
# 4. Loại bỏ sinh viên đầu tiên và cuối cùng
bang_diem_moi = bang_diem[1:-1]
print(f"Bảng điểm mới: {bang_diem_moi}")






