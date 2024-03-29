import matplotlib.pyplot as plt


input_data = [x for x in range(11)]
squares = [x**2 for x in input_data]

plt.plot(input_data, squares, linewidth=5)
plt.title('Square Number', fontsize = 24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
