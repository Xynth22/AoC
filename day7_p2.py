import itertools
import math

def merge(l, r):
    # Concatenate l and r as strings and convert back to int
    return int(str(l) + str(r))

def evaluate_expression(operands, operators):
    result = operands[0]
    for i in range(1, len(operands)):
        if operators[i-1] == '+':
            result += operands[i]
        elif operators[i-1] == '*':
            result *= operands[i]
        elif operators[i-1] == '||':
            result = merge(result, operands[i])
    return result

def generate_operator_combinations(num_operands):
    operators = ['+', '*', '||']
    return itertools.product(operators, repeat=num_operands - 1)

def is_valid_equation(test_value, operands):
    num_operands = len(operands)
    for operator_combo in generate_operator_combinations(num_operands):
        result = evaluate_expression(operands, operator_combo)
        if result == test_value:
            return True
    return False

def process_input(input_data):
    total_sum = 0
    for line in input_data:
        left, right = line.split(": ")
        test_value = int(left)
        operands = list(map(int, right.split()))

        if is_valid_equation(test_value, operands):
            total_sum += test_value

    return total_sum



#with open("test.txt", "r") as file:
with open("input_day7_p1.txt", "r") as file:
  input_data = file.readlines()


print(process_input(input_data))
    
      

