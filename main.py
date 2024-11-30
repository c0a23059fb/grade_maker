from os import system
from sys import exit
from time import strftime


class Students():
    """整頓の出欠と評価を管理するクラス"""

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
        self.high = [[], [], []] # モチベーション
        self.normal = [[], [], []] # 理解力
        self.low = [[], [], []] # 授業態度

    def print_students(self, text = "生徒名簿") -> None:
        """生徒名簿を表示する"""
        print(f"\n[{text}]")
        for i, j in enumerate(self.grades):
            print(i, j)
        print()

    def check(self) -> None:
        """生徒の出欠確認を行う"""
        names = [i for i in self.grades]
        while True:
            checks = input(f"整数{len(names)}桁を入力(出席:0 連絡あり欠席:1 連絡なし欠席:2):")
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
            values = input(f"整数{len(self.grades)}桁を入力(高い:3 普通:2 低い:1):")
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
        """入力文字列の正当性を確認する"""
        for i in string:
            if i not in length:
                return False
        return True

    def identify(self):
        """生徒評価を参考にリストへ振り分ける"""
        for i in self.grades:
            count = 0
            for j in self.grades[i]:
                if j == "3":
                    self.high[count].append(i)
                elif j == "2":
                    self.normal[count].append(i)
                else:
                    self.low[count].append(i)
                count += 1

    def output(self) -> None:
        """入力された出欠と評価をファイルへ出力する"""
        date = strftime("%Y%m%d")
        output = f"grade_books\{date}.txt"
        label = ["モチベーション", "理解力", "授業態度"]

        with open(output, "w", encoding = "utf-8") as file:
            #欠席者追記
            file.write("-----[欠席]-----\n")
            if self.r_absence == [] and self.f_absence == []:
                file.write("なし\n")
            else:
                for i in self.r_absence:
                    file.write(f"{i}\n")
                for i in self.f_absence:
                    file.write(f"{i} (無欠)\n")
            file.write("\n")

            #生徒評価三項目出力
            for i in range(3):
                high = ""
                normal = ""
                low = ""

                file.write(f"-----[{label[i]}]-----\n")

                file.write("高い→") # 高い評価
                for j in self.high[i]:
                    high += f"{j}, "
                high = high[:-2] # 最後のカンマを削除
                file.write(f"{high}\n")

                file.write("普通→") # 普通評価
                for j in self.normal[i]:
                    normal += f"{j}, "
                normal = normal[:-2] # 最後のカンマを削除
                file.write(f"{normal}\n")

                if i != 2: # 低い評価
                    file.write("低い→")
                else:
                    file.write("悪い→")
                for j in self.low[i]:
                    low += f"{j}, "
                low = low[:-2] # 最後のカンマを削除
                file.write(f"{low}\n")
                file.write("\n")

        # cmdでファイルを表示
        print()
        system("chcp 65001") # 日本語文字化け対策
        system(f"type {output}") #


def main(path) -> None:
    students = Students(path)

    #出欠確認
    students.print_students()
    print("生徒の出欠を確認してください")
    students.check()

    #生徒評価の三項目を入力
    students.print_students()
    print("生徒のモチベーションを評価してください")
    students.value()
    print("生徒の理解力を評価してください")
    students.value()
    print("生徒の授業態度を評価しください")
    students.value()

    #生徒評価をテンプレ形式へ変換
    students.identify()

    #生徒評価をファイルへ出力
    students.output()


if __name__ == "__main__":
    # path = "students/sample.txt"
    setting = input("ファイル名を入力してください:")
    path = f"students/{setting}.txt"
    main(path)