#VD-5
a = 10
b = 8
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
thuong_nguyen = a // b
thuong_du = a % b
mu = a ** b

print(tong, hieu, tich, thuong, thuong_nguyen, thuong_du, mu)
#vd-8
a = 10
b = 8
#--Kết quả của phép so sánh có kiểu dữ liệu Boolean---
print('1) Lớn hơn (a > b):', a>b)
print('2) Nhỏ hơn (a < b):', a<b)
print('3) Bằng (a == b):', a==b)
print('4) Lớn hơn hoặc bằng (a>=b):',a>=b)
print('5) Nhỏ hơn hoặc bằng (a<=b):',a<=b)
print('6) Khác (a!=b):',a!=b)
#vd-9
#--Các toán tử logic trong Python:
x = 15
y = True
kt = (x>3) and (x<10) #hoặc: kt = (x>3) & (x<10)
kt2 = (x>3) or (x<10) #hoặc: kt2 = (x>3) | (x<10)
kt3 = not y
print('1) Phép toán AND:', kt)
print('2) Phép toán OR:', kt2)
print('3) Phép toán NOT:', kt3)
#vd11
#--Câu lệnh điều kiện
so_tien = input('Nhập vào số tiền bạn có: ')
so_tien = int(so_tien)
if (so_tien >= 1000000000):
    print('Bạn đã là một tỷ phú!')
else:
    print('Bạn còn phải kiếm nhiều tiền hơn!')
#12
num = 3
if num > 0:
    print(num, "là số dương.")
print("Thông điệp này luôn được in.")
num = -1
if num > 0:
    print(num, "là số dương.")
print("Thông điệp này luôn được in.")
#13
def kiem_tra_so_chan_le(N):
  """Hàm kiểm tra số N là chẵn hay lẻ
  Args:
    N: Số nguyên cần kiểm tra
  Returns:
    Chuỗi thông báo kết quả
  """
  if N % 2 == 0:
    return "Đây là số chẵn!"
  else:
    return "Đây là số lẻ!"
# --Nhập số nguyên từ người dùng
N = int(input("Nhập vào một số nguyên N: "))
# --Gọi hàm kiểm tra và in kết quả
ket_qua = kiem_tra_so_chan_le(N)
print(ket_qua)
#14
num = 3
if num >= 0:
    print("So duong")
else:
    print("So am")

num = -1
if num >= 0:
    print("So duong")
else:
    print("So am")
#15
N = int(input("Nhập vào một số nguyên N: "))
if N % 2 == 0:
    print(N, "là số chẵn.")
else:
    print(N, "là số lẻ.")   
#17
gioi_tinh = int(input("Nhập giới tính (0=Nam, 1=Nữ): "))
if gioi_tinh == 0:
  print("Chào anh đẹp trai!")
elif gioi_tinh == 1:
  print("Chào chị xinh gái!")
else:
  print("Cảnh báo: Giới tính không xác định!")
#18
  num = float(input("Nhập một số: "))
if num >= 0:
    if num == 0:
        print("Số Không")
    else:
        print("Số dương")
else:
    print("Số âm")
 #25
n = int(input('Em sinh tháng mấy?'))
i = 1
while(i <= n):
    print(i, ') I Love You!')
    i = i + 1
print('-----HUMG-----')
#26
n = int(input('Em sinh tháng mấy?'))
i = 1
while(i<=n):
    print(i, ') I Love You!')
    if (i==3):
        break
    i = i + 1
print('-----HUMG-----')
#27
n = 20
i = 1
while (i<=n):
    i = i + 1
    if (i%3==0):
        continue
        #Bỏ qua các câu lệnh phía sau nếu ko chia hết cho 3
    print(i)
#Câu lệnh lặp ngoài vòng lặp while
print('-----HUMG-----')
#28
# chỉ cho phép nhập tháng sinh 1 - 12
while True:
    n = int(input('Em sinh tháng mấy?'))
    if (1<= n <= 12):
        # 'Tháng sinh nhập vào hợp lệ!'
        break;
    print('Tháng không đúng, vui lòng nhập lại')

# Câu lệnh ngoài vòng lặp while
print('Chào em cô gái tháng', n)
#29
n = 10
tich = 1
tong = 0
for i in range (1, n+1):
#Mỗi Lần Lặp biến i tăng lên 1
 tich = tich*i
 tong = tong+i
print ('10! = ', tich)
print('10+ = ', tong)
#30
st = 'HUMG IN MY MIND'
for i in st:
    print('ký tự:', i)

st = 'HUMG IN MY MIND'
dem = 0
for i in st:
    if (i == 'M'):
        dem = dem + 1
print('Số ký tự M có trong chuỗi là: ', dem)   
#31
hoc_sinh = ['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy', 'Trần Thanh Thủy', 'Kiều Thành Công']
print('Danh sách học sinh bao gồm:')
tt = 1
for i in hoc_sinh:
    print(tt, ')', i)
    tt = tt + 1
#33
#Lệnh for với range()
for i in range(5):
    print('i = ',i)

#Lệnh for với range(m,n)
for i in range(5,10):
    print('i = ',i)

#Lệnh for với range(m,n,d)
for i in range(2,11,2):
    print('i = ',i)  
#34
# Hiển thị bảng cửu chương từ 2 -> 9
for i in range(2, 10):
    print('Bảng cửu chương', i)
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)
    print('--------------------') # Dấu phân cách giữa các bảng cửu chương      






