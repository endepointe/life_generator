# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter.ttk import Combobox
import requests
from bs4 import BeautifulSoup
import re
import csv
import sys

class PopulationGenerator:
    '''
    Constructor
    Initialization
    '''
    def __init__(self):
        self.url = 'https://en.wikipedia.org/wiki/United_States_Census'
        self.stateUrl = 'https://en.wikipedia.org/wiki/%s_United_States_census'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}
        self.years = self.getYears()
        self.stateTotalMap = dict()
        self.resultData = None
        self.yearsMapIndex = {'1870': 2}
        self.outDate = csv.writer(open('output.csv', 'w', newline=''))
        self.outDate.writerow(['input_year', 'input_state', 'output_population_size'])
    '''
    UI design
    '''
    def ui(self):
        root = Tk()
        # title of window
        root.title('Pop Gen')
        # Size and position
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root_height = 300
        root_wight = 600
        x_width = (width - root_wight) / 2
        x_height = (height - root_height) / 2
        root.geometry('%dx%d+%d+%d' % (root_wight, root_height, x_width, x_height))
        frameTop = Frame(root, pady=10)
        frameTop.pack()
        frameCenter = Frame(root, pady=10)
        frameCenter.pack()
        frameBottom = Frame(root, pady=10)
        frameBottom.pack()
        # Select year
        yearLabel = Label(frameTop, text='Year:', font=12, pady=3, padx=5)
        yearLabel.grid(row=0, column=0)
        self.yearBox = Combobox(frameTop)
        self.yearBox['values'] = self.years
        self.yearBox.bind('<<ComboboxSelected>>', self.getState)
        self.yearBox.grid(row=0, column=1)
        # Select state
        stateLabel = Label(frameTop, text='State:', font=12, pady=3, padx=5)
        stateLabel.grid(row=0, column=2)
        self.stateBox = Combobox(frameTop)
        self.stateBox.grid(row=0, column=3)
        # Generate button
        button = Button(frameBottom, text='Generate', padx=30, pady=10, command=self.get_result)
        button.pack()
        # show the result
        # self.text = Text(frameBottom, height=4)
        self.resultData = StringVar()
        self.text = Label(frameBottom, textvariable=self.resultData, height=4, bg='green', fg='white', width=50,font=15)
        self.text.pack()
        root.mainloop()
    '''
    '''
    def get_result(self):
        # # print('hello world')
        year = self.yearBox.get()
        state = self.stateBox.get()
        if self.stateTotalMap.__contains__(state):
            # print(year + ':' + state + ':' + self.stateTotalMap[state])
            self.resultData.set(self.stateTotalMap[state])
            self.outDate.writerow([year, state, self.stateTotalMap[state]])
    '''Get the year function'''
    def getYears(self):
        # print('year function')
        return self.wikiYears()
    '''
    Get the information of state accorind to the year
    '''
    def getState(self, *args):
        self.stateTotalMap = self.wikiState(self.yearBox.get())
        # print(len(self.stateTotalMap), self.stateTotalMap)
        self.stateBox['values'] = [k for k in self.stateTotalMap]
    '''
    Get the year from web > tbody > tr:nth-child(1) > td:nth-child(1) > a
    '''
    def wikiYears(self):
        r = requests.get(self.url, params={}).text
        soup = BeautifulSoup(r, 'html.parser')
        years = soup.select(
            '#mw-content-text > div.mw-parser-output > table.sortable.wikitable >tbody > tr >td:nth-child(1)>a')
        return [item.text for item in years]
    '''
    '''
    def wikiState(self, year):
        if year == '1790':
            return self.year1790(year)
        elif year == '1800':
            return self.year1800(year)
        elif year == '1870':
            return self.year1870(year)
        else:
            return self.yearOthers(year)
        return {}
    def year1790(self, year):
        r = requests.get(self.stateUrl % year).text
        soup = BeautifulSoup(r, 'html.parser')
        stateNamesTemp = soup.select(
            '#mw-content-text > div.mw-parser-output>table.wikitable.sortable>tbody> tr>td:nth-child(1)>a')
        stateNames = [item.text for item in stateNamesTemp]
        stateTotalTemp = soup.select(
            '#mw-content-text > div.mw-parser-output >table.wikitable.sortable>tbody > tr > td:nth-child(8)')
        stateTotal = [getDigital(item.text) for item in stateTotalTemp]
        # print(len(stateNames), stateNames)
        # print(len(stateTotal), stateTotal)
        return {k: v for k, v in zip(stateNames, stateTotal)}
    '''
    '''
    def year1800(self, year):
        r = requests.get(self.stateUrl % year).text
        soup = BeautifulSoup(r, 'html.parser')
        stateNamesTemp = soup.select(
            '#mw-content-text > div.mw-parser-output>table.wikitable.sortable>tbody> tr>td:nth-child(1)')
        stateNames = [item.text.strip() for item in stateNamesTemp]
        stateTotalTemp = soup.select(
            '#mw-content-text > div.mw-parser-output >table.wikitable.sortable>tbody > tr > td:nth-child(14)')
        stateTotal = [getDigital(item.text) for item in stateTotalTemp]
        # print(len(stateNames), stateNames)
        # print(len(stateTotal), stateTotal)
        return {k: v for k, v in zip(stateNames, stateTotal)}
    '''
    #mw-content-text > div.mw-parser-output > table:nth-child(15) > tbody > tr:nth-child(1) > td:nth-child(2)
    '''
    def yearOthers(self, year):
        # print(year)
        r = requests.get(self.stateUrl % year).text
        soup = BeautifulSoup(r, 'html.parser')
        soupTemp = soup.select(
            '#mw-content-text > div.mw-parser-output > table.wikitable.sortable')[0]
        stateNamesTemp = soupTemp.select("tbody>tr>td:nth-child(2)")
        stateNames = [item.text for item in stateNamesTemp]
        stateTotalTemp = soupTemp.select(
            'tbody>tr>td:nth-child(3)')
        stateTotal = [getDigital(item.text) for item in stateTotalTemp]
        # print(len(stateNames), stateNames)
        # print(len(stateTotal), stateTotal)
        return {k: v for k, v in zip(stateNames, stateTotal)}
    '''
   #mw-content-text > div.mw-parser-output > table:nth-child(20) > tbody > tr:nth-child(1) > td:nth-child(2) 
    '''
    def year1870(self, year):
        # print(year)
        r = requests.get(self.stateUrl % year).text
        soup = BeautifulSoup(r, 'html.parser')
        soupTemp = soup.select(
            '#mw-content-text > div.mw-parser-output > table.wikitable.sortable.mw-collapsible')[1]
        stateNamesTemp = soupTemp.select("tbody>tr>td:nth-child(2)")
        stateNames = [item.text for item in stateNamesTemp]
        stateTotalTemp = soupTemp.select(
            'tbody>tr>td:nth-child(3)')
        stateTotal = [getDigital(item.text) for item in stateTotalTemp]
        # print(len(stateNames), stateNames)
        # print(len(stateTotal), stateTotal)
        return {k: v for k, v in zip(stateNames, stateTotal)}
    '''
    Direct processing of files
    '''
    def dealCSV(self, name):
        inDate = csv.reader(open(name, 'r'))
        for row in inDate:
            # print(row)
            if row[0] != 'input_year':
                self.stateTotalMap = self.wikiState(row[0])
                row.append(self.stateTotalMap[row[1]] if self.stateTotalMap.__contains__(row[1]) else '')
                self.outDate.writerow(row)
'''
Extract the number before the string
'''
def getDigital(str):
    nums = re.findall(r'^[\d,\,]+', str)
    return nums[0] if len(nums) > 0 else -1
if __name__ == '__main__':
    generator = PopulationGenerator()
    if len(sys.argv) == 1:
        generator.ui()
    elif len(sys.argv) == 2:
        generator.dealCSV(sys.argv[1])