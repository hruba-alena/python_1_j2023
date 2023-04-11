import json

with open('body.json', encoding='utf-8') as infile:
    seznam_body = json.load(infile)
print("seznam_body")
print(seznam_body)
print(type(seznam_body))
print(f'pocet lidi {len(seznam_body)}')
print(f'sezanm zaku {(seznam_body.keys())}')

zpracovane_body = seznam_body
print (zpracovane_body)
for zak, body in seznam_body.items():
    print (zak,body)
    if body >= 60:
        print(f'+ {zak}')
        zpracovane_body.update({zak:"Pass"})
    else:
        print(f'- {zak}')
        zpracovane_body.update({zak:"Fail"})
print("zpracovane_body")
print(zpracovane_body)
with open("prospech.json", mode ="w", encoding='utf-8') as outfile:
    json.dump(zpracovane_body, outfile, ensure_ascii=False)
