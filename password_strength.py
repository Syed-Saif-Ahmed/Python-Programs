def cap_check(paswd):
    for i in paswd:
        if i.isupper():
            return True
    return False
def sml_check(paswd):
    for i in paswd:
        if i.islower():
            return True
    return False
def check_len(paswd):
    if len(paswd)>=6 and len(paswd)<=12:
        return True
    return False

def check_num(paswd):
    for i in paswd:
        if i.isdigit():
            return True
    return False
def check_password(paswd):
    st = ""
    if cap_check(paswd) and sml_check(paswd) and check_len(paswd) and check_num(paswd):
        for i in paswd:
            if i.isalnum():
                continue
            st = st + i
    if st != '':
        for i in st:
            if i != '$' and i != '#' and i != '@':
                return False
            continue
        return True
def main():
    p = input("Enter the password ::")
    if check_password(p):
        print("Valid")
    else:
        print("Invalid")
main()