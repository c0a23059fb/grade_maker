from settings import setting
from modules.students import Students
from modules.auto_typ import AutoTyp


def main(path) -> None:
    students = Students(path)
    students.execute()
    # auto_typ = AutoTyp(students.title, students.notes)


if __name__ == "__main__":
    # file = input("ファイル名を入力してください:")
    # path = f"students/{file}.txt"
    # main(path)
    # a = AutoTyp(file, [])
    # a.execute()
    lis = ["武蔵小杉-マイクラ", "土", "2部"]
    liss = [["A"], ["B"], ["C"], ["D"]]
    aut_typ = AutoTyp(lis, liss)
    aut_typ.execute()