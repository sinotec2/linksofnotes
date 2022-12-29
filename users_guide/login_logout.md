---
layout: default
title: 系統登入與登出
parent: Users Guide
nav_order: 1
date: 2022-12-27
last_modified_date: 2022-12-27 11:00:45
---

# 系統登入與登出

{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>
---

## 背景

- OpenKM可以說擁有KMS領域的最大open source社群 ，其他KMS或有免費版本，但並未提供程式碼，OpenKM的社群版本雖然也提供了專業版和雲端版，但是廠商還是鼓勵社群可以就其程式碼自行修改，以滿足使用者的需求，並且在此歷程提供必要的協助。
- 依據2019/7/26日[官網論壇](https://forum.openkm.com/index.php)WHO IS ONLINE：
  - In total there are 374 users online, 
  - 4 registered, 0 hidden and 370guests (based on users active over the past 5 minutes)
  - Most users ever online was 1263 on Mon Jan 28, 2019 7:29 pm。
- 其forum發表情形：STATISTICS
  - Total posts 31953/ Total topics 6010/ Total members 3419
- 其市佔情形：
  - aimed at all industries, regardless of company size.
  - has made over 6,500 installations worldwide
  - Community version has a monthly average of 5,000 downloads.
- Buyers
  - ABC hospitals/ Cherokee Nation/ Deloitte/ DGT/ Factor Energia
  - Modria/ Sernageomin/ United States Government/ Ypergas/ Zoetis。
- 詳見[有關KM決策的建議.pdf][km_dcs]
- OpenKM與其他KMS的比較，可以參考wiki 或網友 的介紹。
- 使用手冊除了官網([6.4][6.4]、[7.1][7.1])之外，亦有泰國機關所摘寫的英文版手冊([OKM6.4][OKM6.4])
- 其他：可詳見[quick start][qs]

## 登入系統

### 網址

- 開啟瀏覽器(chrome/firefox/IE/safari等)
  1. 網址: http://openkm.sinotech-eng.com:8080/OpenKM
  2. 或網址: http://200.200.12.191:8080/OpenKM
- 說明：
  1. 開頭200.200.XXX.XXX均為「內部」網站，與公司資訊安全之管理(檔案進出公司防火牆)「無關」下載後送出公司外部時、或由外部獲得資料上載到KM，進出公司之際還是必須遵守公司資安設定。
  2. 200.200.12.191(master)為備份、屬試驗性質，必要時才開放，請勿存放文件。

![](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/login.png?raw=true)

### 使用者帳密

1. 名稱:員工編號(4碼)，例如4139
2. 密碼:email的帳號(@左方之名稱)加上員編，例如:yckuang@mail.sinotech-eng.com，密碼就先設成yckuang4139。
3. 登入後在「工具」「選項」中修改。
4. 「第一次」瀏覽器會詢問是否儲存密碼
  - 如果是個人桌機，此處強列建議儲存密碼，會省事很多。
  - 如果瀏覽器不能儲存密碼，可能原因：
    1. 瀏覽器設定為對所有網站、永不儲存密碼，或
    2. 瀏覽器設定對特定網站不儲存密碼(第一次詢問時答否，瀏覽器就會被設定永不儲存該一網站的密碼)，
    3. 必須進入瀏覽器的「設定」中將儲存密碼打開，或在永不儲存特定網站處，將本網站排除。
5. OpenKM系統中修改密碼：

- 進入系統後
  1. 在「工具」(Tools)→
  2. 「選項」(Preferences)→
  3. 「用戶配置」，可更改個人密碼、信箱(下述)等設定。
- 唯「角色」的設定是管理者權限範圍，被分配到某一(些)群組，須由管理者來修改。

|![pw1](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/passwd1.png?raw=true)|![pw2](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/passwd2.png?raw=true)|
|:-:|:-:|
|進入修改密碼畫面之途徑|修改密碼之對話框|

### 語言

- 有4種可以選。中、英、法、西等。
- 主要影響為畫面指令
- 即使選英文、檔名如為中文字也可以顯示，只有在進行翻譯是才會有差別。

###	登入

- 按下Login鍵之後就可以登入了。

## 刷新與重複登入

- 由於系統對設定、目錄檔案的增刪有可能會有些時間差落後，因此系統提供了2個方式刷新
  - 「文件」→刷新，以及「桌面」「個人看板」上方有小工具「刷新」。
  - 按下瀏覽器的「重新整理」系統也會重新載入設定，但「不會」登出，要登出還是要按照下列步驟。

![redraw](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/redraw.png?raw=true)

### 重覆登入

- 同一使用者在同一IP或不同IP重覆登入，
  - 並沒有什麼特別的問題，系統會按時間自動更新。
  - 只要電腦的時鐘保持正確。
- 重複登入是否造成錯誤
  - 因系統為即時更新，即使重複登入，系統只會回應最新的更新、修改等指令。
- 同一IP、同一權限等級的不同使用者登入：系統不允許，前一使用者會強制登出。

## 登出系統

1. 關閉網頁即可、或
2. 由File(文件)→Exit(退出)→Accept(接受)
3. 系統會出現「已經正確關閉」對話框
4. 開著網頁沒有存取，OpenKM紀錄是有差別的，所以不必擔心掛網有什麼後果。

[6.4]: <https://docs.openkm.com/kcenter/view/okm-6.4/> "OpenKM(2016)Documentation for OpenKM"
[7.1]: <https://docs.openkm.com/kcenter/view/okm-7.1/> "OpenKM(2016)Documentation for OpenKM"
[OKM6.4]: <https://www.seameo.org/seameoweb2/images/stories/Programmes_Projects/OpenKM/OpenKM%20User%20Guide.pdf> "Southeast Asian Ministers of Education Organization Secretariat (SEAMEO Secretariat) OpenKM Users Guide"
[qs]: <https://docs.openkm.com/kcenter/view/okm-6.3-com/quick-start.html> "OpenKM(2016)OpenKM 6.3 - CE Quick start"
[km_dcs]: <http://openkm.sinotech-eng.com:8080/OpenKM/index.jsp?uuid=1544f8fa-e45a-40a6-bd99-5d2fbef832a1> "曠永銓(2019)有關KM決策的建議"
