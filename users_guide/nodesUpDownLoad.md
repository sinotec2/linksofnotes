---
layout: default
title: 節點增減與上下載
parent: Users Guide
nav_order: 3
date: 2022-12-27
last_modified_date: 2022-12-27 14:27:14
---

# 節點(文件夾、文件、郵件、訊息)之增減與上下載

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

- 在OpenKM中所謂的節點(node,包括文件夾、文件、郵件、訊息等)，在資料庫中形成一個單元，其內容則會拆解成個別封包分別儲存，以增加全文搜尋的速度。

## 新建/刪除文件夾

- 使用者可以在具有寫入權限的地方，創建新的文件夾(目錄)或刪除，
  - 位置包括「公共文件」「自定義分類」與個人空間
  - 使用者也可以進行安全管理，決定對哪些角色或使用者個人開啟權限。
- 個人空間不論權限如何設定，其他非管理者個人無法讀取。

## 文件上載

1. 檔案必須有所歸屬，因此必須先點選目錄，再按新增文件(Add document)，
2. 按左側選擇檔案鍵，會開啟window的檔案總管介面，選好檔案後右側會出現檔名，再按Upload即可。(如圖)
3. 如果要再在同一目錄增加檔案，可以在同畫面繼續進行。
4. 「通知用戶」notify to user

![add_new_doc](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/add_new_doc.png?raw=true)

### 通知用戶功能

- 此一通知有廣播的作用，可以將檔案的基本介紹寫在message(通知消息)框架內，選擇使用者、或者群組(角色)，上載的同時就會通知其他人上來看檔案。
- 選擇時要注意是否有勾選「過濾」，如果勾選了，將無名單顯示，須先取消「過濾」才能選擇。
- 如果方向鍵不能作用，試看看不同方向。

![notify_to_users](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/notify_to_users.png?raw=true)

### email通知功能

- 如果伺服器沒有收信的功能，也不會留存寄件備份，可以在external mail address寫下自己的email，這樣OpenKM也會寄一份通知給自己做為備份。
- 由於通知消息的格式語法是html格式，換行必須加註`<br>`，段落設定則為`<p>…</p>`。
- 注意：
- linux OpenKM CE版跨window沒有拉放功能，
- 非管理者沒有批次上傳功能，批次上下載詳[後述]()。
- ZIP上傳可以有批次上傳的效果，但只接受ZIP內英文檔名

## 下載

- 點選要下載的檔案，按滑鼠右鍵Download即可下載到window個人的Download(下載) 目錄。
- 目前OpenKM_CE版還沒有「只允許讀取」卻不能「下載」功能，因此如果有檔案不允許別人下載，建議連讀取都不必開放。

![download](https://github.com/sinotec2/OpenKM/blob/gh-pages/assets/image/download.png?raw=true)
