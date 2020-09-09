import matplotlib.pyplot as pyplot
import csv

# pyplot.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# pyplot.show() Отображение таблицы

def getDataFromCsv(filename):

	with open(filename, 'r', encoding='utf-8') as file:

		data = csv.reader(file)