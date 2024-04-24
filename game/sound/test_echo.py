def echo():
    print("eeeeecho")


from .echo import echo_test


def z():
    echo_test()
