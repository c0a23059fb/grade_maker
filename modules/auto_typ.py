from sys import exit
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import setting

class AutoTyp:
    """LINE WORKSへの自動入力及び投稿を行うクラス"""
    xpaths = [ # XPATHのリスト
            "//*[@id='component_ec60d218f64f']", # 欠席入力項目のxpath
            "//*[@id='component_e1dcfe1e89e9']", # モチベーション入力項目のxpath
            "//*[@id='component_46db6bb1576f']", # 理解力入力項目xpath
            "//*[@id='component_7b586f568f51']", # 授業態度入力項目のxpath
            ]

    def __init__(self, title: list[str] ,notes: list) -> None:
        """
        title: ファイルから読み取れるタイトル
        notes: 生徒評価の文字列リスト
        """
        self.notes = {k: v for k, v in zip(__class__.xpaths, notes)} # 生徒評価の文字列リスト
        self.template = self.select_template(title) # 指定テンプレート名
        if self.template == "": # テンプレートが見つからない場合に終了
            print("適当なテンプレートが見つかりませんでした")
            exit()
        self.driver = webdriver.Chrome() # ドライバー
        self.wait = WebDriverWait(self.driver, 15) # 待機ドライバーと時間

    def select_template(self, title) -> str:
        """
        指定テンプレート名を返す
        title: Studentsクラスで作成された文字列
        """
        for i in setting.places:
            if i in title[0]: # 場所特定
                for j in setting.places[i]:
                    if title[1] in j: # 曜日特定
                        for k in setting.courses:
                            if k in j and k in title[0]:
                                return j
        else:
            return ""

    def default(self) -> None:
        # ログイン
        self.driver.get(setting.login_url) # ログインページへ
        # ID入力欄が表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.ID, "user_id")))
        self.driver.find_element(By.ID, "user_id").send_keys(setting.id) # IDを入力
        self.driver.find_element(By.ID, "loginStart").click() # ログインボタンをクリックしてパスワード入力へ
        # パスワード入力欄が表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.ID, "user_pwd")))
        self.driver.find_element(By.ID, "user_pwd").send_keys(setting.password) # パスワードを入力
        self.driver.find_element(By.ID, "loginBtn").click() # ログインボタンをクリックしてログイン

        # ノートテンプレート選択
        self.driver.get(setting.note_url) # ノート作成ページへ
        # セレクトボックスが表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select_box")))
        self.driver.find_element(By.CLASS_NAME, "subject_input").send_keys("kafdsl;kj") # 投稿タイトル入力
        self.driver.find_element(By.CLASS_NAME, "select_box").click() # テンプレート選択肢を表示
        target = "武蔵小杉-金-＜ビスケット・スクラッチ＞" # 指定したいテンプレート名
        # 指定テンプレートを選択
        for select in self.driver.find_elements(By.CLASS_NAME, "posts_list li a"):
            if target in select.text:
                select.click()

        # テムプレート作成
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='note_editor']/div/div[3]/iframe")))
        iframe = self.driver.find_element(By.XPATH, "//*[@id='note_editor']/div/div[3]/iframe")
        self.driver.switch_to.frame(iframe) # iframeへ切り替え
        self.driver.find_element(By.LINK_TEXT, "作成").click() # テンプレート作成
        self.driver.switch_to.window(self.driver.window_handles[-1]) # 入力用ウィンドウへ切り替え
        # 新ウィンドウが表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='iframe']")))
        iframe = self.driver.find_element(By.XPATH, "//*[@id='iframe']")
        self.driver.switch_to.frame(iframe) # iframeへ切り替え

        # 入力
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text_wrap")))
        for k, v in self.notes.items():
            self.driver.find_element(By.XPATH, k).send_keys(v) # 入力
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, k), v)) # 入力完了まで待機
        self.driver.find_element(By.CLASS_NAME, "btn_text").click() # 完了ボタンをクリックして入力終了
        self.driver.switch_to.window(self.driver.window_handles[0]) # 元のウィンドウへ切り替え

    def execute(self) -> None:
        """通常プロセス"""
        self.default()