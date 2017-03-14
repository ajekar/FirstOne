import glob

for f in glob.glob1("E:\Documents\Stock", "EQ*.CSV"):
    print(f)
    dd = f[2:4]
    mm = f[4:6]
    yy = f[6:8]
    print('20' + yy + '-' + mm + '-' + dd)