from io import StringIO
import sys
from main import main
import time

time_limit: float = 1.0 
def run_test_case(input_data: str, expected_output: str):
    orig_stdin = sys.stdin
    orig_stdout = sys.stdout
    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()
    start_time = time.perf_counter()
    try:
        main()
        out = sys.stdout.getvalue()
    finally:
        end_time = time.perf_counter()
        sys.stdin = orig_stdin
        sys.stdout = orig_stdout

    elapsed_time = end_time - start_time
    # Check for time limit violation (This is local timing, not strict enforcement)
    if elapsed_time > time_limit:
        print(f"⚠️ **Time Limit Exceeded** (Local Estimate): {elapsed_time:.4f}s > {time_limit}s", file=sys.stderr)



    assert out == expected_output
    # # ------ Uncomment the following line if testing are too strict about float precision ------
    # assert abs(float(out.strip()) - float(expected_output.strip())) < 1e-6
    # assert out.strip() == expected_output.strip()


    #Report time
    print(f"Test successful. Time: {elapsed_time*1000:.4f}ms", file=sys.stderr)

# -------------------------------------------------------------------------------

## Example test case template that you can copy and modify for your tests

# def test_descriptive_name():
#     # 1. Define the Problem Input
#     input_data = (
#         "Line 1 of input data\n"
#         "Line 2 of input data\n"
#     )

#     # 2. Define the Expected Output
#     expected_output = "The_Correct_Answer_Here"

#     # 3. Execute the test
#     run_test_case(input_data, expected_output)

# -------------------------------------------------------------------------------

def test_standard_case_duplicates():
    # N=8, Q=1. A = [10, 20, 30, 30, 30, 40, 50, 60]. X = 30.
    # 30's 1-indexed positions are 3 and 5.
    input_data = (
        "8 4\n"
        "2 4 4 4 5 8 10 12\n"
        "4\n"
        "10\n"
        "5\n"
        "11\n"
    )

    # Expected: First at 3, Last at 5
    expected_output = (
        "2 4\n"
        "7 7\n"
        "5 5\n"
        "-1 -1\n"
    )

    run_test_case(input_data, expected_output)

def test_no_match_case():
    # N=5, Q=1. A = [5, 15, 25, 35, 45]. X = 20.
    input_data = (
        "5 1\n"
        "5 15 25 35 45\n"
        "20\n"
    )

    # Expected: Not found
    expected_output = "-1 -1\n"

    run_test_case(input_data, expected_output)

def test_edge_case_first_element():
    # N=7, Q=1. A = [5, 5, 5, 10, 15, 20, 25]. X = 5.
    # 5's 1-indexed positions are 1 and 3.
    input_data = (
        "7 1\n"
        "5 5 5 10 15 20 25\n"
        "5\n"
    )

    # Expected: First at 1, Last at 3
    expected_output = "1 3\n"

    run_test_case(input_data, expected_output)




# 4. Edge Case - Last Element (with Duplicates) - FIXED
def test_edge_case_last_element():
    # N=6, Q=1. A = [10, 20, 30, 40, 50, 50]. X = 50.
    # 50's 1-indexed positions are 5 and 6.
    input_data = (
        "6 1\n"
        "10 20 30 40 50 50\n"
        "50\n"
    )

    # Expected: First at 5, Last at 6 (FIXED: Added '\n')
    expected_output = "5 6\n"

    run_test_case(input_data, expected_output)

# 5. Single Element Array - FIXED
def test_single_element_array():
    # N=1, Q=1. A = [99]. X = 99.
    input_data = (
        "1 1\n"
        "99\n"
        "99\n"
    )

    # Expected: First at 1, Last at 1 (FIXED: Added '\n')
    expected_output = "1 1\n"

    run_test_case(input_data, expected_output)

# 6. Full Array Match - FIXED
def test_full_array_match():
    # N=5, Q=1. A = [7, 7, 7, 7, 7]. X = 7.
    # 7's 1-indexed positions are 1 and 5.
    input_data = (
        "5 1\n"
        "7 7 7 7 7\n"
        "7\n"
    )

    # Expected: First at 1, Last at 5 (FIXED: Added '\n')
    expected_output = "1 5\n"

    run_test_case(input_data, expected_output)

# 7. Negative Numbers - FIXED
def test_negative_numbers():
    # N=7, Q=1. A = [-50, -40, -40, -30, -20, -10, -5]. X = -40.
    # -40's 1-indexed positions are 2 and 3.
    input_data = (
        "7 1\n"
        "-50 -40 -40 -30 -20 -10 -5\n"
        "-40\n"
    )

    # Expected: First at 2, Last at 3 (FIXED: Added '\n')
    expected_output = "2 3\n"

    run_test_case(input_data, expected_output)

# 8. Large Numbers and Missing Boundary Case - NEW
def test_large_and_missing_numbers():
    # N=6, Q=2. A = [10000, 20000, 20000, 30000, 30000, 40000].
    # Q1: X=30000 -> 4 5
    # Q2: X=15000 (Missing) -> -1 -1
    input_data = (
        "6 2\n"
        "10000 20000 20000 30000 30000 40000\n"
        "30000\n"
        "15000\n"
    )

    expected_output = (
        "4 5\n"
        "-1 -1\n"
    )

    run_test_case(input_data, expected_output)




