if __name__ == "__main__":
    print("Dime un número")    
    A = int(input())
    print("Dime otro número")
    B = int(input())
    if A > B:
        print(f"El valor {A} es mayor al valor {B}")
    else:
        if B > A:
            print(f"El valor {B} es mayor al valor {A}")
        print(f"El valor {A} es igual al valor {B}")