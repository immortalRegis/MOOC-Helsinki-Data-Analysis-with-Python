#!/usr/bin/env python3

import re
def file_extensions(filename):
    ext = re.compile(r'\.\w+\n')
    extension_holder = {}
    no_extension = []
    with open(filename, 'r') as f:
        for line in f:
            met_criterion = ext.findall(line) 
            try:
                name = met_criterion[0].strip('.')
                name = name.strip('\n')
                if not name in extension_holder.keys():
                    extension_holder[name] = []
                extension_holder[name].append(line.strip())
            except IndexError:
                no_extension.append(line.strip('\n'))
    return (no_extension, extension_holder)

def main():
    contents = file_extensions('src/filenames.txt')
    print(f'{len(contents[0])} files with no extension')
    for file_type, number in contents[1].items():
        print(f'{file_type} {len(number)}')

if __name__ == "__main__":
    main()
