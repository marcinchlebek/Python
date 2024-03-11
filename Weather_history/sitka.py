import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        lows.append(low)
        highs.append(high)
        dates.append(current_date)

    print(highs)

# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Najwyższa i najniższa temperatura dnia - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()