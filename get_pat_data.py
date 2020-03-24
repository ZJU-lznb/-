# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import csv
import requests
from urllib.request import quote
g_sheet = None
g_file = None
g_count = 0
name_xls  =''
class get_patent_data_csv:
    def __init__(self):
        global name_xls
        key = input('请输入需要查询的关键词')
        page = input('请给出需要的页数')
        name_xls = input('保存名称')

        pageint = int(page)
        header = ['序号','专利号','类型','名称','链接','发明机构','摘要']#date 专利号
        with open('{0}.csv'.format(name_xls),'a',newline='',encoding='UTF-8')as f:
            f_csv = csv.DictWriter(f, header)
            f_csv.writeheader()
        a = get_patent_data_csv.download_pat_info(self, key, pageint)


# 下载专利信息 主函数
    def download_pat_info(self,key,pageCnt):
        global g_count
        eachPageUrls = []

        keyUrl = quote(key)
        baseUrl = 'http://www2.soopat.com/Home/Result?SearchWord=' + keyUrl + '&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'

        for i in range(0, pageCnt):
            if i != 0:
                # 第一页序号不一样
                url = baseUrl + '&PatentIndex=' + str(i * 10)
            else:
                url = baseUrl
            eachPageUrls.append(url)
            print(url)

        for url in eachPageUrls:
            print(g_count)
            req = requests.get(url)
            req.encoding = 'utf-8'
            html = req.text
            table_bf = BeautifulSoup(html, 'lxml')
            try:
                for each in table_bf.find_all('div', attrs={"style": "min-height: 180px;max-width: 1080px;"}):  # attrs={'scope':"col"}):
                    # print(each.get_text())
                    content = {}
                    # 序号
                    g_count += 1
                    content['序号'] = (str(g_count))#g_count指代序号
                    typeblock = each.find('h2')
                    type = typeblock.find('font')
                    # [发明]
                    nameAndDate = typeblock.find('a')
                    date = nameAndDate.find('font', attrs={"size": "-1"})
                    list = nameAndDate.get_text().split(' - ')
                    # 201910993873.X
                    date = list[1]

                    name = list[0]
                    content['专利号'] = (date)
                    # 类型
                    content['类型'] = (type.get_text()[1:])
                    # 名称
                    content['名称'] = (name)
                    # 链接
                    content['链接'] = ('http://www2.soopat.com' + nameAndDate['href'])
                    # XXX有限责任公司
                    head = each.find('span', attrs={"class": "PatentAuthorBlock"})
                    company = head.find('a')
                    content['发明机构'] = (company.get_text())
                    # 摘要正文
                    text = each.find('span', attrs={"class": "PatentContentBlock"})
                    content['摘要'] = (text.get_text())
                    print()
                    get_patent_data_csv.write_csv(self, content)
                    # print(content)
            except Exception as aa:
                print(aa)

    def write_csv(self,date):
        header = ['序号','date','类型','名称','链接','发明机构','摘要']
        global name_xls
        with open('{0}.csv'.format(name_xls),'a',newline='',encoding='UTF-8')as f:
            f_csv = csv.DictWriter(f,header)
            f_csv.writerow(date)



if __name__ == '__main__':

    hd = get_patent_data_csv()

    print('保存完成')