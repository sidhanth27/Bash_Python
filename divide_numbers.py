import sys
numerator = int(sys.argv[1]) if len(sys.argv) > 1 else 10
denominator = int(sys.argv[2]) if len(sys.argv) > 2 else 2
try:
    result = numerator // denominator
    print(f"Numerator: {numerator}")
    print(f"Denominator: {denominator}")
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero")