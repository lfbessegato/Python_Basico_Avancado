import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]

plt.plot(x, y)
plt.show()

# Adcionar legendas
legend = ["January", "February", "March", "April"]
plt.xticks(x, legend)
plt.plot(x, y)
plt.show()

# Barras
plt.bar(x, y)
plt.ylabel("Sales in US$")
plt.title("Monthly Sales")
plt.show()