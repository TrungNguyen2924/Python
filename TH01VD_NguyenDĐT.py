#trang20
# Hiển thị thông báo chào mừng
print('Chào mừng bạn đến với ngôn ngữ lập trình Python!')
# Nhập tên vào biến name
name = input('Nhập tên của bạn:')
# Hiển thị thông báo
print('Chúc bạn', name, 'sẽ thành thạo Python sau khóa học này!')
#trang23
#khởi tạo biến a = 0; A = 0
a = 0
A = 0

for i in range(1,6):
    print(i)
    a = a + i

#Hiển thị kết quả biến a
print('Giá trị của biến a = ',a)
print('-----------------')

for i in range (1,6,2):
    print(i)
    A = A + i

#HIển thị kết quả biến A
print('Giá trị của biến A = ',A)

#trang38
a = 52348252408
b = 523482034
c = 545354645577
d = a + b + c
print(d)

#trang 46
a = 10
b = 8

#---------------------------------------------------
tong = a + b            # Tổng của hai số (+)
hieu = a - b            # Hiệu của hai số (-)
tich = a*b             # Tích của hai số (*)
thuong = a/b          # Thương của hai số (/)
thuong_nguyen = a//b  # Phép chia lấy phần nguyên (//)
thuong_du = a % b        # Phép chia lấy phần dư (%)
mu = a**b           # Tính giá trị a lũy thừa b (**)

print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Thương:", thuong)
print("Thương nguyên:", thuong_nguyen)
print("Thương dư:", thuong_du)
print("Mũ:", mu)

#trang 47
#Kiểm tra kiểu dữ liệu của biến
x = 1985
y = 3.1415926535
z = 'Dai hoc Mo Dia chat'
n = [5, 7, 9, 8]
b = True
#-----------------------
print('Kiểu dữ liệu biến x: ', type(x))
print('Kiểu dữ liệu biến y:', type(y))
print('Kiểu dữ liệu biến z:', type(z))
print('Kiểu dữ liệu biến n:', type(n))
print('Kiểu dữ liệu biến b:', type(b))

#Kiểu dữ liệu số: a = 123
a = 123
print('Số:', a)
#Kiểu dữ liệu chuỗi ký tự: A = '123'
A = '123'
print('Chuỗi: ', A)

#trang52
st = 'HUMG là Trường đại học hàng đầu tại Việt Nam'
x = 'HUMG' in st
y = 'Python' in st
print('Kết quả kiểm tra HUMG:', x)
print('Kết quả kiểm tra Python:', y)

#trang62
#KHAI BÁO DANH SÁCH LIST
#khai báo danh sách học_sinh gồm các chuỗi tên của học sinh
hoc_sinh=['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy']
print(hoc_sinh)
#Khai báo danh sách diem_chu gồm các chuỗi ký tự
diem = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
print(diem)
#Khai báo danh sách gồm các số nguyên
list_so = [9,5,8,13,0,4,7,-9,11]
print(list_so)
#Khai báo danh sách với nhiều kiểu dữ liệu khác nhau
person_info = ['Mary', 1998, 'Tokyo, Japan', 1.70, 65]
print(person_info)
#Khai báo danh sách rồng
list_rong = []
print(list_rong)

#Truy xuất dữ liệu trong danh sách:
#Hiển thị tên học sinh ở vị trí thứ 3
print('Học sinh vị trí thứ 3: ', hoc_sinh[2])
#hiển thị tên người - chiều cao trong biến person_info
print('Họ tên:', person_info[0],' -Chiều cao:', person_info[3])
#Truy xuất nhiều phần tử trong danh sách
print(list_so[3:8])

#Thay đổi giá trị của một phần tử trong danh sách
hoc_sinh=['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy']
print('Ban đầu:', hoc_sinh)
hoc_sinh[2] = 'Nguyễn Thị Lan Anh'
print('Thay đổi:', hoc_sinh)

