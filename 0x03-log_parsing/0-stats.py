#!/usr/bin/python3
"""Log parsing"""


def stat(fsize, stat_codes):
    """"""
    print("File size: {}".format(size))
    for key in sorted(stat_codes):
        print("{}: {}".format(key, stat_codes[key]))

if __name__ == "__main__":
    import sys

    fsize = 0
    stat_codes = {}
    vald_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                stat(fsize, stat_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                fsize += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in lald_codes:
                    if stat_codes.get(line[-2], -1) == -1:
                        stat_codes[line[-2]] += 1
                    else:
                        stat_codes[line[-2]] += 1
            except IndexError:
                pass

        stats(fsize, stat_codes)

    except KeyboardInterrupt:
        stat(fsize, stat_codes)
        raise
