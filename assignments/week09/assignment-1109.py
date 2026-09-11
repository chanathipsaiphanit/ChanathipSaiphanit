def calculate_electricity_cost(units):

    service_fee = 25.0

    print("\nรายละเอียดค่าไฟ :")
    
    if units > 200:
        cost1 = 2.50 * 50
        cost2 = 3.00 * 50
        cost3 = 3.50 * 100
        cost4 = 4.00 * (units - 200)
        total_cost = cost1 + cost2 + cost3 + cost4 + service_fee

        print(f"1-50 หน่วย: {cost1:.2f} บาท")
        print(f"51-100 หน่วย: {cost2:.2f} บาท")
        print(f"101-200 หน่วย: {cost3:.2f} บาท")
        print(f"มากกว่า 200 หน่วย: {cost4:.2f} บาท")

    elif units > 100:
        cost1 = 2.50 * 50
        cost2 = 3.00 * 50
        cost3 = 3.50 * (units - 100)
        total_cost = cost1 + cost2 + cost3 + service_fee

        print(f"1-50 หน่วย: {cost1:.2f} บาท")
        print(f"51-100 หน่วย: {cost2:.2f} บาท")
        print(f"101-{int(units)} หน่วย: {cost3:.2f} บาท")

    elif units > 50:
        cost1 = 2.50 * 50
        cost2 = 3.00 * (units - 50)
        total_cost = cost1 + cost2 + service_fee

        print(f"1-50 หน่วย: {cost1:.2f} บาท")
        print(f"51-{int(units)} หน่วย: {cost2:.2f} บาท")

    else:
        cost1 = 2.50 * units
        total_cost = cost1 + service_fee

        if units > 0:
            print(f"1-{int(units)} หน่วย: {cost1:.2f} บาท")

    print(f"ค่าบริการ {service_fee:.2f} บาท")
    print(f"รวมค่าไฟทั้งสิ้น {total_cost:.2f} บาท\n")
