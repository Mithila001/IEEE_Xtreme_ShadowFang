from io import StringIO
import sys
from Question1.main import main

def run_test_case(input_data: str, expected_output: str):
    orig_stdin = sys.stdin
    orig_stdout = sys.stdout
    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()
    try:
        main()
        out = sys.stdout.getvalue()
    finally:
        sys.stdin = orig_stdin
        sys.stdout = orig_stdout
    assert out == expected_output
    # # ------ Uncomment the following line if testing are too strict about float precision ------
    # assert abs(float(out.strip()) - float(expected_output.strip())) < 1e-6
    # assert out.strip() == expected_output.strip()

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




