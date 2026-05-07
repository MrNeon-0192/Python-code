def total_calc(bill, tipperc):
    total = bill * (1 + 0.01 * tipperc)
    total = round(total, 2)
    print(f"Please pay ${total}")
    
total_calc(170,17)
