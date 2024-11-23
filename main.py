import time


class Students():
    with open("students/sample.txt", "r", encoding = "utf-8") as file:
        lines = file.read().split("\n")
    students_list = lines


def main():
    students = Students()
    print(Students.students_list)


if __name__ == "__main__":
    main()