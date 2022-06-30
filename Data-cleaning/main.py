import pandas as pd
df = pd.DataFrame({})

f = open("inputs/100 Software Company info.txt", "r")
lines = f.readlines()
count = 0

record_dic = {}
for i in range(0,len(lines)):        
    stripped_string = ''.join([c for c in lines[i] if c not in ['\t', '\n']])
    stripped_string = stripped_string.strip()
    if 'https://Awww' in stripped_string :
        stripped_string = stripped_string.replace('https://Awww.','https://www.')
    if 'https:/Awww' in stripped_string :
        stripped_string = stripped_string.replace('https:/Awww.','https://www.')
    if 'https://www._' in stripped_string :
        stripped_string = stripped_string.replace('https://www._','https://www.')
    if 'https://www_' in stripped_string :
        stripped_string = stripped_string.replace('https://www_','https://www.')
    if 'https://wwww.' in stripped_string :
        stripped_string = stripped_string.replace('https://wwww.','https://www.')
    if 'https:/fweb.' in stripped_string :
        stripped_string = stripped_string.replace('https:/fweb.','https://www.')
    if 'https://web.' in stripped_string :
        stripped_string = stripped_string.replace('https://web.','https://www.')
    if 'https:/Aweb.' in stripped_string :
        stripped_string = stripped_string.replace('https:/Aweb.','https://www.')
    if 'https://Aweb.' in stripped_string :
        stripped_string = stripped_string.replace('https://Aweb.','https://www.')
    if 'https:/Aveb.' in stripped_string :
        stripped_string = stripped_string.replace('https:/Aveb.','https://www.')
    if 'https:/web.' in stripped_string :
        stripped_string = stripped_string.replace('https:/web.','https://www.')
    if 'https:/Mweb.' in stripped_string :
        stripped_string = stripped_string.replace('https:/Mweb.','https://www.')
    if 'https://fweb.' in stripped_string :
        stripped_string = stripped_string.replace('https://fweb.','https://www.')
    if 'https:/iweb.' in stripped_string :
        stripped_string = stripped_string.replace('https:/iweb.','https://www.')

    if 'Facebook:' in stripped_string:
        record_dic['facebook'] = stripped_string.replace("Facebook:", "")
    elif 'Linkedin:' in stripped_string:
        record_dic['linkedin'] = stripped_string.replace("Linkedin:", "")
    elif stripped_string != '':
        record_dic['name'] = stripped_string

    if 'facebook' in record_dic and 'linkedin' in record_dic and 'name' in record_dic:
        df = df.append(record_dic, ignore_index = True)
        record_dic = {}
        count += 1
        
print(count)
df.reset_index(drop=True, inplace=True)
df.to_csv('output.csv',index=False)