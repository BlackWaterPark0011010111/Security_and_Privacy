import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares=     [1,4,9,16,25]

#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)
#ax.plot(squares,linewidth=3)
ax.plot(input_values,squares,linewidth=3)
ax.set_title('Square Nums', fontsize=30)
ax.set_xlabel('Value', fontsize=15)
ax .set_ylabel('Square of Value', fontsize=10)
ax.tick_params(axis='both',labelsize=15)
plt.grid()
plt.show()



