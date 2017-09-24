import re

class NM2Parser:

    def __init__(self, infile):
        self.infile = infile

    def is_header_label(self, line):
        return line.startswith('# ')

    def is_delimiter(self, line):
        return line.startswith('##')

    def is_data(self, line):
        return re.match('^.*:.*$', line) and not line.startswith('#')

    def create_section(self, key_name):
        return { key_name: {} }

    def add_key(self, json_obj, line):
        key_val = line.split(':')
        key = key_val[0].strip()
        val = key_val[1].strip()
        json_obj[key] = val
