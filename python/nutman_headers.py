f = open('../data/8-20-17.nm2')
out = open('../data/8-20-17-headers.txt', 'w')

for line in f:
    if line.startswith('# '):
        if line.startswith('# Field Record'):
            out.writelines('\n')
        out.writelines(line)
out.close()