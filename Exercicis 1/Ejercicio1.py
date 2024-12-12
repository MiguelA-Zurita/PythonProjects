if __name__ == "__main__":
    A = 0
    B = 0
    print("Dime un número (Se guarda en A)")
    A = input()
    print("Dime otro número (Se guarda en B)")
    B = input()
    A, B = B, A
    print("Los números se han cambiado.")
    print("A = " + A)
    print("B = " + B)
    


