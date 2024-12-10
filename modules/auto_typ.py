

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import setting

class auto_typ:
    """LINE WORKSへの自動入力及び投稿を行うクラス"""
    xpaths = [ # XPATHのリスト
            "//*[@id='component_ec60d218f64f']", # 欠席入力項目のxpath}
            "//*[@id='component_e1dcfe1e89e9']", # モチベーション入力項目のxpath
            "//*[@id='component_7b586f568f51']", # 授業態度入力項目のxpath
            ]
    def __init__(self, select: str ,notes: list) -> None:
        """
        select: 指定テンプレート名
        notes: 生徒評価の文字列リスト
        """
        self.notes = notes # 生徒評価の文字列リスト
        self.select = select # 指定テンプレート名
        self.execute() # 入力及び投稿操作実行

    @classmethod
    def execute(cls) -> None:
        """LINE WORKSへの自動入力及び投稿を行う"""
        pass