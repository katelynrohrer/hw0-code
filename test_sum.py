
import start_here

def test_add_two_nums():
    assert start_here.add_two_nums(4, 5) == 9
    assert start_here.add_two_nums(4, -2) == 2
    assert start_here.add_two_nums(0, 0) == 0
    assert start_here.add_two_nums(-8, -6) == -14
