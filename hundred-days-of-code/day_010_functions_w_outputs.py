#* Functions with Outputs

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    
    #* return keyword means the end of a function
    #* any code after it does not run
    return f"{f_name} {l_name}"

formatted_string = format_name("AngELa", "YU")
print(formatted_string)