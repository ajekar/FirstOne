import glob

outf = open('D:\Stocks\A-Consolidated.csv', 'w')

for f in glob.glob1("D:\Stocks", "EQ*.CSV"):
    dt = '20' + f[6:8] + '-' + f[4:6] + '-' + f[2:4]
    print(f, dt)

    lineno = 1
    for line in open("D:\Stocks\\" + f):
        if(lineno > 1):
            outf.write(dt + "," + line )
        lineno += 1



