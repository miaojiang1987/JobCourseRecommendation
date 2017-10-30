from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
#-*- coding: utf-8 -*-  

web=webdriver.Firefox()
for i in range(1707,1724):
	if (i==1716):
		continue
	url='http://coursecatalog.syr.edu/content.php?catoid=13&navoid=%d'%i
	url='file:///C:/Users/Lan/Downloads/sucourse/%d.html'%i
	#open url
	web.get(url)
	html=web.page_source
	soup=BeautifulSoup(html.encode('utf-8'),'html.parser')
	title=soup.find_all(id='acalog-page-title')[0].get_text().strip()
	title_out=re.sub(' ','_',title)
	coursenames=soup.find_all('li',style="list-style-type: none")
	print(title)
	pages=re.findall(r'\| <a href="(.*?)">',html)

	#save all text
	file_object = open('C:/Users/Lan/Downloads/sucourse/%s.txt'%title,'w',encoding='utf-8')


	#first page
	for out in coursenames:
		course=out.a.get_text().split('-',1)
		coursenum=course[0].strip()
		coursename=course[1].strip()
		link='http://coursecatalog.syr.edu/%s'%out.a.get('href')
		web.get(link)
		html=web.page_source.encode('utf-8')
		soup=BeautifulSoup(html,'html.parser')
		content=soup.find_all('td',class_="block_content")[0]
		try:
			preq=re.search(r'PREREQ:[\s\S]*?>(.*?)</a>',str(content)).group(1)
		except:
			contents=re.search(r'<br/>([\s\S]*?)<hr/>([\s\S]*?)<hr/>',str(content))
			credit=contents.group(1).strip()
			description=re.sub('<.*?>',' ',contents.group(2)).strip()
			preq='None'						
		else:
			contents=re.search(r'<br/>([\s\S]*?)<hr/>([\s\S]*?)PREREQ',str(content))
			credit=contents.group(1).strip()
			description=re.sub('<.*?>',' ',contents.group(2)).strip()		
		info="%s;%s;%s;%s;%s\n"%(coursenum,coursename,credit,str(description),str(preq))
		file_object.write(info)

	#pages
	for page in pages:
		url='http://coursecatalog.syr.edu%s'%page
		for out in coursenames:
			course=out.a.get_text().split('-',1)
			coursenum=course[0].strip()
			coursename=course[1].strip()
			link='http://coursecatalog.syr.edu/%s'%out.a.get('href')
			web.get(link)
			html=web.page_source.encode('utf-8')
			soup=BeautifulSoup(html,'html.parser')
			content=soup.find_all('td',class_="block_content")[0]
			try:
				preq=re.search(r'PREREQ:[\s\S]*?>(.*?)</a>',str(content)).group(1)
			except:
				contents=re.search(r'<br/>([\s\S]*?)<hr/>([\s\S]*?)<hr/>',str(content))
				credit=contents.group(1).strip()
				description=re.sub('<.*?>',' ',contents.group(2)).strip()
				preq='None'						
			else:
				contents=re.search(r'<br/>([\s\S]*?)<hr/>([\s\S]*?)PREREQ',str(content))
				credit=contents.group(1).strip()
				description=re.sub('<.*?>',' ',contents.group(2)).strip()
			info="%s;%s;%s;%s;%s\n"%(coursenum,coursename,credit,str(description),str(preq))
			file_object.write(info)
	file_object.close()    


         

	
