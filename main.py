import argparse


def feature():
    """A tiny feature introduced on feature-1 branch."""
    return "Feature-1: enhanced greeting from demo repository"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--feature', action='store_true', help='Run feature-1')
    args = parser.parse_args()

    if args.feature:
        print(feature())
    else:
        print("Hello from demo repository!")


if __name__ == '__main__':
    main()
