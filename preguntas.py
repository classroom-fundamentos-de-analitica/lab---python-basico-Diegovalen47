"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
  with open("data.csv", "r") as file:
    data = file.readlines()
  return sum([int(line.replace('\n', " ").replace('\t', " ").split(",")[0][2]) for line in data])


def pregunta_02():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    key = line.replace('\n', " ").replace('\t', " ").split(",")[0][0]
    if key in dictionary:
      dictionary[key] += 1
    else:
      dictionary[key] = 1
  return sorted(dictionary.items())


def pregunta_03():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    item = line.replace('\n', " ").replace('\t', " ").split(",")[0]
    key = item[0]
    if key in dictionary:
      dictionary[key] += int(item[2])
    else:
      dictionary[key] = int(item[2])
  return sorted(dictionary.items())


def pregunta_04():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    item = line.replace('\n', " ").replace('\t', " ").split(",")[0]
    key = item[9:11]
    if key in dictionary:
      dictionary[key] += 1
    else:
      dictionary[key] = 1
  return sorted(dictionary.items())


def pregunta_05():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    item = line.replace('\n', " ").replace('\t', " ").split(",")[0]
    key = item[0]
    if key in dictionary:
      dictionary[key].append(int(item[2])) 
    else:
      dictionary[key] = [int(item[2])]
  return sorted([(key, max(dictionary[key]), min(dictionary[key])) for key in dictionary])


def pregunta_06():
  with open("data.csv", "r") as file:
    data = file.readlines()
  items = [item for line in data for item in line.replace('\n', " ").split('\t')[4].split(',')]
  dictionary = {}
  for item in items:
    key = item[:3]
    value = int(item[4:])
    if key in dictionary:
      dictionary[key].append(value)
    else:
      dictionary[key] = [value]
  return sorted([(key, min(dictionary[key]), max(dictionary[key])) for key in dictionary])


def pregunta_07():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    row = line.replace('\n', " ").split('\t')
    key = int(row[1])
    if key in dictionary:
      dictionary[key].append(row[0])
    else:
      dictionary[key] = [row[0]]
  return sorted(dictionary.items())


def pregunta_08():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    row = line.replace('\n', " ").split('\t')
    key = int(row[1])
    if key in dictionary:
      dictionary[key].append(row[0])
    else:
      dictionary[key] = [row[0]]
  return sorted([(key, sorted(list(set(dictionary[key])))) for key in dictionary])


def pregunta_09():
  with open("data.csv", "r") as file:
    data = file.readlines()
  items = [item for line in data for item in line.replace('\n', " ").split('\t')[4].split(',')]
  dictionary = {}
  for item in items:
    key = item[:3]
    if key in dictionary:
      dictionary[key] += 1
    else:
      dictionary[key] = 1
  sorted_list = sorted(dictionary.items(), key=lambda x:x[0])
  sorted_dict = dict(sorted_list)
  return sorted_dict


def pregunta_10():
  with open("data.csv", "r") as file:
    data = file.readlines()
  lista = []
  for line in data:
    row = line.replace('\n', " ").split('\t')
    first_element = row[0]
    second_element = len(row[3].split(','))
    third_element = len(row[4].split(','))
    lista.append((first_element, second_element, third_element))
  return lista


def pregunta_11():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    row = line.replace('\n', " ").split('\t')
    for letter in row[3].split(','):
      if letter in dictionary:
        dictionary[letter] += int(row[1])
      else:
        dictionary[letter] = int(row[1])
  sorted_list = sorted(dictionary.items(), key=lambda x:x[0])
  sorted_dict = dict(sorted_list)
  return sorted_dict


def pregunta_12():
  with open("data.csv", "r") as file:
    data = file.readlines()
  dictionary = {}
  for line in data:
    row = line.replace('\n', " ").split('\t')
    for letter in row[4].split(','):
      if row[0] in dictionary:
        dictionary[row[0]] += int(letter[4:])
      else:
        dictionary[row[0]] = int(letter[4:])
  sorted_list = sorted(dictionary.items(), key=lambda x:x[0])
  sorted_dict = dict(sorted_list)
  return sorted_dict
