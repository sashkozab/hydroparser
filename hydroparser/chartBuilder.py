#!/usr/bin/env python
# -*- coding: utf8 -*-

import re
import openpyxl
import xlsxwriter
import numpy as np

xlsxFile = "Temperature_water_SeverskyDonets.xlsx"

class Charter:
    def __init__(self,xlsxFile):
        self.xlsxFile = xlsxFile
        self.listOfYears = []
        self.setSheetes = []

    def set_range_of_sheets(self):
        rangeSheetes = input("Please,choose massive of sheetes you want to work with.\nFor example,type: [5:11] or [5:] or [:11]  or just press ENTER to work with all sheetes.")
        wb = openpyxl.load_workbook(self.xlsxFile)
        self.setSheetes = eval("wb.get_sheet_names()" + rangeSheetes)
        if not isinstance(self.setSheetes,list):
            self.setSheetes = [self.setSheetes]
        print(self.setSheetes)
        print("\nTotal number of sheetes you've chosen = {}\n".format(len(self.setSheetes)))

    def parseXLSXfile(self):
        wb = openpyxl.load_workbook(self.xlsxFile)
        sh = wb.worksheets[0]
        if len(self.setSheetes) == 0:self.setSheetes = wb.get_sheet_names()
        for sheetName in self.setSheetes:
            sheet = wb.get_sheet_by_name(sheetName)
            sheetDict = {}
            highestrow = sheet.get_highest_row()
            gutIt = False
            for i in range(4,highestrow+1):
                try:
                    if re.search(r'[0-9]{4}',str(sheet.cell(row=i,column=1).value)):
                        number = 0
                        gutIt = True
                        try:
                            avarege = np.mean(np.array([float(sheet.cell(row=i,column=x).value) for x in range(2,14)]))
                        except TypeError:
                            avarege = None
                        # for x in range(2,14):
                        #     try:
                        #         number += float(sheet.cell(row=i,column=x).value)
                        #     except TypeError:
                        #         pass
                        # avarege = number/12
                        sheetDict.update({int(sheet.cell(row=i,column=1).value) : avarege})
                except (TypeError, ValueError):
                    pass
            if gutIt:
                yield (sheetName,sheetDict)

    def prepareToMethod(self,xlsxGenerator):
        for sheet in xlsxGenerator:
            header = sheet[0]
            sheetDict = sheet[1]
            listOfdata = []
            if len(self.listOfYears) == 0:add = True
            else:add = False
            for k in sheetDict:
                listOfdata.append(sheetDict[k])
                if add:self.listOfYears.append(k)
            yield (header,listOfdata)
        
    

    def prepareToChart(self,Years,listOfDataheader):
        data = []
        headings = []
        for header,values in listOfDataheader:
            #print(listOfDataheader)
            if len(headings) == 0 and len(data) == 0:
                headings.append('Years')
                data.append(Years)
            headings.append(header)
            data.append(values)
        #print("=====>",data)
        return(headings,data)




def createCharts(methodsList,xlsxFile):
    inputXLSXfile = xlsxFile[:-5] + "_Charts.xlsx"
    workbook = xlsxwriter.Workbook(inputXLSXfile)
    for chartData,sheetName,private in methodsList:
        worksheet = workbook.add_worksheet(sheetName)
        bold = workbook.add_format({'bold': 1})
        # Add the worksheet data that the charts will refer to.
        headings = chartData[0]
        data = chartData[1]
        worksheet.write_row('A1', headings, bold)
        for i,valueList in enumerate(data):
            print(i,"<======>",valueList)
            for r,value in enumerate(valueList):
                if isinstance(value,(float,int)) and not np.isnan(value):
                    print(type(value),value)
                    worksheet.write(r + 1, i, value)
                else:
                    print(type(value),value)
        print(len(headings),len(data))
        # Create a new chart object. In this case an embedded chart.
        chart1 = workbook.add_chart({'type': 'line'})
        # Configure the series.
        rowdistance = len(data[0])+5
        coldistance = 0
        count = 1
        for i in range(1, len(data)):
            if private:
                chart1 = workbook.add_chart({'type': 'line'})
                chart1.add_series({
                'name':       [sheetName, 0, i],
                'categories': [sheetName, 1, 0, len(data[0]), 0],
                'values':     [sheetName, 1, i, len(data[0]), i],
                'marker': {'type': 'diamond'},
                'trendline': {'type': 'linear'},
                })
                chart1.set_size({'width': 700, 'height': 500})
                # Add a chart title and some axis labels.
                chart1.set_title ({'name': headings[i]})
                chart1.set_x_axis({'name': headings[0]})
                chart1.set_y_axis({'name': 'Something'})
                # Set an Excel chart style. Colors with white outline and shadow.
                chart1.set_style(10)
                # Insert the chart into the worksheet (with an offset).
                worksheet.insert_chart(rowdistance, coldistance, chart1, {'x_offset': 25, 'y_offset': 10})
                if count % 7 == 0:
                    rowdistance += 30
                    coldistance = 0
                else:
                    coldistance += 12
                count += 1
            else:
                chart1.add_series({
                'name':       [sheetName, 0, i],
                'categories': [sheetName, 1, 0, len(data[0]), 0],
                'values':     [sheetName, 1, i, len(data[0]), i],
                'marker': {'type': 'diamond'},
            })
        if not private:
            chart1.set_size({'width': 2000, 'height': 1000})
            # Add a chart title and some axis labels.
            chart1.set_title ({'name': sheetName})
            chart1.set_x_axis({'name': headings[0]})
            chart1.set_y_axis({'name': 'Samething'})
            # Set an Excel chart style. Colors with white outline and shadow.
            chart1.set_style(10)
            # Insert the chart into the worksheet (with an offset).
            worksheet.insert_chart(0,len(headings), chart1, {'x_offset': 250, 'y_offset': 100})

    workbook.close()


