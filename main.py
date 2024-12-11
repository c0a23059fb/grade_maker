from settings import setting
from modules.students import Students
from modules.auto_typ import auto_typ


def main(path) -> None:
    students = Students(path)
    students.execute()


if __name__ == "__main__":
    # path = "students/sample.txt"
    file = input("ファイル名を入力してください:")
    path = f"students/{file}.txt"
    main(path)