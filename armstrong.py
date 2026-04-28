def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    return armstrong_sum == num

input_num = int(input("Enter a number: "))
if is_armstrong(input_num):
    print("Armstrong")
else:
    print("Not an Armstrong number")
