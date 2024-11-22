import os
def find_ip(filepath):
    with open(filepath, 'rb') as file_read:
        # for linenumber, line in enumerate(file_read):
            # if b"Suraj" in line:
            #    print(file_read.tell())
            #    print (file_read.seek(linenumber))
            #    print(line)
            #    print(line)
            #    print(file_read.seek(b"line"))
            # if 'Suraj' in file_read:
            #     line
    #         else:
    #             continue
    #     IP_SET = file_read.readline().strip()
    # return IP_SET
        offset = file_read.seek(20)
        info = file_read.readline()
    return info



print(find_ip('my_file.txt'))