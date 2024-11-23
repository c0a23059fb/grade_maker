import time
from sys import exit


class Students():
    with open("students/sample.txt", "r", encoding = "utf-8") as file:
        lines = file.read().split("\n")
    students_list = lines
    if len(students_list) == 0:
        print("生徒が存在しません")
        exit()

    def __init__(self) -> None:
        self.grades = {i:"" for i in __class__.students_list}
        self.r_absence = [] # 連絡あり欠席
        self.f_absence = [] # 連絡なし欠席

    # def check(self) -> None:
    #     """生徒の出欠確認を行う"""
    #     checks = input("出欠を入力してください（出席:0 連絡あり欠席:1 連絡なし欠席:2）")

    #     if len(checks) == len(self.grades):
    #         for i in self.grades:

    def value(self) -> None:
        flag = True

        while True:
            values = input(f"整数を{len(self.grades)}桁を入力(高い:3 普通:2 低い:1)")
            if len(values) == len(self.grades):
                for i, j in enumerate(self.grades.keys()):
                    if values[i] not in "123":
                        print("不正な数値です")
                        break
                    self.grades[j] += values[i]
                    print(j, self.grades[j])
                else:
                    break
            else:
                print("入力が不正です")

    # def identify(self):
    #     for i in self.grades.keys():


def main() -> None:
    students = Students()

    #出欠確認
    print("生徒の出欠を確認してください")
    students.check()

    #生徒評価の三項目を入力
    print("生徒のモチベーションを評価してください")
    students.value()
    print("生徒の理解力を評価してください")
    students.value()
    print("生徒の授業態度を評価しください")
    students.value()

    #生徒評価をテンプレ形式へ変換
    # students.identify()

    print(students.grades)


if __name__ == "__main__":
    main()