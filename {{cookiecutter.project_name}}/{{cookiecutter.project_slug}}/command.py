import argparse


def main():
    """
    {{ cookiecutter.project_name.capitalize() }}

    :param output: Output file.
    """

    parser = argparse.ArgumentParser(description="{{ cookiecutter.project_name.capitalize() | replace('-', ' ') | replace('_', ' ')}}")
    parser.add_argument("-o", "--output", type=str, help="Output file.")
    args = parser.parse_args()

    print("[+]:", args)

    print("[+]:", args.output)


if __name__ == "__main__":
    main()