list_so = [9,5,8,13,0,4,7,-9,11]
print('Ban đầu: ', list_so)
#Thay giá trị của phần tử cuối cùng trong list = 0
list_so[-1] = 0
print('Thay đổi:', list_so)

list_a = [8, 4, 8, 2]
list_b = [3, 0, 7, 6, 5]
#----Cộng hai danh sách (+)---:
list_ab = list_a + list_b
print('List mới: ', list_ab)

#Lấy độ dài của danh sách list_ab: len(list_ab)
print(list_ab, 'Có số phần tử là: ', len(list_ab))
#Kiểm tra phần tử có thuộc danh sách ko?
print(list_ab)
#Kiểm tra phần tử 0:
bol_0 = 0 in list_ab
print('Phần tử 0 có thuộc list_ab ? ', bol_0)
#Kiểm tra phần tử 9:
bol_9 = 9 in list_ab
print('Phần tử 9 có thuộc list_ab ?', bol_9)

#Thêm phần tử vào danh sách:
print('Danh sách ban đầu: \n', list_ab)
#Thêm vào cuối danh sách:
list_ab.append(10)
print('Danh sách thêm vào cuối:\n', list_ab)
#Thêm vào vị trí bất kỳ trong danh sách
list_ab.insert(1,100)
print('Danh sách thêm vào vị trí thứ 2: \n', list_ab)

#Xóa phần tử khỏi danh sách:
print('Danh sách ban đầu: \n', list_ab)

#Xóa phần tử cuối
list_ab.pop()
print('Danh sách xóa phần tử cuối:\n', list_ab)

#Xóa phần tử tại vị trí số 2
del list_ab[1]
print('Danh sách xóa phần tử ở vị trí số 2: \n', list_ab)

#Xóa phần tử có giá trị 0 xuất hiện đầu tiên
list_ab.remove(0)
print('Xóa phần tử có giá trị 0 đầu tiên: \n', list_ab)

#Đếm số lần xuất hiện của một phần tử trong danh sách:
print('Danh sách ban đầu: \n', list_ab)

#Số lần xuất hiện số 8 trong danh sách
print(' Số 8 xuất hiện: ', list_ab.count(8))

#Số lần xuất hiện số 1 trong danh sách
print(' Số 1 xuất hiện: ', list_ab.count(1))

#Trường hợp số, chuỗi
a = 10                              #Khai báo biến a có giá trị =10
b = a                               # Gán giá trị của biến a cho biến b
b = 5                               # thay đổi giá trị của biến b, bằng giá trị mới
print('Giá trị của biến a: ', a)
print('Giá trị của biến b: ', b)

#Trường hợp danh sách:
ds_a = [4, 5, 8, 9]           #Khai báo danh sách ds_a
ds_b = ds_a                   #Gán giá trị của biến ds_a cho ds_b
ds_b[1] = 10                  #Thay đổi giá trị vị trí số 2 trong ds_b
print('Biến ds_a: ', ds_a)
print('Biến ds_b: ', ds_b)

#Sao chép một danh sách độc lập:
ds_a = [4, 5, 8, 9]       #Khai báo danh sách ds_a
ds_b = ds_a.copy()       #Sao chép ds_a cho ds_b
ds_b[1] = 10              #Thay đổi giá trị vị trí số 2 trong ds_b

#---------------------------------------
print('Biến ds_a: ', ds_a)
print('Biến ds_b: ', ds_b)

#Khai báo biến kiểu dữ liệu Boolean:
x = True
y = False
#Khai báo biến kiểu dữ liệu boolean qua biểu thức
z = 5 > 8
w = 12 == 12
#---------------------------------------
print ('Kiểu dữ liệu của biến x:', type(x), ', Giá trị: ', x)
print ('Kiểu dữ liệu của biến y:', type(y), ', Giá trị: ', y)
print ('Kiểu dữ liệu của biến z:', type(z), ', Giá trị: ', z)
print ('Kiểu dữ liệu của biến w:', type(w), ', Giá trị: ', w)

