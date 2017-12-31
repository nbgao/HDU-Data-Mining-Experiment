def Output(L, file):
    fout = open(file, 'w')
    for s in L:
        for x in s:
            fout.write(str(x) + '\t')
        fout.write('\n')
    print("数据成功导出到文件中")
    fout.close()