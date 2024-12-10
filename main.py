from settings import setting
from modules.students import Students
from modules.auto_typ import auto_typ


def main(path) -> None:
    students = Students(path)

    #出欠確認
    students.print_students()
    print("生徒の出欠を確認してください")
    students.check()
    print()

    #生徒評価の三項目を入力
    print("生徒のモチベベーション、理解力、授業態度を評価してください")
    students.value()
    print()

    #生徒評価をテンプレ形式へ変換
    students.identify()

    #生徒評価をファイルへ出力
    students.output()


if __name__ == "__main__":
    # path = "students/sample.txt"
    file = input("ファイル名を入力してください:")
    path = f"students/{file}.txt"
    main(path)