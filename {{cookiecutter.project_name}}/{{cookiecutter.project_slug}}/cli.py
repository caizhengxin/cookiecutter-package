import argparse

from {{cookiecutter.project_slug}} import __version__


def main():
    """
    {{ cookiecutter.project_name.capitalize() }}

    :param output: Output file.
    """

    parser = argparse.ArgumentParser(description="{{ cookiecutter.project_name.capitalize() | replace('-', ' ') | replace('_', ' ')}}")
    parser.add_argument("-v", "--version", action='version', version=f'%(prog)s {__version__}', help="Version")
    args = parser.parse_args()

    print("[+]:", args)


if __name__ == "__main__":
    main()
