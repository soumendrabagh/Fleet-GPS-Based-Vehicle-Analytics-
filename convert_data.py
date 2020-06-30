import csv, itertools, yaml, json
import pandas as pd
def convert_data(file_name = 'data_1.csv'):
  data = []
  with open(file_name) as f:
    dialect = csv.Sniffer().sniff(f.read(5))
    f.seek(0)
    read = csv.reader(f, dialect)
    i = 4000000
    for row in itertools.islice(read, 4000000, None):
      if i % 100000 == 0: print(i)
      row = [w.replace('560080\\", 6th A Cross Road, Lower Palace Orchard', '560080 6th A Cross Road, Lower Palace Orchard') for w in row]
      row1 = ','.join(map(str, row))
      row1 = (row1.replace('}', '')
                .replace('{','')
                .replace("'560080\', ", "'")
                .replace(',_id:,$oid:', '"oid":')
                .replace('$numberLong', "'numberLong'")
                .replace('"', "'")
                .replace("'8459''", "'8459'")
                .replace("'4890''", "'4890'")
                .replace("':'", "': '")
                .replace("'s", "s")
                .replace(":10.0", ": 10.0")
                .replace(",speed'", ",'speed'")
                .replace("Artists'", "Artists")
                .replace("'n", "n")
                .replace("O'Shaungnessy Road", "O Shaungnessy Road")
                .replace("D'Mellows", "D Mellows")
                .replace("Girls'", "Girls")
                .replace("Officers'", "Officers")
                .replace("Women'", "Women")
                .replace("Ladies'", "Ladies")
                .replace("Kaggis'", "Kaggis")
                .replace("C'lai", "Clai")
                .replace("NPL'S", "NPLS")
                .replace("HELMET'S", "HELMETS")
                .replace("no:-3", "no3")
                .replace("Legislatures'", "Legislatures")
                .replace("Angels'", "Angels")
                .replace("P D'", "P D")
                .replace("Visitors'", "Visitors")
                .replace("D'Lish", "D Lish")
                .replace("no:45", "no 45")
                .replace("CHILDREN'S", "CHILDREN")
                )
      row1 = '"{' + row1 + '}"'
      row1 = yaml.load(yaml.load(row1))
      data.append(row1)
      i +=1
    return data