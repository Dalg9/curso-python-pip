import matplotlib.pyplot as plt 
#plt es un sinonimo, podemos normbrarlo libremente
def generate_bar_chart(name, labels, values):
  fig, ax =plt.subplots()  #ax son cordenadas
  ax.bar(labels, values)       #grafica de barras
  #plt.show()# que haga o muestre la grafica
  plt.savefig (f"./imgs/{name}.png")
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax =plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  #plt.show() solo lo comente para no eliminarlo
  plt.savefig ("pie.png")
  plt.close()


if __name__ == '__main__': #se ejecute como archivo
  labels = ['a','b', 'c']
  values= [10, 40, 850]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values )