import argparse
import sys

from CalcRating import CalcRating
from CalcQuartile import CalcQuartile
from TextDataReader import TextDataReader
from JSONDataReader import JSONDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if path.endswith(".json"):
        reader = JSONDataReader()
    else:
        reader = TextDataReader()

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    third_quartile = CalcQuartile(students).get_students_in_third_quartile()
    print("Third quartile students: ", third_quartile)


if __name__ == "__main__":
    main()
