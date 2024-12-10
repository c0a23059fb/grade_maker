

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import setting

class auto_typ:
    """LINE WORKSへの自動入力及び投稿を行うクラス"""
    guide = {} # XPATH: 入力文字列の辞書
    def __init__(self, select: str ,notes: list) -> None:
        """
        select: 指定テンプレート名
        notes: 生徒評価の文字列リスト
        """
        self.notes = notes # 生徒評価の文字列リスト
        self.select = select # 指定テンプレート名
        auto_typ.guide = {k: v for k, v in zip(setting.xpaths, notes)} # XPATH: 入力文字列の辞書の要素作成
        self.execute() # 入力及び投稿操作実行

    @classmethod
    def execute(cls) -> None:
        """LINE WORKSへの自動入力及び投稿を行う"""
        pass