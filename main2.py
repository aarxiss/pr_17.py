from math_utils import Calculator

calc = Calculator()

def get_input():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

while True:
    print("\n=== Калькулятор ===")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    choice = input("Оберіть операцію (1-5): ")

    if choice == "5":
        print("Завершення роботи.")
        break

    if choice in ["1", "2", "3", "4"]:
        a, b = get_input()
        if choice == "1":
            print("Результат:", calc.add(a, b))
        elif choice == "2":
            print("Результат:", calc.subtract(a, b))
        elif choice == "3":
            print("Результат:", calc.multiply(a, b))
        elif choice == "4":
            print("Результат:", calc.divide(a, b))
    else:
        print("Невірний вибір. Спробуйте ще раз.")
