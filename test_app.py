from app import sum_numbers

def test_sum_numbers():
    a = sum_numbers(2,3)
    assert a == 5, "Should be 5"

if __name__ == "__main__":
    test_sum_numbers()
