from selenium import webdriver #import selenium套件
import time
from config import *

#check if n is prime number
def isPrime(n):
	count = 0
	if n == 2:
		return True
	if n%2 == 0 or n <=1:
		return False
	for i in range(2,n-1):
		#print(i)
		if n % i ==0:
			count+=1
	if count == 0:
		return True
	else:
		return False

def numOrChar(string):
	numbers = []
	letters = []
	for ch in string:
		if str(ch).isdigit():
			numbers.append(ch)
		else:
			letters.append(ch)
	return numbers,letters
	
	
def calPrime(number_list):
	prime_numbers = []
	composite_numbers = []
	for num in number_list:
		if isPrime(int(num)):
			prime_numbers.append(int(num))
		else:
			composite_numbers.append(int(num))
	
	composite_numbers = [i for i in composite_numbers if i !=1 ]
	composite_numbers = [i for i in composite_numbers if i !=0 ]
	
	return sum(prime_numbers) * sum(composite_numbers)
	
def shift_ascii(char_list):
	char_list = char_list[:25]
	result = ''
	for char in char_list:
		x = ord(char)
		result += chr(x+1)
	return result


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

print(ans)

ansInput = driver.find_element_by_name("solution") #找到答案欄位
ansInput.send_keys(str(ans)) #輸入答案


submitBtn = driver.find_element_by_name("submitbutton") #找到submit按鈕
submitBtn.click() #submit

