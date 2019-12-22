import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("This program will help you type faster. You will have to type the word 'programing' as fast as you can for  five times")
input("Press enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)
    if (word.lower() != "programming"):
        mistakes += 1
print("You made " + str(mistakes) + " mistakes.")
print("Now let's see your evolution.")
t.sleep(3)

# montando o gráfico
x = [1, 2, 3, 4, 5]
y = times
plt.plot(x, y)

legend = ["1", "2", "3", "4", "5"]
plt.xticks(x,legend)
plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Your typing evolution')

plt.show()
