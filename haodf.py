import requests
from bs4 import BeautifulSoup
import re
import random
import  time
from xml.dom.minidom import Document
class Spider():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    def __spider(self):
        list = []
        for i in range(1, 35):
            link = 'https://zixun.haodf.com/dispatched/all.htm?p=' + str(i)
            response = requests.get(link, headers=self.headers, verify=False, timeout=10)
            # 每爬一个页面设置 休眠时间，若不设置会导致很多403
            time.sleep(random.randint(0, 3))
            print(str(i), 'status_code:', response.status_code)
            html_text = response.text
            soup = BeautifulSoup(html_text, 'lxml')
            item = soup.select('ul > li[class="clearfix"] > span')
            for count in range(0, 60, 2):
                list_temp = []
                try:
                    item_user = str(item[count]).split('a>')[1]
                    link = re.findall(r'href="(.*?)"', item_user)  # 帖子链接
                    title = re.findall(r'<a .*?>(.*?)</', str(item_user), re.S)  # 帖子标题
                    doctor_link_page = re.findall(r'href="(.*?)"', str(item[count + 1]))  # 帖子链接
                    doctor_name = re.findall(r'<a .*?>(.*?)</a>', str(item[count + 1]))  # 帖子标题
                    list_temp = [link[0], title[0], doctor_name[0], doctor_link_page[0]]
                    list.append(list_temp)
                except:
                    continue
        return list
    def __write_xml(self,list):
        #创建dom文档
        doc = Document()

        # 创建根节点
        orderlist = doc.createElement('orderlist')
        doc.appendChild(orderlist)

        for item in list:
            # 创建一个order结点，并插入到根节点上

            order = doc.createElement('order')
            orderlist.appendChild(order)

            #link结点
            link = doc.createElement('link')
            link_text = doc.createTextNode(item[0])
            link.appendChild(link_text)
            order.appendChild(link)

            #title结点
            title = doc.createElement('title')
            title_text = doc.createTextNode(item[1])
            title.appendChild(title_text)
            order.appendChild(title)

            #doctor结点
            doctor = doc.createElement('doctor')
            doctor_text = doc.createTextNode(item[2])
            doctor.appendChild(doctor_text)
            order.appendChild(doctor)

            #doctor_page结点
            doctor_link_page = doc.createElement('doctor_link_page')
            doctor_link_page_text = doc.createTextNode(item[3])
            doctor_link_page.appendChild(doctor_link_page_text)
            order.appendChild(doctor_link_page)

        with open('haohf','wb+') as f:
            f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))
        return

    def go(self):
        list = self.__spider()
        self.__write_xml(list)

spider = Spider()
spider.go()


















'''

list = []
for i in range(1,35):
    link = 'https://zixun.haodf.com/dispatched/all.htm?p='+str(i)
    response = requests.get(link, headers=headers, verify=False,timeout = 10)
    # 每爬一个页面设置 休眠时间，若不设置会导致很多403
    time.sleep(random.randint(0, 3))
    print(str(i),'status_code:',response.status_code)
    html_text = response.text
    soup = BeautifulSoup(html_text,'lxml')
    item = soup.select('ul > li[class="clearfix"] > span')
    for count in range(0,60,2):
        list_temp = []
        try:
            item_user = str(item[count]).split('a>')[1]
            link = re.findall(r'href="(.*?)"', item_user)  # 帖子链接
            title = re.findall(r'<a .*?>(.*?)</', str(item_user), re.S)  # 帖子标题
            doctor_link_page = re.findall(r'href="(.*?)"', str(item[count+1]))  # 帖子链接
            doctor_name = re.findall(r'<a .*?>(.*?)</a>',str(item[count+1]))  # 帖子标题
            list_temp = [link[0], title[0], doctor_name[0], doctor_link_page[0]]
            list.append(list_temp)
        except:
            continue

print(len(list))
print(list)

'''

















