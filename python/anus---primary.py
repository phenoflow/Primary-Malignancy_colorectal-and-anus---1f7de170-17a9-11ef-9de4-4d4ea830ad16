# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"27897.0","system":"readv2"},{"code":"1800.0","system":"readv2"},{"code":"1220.0","system":"readv2"},{"code":"93478.0","system":"readv2"},{"code":"27855.0","system":"readv2"},{"code":"10864.0","system":"readv2"},{"code":"5901.0","system":"readv2"},{"code":"28163.0","system":"readv2"},{"code":"22163.0","system":"readv2"},{"code":"50974.0","system":"readv2"},{"code":"10946.0","system":"readv2"},{"code":"11628.0","system":"readv2"},{"code":"9491.0","system":"readv2"},{"code":"24370.0","system":"readv2"},{"code":"9088.0","system":"readv2"},{"code":"7219.0","system":"readv2"},{"code":"46159.0","system":"readv2"},{"code":"18632.0","system":"readv2"},{"code":"55659.0","system":"readv2"},{"code":"6935.0","system":"readv2"},{"code":"3811.0","system":"readv2"},{"code":"101700.0","system":"readv2"},{"code":"48231.0","system":"readv2"},{"code":"18619.0","system":"readv2"},{"code":"35357.0","system":"readv2"},{"code":"9118.0","system":"readv2"},{"code":"2815.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_colorectal-and-anus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
