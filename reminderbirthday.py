dict={}
while True:
    print("-----Birthday App------")
    print("1.Show birthday")
    print("2.Add to birthday date")
    print("3.Exit")
    choice=int(input("enter the choice"))
    if choice == 1:
        if len(dict.keys())==0:
            print("nothing to show")

        else:
            name=input("enter name to look for birthday")
            birthday=dict.get(name,"no data found")
            print(birthday)
    elif choice == 2:
        name=input("enter friends name")
        data=input("enter birthday date")
        dict[name]=date
        print("birthday added")
    elif choice == 3:
        break
    else:
        print("choose valid option")
                   
