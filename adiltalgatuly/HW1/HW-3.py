import csv


source_data = [
    ("year", "region", "value"),
    ["2020", "Almaty", "130500"],
    ["2021", "Almaty", "150500"],
]

write = lambda data: (f := open("result.csv", "w", newline=""), csv.writer(f).writerows(data), f.close())

write(source_data)

with open('source_data.csv', 'r', newline="") as file:
    reader = csv.reader(file)
    m = list(map(lambda x: x if x[0]=='year' else [f"{x[0]}-01-01"]+x[1:], reader))

write(m)
