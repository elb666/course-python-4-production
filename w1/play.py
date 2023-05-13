

with open('micro.csv') as data_file:

    column_names = [name.strip() for name in data_file.readline().split(',')]

    for line in data_file:
        record = [field.strip() for field in line.split(',')]
        record = dict(zip(column_names, record))

