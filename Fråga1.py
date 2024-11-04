def calculate_loan():
    property_price = input("property price: ")
    loan = float(input("loan: "))
    interest_rate = float(input("interest rate: "))
    loan_rate = int(loan) /int(property_price) 
    if loan_rate > 0.7:
        amortization_rate = 0.02
    elif loan_rate > 0.5:
        amortization_rate = 0.01
    else:
        amortization_rate = 0 

    amortization = (amortization_rate * int(property_price)) / 12
    interest = (((interest_rate) / 100) * loan) / 12
    total = amortization + interest
    print("")
    print("per month")
    print("--------")
    print("amortization: " , amortization)
    print("interest: " , interest)
    print("total: " , total)


    
    



calculate_loan()