import xlrd
import xlwt
'''
print(name_list)
print(name_list[0],name_list[-1])
print(list(name_list[0]),list(name_list[-1]))
'''

#print(table.row_values(2)[2:3])
#print(table.row_values(2)[:13])

class Copy():

    '''
    数据表格指针获取
    '''
    data0 = xlrd.open_workbook('total.xlsx')
    data1 = xlrd.open_workbook('needwrite.xlsx')
    def __obtain_seed(self):
        name_list = []
        table = Copy.data1.sheets()[2]
        nrows = table.nrows
        for i in range(nrows):
            if i < 2:
                continue
            name_list.append(table.row_values(i)[1:2])
        return name_list

    def __obtain_matching_col(self,name_list):
        match_key = {}
        list_ce = []
        # 表格中三张sheet的行数为nrow0/nrow1/nrow2
        table0 = Copy.data0.sheets()[0]
        nrows0 = table0.nrows
        table1 = Copy.data0.sheets()[1]
        nrows1 = table1.nrows
        table2 = Copy.data0.sheets()[2]
        nrows2 = table2.nrows
        for i in range(nrows0):
            name = table0.row_values(i)[1:2]
            for j in range(len(name_list)):
                if name == name_list[j]:
                    match_key.update({j:i+1000})

        for i in range(nrows1):
            name = table1.row_values(i)[1:2]
            for j in range(len(name_list)):
                if name == name_list[j]:
                    match_key.update({j:i+2000})

        for i in range(nrows2):
            name = table2.row_values(i)[1:2]
            for j in range(len(name_list)):
                if name == name_list[j]:
                    match_key.update({j:i+3000})

        for i in match_key.keys():
            if match_key[i] < 2000:
                list_ce.append(table0.row_values(match_key[i] - 1000)[1:2])
            if match_key[i] > 3000:
                list_ce.append(table2.row_values(match_key[i] - 3000)[1:2])
            if 2000 < match_key[i] < 3000:
                list_ce.append(table1.row_values(match_key[i] - 2000)[1:2])

        print(list_ce)
        print(name_list)
        print(match_key)
        #print(match_key)
        return match_key

    def __write_excel(self,match_key):
        pass

    def go(self):
        name_list = self.__obtain_seed()
        #  match_key里面的键值对都是整型，而从excel中读取的都是浮点型
        match_key = self.__obtain_matching_col(name_list)
        self.__write_excel(match_key)

        print("下面是匹配失败的几个键值对：")
        list_ce = list(match_key.keys())
        for i in range(299):
            if i not in list_ce:
                print(i)
                print(name_list[i])

        print(len(list(match_key.keys())))
        '''
        print(name_list)
        print(len(name_list))
        print(match_key)
        '''
copy = Copy()
copy.go()