#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("number of argument(s): 0.")
    elif num_args == 1:
        print(f"Number of argument(s): 1. Argument: \n{sys.argv[1]}.")
    else:
        print(f"Number of argument(s): {num_args}. Arguments: ")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
        print()
