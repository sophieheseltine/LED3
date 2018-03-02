import sys
import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """ Console script for LED3 """
    print("input", input)
    
    N, instructions = parseFile(input)
    
    ledTester = LEDTester(N)
    for instruction in instructions:
        ledTester.apply(instruction)
        
    print("Number of occupied lights: ", ledTester.countOccupied())
    return 0

if __name__ == "__main__":
    sys.exit(main())