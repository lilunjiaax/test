import xlrd
import xlwt
import csv
import openpyxl
class Copy():

    '''
    数据表格指针获取
    '''
    data0 = xlrd.open_workbook('total.xlsx')
    data1 = xlrd.open_workbook('needwrite.xlsx')
    data_EMS = xlrd.open_workbook('EMS.xlsx')
    data_EMS2 = xlrd.open_workbook('EMS2.xlsx')
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
        for i in range(len(name_list)):
            for j in range(nrows0):
                if table0.row_values(j)[1:2] == name_list[i]:
                    match_key.update({i:1000+j})

            for j in range(nrows1):
                if table1.row_values(j)[1:2] == name_list[i]:
                    match_key.update({i:2000+j})

            for j in range(nrows2):
                if table2.row_values(j)[1:2] == name_list[i]:
                    match_key.update({i:j+3000})

        return match_key
        '''
        for i in match_key.keys():
            
        print(list_ce)
        print(name_list)
        print(match_key)
        #print(match_key)
        return match_key
        :param name_list:
        :return:
        '''
    def __write_excel(self,match_key):
        '''
        table0 = Copy.data0.sheets()[0]
        nrows0 = table0.nrows
        table1 = Copy.data0.sheets()[1]
        nrows1 = table1.nrows
        table2 = Copy.data0.sheets()[2]
        nrows2 = table2.nrows
        for i in match_key.keys():
            if match_key[i] < 2000:
                row = match_key[i] - 1000
                project = table0.row_values(row)[1:13]
                print(project[1])
        '''
        csvFile = open("C://Users//jvlunl//Desktop//test1.csv", 'w')
        writer = csv.writer(csvFile)
        # 采集第一列编号的准备
        table = Copy.data1.sheets()[2]
        nrows = table.nrows
        # 总表格中三张sheet的行数为nrow0/nrow1/nrow2
        table0 = Copy.data0.sheets()[0]
        nrows0 = table0.nrows
        table1 = Copy.data0.sheets()[1]
        nrows1 = table1.nrows
        table2 = Copy.data0.sheets()[2]
        nrows2 = table2.nrows

        # 地址表格1
        table_EMS = Copy.data_EMS.sheets()[0]
        nrows_EMS = table_EMS.nrows


        # 地址表格2中也有三个sheet表
        table0_EMS2 = Copy.data_EMS2.sheets()[0]
        nrows0_EMS2 = table0_EMS2.nrows
        table1_EMS2 = Copy.data_EMS2.sheets()[1]
        nrows1_EMS2 = table1_EMS2.nrows
        table2_EMS2 = Copy.data_EMS2.sheets()[2]
        nrows2_EMS2 = table2_EMS2.nrows

        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
        sheet1.write(0,0,'this is fff')
        #workbook.save(ceshi.xls)
        #writer = csv.writer(csvFile)
        #writer.writerow(('number', 'number pius 2', 'number times 2'))

        for i in match_key.keys():
            if match_key[i] < 2000:
                row = match_key[i] - 1000
                project = table0.row_values(row)[1:13]
                for aa in range(nrows):
                    if project[0] == table.row_values(aa)[1:2][0]:
                        project.append(table.row_values(aa)[0:1])

                for bb in range(nrows_EMS):
                    if project[0] == table_EMS.row_values(bb)[1:2][0]:
                        project.append(table_EMS.row_values(bb)[4:5])
                for cc in range(nrows0_EMS2):
                    if project[0] == table0_EMS2.row_values(cc)[1:2][0]:
                        project.append(table0_EMS2.row_values(cc)[6:7])
                for dd in range(nrows1_EMS2):
                    if project[0] == table1_EMS2.row_values(dd)[1:2][0]:
                        project.append(table1_EMS2.row_values(dd)[6:7])
                for ee in range(nrows2_EMS2):
                    if project[0] == table2_EMS2.row_values(ee)[1:2][0]:
                        project.append(table2_EMS2.row_values(ee)[6:7])
                writer.writerow((project[12], project[0], project[1], project[2], project[3], project[4], project[5],
                                 project[6], project[7], project[8], project[9], project[10], project[11], project[13]))
                continue
            if match_key[i] > 3000:
                row = match_key[i] - 3000
                project = table2.row_values(row)[1:13]
                for aa in range(nrows):
                    if project[0] == table.row_values(aa)[1:2][0]:
                        project.append(table.row_values(aa)[0:1])

                for bb in range(nrows_EMS):
                    if project[0] == table_EMS.row_values(bb)[1:2][0]:
                        project.append(table_EMS.row_values(bb)[4:5])
                for cc in range(nrows0_EMS2):
                    if project[0] == table0_EMS2.row_values(cc)[1:2][0]:
                        project.append(table0_EMS2.row_values(cc)[6:7])
                for dd in range(nrows1_EMS2):
                    if project[0] == table1_EMS2.row_values(dd)[1:2][0]:
                        project.append(table1_EMS2.row_values(dd)[6:7])
                for ee in range(nrows2_EMS2):
                    if project[0] == table2_EMS2.row_values(ee)[1:2][0]:
                        project.append(table2_EMS2.row_values(ee)[6:7])
                writer.writerow((project[12], project[0], project[1], project[2], project[3], project[4], project[5],
                                 project[6], project[7], project[8], project[9], project[10], project[11], project[13]))
                continue
            if 2000 < match_key[i] < 3000:
                row = match_key[i] - 2000
                project = table1.row_values(row)[1:13]
                for aa in range(nrows):
                    if project[0] == table.row_values(aa)[1:2][0]:
                        project.append(table.row_values(aa)[0:1])

                for bb in range(nrows_EMS):
                    if project[0] == table_EMS.row_values(bb)[1:2][0]:
                        project.append(table_EMS.row_values(bb)[4:5])
                for cc in range(nrows0_EMS2):
                    if project[0] == table0_EMS2.row_values(cc)[1:2][0]:
                        project.append(table0_EMS2.row_values(cc)[6:7])
                for dd in range(nrows1_EMS2):
                    if project[0] == table1_EMS2.row_values(dd)[1:2][0]:
                        project.append(table1_EMS2.row_values(dd)[6:7])
                for ee in range(nrows2_EMS2):
                    if project[0] == table2_EMS2.row_values(ee)[1:2][0]:
                        project.append(table2_EMS2.row_values(ee)[6:7])
                writer.writerow((project[12], project[0], project[1], project[2], project[3], project[4], project[5],
                                 project[6], project[7], project[8], project[9], project[10], project[11], project[13]))
                continue
        csvFile.close()

    def go(self):
        name_list = self.__obtain_seed()
        #  match_key里面的键值对都是整型，而从excel中读取的都是浮点型
        match_key = self.__obtain_matching_col(name_list)
        self.__write_excel(match_key)

        '''
        list_ce = list(match_key.keys())
        for i in range(299):
            if i not in list_ce:
                print(i)
                print(name_list[i])

        print(len(list(match_key.keys())))
        '''

        '''
        print(len(name_list))
        print(match_key)
         print(name_list)
        print(len(name_list))
        print(match_key)
        print(len(list(match_key.keys())))
        '''
        print("下面是匹配失败的几行：")
        for i in range(len(name_list)):
            if i not in list(match_key.keys()):
                print(i,name_list[i])


copy = Copy()
copy.go()