#Bài 1 hàm greating-17
def greeting(full_name: str, birth_year: int) -> str:
    
    from datetime import datetime

    current_year = datetime.now().year
    age = current_year - birth_year

    # Trả về câu chào
    return f"Xin chào {full_name}! Bạn năm nay {age} tuổi."

# Ví dụ sử dụng
print(greeting("Nguyễn Văn A", 1999))
#Bài 2 hàm rabit_count-17
def rabbit_count(months: int) -> int:
    if months <= 0:
        return 0  # Không có tháng thì không có thỏ
    elif months == 1:
        return 1  # Tháng đầu tiên chỉ có một cặp thỏ
    elif months == 2:
        return 1  # Tháng thứ hai cũng chỉ có một cặp thỏ
    # Tính số thỏ theo quy luật Fibonacci
    prev, curr = 1, 1
    for _ in range(3, months + 1):
        prev, curr = curr, prev + curr

    return curr
# Ví dụ sử dụng
print(rabbit_count(10))  # Tính số thỏ sau số tháng
#Bài 3 hàm count_mart-17
def count_mark(grades: list) -> tuple:
    if not grades:
        return 0, 0  # Nếu không có sinh viên, trả về 0, 0
    num_retake = sum(1 for grade in grades if grade < 5)
    total_students = len(grades)
    return num_retake, total_students
# Ví dụ sử dụng
grades = [4.5, 6.0, 3.2, 7.8, 4.0, 8.5, 5.0]
num_retake, total_students = count_mark(grades)
print(f"Số sinh viên học lại: {num_retake}")
print(f"Tổng số sinh viên: {total_students}")
#Bài 4 bmi_show-18
def bmi_show() -> str:
    try:
        height = float(input("Nhập chiều cao (m): "))
        weight = float(input("Nhập cân nặng (kg): "))
    except ValueError:
        return "Vui lòng nhập số hợp lệ cho chiều cao và cân nặng."

    if height <= 0 or weight <= 0:
        return "Chiều cao và cân nặng phải lớn hơn 0."
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        return f"BMI của bạn là {bmi:.2f}. Bạn thuộc nhóm thiếu cân."
    elif 18.5 <= bmi < 24.9:
        return f"BMI của bạn là {bmi:.2f}. Bạn thuộc nhóm cân nặng bình thường."
    elif 25 <= bmi < 29.9:
        return f"BMI của bạn là {bmi:.2f}. Bạn thuộc nhóm thừa cân."
    else:
        return f"BMI của bạn là {bmi:.2f}. Bạn thuộc nhóm béo phì."

print(bmi_show())
#Bài 5 cal_point-18
def cal_point(grades: list) -> tuple:
    if not grades:
        return 0, 0  # Nếu danh sách điểm rỗng, trả về 0 cho cả hai hệ
    avg_10 = sum(grades) / len(grades)
    if avg_10 >= 9:
        avg_4 = 4
    elif avg_10 >= 7:
        avg_4 = 3
    elif avg_10 >= 5:
        avg_4 = 2
    else:
        avg_4 = 1
    return avg_10, avg_4
#VD
grades = [7.5, 8.0, 6.5, 9.0, 7.0]
avg_10, avg_4 = cal_point(grades)
print(f"Điểm trung bình hệ 10: {avg_10:.2f}")
print(f"Điểm trung bình hệ 4: {avg_4}")
#Bài 6 list_prime-18
def list_prime(n: int) -> list:
    primes = []
    # Kiểm tra các số từ 2 đến n
    for num in range(2, n + 1):
        # Kiểm tra xem num có phải là số nguyên tố không
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
# Ví dụ 
n = 20
prime_numbers = list_prime(n)
print(f"Các số nguyên tố từ 1 đến {n}: {prime_numbers}")




