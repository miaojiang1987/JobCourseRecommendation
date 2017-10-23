import urllib.request
import re
import time
import random
import sys
from selenium import webdriver #
import time

#-*- coding: utf-8 -*-  
# USER_AGENTS = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
# ]
# # give a random user-agents
# ra=random.randint(0, len(USER_AGENTS))
# headers ={'User-Agent':USER_AGENTS[ra]}



#start time
time_start=time.time();

# give the list of job ID
job_id=['389861378','445768897','389861378','435429391','432139389','448626733','435426640']

countA=0#first random counter(short period visit limitation)
countB=0#second random counter(long period visit limitation)
countC=0#third random counter(sleep period visit limitation)
sum=0#total number of visits

#open browser(the Firefox broswer is required)
web=webdriver.Firefox()

#login
web.get('https://www.linkedin.com/uas/login?fromSignIn=true&trk=uno-reg-guest-home')
web.find_element_by_name("session_key").send_keys("xinkaokao4@163.com")
web.find_element_by_name("session_password").send_keys("413672751")
web.find_element_by_name("signin").click()
time.sleep(3)

i=str(random.randint(400000000, 459999999))
#for i in job_id:
while 1+1>1:
	url=('https://www.linkedin.com/jobs/view/%s'%(urllib.parse.quote(i)))
	#open url
	web.get(url)
	time.sleep(1)
	try:#whether relogin or not
		web.find_element_by_name("login-submit").click()
	except:#don't need login
		sum=sum+1
		clock=time.time()-time_start
		print('total visits:%d total time:%ds speed:%f/min'%(sum,clock,sum/clock*60))
	else:#relogin
		web.get('https://www.linkedin.com/uas/login?fromSignIn=true&trk=uno-reg-guest-home')
		#web.find_element_by_name("session_key").send_keys("")
		#web.find_element_by_name("session_password").send_keys("")
		web.find_element_by_name("signin").click()
		time.sleep(3)
		web.get(url)
	#crawling
	countA=countA+1
	countB=countB+1
	countC=countC+1

	#read content
	sleeptime=random.uniform(3,20)
	time.sleep(sleeptime)
	html=web.page_source.encode('utf-8')
	if sys.getsizeof(html)>100000:
		#save all text
		file_object = open('C:/Users/Lan/Downloads/test/%s.html'%i, 'wb')
		file_object.write(html)
		file_object.close( )
	else:
		print(i)
		file_object = open('C:/Users/Lan/Downloads/test/wrong.txt', 'w+')
		file_object.write("%s\n"%i)
		file_object.close( )
	i=str(random.randint(400000000, 459999999))
	# give a random visit time
	visitrandom=random.randint(0, 10)

	# give the max times of visiting

	#open url time
	if countA>25-visitrandom:
		sleeptime=random.randint(30, 100)
		time.sleep(sleeptime)
		countA=0

	#read time
	elif countB>120-visitrandom:
		sleeptime=random.randint(240, 500)
		time.sleep(sleeptime)
		countA=0;
		countB=0;

	#sleep time
	elif countC>2000-visitrandom*50:
		sleeptime=random.randint(1000, 3000)
		time.sleep(sleeptime)
		countA=0;
		countB=0;
		countC=0;

	
