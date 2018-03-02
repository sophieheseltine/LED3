# Sample Test passing with nose and pytest

import urllib.request
import requests

def test_pass():
    assert True, "dummy sample test"

filename = "test_data.txt"
with open(filename) as f:
    for line in f.readlines():
        # process line        
        print(line)
        
        
# read the whole file into a buffer
buffer = open(filename).read()
for line in buffer.split('\n'):
    # process line
    print(line)
    
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
r = requests.get(uri).text
print('\n'.join(r.split('\n')[:5]))