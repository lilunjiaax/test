'''
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
url = 'http://you.ctrip.com/searchsite/Asks?query=%25e5%258d%2597%25e4%25ba%25ac%25e6%2597%2585%25e6%25b8%25b8'

'''
import requests
from bs4 import BeautifulSoup
import re
from xml.dom.minidom import Document

class Spider():

    url = 'http://you.ctrip.com/searchsite/Asks?query=%25e5%258d%2597%25e4%25ba%25ac%25e6%2597%2585%25e6%25b8%25b8'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    def __spider_(self):
        list = []
        response = requests.get(self.url, headers = self.headers, verify=False)
        html_test = response.text
        soup = BeautifulSoup(html_test, 'lxml')
        question_list = soup.select("li > dl > dt")
        # print(question_list)
        inf_list = soup.select("li > dl > dd.color-999")
        for x, y in zip(question_list, inf_list):
            title = re.findall(r'<a .*?>(.*?)</a>', str(x))  # 帖子标题
            link = re.findall(r'href="(.*?)"', str(x))  # 帖子链接

            time = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", str(y))
            user_id = re.findall(r'<a .*?>(.*?)</a>', str(y))
            user_id_page = re.findall(r'href="(.*?)"', str(y))
            '''
            data = {
                'title': title,
                'link': link,
                'id': user_id,
                'id page': user_id_page,
                'time': time,
            }
            print(data)
            '''
            list_temp = [link[0],title[0],user_id[0],time[0],user_id_page[0]]
            list.append(list_temp)
        return list
        #print(list)

    def __write_xml(self,list):
        # 创建dom文档
        doc = Document()

        # 创建根节点
        orderlist = doc.createElement('orderlist')
        doc.appendChild(orderlist)
        # list_temp = [link[0],title[0],user_id[0],time[0],user_id_page[0]]
        for item in list:
            # 创建一个order结点，并插入到根节点上

            order = doc.createElement('order')
            orderlist.appendChild(order)

            # link结点
            link = doc.createElement('link')
            link_text = doc.createTextNode(item[0])
            link.appendChild(link_text)
            order.appendChild(link)

            # title结点
            title = doc.createElement('title')
            title_text = doc.createTextNode(item[1])
            title.appendChild(title_text)
            order.appendChild(title)

            # user_id结点
            user_id = doc.createElement('user_id')
            user_id_text = doc.createTextNode(item[2])
            user_id.appendChild(user_id_text)
            order.appendChild(user_id)

            # time结点
            time = doc.createElement('time')
            time_text = doc.createTextNode(item[3])
            time.appendChild(time_text)
            order.appendChild(time)

            # user_id_page结点
            user_id_page = doc.createElement('user_id_page')
            user_id_page_text = doc.createTextNode(item[4])
            user_id_page.appendChild(user_id_page_text)
            order.appendChild(user_id)

        with open('xie_cheng', 'wb+') as f:
            f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
        return

    def go(self):
        list = self.__spider_()
        self.__write_xml(list)

spider = Spider()
spider.go()









