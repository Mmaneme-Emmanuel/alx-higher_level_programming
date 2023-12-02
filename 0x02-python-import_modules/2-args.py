#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("Number of argument(s): 0 arguments.")
    elif num_args == 1:
        print(f"Number of argument(s): 1 argument: \n1: {sys.argv[1]}")
    else:
        print(f"Number of argument(s): {num_args} arguments: ")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
        print()
