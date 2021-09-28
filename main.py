import re

f_html = open('/Users/Roman/Documents/coord.htm', 'r', encoding="windows-1251").read()
f_csv = open ('/Users/Roman/Documents/coord.csv', 'w', encoding="utf-8")
result = re.findall("<td>(.*)</td>\n<td>(.*)</td>\n<td>(.*)</td>\n<td>(.*)</td>", f_html)
#f_csv.write(f"Узел,Статус,Имя компьютера, Версия ПО, Версия ОС, Дополнительно")
f_csv.write(f"Узел,Статус,Имя компьютера, Версия ПО\n")
for res in result:
    f_csv.write(f"{res[0]},{res[1]},{res[2]},{res[3]}\n")
    print(f"Address: {res[0]}\n Status: {res[1]}")
f_csv.close()
