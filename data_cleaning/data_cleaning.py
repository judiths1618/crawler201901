# coding=utf-8

# 数据去重
def de_duplicaton(infile, outfile):
    infopen = open(infile, 'r', encoding='utf-8')
    outopen = open(outfile, 'w', encoding='utf-8')
    lines = infopen.readlines()
    list_l = []
    for line in lines:
        if line not in list_l:
            list_l.append(line)
            outopen.write(line)
    infopen.close()
    outopen.close()

if __name__ == '__main__':
    de_duplicaton('..\\crawlers\\Sprited Away.txt', 'de_duplication.dat')
