import sys
sys.path.append('.')
import LEDtest1
from click.testing import CliRunner
from LED3 import cli
from LED3 import parser

def test_command_line_interface():
    ifile = "./data/test_data.txt"
    N, instructions = parser.parseFile(ifile)
    assert N is not None
