def convert(to_cover):
    res=[]
    for str1 in to_cover.split():
        tmp = str1[::-1].lower()
        for i,_ in enumerate(str1):
            if _.isupper():
                ts=[s for s in tmp]
                ts[i] = tmp[i].upper()
                tmp=''.join(ts)
        res.append(tmp)
    return ' '.join(res)

if __name__ == '__main__':
    res=convert('Many people spell MySQL incorrectly')
    print(res)
    res = convert('Ynam elpoep lleps LqSYM yltcerrocni')
    print(res)
