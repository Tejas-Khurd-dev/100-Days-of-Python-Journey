def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "Please enter first and last name properly"
    elif f_name == "":
        return "Please enter first name properly"
    elif l_name == "":
        return "Please enter last name properly"
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"Formatted Name: {formated_f_name} {formated_l_name}"


print(format_name(input("Enter your first name: "), input("Enter your last name: ")))

