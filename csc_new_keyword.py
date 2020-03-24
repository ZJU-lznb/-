import csv

import jiagu

with open('废弃物回收.csv', 'r', encoding='utf-8') as read:
    count = 1
    text = csv.DictReader(read)
    for i in text:
        print(i)
        #print(type(i))
        #print(i['发明机构'])
        keyword = jiagu.keywords(str(i['摘要']), 5)
        # 写入关键词
        #print(keyword)
        with open('废弃物test.csv', 'a', newline='',encoding='utf-8') as wr:
            i['关键词'] = keyword
            header = ['序号', 'date', '类型', '名称', '链接', '发明机构', '摘要', '关键词']
            r_csv = csv.DictWriter(wr, header)
            if count == 1:
                r_csv.writeheader()
            r_csv.writerow(i)
            wr.close()
        count += 1
        if i == None:
            break
