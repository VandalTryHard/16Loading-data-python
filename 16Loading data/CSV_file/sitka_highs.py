import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_name = 'c:/Users/Val/Desktop/Py/Project_2/16Loading data/CSV_file/sitka_weather_2018_simple.csv'
with open(file_name) as f:
	reader = csv.reader(f) #csv.reader() метод принимет объект файла в аргументе, чтобы создать объект чтения данных для этого файла
	header_row = next(reader)

	for index, column_header in enumerate(header_row): #enumerate() возвращает индекс каждого элемента и его значение при переборе списка
		print(index, column_header)
	
	#Чтение дат и максимальных температур из файла
	dates, highs = [], []
	
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)
	print(highs)

	#Нанесение данных на диаграмму
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates, highs, c='red')

	#форматирование диаграммы
	plt.title("Daily high temperatures - 2018", fontsize = 24)
	plt.xlabel('', fontsize = 16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize = 16)
	plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

	plt.show()
