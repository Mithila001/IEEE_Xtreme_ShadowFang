## Hackenthon Provided Template
# DO NOT MODIFY THIS PART
# USE THIS FOR INPUT PARSING
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
    
## END OF PROVIDED TEMPLATE

def solve_case(N):
    # Condition 1: If N is odd, no solution exists.
    if N % 2 != 0:
        return -1
    
    # Condition 2: Special cases for small even N (N=2, N=4)
    # The general solution (N/2 - 2) requires N/2 > 2, so N > 4.
    if N < 6:
        # N=2 and N=4 have no solution with positive distinct integers
        return -1

    # Condition 3: N >= 6 and even.
    # Construction: A = N+2, B = N/2 - 2, C = N/2
    
    # K = N/2
    K = N // 2
    
    A = N + 2
    B = K - 2
    C = K
    
    # Sanity check: ensure all are positive (covered by N >= 6) and distinct
    # N+2 > N/2 > N/2 - 2. All are distinct and positive.
    
    # Return the triplet as a space-separated string
    return f"{A} {B} {C}"

def main(): 
    # Read the number of test cases T
    T = get_number()
    
    # Process each test case
    for _ in range(T):
        N = get_number()
        
        result = solve_case(N)
        print(result)



# This line ensures the code runs only when executed normally, 
# but not when imported by the test script.
if __name__ == "__main__": 
    main()