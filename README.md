# HTS_Programming-Mission-12
### 題目網址:[String manipulation](https://www.hackthissite.org/missions/prog/12/)

![](https://i.imgur.com/2ubIwKu.png))

1. 將題目給定的字串中字母與數字分開。
2. 設定數字皆為一位數且計算字串中所有質數和與所有非質數分開和的積 ( product )
3. 取字串中前25個字母並將其 ASCII value 加一（charList）
4. 最後 charList 與 product 連接形成答案
5. 答案格式: nc\$jdw$vx%o%puzznexeijzzt79926
6. 5秒內必須提交答案

### [Selenium Installation Tutorial](https://hackmd.io/Pc0Vxs3oRriemb31mRJneA)
### 解法 : 利用 Selenium 驅動瀏覽器操作網頁

### 程式碼
```python=
from selenium import webdriver #import selenium套件

driver = webdriver.Firefox() #開啟瀏覽器
driver.get('https://www.hackthissite.org/') #到達 HTS 官網
time.sleep(2) #緩衝一下 以免未完全load造成錯誤 (以下相同部分同理)

search_input = driver.find_element_by_name("username") #找到網頁user欄位
search_input.send_keys(info['user']) #輸入帳號
time.sleep(2)

search_input = driver.find_element_by_name("password") #找到網頁pwd欄位
search_input.send_keys(info['pwd']) #輸入密碼
time.sleep(2)

start_search_btn = driver.find_element_by_name("btn_submit") #找到登入按鈕
start_search_btn.click() #按下登入　
time.sleep(2)

driver.get('https://www.hackthissite.org/missions/prog/12/') #到達題目網站

allHtml = driver.page_source #取得題目網站html內容


startPos = str(allHtml).find("String:") #找尋String欄位
endPos = str(allHtml).find("<form")

targetStr = allHtml[startPos+38:endPos-17] #根據網頁內容位移取得單純字串內容

print('str ' + str(targetStr))

numList, charList = numOrChar(targetStr) #判斷字串內數字&字元

numberProduct = calPrime(numList) #計算(質數和)*(非質數和)

shiftedString = shift_ascii(charList) #計算前25個字元 ASCII code + 1 的結果

ans = shiftedString + str(numberProduct) #串接形成答案

ansInput = driver.find_element_by_name("solution") #找到答案欄位
ansInput.send_keys(str(ans)) #輸入答案

submitBtn = driver.find_element_by_name("submitbutton") #找到submit按鈕
submitBtn.click() #submit
```
