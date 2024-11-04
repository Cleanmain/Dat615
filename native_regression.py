def main(): 
    age_as_string = input("What is your age: ")
    age = int(age_as_string)
    print("Your legal status is: " + legal_status(age))


def legal_status(age):
    if age <= 18:
        return "minor"
    elif 18 < age <= 21:
        return "adult"
    elif 21 < age <= 30:
        return "alcohol"
    else:
        return "president"

    
main()


