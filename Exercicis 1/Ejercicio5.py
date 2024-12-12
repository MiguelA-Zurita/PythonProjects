if __name__ == "__main__":
    print("Dime un número")
    A = int(input())
    print("Dime otro número")
    B = int(input())
    print("Dime un número más")
    C = int(input())
    if A < 0:
        resultado = A*B*C
    else:
        resultado = A+B+C
    print(f"Este es el resultado: {resultado}")

