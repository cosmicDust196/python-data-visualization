import csv
import matplotlib.pyplot as plt

days = []
temperatures = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        days.append(row["day"])
        temperatures.append(float(row["temperature"]))

plt.plot(days, temperatures, marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Weekly Temperature Trend")
plt.grid(True)
plt.show()

