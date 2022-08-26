fileDay = '08-26' # 編集する日付を指定

filename = './twitterAPI_%s-conv.txt' % fileDay
splitedArr = []
textArr = [] 
frontArr = [] 
editedArr = []
idx = 0

print('          '*40)


def convertToCsv(frontArr):
  for i in range(4):
    frontArr[i] += ','
  return frontArr



with open(filename, 'r', encoding='utf-8') as f:
  s = open('twitterAPI_%s.csv' % fileDay, 'w', encoding="utf-8", errors="ignore")
  
  for line in f:
    splitedArr += [line.split(' ')] # 半角スペース毎に配列に格納

    textArr = [''.join(splitedArr[idx][4:])]

    textArr = [textArr[0].replace(',', '')]
    textArr = textArr[0].replace('\"', '')
    frontArr = splitedArr[idx][:4]
    frontArr.extend([textArr])

    if 'iHerb最新コード' in frontArr[4]:
      pass
    else:
      convertToCsv(frontArr)
      s.writelines(frontArr)

    print(idx, frontArr)
    
    idx += 1

  s.close()
f.close()



