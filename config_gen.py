#!/usr/bin/python3

# combine multiple defconfigs into one giant megaconfig

import sys

filenames = sys.argv[1:]

if not filenames:
    print("usage: {} [defconfig filenames]".format(sys.argv[0]))
    sys.exit(1)

config_lines = {}

for filename in filenames:
    with open(filename, 'r') as f:
        for line in f:
            if '=' not in line:
                continue

            k, v = line.split('=')

            if k in config_lines:
                # y > m > n
                old_v = config_lines[k]
                if (v == 'y') or (old_v == 'n' and v == 'm'):
                    config_lines[k] = v
                if v.isnumeric():
                    if int(v) > int(old_v):
                        config_lines[k] = v
            else:
                config_lines[k] = v

print('\n'.join(sorted(
    ['{}={}'.format(k, v).strip() for k, v in config_lines.items()])))
