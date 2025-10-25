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

def find_first(sorted_arr, target_val):
    """Finds the 0-indexed position of the first occurrence of target_val."""
    arr_len = len(sorted_arr)
    result_idx = -1
    start_ptr = 0
    end_ptr = arr_len - 1

    while start_ptr <= end_ptr:
        mid_idx = start_ptr + (end_ptr - start_ptr) // 2
        
        if sorted_arr[mid_idx] == target_val:
            result_idx = mid_idx
            end_ptr = mid_idx - 1  # Look left for an earlier occurrence
        elif sorted_arr[mid_idx] < target_val:
            start_ptr = mid_idx + 1
        else:
            end_ptr = mid_idx - 1
            
    return result_idx

def find_last(sorted_arr, target_val):
    """Finds the 0-indexed position of the last occurrence of target_val."""
    arr_len = len(sorted_arr)
    result_idx = -1
    start_ptr = 0
    end_ptr = arr_len - 1

    while start_ptr <= end_ptr:
        mid_idx = start_ptr + (end_ptr - start_ptr) // 2
        
        if sorted_arr[mid_idx] == target_val:
            result_idx = mid_idx
            start_ptr = mid_idx + 1  # Look right for a later occurrence
        elif sorted_arr[mid_idx] < target_val:
            start_ptr = mid_idx + 1
        else:
            end_ptr = mid_idx - 1
            
    return result_idx

def main():
    """Reads input, processes queries, and prints output."""
    import sys
    
    # 1. Read size_N and num_Q
    size_N = get_number()
    num_Q = get_number()
    
    if size_N is None or num_Q is None:
        return

    # 2. Read the sorted array 'data_array'
    data_array = []
    for _ in range(size_N):
        val = get_number()
        if val is not None:
            data_array.append(val)

    # 3. Process num_Q queries
    res_output = []
    
    for _ in range(num_Q):
        query_X = get_number()
        
        if query_X is None:
            break

        first_occurrence_idx = find_first(data_array, query_X)

        if first_occurrence_idx != -1:
            last_occurrence_idx = find_last(data_array, query_X)
            
            # Convert 0-indexed to 1-indexed
            first_1_based_pos = first_occurrence_idx + 1
            last_1_based_pos = last_occurrence_idx + 1
            
            res_output.append(f"{first_1_based_pos} {last_1_based_pos}")
        else:
            res_output.append("-1 -1")

    # Write all results separated by newlines
    sys.stdout.write('\n'.join(res_output) + '\n')


if __name__ == "__main__":
    main()