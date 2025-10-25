# a simple parser for python. use get_number() and get_word() to read
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

def find_first(A, X):
    N = len(A)
    # The result index (0-indexed)
    index = -1
    low = 0
    high = N - 1

    while low <= high:
        mid = low + (high - low) // 2
        
        if A[mid] == X:
            # Match found, store the index and look in the left half 
            # for an even earlier occurrence.
            index = mid
            high = mid - 1
        elif A[mid] < X:
            # X is in the right half
            low = mid + 1
        else: # A[mid] > X
            # X is in the left half
            high = mid - 1
            
    return index

def find_last(A, X):

    N = len(A)
    # The result index (0-indexed)
    index = -1
    low = 0
    high = N - 1

    while low <= high:
        mid = low + (high - low) // 2
        
        if A[mid] == X:
            # Match found, store the index and look in the right half 
            # for an even later occurrence.
            index = mid
            low = mid + 1
        elif A[mid] < X:
            # X is in the right half
            low = mid + 1
        else: # A[mid] > X
            # X is in the left half
            high = mid - 1
            
    return index

def main():
    # 1. Read N (number of elements) and Q (number of queries)
    N = get_number()
    Q = get_number()
    
    if N is None or Q is None:
        # Handle case of empty input
        return

    # 2. Read the sorted array A
    A = []
    for _ in range(N):
        num = get_number()
        if num is not None:
            A.append(num)
        

    # 3. Process Q queries
    import sys
    output = []
    
    for _ in range(Q):
        X = get_number()
        
        if X is None:
            break # Stop if no more query numbers

        # Find the 0-indexed position of the first occurrence
        first_idx = find_first(A, X)

        if first_idx != -1:
            # X is found, so proceed to find the last occurrence
            last_idx = find_last(A, X)
            
            # Convert 0-indexed positions to 1-indexed for output
            first_pos = first_idx + 1
            last_pos = last_idx + 1
            
            output.append(f"{first_pos} {last_pos}")
        else:
            # X is not found
            output.append("-1 -1")

    
    sys.stdout.write('\n'.join(output) + '\n')


if __name__ == "__main__":
    main()