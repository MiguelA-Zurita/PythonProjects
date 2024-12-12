if __name__ == "__main__":
    print("Dime un número")
    A = int(input())
    print("Dime otro número")
    B = int(input())
    print("Dime otro número más")
    C = int(input())
    if A > B and A > C and B > C:
        print(f"El orden de los números de mayor a menor es: {A},{B}, {C}")
    if A > B and A > C and C > B:
        print(f"El orden de los números de mayor a menor es: {A},{C}, {B}")
    if B > A and B > C and A > C:
        print(f"El orden de los números de mayor a menor es: {B},{A}, {C}")
    if B > A and B > C and C > A:
        print(f"El orden de los números de mayor a menor es: {B},{C}, {A}")
    if C > A and C > B and A > B:
        print(f"El orden de los números de mayor a menor es: {C},{A}, {B}")
    if C > A and C > B and B > A:
        print(f"El orden de los números de mayor a menor es: {C}, {B}, {A}")