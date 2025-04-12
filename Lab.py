Total = int(input("Enter your Total: "))
if Total >= 100:
    print("Century")
elif Total >= 90:
    print("Ninety")
elif Total >= 80:
    print("Eighty")
elif Total >= 70:
    print("Seventy")
elif Total >= 60:
    print("Sixty")
else:
    print("Fifty")
    for Total in range(1, 51):  
        print("Failed")