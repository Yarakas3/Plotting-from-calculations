import matplotlib.pyplot as pyplot
import csv



def createShedule():

	pyplot.figure(figsize=(14, 14))

	pyplot.subplot(2, 2, 1)
	pyplot.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
	pyplot.title('Скорость', fontsize = 20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('скорость м/с', fontsize=12)

	pyplot.subplot(2, 2, 2)
	pyplot.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'r')
	pyplot.title('Температура', fontsize=20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('температура', fontsize=12)


	pyplot.subplot(2, 2, 3)
	pyplot.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'purple')
	pyplot.title('Давление', fontsize = 20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('давление', fontsize=12)

	pyplot.subplot(2, 2, 4)
	pyplot.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'g')
	pyplot.title('Высота', fontsize=20)
	pyplot.xlabel('секунды', fontsize=12)
	pyplot.ylabel('высота', fontsize=12)


	pyplot.show()


def getDataFromCsv(filename):

	with open(filename, 'r', encoding='utf-8') as file:

		data = csv.reader(file)


createShedule()