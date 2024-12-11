from settings import setting
from modules.students import Students
from modules.auto_typ import AutoTyp


def main(path) -> None:
    students = Students(path)
    students.execute()
    # auto_typ = AutoTyp(students.title, students.notes)


if __name__ == "__main__":
    file = input("ファイル名を入力してください:")
    path = f"students/{file}.txt"
    main(path)
    # a = AutoTyp(file, [])
    # a.execute()