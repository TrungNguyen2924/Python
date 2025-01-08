#bai 16: 
class Person:
    def __init__(self, name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight
    
    def Getting(self):
        print("Thông tin: ")
        print(f"Name: {self.name}")
        print(f"Year of Birth: {self.year}")
        print(f"Height: {self.height} m")
        print(f"Weight: {self.weight} kg")
    
    def Bmi(self):
        if self.height <= 0:
            return "Chiều cao phải lớn hơn 0 để tính BMI."
        bmi_value = self.weight / (self.height ** 2)
        return round(bmi_value, 2)

def get_input():
    while True:
        try:
            print("Nhập thông tin")
            name = input("Vui lòng nhập tên: ")
            if any(char.isdigit() for char in name):
                raise ValueError("Tên không được chứa số.")
                
            year = int(input("Vui lòng nhập năm sinh: "))
            height = float(input("Vui lòng nhập chiều cao (m): "))
            weight = float(input("Vui lòng nhập cân nặng (kg): "))
            
            # Kiểm tra năm sinh, chiều cao và cân nặng có hợp lệ không
            if year <= 0 or height <= 0 or weight <= 0:
                raise ValueError("Năm sinh, chiều cao và cân nặng phải > 0.")
                
            return name, year, height, weight
            
        except ValueError as e:
            print(f"Lỗi nhập liệu: {e}. Vui lòng nhập lại.")

def main():
    name, year, height, weight = get_input()
    person = Person(name, year, height, weight)
    
    while True:
        print("\nChọn hành động:")
        print("1. Hiển thị thông tin")
        print("2. Tính chỉ số BMI")
        print("3. Thoát")
        
        try:
            choice = int(input("Nhập lựa chọn của bạn (1/2/3): "))
            
            if choice == 1:
                person.Getting()
            elif choice == 2:
                bmi = person.Bmi()
                print(f"BMI: {bmi}")
            elif choice == 3:
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ.")

# Chạy chương trình
main()

#bai17: Đọc/Ghi file
# Đọc dữ liệu từ file dayso1_bai17.txt
with open('D:\Python\PythonGit\dayso1.txt', 'r') as file:
    # Giả sử dữ liệu trong file là một dãy số cách nhau bởi dấu phẩy
    data = file.read().strip()
    numbers = list(map(int, data.split(' ')))

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = max(numbers)
min_value = min(numbers)

# Tìm chỉ số của phần tử lớn nhất và nhỏ nhất xuất hiện đầu tiên
max_index = numbers.index(max_value)
min_index = numbers.index(min_value)

# Đổi chỗ phần tử lớn nhất và nhỏ nhất
numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

# Lưu dãy mới vào file dayso2_bai17.txt
with open('D:\Python\PythonGit\dayso2.txt', 'w') as file:
    file.write(' '.join(map(str, numbers)))

print("Đã đổi chỗ thành công và lưu vào file dayso2.txt")
