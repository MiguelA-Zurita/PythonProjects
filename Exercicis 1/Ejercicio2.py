if __name__ == "__main__":
    print("Dime un número")
    A = int(input())
    print("Dime otro número")
    B = int(input())
    print(f"La suma de estos números es: {A + B}")
    print(f"La resta entre estos números es: {A - B}")
    print(f"La multiplicación entre estos números es: {A * B}")
    try:
        print(f"La división entre estos números es: {A / B}")
    except:
        print("No se puede dividir por 0!")
