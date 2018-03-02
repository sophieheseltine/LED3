import sys
import click
click.disable_unicode_literals_warning = True


def main(args = None):
    click.echo("Replace this message by putting code into cli.main")
    click.echo("See click documentation")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())