import time
print("Petro Jackson\n")




def passgen(passwd):
    tim = str(time.time_ns())
    newval = ""
    t = 5
    while t>0:
        newval+=(tim[len(tim)-t])
        t-=1
    _passwd = ""
    for i in passwd:
        _passwd += str(i)
    return(_passwd+newval)

def run():
    getpass = input("Enter Plaintext: ")

    while len(getpass)==0:
        run()
    else:
        print("Your password: "+passgen(getpass))
        print("\n")

        ask = input("Do you want to continue? [Y/N] ")
        if ask=="y":
            run()
        else:
            exit()
        

run()