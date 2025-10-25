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

def main(): 
    # Solution code goes here
    print("Hello, World!")  # Placeholder implementation



# This line ensures the code runs only when executed normally, 
# but not when imported by the test script.
if __name__ == "__main__": 
    main()