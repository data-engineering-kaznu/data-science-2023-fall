import csv
data = [
    ("year", "region", "value"),
    ["2022-Feb", "Almaty", "130500"],
    ["2021-Feb", "Astana", "150500"],
    ["2022-Mar", "Almaty", "150500"],
    ["2022-Mar", "Astana", "150500"],
]

with open('labka31.csv', "w") as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)
with open('labka31.csv', "w") as b:
    writer = csv.writer(b)
    for i in range(1, (len(data))):
        if "-Feb" in data[i][0]:
            data[i][0] = data[i][0].replace("-Feb", "-02-01")
        elif "-Mar" in data[i][0]:
            data[i][0] = data[i][0].replace("-Mar", "-03-01")

with open('labka32.csv', 'w', newline='') as c:
    csvwriter = csv.writer(c)
    csvwriter.writerows(data)
