import csv
import xlrd
import xlwt

class Copy():
    '''
    获取表格操作指针
    '''
    data0 = xlrd.open_workbook('shenfenseed.xlsx')
    data1 = xlrd.open_workbook('outschool.xls')
    data2 = xlrd.open_workbook('njupt.xls')

    def __catch_seed(self):
        infor_dict = {}
        table = Copy.data0.sheets()[2]
        rows = table.nrows
        for i in range(rows):
            if i < 2:
                continue
            infor_dict.update({table.row_values(i)[2:3][0]:table.row_values(i)[3:4][0]})
        return infor_dict


    def __csv_table(self,infor_dict):
        list_ans = []
        table1 = Copy.data1.sheets()[0]  #外校
        table2 = Copy.data2.sheets()[0]  #南邮
        rows1 = table1.nrows
        rows2 = table2.nrows

        csvFile = open("C://Users//jvlunl//Desktop//test5.csv", 'w',newline='')
        writer = csv.writer(csvFile)
        #print(len(infor_dict))
        for name,school in infor_dict.items():
            #print(name,school)
            for k in range(rows1):
                if name == table1.row_values(k)[1:2][0]:
                    list_ans.append(name)
                    gonghao = table1.row_values(k)[0:1][0]
                    gonghao = 'pp'+ gonghao  #保证超过15位的身份证号能以文本方式写入
                    writer.writerow((name,school,gonghao))

        csvFile.close()
        return list_ans
        '''
            if school == '南京邮电大学':
                for i in range(rows2):
                    if name == table2.row_values(i)[1:2][0]:
                        number = table2.row_values(i)[0:1][0]
                        writer.writerow((name,school,number))
            else:
                for k in range(rows1):
                    if name == table1.row_values(k)[1:2][0]:
                        number = table1.row_values(k)[0:1][0]
                        writer.writerow((name,school,number))
        csvFile.close()
        '''


    def go(self):
        infor_dict = self.__catch_seed()
        list_ans = self.__csv_table(infor_dict)
        for name,school in infor_dict.items():
            if name not in list_ans:
                print(name)

copy = Copy()
copy.go()



