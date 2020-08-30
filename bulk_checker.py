import IPAPI

# file name for list of ip addresses
IN_FILE_NAME = "allips.txt"

# filenames for target output files
OUT_FILE_NAME_GOOD = "good.txt"
OUT_FILE_NAME_BAD = "bad.txt"

# helper function for reading input file to a python list
def get_ip_addresses():
    file1 = open(IN_FILE_NAME, 'r')
    lines = file1.readlines()
    file1.close()
    for i, line in enumerate(lines):
        lines[i] = line.strip()
    return lines

# helper function for writing the good and bad ips to diff lists
def write_ip_addresses(good_list, bad_list):
    file2 = open(OUT_FILE_NAME_GOOD, 'w')
    file2.writelines(good_list)
    file2.close()

    file3 = open(OUT_FILE_NAME_BAD, 'w')
    file3.writelines(bad_list)
    file3.close()

# key: the desired field to check (ex. 'countryCode' or 'proxy')
# match: the matching value to put in the 'good' file (ex. 'US' or False)
def bulk_check(key, match):
    addresses = get_ip_addresses()
    bad_list = []
    good_list = []
    count = 0
    for add in addresses:
        data = IPAPI.Lookup(add)
        if data['status'] == 'success':
            if data[key] == match:
                good_list.append("".join((add,"\n")))
            else:
                bad_list.append("".join((add,"\n")))
        else:
            print(f"address {add} encountered an error")
        print(count)
        count += 1

    write_ip_addresses(good_list, bad_list)

bulk_check('proxy', False)



