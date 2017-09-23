def get_field_name_from_line(line):
    return line.split(':')[1].strip()

def remove_description(line):
    if '-' in line:
        return line.split('-')[0].strip()
    else:
        return line

def split_multiple_field_names(line):
    if ',' in line:
        field_names = line.split(',')
        return map(lambda x: x.strip().upper(), field_names)
    else:
        return [line.upper()]

f = open('../data/8-20-17.nm2')
out = open('../data/8-20-17-field-names.txt', 'w')

for line in f:
    if line.startswith('FieldName'):
        field_name = get_field_name_from_line(line)
        field_name = remove_description(field_name)
        field_name_list = split_multiple_field_names(field_name)
        for name in field_name_list:
            out.writelines([name, '\n'])

f.close()
out.close()