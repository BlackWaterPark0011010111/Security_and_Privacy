import matplotlib.pyplot as plt
import seaborn as sns


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

ax.scatter(input_values, squares, s=50, c='red', label='points')
ax.plot(input_values, squares, linewidth=3, label='line')

ax.set_title('Square Numbers', fontsize=30)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Square of Value', fontsize=15)
ax.tick_params(axis='both', labelsize=12)
ax.grid()
ax.legend()
fig.tight_layout()
plt.show()
