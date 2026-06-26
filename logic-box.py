while True:
    print("Welcome to pattern genertaor and number analyzer")
    print("Select an option:")
    print("1. Right angled triangle")
    print("2. Pyramid")
    print("3. Left-angeled triangel")
    print("4. Analyze a range of number:")
    choice = int(input("Enter your choice:"))
    if choice <= 0:
        print("invalid choice")
        continue
    elif choice == 1:
        print("your choose 1")
        rows = int(input("Enter Number of rows:"))
        if rows <= 0:
            print("invalid rows:")
            continue
        for i in range(1, rows+1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()


    elif choice == 2:
        print("your choose 2")
        rows = int(input("Enter Number of rows:"))
        if rows <= 0:
            print("invalid rows:")
            continue
        for i in range(rows):
            for space in range(rows - i - 1 ):
                print(" ", end=" ")
            for j in range(2* i + 1):
                print("*", end=" ")
            print()

    elif choice == 3:
        print("your choose 3")
        rows = int(input("Enter Number of rows:"))
        if rows <= 0:
            print("invalid rows:")
            continue
        for i in range(1, rows + 1):
            for space in range(rows - i + 1 ):
                print(" ", end=" ")
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == 4:
        print("your choose 4")
        start = int(input("enter your starting number: "))
        end = int(input("enter your ending number: "))
        if end < start:
            print("starting number should be greater")
            continue
        total = 0
        for i in range(start, end + 1):
            if i == 0:
                pass
            elif i % 2 == 0:
                print(f"number {i} is even")
            else:
                print(f"number {i} is odd")
            total += i
        print(f"sum of numbers from{start} to {end} is: {total}")
    elif choice == 5:
        print("thank you")
        break
    else:
        print("invalid choice") 


    
        
    


















