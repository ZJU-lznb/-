import csv
#'序号', '专利号', '类型', '名称', '链接', '发明机构', '摘要', '关键词'
#能够将CSV转化为列表，其中每一个位置都是一条专利信息
def csv_to_dict(filename):#能够将CSV转化为列表，其中每一个位置都是一条专利信息
    with open('{0}.csv'.format(filename),'r' ,encoding='utf-8') as f:
        data = csv.DictReader(f)
        print()
        pat_list = []
        num = 2
        for i in data:   #存入相应代码块
            newdict = {}
            newdict['序号'] = i['序号']
            newdict['专利号'] = i['date']
            newdict['类型'] = i['类型']
            newdict['名称'] = i['名称']
            newdict['链接'] = i['链接']
            newdict['发明机构'] = i['发明机构']
            newdict['摘要'] = i['摘要']
            newdict['关键词'] = i['关键词']
            pat_list.append(newdict)
            if i == None:
                break
    return pat_list

a = csv_to_dict('废弃物test')#输入文件名，返回列表
print(a)


'''
date = pd.to_datetime(data['日期'], format='%Y-%m-%d')
plt.figure(figsize=(20,5))
plt_data = date.dt.year.value_counts().sort_index()
plt.bar(plt_data.index, plt_data.values)
plt.plot(plt_data.index, plt_data.values, 'r')
plt.xlabel('年份',fontsize=12)
plt.ylabel('专利申请数量',fontsize=12)
plt.title('专利申请数量的年度分布',fontsize=12)
plt.show()'''