class GydroGenMethod:
    """Using Gydro Genethich method in flow calculation"""
    empcount = 0

    def __init__(self,Q):
        self.Q = Q
        GydroGenMethod.empcount += 1
        #print ("Q:----->",self.Q)

    def rizn_inter_kruvi(self):
        calculate_list = []
        Q_array = np.array(self.Q)
        #print (Q_array.sum())
        Qfllist = [x for x in self.Q if isinstance(x, float)]
        lenQfllist = len(Qfllist)
        print("Qfllist: ",Qfllist,lenQfllist)
        Qav = np.mean(Qfllist)                       #Q_array.sum()/len(self.Q)
        print("Qav = ",Qav)
        sumQ = ((Qfllist - Qav)**2).sum()
        print ("sumQ",sumQ)
        lastValue = None
        for i,q in enumerate(self.Q):
            if not lastValue and q:
                lastValue = q/Qav - 1
                calculate_list.append(lastValue)
                #print ((q/Qav - 1))
                continue
            elif not q:
                calculate_list.append(None)
            else:
                calculate_list.append(q/Qav - 1 + lastValue)
                lastValue += q/Qav - 1
        Ki_array = np.array(calculate_list)
        print ("Ki_array",list(Ki_array))
        y = np.sqrt(sumQ/(lenQfllist-1))/Qav
        #rizn_int_kr = Ki_array / (np.sqrt(sumQ/(lenQfllist-1))/Qav)
        #print ("riznintkruvi:---->",rizn_int_kr)

        rizn_int_kr = [float("{0:.2f}".format(x/y)) if x is not None else None for x in Ki_array]
        #print("======>",rizn_int_kr)
        return rizn_int_kr

    def sumCurves(self):
        curveList = []
        lastValue = None
        for i,value in enumerate(self.Q):
            if not lastValue and value:
                curveList.append(value)
                lastValue = value
            elif lastValue and value:
                curveList.append(value + lastValue)
                lastValue += value
            else:
                curveList.append(None)
        return curveList

def build_charts():
    outputFile = Charter(xlsxFile)
    outputFile.set_range_of_sheets()
    genFile = outputFile.parseXLSXfile()
    prepareForMethods = outputFile.prepareToMethod(genFile)
    listOfDataHeader = []
    listOfSumCurvesHeader = []
    listOfChronology = []
    for f in prepareForMethods:
        riznIntKr = GydroGenMethod(f[1])
        rizn = riznIntKr.rizn_inter_kruvi()
        listOfDataHeader.append((f[0],rizn))
        sumCurve = riznIntKr.sumCurves()
        listOfSumCurvesHeader.append((f[0],sumCurve))
        listOfChronology.append((f[0],f[1]))
    years = outputFile.listOfYears
    indexOfYears = range(len(years))
    MethodRizInt = outputFile.prepareToChart(years,listOfDataHeader)
    MethodSumCurves = outputFile.prepareToChart(indexOfYears,listOfSumCurvesHeader)
    MethodChronology = outputFile.prepareToChart(years,listOfChronology)
    methodsList = [(MethodRizInt,"Rizn_Int_Kruvi",False),(MethodSumCurves,"Sum Curves",True),(MethodChronology,"Chronology",True)]
    createCharts(methodsList,xlsxFile)



if __name__ == "__main__":
    build_charts()
    #print (prepare(parseXLSXfile(xlsxFile),"rizn_inter_kruvi"))
    #createCharts(prepare(parseXLSXfile(xlsxFile),"rizn_inter_kruvi"))