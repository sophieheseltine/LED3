# Sample Test passing with nose and pytest

def test_pass():
    assert True, "dummy sample test"

filename = "test_data.txt"
with open(filename) as f:
    for line in f.readlines():
        # process line        
        print(line)