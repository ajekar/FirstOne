import glob

outf = open('E:\Documents\Stock\A-Consolidated.csv', 'w')

for f in glob.glob1("E:\Documents\Stock", "EQ*.CSV"):
    dt = '20' + f[6:8] + '-' + f[4:6] + '-' + f[2:4]
    print(f, dt)

    lineno = 1
    for line in open("E:\Documents\Stock\\" + f):
        if(lineno > 1):
            print(dt + "," +line, file = outf)
        lineno += 1



