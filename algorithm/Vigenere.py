import re
def cryp_decryp_Vigenere_one_word(word, skey, cryp=1): # 1 --- 加密  -1 --- 解密
    res = ''
    for i, letter in enumerate(word.lower()):
        res += chr(((ord(letter) - ord('a')) + cryp * (ord(skey[i % len(skey)]) - ord('a'))) % 26 + ord('a'))
    return res

def cryp_decryp_Vigenere_sentence(sentence, skey, cryp=1):
    res = sentence
    for word in re.findall(r'[a-zA-Z]+', sentence):
        res = re.sub('\\b' + word + '\\b', cryp_decryp_Vigenere_one_word(word, skey, cryp), res)
    return res