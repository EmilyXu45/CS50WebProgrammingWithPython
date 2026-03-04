import functions
# can also from filename/module import function: from functions import square

for i in range (10):
    print(f"The square of {i} is {functions.square(i)}")
    # or simply square(i) if the imported function is specified