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

    def __init__(self, title: list ,notes: list, note_name: str) -> None:
        """
        title: ファイルから読み取れるタイトル
        notes: 生徒評価の文字列リスト
        note_name: 投稿ノート名
        """
        self.notes = {k: v for k, v in zip(__class__.xpaths, notes)} # 生徒評価の文字列リスト
        self.template = self.select_template(title) # 指定テンプレート名
        if self.template == "": # テンプレートが見つからない場合に終了
            print("適当なテンプレートが見つかりませんでした")
            exit()
        self.note_name = note_name
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
                        for k in setting.courses: # コース特定
                            if k in j and k in title[0]:
                                return j
        else:
            return ""

    def login(self) -> None:
        """ログイン"""
        self.driver.get(setting.login_url) # ログインページへ
        # ID入力欄が表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.ID, "user_id")))
        self.driver.find_element(By.ID, "user_id").send_keys(setting.id) # IDを入力
        self.driver.find_element(By.ID, "loginStart").click() # ログインボタンをクリックしてパスワード入力へ
        # パスワード入力欄が表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.ID, "user_pwd")))
        self.driver.find_element(By.ID, "user_pwd").send_keys(setting.password) # パスワードを入力
        self.driver.find_element(By.ID, "loginBtn").click() # ログインボタンをクリックしてログイン

    def setting_template(self) -> None:
        """テンプレート指定"""
        self.driver.get(setting.note_url) # ノート作成ページへ
        # セレクトボックスが表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select_box")))
        self.driver.find_element(By.CLASS_NAME, "subject_input").send_keys(self.note_name) # 投稿タイトル入力
        self.driver.find_element(By.CLASS_NAME, "select_box").click() # テンプレート選択肢を表示
        # 指定テンプレートを選択
        for select in self.driver.find_elements(By.CLASS_NAME, "posts_list li a"):
            if self.template in select.text:
                select.click()

    def set_note(self) -> None:
        """ノート入力"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='note_editor']/div/div[3]/iframe")))
        iframe = self.driver.find_element(By.XPATH, "//*[@id='note_editor']/div/div[3]/iframe")
        self.driver.switch_to.frame(iframe) # iframeへ切り替え
        self.driver.find_element(By.LINK_TEXT, "作成").click() # テンプレート作成
        self.driver.switch_to.window(self.driver.window_handles[-1]) # 入力用ウィンドウへ切り替え
        # 新ウィンドウが表示されるまで待機
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='iframe']")))
        iframe = self.driver.find_element(By.XPATH, "//*[@id='iframe']")
        self.driver.switch_to.frame(iframe) # iframeへ切り替え

    def typ_note(self) -> None:
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text_wrap")))
        sleep(1)
        for k, v in self.notes.items():
            print(k, v)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, k))).send_keys(v) # 入力
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, k), v)) # 入力完了まで待機
            sleep(0.5)
        self.driver.find_element(By.CLASS_NAME, "btn_text").click() # 完了ボタンをクリックして入力終了
        self.driver.switch_to.window(self.driver.window_handles[0]) # 元のウィンドウへ切り替え

    def post_note(self) -> None:
        """ノート投稿"""
        self.driver.find_element(By.CLASS_NAME, "btn_point").click() # 投稿ボタンをクリック
        # 通知設定用チェックボックス表示まで待機
        check_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[3]/div[2]/div[1]/div/p/input")))
        self.driver.execute_script("arguments[0].click();", check_box)# 通知を送らない
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "OK")))
        self.driver.find_element(By.LINK_TEXT, "OK").click() # OKをクリック

    def execute(self) -> None:
        """通常プロセス"""
        # ログイン
        while True: # ログイン成功までループ
            try:
                self.login()
                self.setting_template() # ノートテンプレート選択
                break
            except:
                print("再試行")

        self.set_note() # テムプレート指定
        self.typ_note() # 入力
        self.post_note() # 投稿
        self.driver.quit() # 終了