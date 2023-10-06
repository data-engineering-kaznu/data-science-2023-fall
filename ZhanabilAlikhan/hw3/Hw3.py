import csv



with open('hw3.csv', 'r') as i, open('hw3-result.csv', 'w', newline='') as o:
    csv_reader = csv.reader(i)
    csv_write = csv.writer(o)
    date = []
    for row in csv_reader:
        date.append(row)
    
    for row in date:
        if row[0][5:8].istitle():
            match row[0][5:8]:
                case 'Jan':
                    row[0]=  '-01-01'.join([row[0][:4], row[0][8:]]) 
                    
                case 'Feb':
                    row[0]= '-02-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Mar':
                    row[0]= '-03-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Apr':
                    row[0]= '-04-01'.join([row[0][:4], row[0][8:]])
                case 'May':
                    row[0]= '-05-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Jun':
                    row[0]= '-06-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Jul':
                    row[0]= '-07-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Aug':
                    row[0]= '-08-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Sep':
                    row[0]= '-09-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Oct':
                    row[0]= '-10-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Nov':
                    row[0]= '-11-01'.join([row[0][:4], row[0][8:]])
                    
                case 'Dec':
                    row[0]= '-12-01'.join([row[0][:4], row[0][8:]])
            row[0] = row[0][:18] + '130500'
        else:
            row[0]= ''.join([row[0][:4], row[0][10:]])
            
    for row in date:
        csv_write.writerow(row)