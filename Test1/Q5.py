#Write a function called PrintStatus that is passed status code “S”, “M”, “D”, or “U” and returns string “SEPARATED”, “MARRIED”, “DIVORCED”, or “UNMARRIED” respectively. Incase an inappropriate message passed print an appropriate message.
def PrintStatus(code):
    if code == "S":
        print("SEPARATED")
    elif code == "M":
        print("MARRIED")
    elif code == "D":
        print("DIVORCED")
    elif code == "U":
        print("UNMARRIED")
    else:
        print("Incorrect Input")
code=input("Enter the status code:")
PrintStatus(code)