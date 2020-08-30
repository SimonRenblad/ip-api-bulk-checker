import IPAPI
import pickle

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

def batchify(addresses):
    target_address_list = []
    num_addresses = len(addresses)
    batch_size = 100
    num_batches = num_addresses / batch_size
    remaining_addresses = num_addresses % batch_size
    batch_i = 0
    while batch_i < num_batches:
        target_address_list.append(addresses[(batch_i * batch_size):((batch_i + 1) * batch_size)])
        batch_i += 1

    if remaining_addresses != 0:
        target_address_list.append(addresses[(batch_i * batch_size) : ])

    return target_address_list

def batch_pickle_result():
    addresses = get_ip_addresses()
    addresses = batchify(addresses)
    result_list = []

    for batch in addresses:
        result = IPAPI.LookupBatch(batch)
        result_list += result

    with open('results.pickle', 'wb') as fb:
        pickle.dump(result_list, fb)

def unpickle_result_list():
    pickle_off = open('results.pickle', 'rb')
    results = pickle.load(pickle_off)
    return results

batch_pickle_result()
