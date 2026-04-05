medical_cause=input("Did you have a medical cause?(Y/N): ").strip().upper()

if medical_cause == "Y":
    print("Allowed")
else:
    attendance=int(input("What is your attendance score?"))

    if attendance >= 75:
        print("Allowed")
    else:
        print('Not allowed')