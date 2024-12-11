from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import setting

class AutoTyp:
    """LINE WORKSへの自動入力及び投稿を行うクラス"""
    xpaths = [ # XPATHのリスト
            "//*[@id='component_ec60d218f64f']", # 欠席入力項目のxpath}
            "//*[@id='component_e1dcfe1e89e9']", # モチベーション入力項目のxpath
            "//*[@id='component_7b586f568f51']", # 授業態度入力項目のxpath
            ]

    def __init__(self, title: list[str] ,notes: list) -> None:
        """
        title: ファイルから読み取れるタイトル
        notes: 生徒評価の文字列リスト
        """
        self.notes = notes # 生徒評価の文字列リスト
        self.target = self.selecter # 指定テンプレート名
        self.execute() # 入力及び投稿操作実行
        self.driver = webdriver.Chrome() # ドライバー
        self.wait = WebDriverWait(self.driver, 10) # 待機ドライバーと時間

    def login(self) -> None:
        """対象ページへログイン"""
        self.driver.get(setting.login_url) # ログインページへ
        # ID入力欄が表示されるまで待機してから入力
        self.wait.until(EC.presence_of_element_located((By.ID, "user_id"))).send_keys(setting.id)
        self.driver.find_element(By.ID, "loginStart").click() # ログインボタンをクリックしてパスワード入力へ
        # パスワード入力欄が表示されるまで待機してから入力
        self.wait.until(EC.visibility_of_element_located((By.ID, "user_pwd"))).send_keys(setting.password)
        self.driver.find_element(By.ID, "loginBtn").click() # ログインボタンをクリックしてログイン

    def select_template(self) -> None:
        """テンプレート選択"""
        self.driver.get(setting.note_url) # ノート作成ページへ
        # セレクトボックスが表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select_box")))
        self.driver.find_element(By.CLASS_NAME, "subject_input").send_keys("kafdsl;kj") # 投稿タイトル入力
        self.driver.find_element(By.CLASS_NAME, "select_box").click() # テンプレート選択肢を表示
        target = "武蔵小杉-日-＜マイクラ＞" # 指定したいテンプレート名
        # 指定テンプレートを選択
        for select in self.driver.find_elements(By.CLASS_NAME, "posts_list li a"):
            if target in select.text:
                select.click()

    def execute(self) -> None:
        """通常プロセス"""
        self.login()
        self.select_template()

if __name__ == "__main__":
    # aut_typ = AutoTyp(setting.places_1, []) # インスタンス生成
    AutoTyp.login()