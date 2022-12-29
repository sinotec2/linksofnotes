---
layout: default
title: 桌面、搜尋及看板
parent: Users Guide
nav_order: 2
date: 2022-12-27
last_modified_date: 2022-12-27 14:27:14
---

# 桌面、文件搜索、個人看板

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

- 登入OpenKM後畫面(`桌面`、如圖)第一行為主功能表、下拉選單
  - `文件(Files)`與一般軟體之`檔案`功能類似
  - `編輯(Edit)`有關檔案安全性、編輯、屬性、與訂閱
  - `工具(Tools)`系統語言、外觀、選項等設定
  - `收藏夾(Bookmarks)`會記錄看過文件的位置，
  - `樣板(Templates)`功能未開放。
- 第二行左側為小工具，下載、列印、開目錄、上傳檔案等等(如下圖)
- 第二行右側有3個頁面(tab)
  - [桌面(Desktop)](#桌面desktop)、[文件搜尋(Search)](#文件搜索)、[個人看板(Dashboard)](#個人看板)，可以自由切換。
  - 管理者另還有`管理面板(Admins)`，來控制整個系統。

![entry_adm1](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/entry_adm1.png?raw=true)

![widget](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/widget.png?raw=true)

## 桌面(Desktop)

- 包括左側[目錄架構](#目錄架構)、[文件列表](#文件列表)、[檔案內容(Preview)](#文件屬性及預覽)等3個區塊與介面。
- 組織循序切換的順序
  1. [目錄架構](#目錄架構)選取檔案的屬性或類別
  2. [文件列表](#文件列表)選取特定目錄、檔案
  3. [檔案內容(Preview)](#文件屬性及預覽)：檢視內容、新增評論等動作。

### 目錄架構

- 「公共文件」(Taxonomy知識分類學)：按檔案內容的知識屬性分類 
  - 建議至少按照Sinotech KM分法，以承接其內容，有必要則另創。
  - Sinotech KM分法
    - 污水處理廠、污水管線工程、自來水工程、水污染整治
    - 環境影響評估及監測 、噪音污染評估防制及設計、空氣污染防制及健康風險、溫減碳排等
    - 土壤及地下水污染調查評估與整治
    - 廢棄物管理規劃、廢棄物處理設施營管服務、產業能資源整合輔導、焚化廠效能提昇整建 
- 「自定義分類」(categories)
  - 可自創檔案夾，不能新增檔案，只能連結。
  - 按屬性、可跨組、共通性的檔案放在這裡。
  - 「新建資料夾」→到「我的文件」選取文件→按右鍵「加以自定義分類」→選取該資料夾。類似公開筆記或個人書架的概念。
- 「詮釋資料」(metadata)將檔案予以評等、分級之後，將在此處彙整。可視為經評鑑後的檔案。
- 「詞典」(Thesaurus同義詞，用來提供關鍵詞選擇用)
- 「樣板」(Template功能未知)
- 「我的文件」存放個人文件的地方，除了ROLE_ADMIN之外，即使開放別人也讀不到，必須複製到公共空間。
- 電子郵件
  - 電子郵件的設定在「工具」→「選項」→「用戶配置」，範例：
  - master /sino4都具有寄信功能

```bash
(i) mail server: mail.sinotech.com.tw
(ii) Mail user name:openkm
(iii) Mail user password:yck4139
(iv) Mail folder:/var/spool/mail
```

- mail.sinotech.com.tw(mail.sinotech-eng.com或imap.gmail.com)(如下圖, deprecated)

```bash
(i) mail server: mail.sinotech.com.tw
(ii) Mail user name:yckuang
(iii) Mail user password:***** (在申請email帳號時設定的密碼)
(iv) Mail folder:Inbox
```

- 經測試必須「Mail configuration OK」

### 文件列表

- 位置在「桌面」中上
- 第一行為所在的目錄(非實質目錄)。此處列表包括項
  1. 目錄(黃色文件夾)、
  2. 檔案(淺藍色文件)、以及
  3. 郵件(白色信封)，可以分別點選。
- 其次漏斗為篩選「過濾」，可以設定名稱、大小、日期、作者、版本等進行篩選。
- 分頁與否，以及排序(反轉)，須在此設定，按表頭並不會作用。
- 勾選同批處理，也可以按detail圖案全選。
- 增加屬性(metadata)：針對文件或目錄的評等。按詮釋資料中的定義來勾選。

![fs_sort](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/fs_sort.png?raw=true)

- 編輯中(紙張+筆)、有評論文件(黃色便利貼)

![comment](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/comment.png?raw=true)

### 文件屬性及預覽

- 位置在「桌面」中下
- 屬性頁面，創建者必須自己加入「關鍵字」，好讓系統可以更快搜索。也可以加入「自定義分類」編輯個人專輯，方便別人查找。
- (文件)備註
  - 可以加入個人的見解、評論、等。
  - 不必特別加註人名、時間，系統會自行加入。
- 文件(資料夾)權限
  - 可以指定個別使用者或群組(角色)，
  - 權限包括讀、寫、刪除、安全(改變權限之權限)。
- 版本：如開放編輯，將會記錄文件編修的過程
- 預覽：詳見下述

## 文件搜索

- OpenKM的搜索包括檔名、全文。
- 進入OpenKM後，如果知道檔案在「公共文件」哪個架構位置，可以由「桌面」左側目錄下手循序點選。
- 如果不知道，可以由左方小工具中的[望遠鏡](#目錄及檔名搜索)下手，尋找資料夾、文件名稱、或類似文件
- 如果還是不知道，可以用右側的文件搜索頁面，搜尋關鍵字、內容、檔案名、人名或其他

### 資料夾及文件查找

- 「桌面」公共文件工具列中的望遠鏡，為目錄及檔名搜索。
  - 目錄及檔名搜索
    - 按照資料夾、或檔案名稱過濾(從左側開始比對、無法進行片語、字詞比對)
    - 可以在對話窗輸入查找，或
  - 先在文件列表中點選某一檔案，查找**類似文件**。
- 只有在「公共文件」中的文件檔案、目錄才可以被找得到。自定義分類中的文件，雖然別的使用者也看得到，但不能查找。

### 全文查找

- 全文、關鍵詞等查找可以在右方的放大鏡旁，或者在「文件搜索」中進行。搜索結果將出現在下方。
- 字詞輸入
  - 中文字詞的前後要加雙引號及星號如`"*健康*"`，
  - 英文則不限。
  - 輸入後必須按`enter`鍵，系統出現「正在更新」隨即在下方出現文件位置及名稱
- 搜索結果可以儲存在左側(保存)或用戶消息中，後者將出現在個人看板。
- 查找搜索之細節將在[下面](https://sinotec2.github.io/OpenKM/users_guide/edit_search/#搜尋功能)詳述。

![search](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/search.png?raw=true)

## 個人看板

- 共有6個頁面：
  1. 個人用戶：鎖定、正編輯修改過、最近下載上傳、訂閱的文件或資料夾。
  2. 郵件：由於未開啟收信功能，此處無作用。
  3. 查詢訊息：前述「文件搜索」的結果，儲存之後將會在此列表，讀過會取消黑體，數字減少。
  4. 公共信息：系統推薦最近被看過最多次的文件，修改最多的文件等等。
  5. 工作流程：類似傳遞單功能。
  6. 關鍵字集：目前關鍵字檔案的多寡、排序，可做整理。

![dash_board](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/dash_board.png?raw=true)

![kw_cloud](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/kw_cloud.png?raw=true)