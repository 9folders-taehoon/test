import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

version = 3.5


def print_version_info():
    print(f"The version of this game is {version}")


print("initializing game...")
