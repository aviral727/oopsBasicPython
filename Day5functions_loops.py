class loops_functions:

    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
    
    for i in range(1, 11):
        if is_even(i):
            print(f"{i} is even")
        else:
            print(f"{i} is odd")