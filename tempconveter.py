unit = input("Enter which to which temperature you want to convert C to F press 1 or F to C press 2: ").strip().upper()

a = int(input("Enter temperature to convert: "))
if unit == '2':
    c = (a - 32) * 5/9
    print(f"{a} F is {c:.2f} C")
elif unit == '1':
    f = (a * 9/5) + 32
    print(f"{a} C is {f:.2f} F")