import csv

def read_csv(path):#la ubicacion del archivo
  with open(path, 'r') as csvfile:# abrir el archivo con permisos de lectura
    reader= csv.reader(csvfile, delimiter=',')#el delimitdor es la forma como viene separado los datos
    header = next(reader)
    data= []
    for row in reader:# ciclo para ver fila por fila
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable }
      data.append(country_dict)
    return data


#ejecutar el archivo como script
if __name__ == '__main__':
  data=read_csv('app/data.csv')
  print(data[0])