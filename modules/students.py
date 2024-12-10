from os import system
from sys import exit
from time import strftime


class Students:
    """整頓の出欠と評価を管理するクラス"""
    def __init__(self, path: str) -> None:
        """
        ファイルを読み込み、生徒情報を初期化する
        path: 生徒名簿が記載されたファイルへのパス
        """
        with open(path, "r", encoding = "utf-8") as file:
            lines = file.read().split("\n")
        students_list = lines[1:] # 生徒名簿のリスト
        if len(students_list) == 1 and students_list[0] == "":
            print("生徒が存在しません")
            exit()

        self.title = lines[0].split() # タイトル
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
            for i in self.grades:
                values = input(f"{i}の評価を整数3桁で入力(高い:3 普通:2 低い:1):")
                if len(values) == 3:
                    if not self.input_checker(values, "123"):
                        print("不正な数値です")
                    else:
                        self.grades[i] = values
                else:
                    print("入力が不正です")
            else:
                break

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

    def output(self) -> list[str, str, str]:
        """
        入力された出欠と評価をファイルへ出力する
        出力内容をリストにして返す
        """
        date = strftime("%Y%m%d")
        output = f"grade_books/{date}.txt"
        label = ["モチベーション", "理解力", "授業態度"]
        notes = []

        with open(output, "w", encoding = "utf-8") as file:
            # タイトル出力
            file.write(f"---{self.title[0]} ({self.title[1]}) {self.title[2]}---\n\n")

            #欠席者追記
            file.write("-----[欠席]-----\n")
            r = ""
            f = ""
            if self.r_absence == [] and self.f_absence == []:
                file.write("なし\n")
            else:
                for i in self.r_absence:
                    r += f"{i}\n"
                for i in self.f_absence:
                    f += f"{i}(無欠)\n"
            file.write(r + f + "\n")

            #生徒評価三項目出力
            for i in range(3):
                high = ""
                normal = ""
                low = ""

                file.write(f"-----[{label[i]}]-----\n")

                high += "高い→" # 高い評価
                for j in self.high[i]:
                    high += f"{j}, "
                if high[-1] != "→":
                    high = high[:-2] # 最後のカンマを削除
                high += "\n"

                normal += "普通→" # 普通評価
                for j in self.normal[i]:
                    normal += f"{j}, "
                if normal[-1] != "→":
                    normal = normal[:-2] # 最後のカンマを削除
                normal += "\n"

                if i != 2: # 低い評価
                    low += "低い→"
                else:
                    low += "悪い→"
                for j in self.low[i]:
                    low += f"{j}, "
                if low[-1] != "→":
                    low = low[:-2] # 最後のカンマを削除
                low += "\n"
                note = high + normal + low
                file.write(note + "\n")
                file.write("\n")
                notes.append(note)
            return notes

        # cmdでファイルを表示(cmd実行時用)
        # print()
        # system("chcp 65001") # 日本語文字化け対策
        # system(f"type {output}") # ファイル内容表示


if __name__ == "__main__":
    Students("students/sample.txt")