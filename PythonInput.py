import serial, time, xlsxwriter
com = raw_input("Which number COM Port is the arduino on? Check in device manager>>Ports \n")
comport = 'COM'+com
Arduino = serial.Serial(comport, 115200, timeout = .5)
start = time.strftime("%d-%m-%Y") +"_" + time.strftime("%H-%M-%S")
name = start + '_Speed_Data.xlsx'
workbook = xlsxwriter.Workbook(name)
worksheet = workbook.add_worksheet()
row = 0
col = 0
worksheet.write(row, 1, 'RPM')
worksheet.write(row, 0, 'Time')
row += 1
cont = 0
mydata = [0]

while cont == 0:
    data = Arduino.readline()[:5]
    if data:
        print data
        data = float(data)
        if(data < 0):
            cont = 1
            break
        mydata.append(data)
        worksheet.write(row, 1, data)
        row+=1
t = 0
for x in range(1, row):
    t = (1.0)/(mydata[x]/60.0) + t
    worksheet.write(x, 0, t)
workbook.close()
print "Done!"
