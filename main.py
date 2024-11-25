import time
from sys import exit


class Students():

    def __init__(self, path: str) -> None:
        """
        ファイルを読み込み、生徒情報を初期化する
        path: 生徒名簿が記載されたファイルへのパス
        """
        with open(path, "r", encoding = "utf-8") as file:
            lines = file.read().split("\n")
        students_list = lines
        if len(students_list) == 0:
            print("生徒が存在しません")
            exit()

        self.grades = {i:"" for i in students_list} # 名前と評価の辞書
        self.r_absence = [] # 連絡あり欠席
        self.f_absence = [] # 連絡なし欠席

    def check(self) -> None:
        """生徒の出欠確認を行う"""
        names = [i for i in self.grades]
        while True:
            checks = input("出欠を入力してください(出席:0 連絡あり欠席:1 連絡なし欠席:2):")
            if len(checks) == len(names):
                if not self.input_checker(checks, "012"):
                    print("不正な数値です")
                else:
                    for i, j in enumerate(names):
                        if checks[i] != "0":
                            if checks[i] == "1":
                                self.r_absence.append(j)
                            else:
                                self.f_absence.append(j)
                            del self.grades[j]
                    break
            else:
                print("不正な入力です")

    def value(self) -> None:
        """
        生徒の評価を行う
        評価硬膜は三項目(モチベーション、理解力、授業態度)
        """
        while True:
            values = input(f"整数を{len(self.grades)}桁を入力(高い:3 普通:2 低い:1):")
            if len(values) == len(self.grades):
                if not self.input_checker(values, "123"):
                    print("不正な数値です")
                else:
                    for i, j in enumerate(self.grades):
                        self.grades[j] += values[i]
                    break
            else:
                print("入力が不正です")

    def input_checker(self, string: str, length: str) -> bool:
        for i in string:
            if i not in length:
                return False
        return True

    # def identify(self):
    #     for i in self.grades.keys():


def main() -> None:
    students = Students("students/sample.txt")

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