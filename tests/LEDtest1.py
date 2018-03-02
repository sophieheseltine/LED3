import sys
sys.path.append('.')
import LEDtest1
from click.testing import CliRunner
from LED3 import cli
from LED3 import parser

def test_read_file():
    ifile = "./test_data.txt"
    N, instructions = parser.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']
