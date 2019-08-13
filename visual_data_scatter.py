import matplotlib.pyplot as plt

max_value = 101
autosave = True
x_values = list(range(max_value))
y_values = [x**2 for x in x_values]


# c - color of point, edgecolor, s - dimension of point
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues,
            edgecolor='none', s=5)

# Призначення заголовку діаграми і міток осей
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Призначення розміру шрифта ділення на осях
plt.tick_params(axis='both', which='major', labelsize=14)

# Призначення діапазону для кожної осі
plt.axis((1, max_value, 0, max_value**2))

if autosave:
    plt.savefig('squares_auto.png', bbox_inches='tight')
else:
    plt.show()


