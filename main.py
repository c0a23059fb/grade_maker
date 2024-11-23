import time


class Students():
    with open("students/sample.txt", "r", encoding = "utf-8") as file:
        lines = file.read().split("\n")
    students_list = lines
    if len(students_list) == 0:
        print("生徒が存在しません")

    def __init__(self) -> None:
        self.grades = {i:"" for i in __class__.students_list}

    def value(self) -> None:
        flag = True

        while flag:
            values = input(f"整数を{len(self.grades)}桁を入力")
            if len(values) == len(self.grades):
                for i, j in enumerate(self.grades.keys()):
                    if values[i] not in "0123":
                        print("不正な数値です")
                        break
                    self.grades[j] += values[i]
                    print(j, self.grades[j])
                else:
                    flag = False
            else:
                print("入力が不正です")

            if not flag:
                print(self.grades)
                break

    # def identify(self):
    #     for i in self.grades.keys():


def main():
    students = Students()

    print("生徒のモチベーションを評価してください")
    students.value()
    print("生徒の理解力を評価してください")
    students.value()
    print("生徒の授業態度を評価しください")
    students.value()

    print(students.grades)


if __name__ == "__main__":
    main()