print ("Hello World")
print("Also print this")


def print_this(x):
    print ("this")
    return x

def test_print_this():
    assert print_this('Semaphore') == 'Semaphore'
