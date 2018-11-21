import re
#规定密钥
ls1 = [0,18,9,13,25,19,7,15,6,21,3,10,4,16,8,11,22,17,1,24,5,23,12,20,2,14]
ls2 = [0,5,3,14,2,13,11,22,4,15,1,21,18,10,17,24,23,12,6,9,7,20,8,25,16,19]

def crypt_rotor_one_word(word, ls1, ls2):
    left_ls1, left_ls2 = [i for i in range(26)], [i for i in range(26)]
    right_ls1, right_ls2 = ls1, ls2
    res = ''
    for letter in word.lower():
        in1 = left_ls1[ord(letter) - ord('a')]
        out1 = right_ls1.index(in1)
        in2 = left_ls2[out1]
        out2= right_ls2.index(in2)
        res += chr(out2 + ord('a'))
        left_ls1, right_ls1 = left_ls1[-1:] + left_ls1[:-1], right_ls1[-1:] + right_ls1[:-1]
        if left_ls1[0] == 0:
            left_ls2, right_ls2 = left_ls2[-1:] + left_ls2[:-1], right_ls2[-1:] + right_ls2[:-1]
    return res

def decrypt_rotor_one_word(word, ls1, ls2):
    left_ls1, left_ls2 = [i for i in range(26)], [i for i in range(26)]
    right_ls1, right_ls2 = ls1, ls2
    res = ''
    i, j = (len(word) - 1) % 26, (len(word) - 1) // 26
    left_ls1, right_ls1 = left_ls1[-i:] + left_ls1[:-i], right_ls1[-i:] + right_ls1[:-i]
    left_ls2, right_ls2 = left_ls2[-j:] + left_ls2[:-j], right_ls2[-j:] + right_ls2[:-j]
    for letter in word[::-1]:
        in1 = right_ls2[ord(letter) - ord('a')]
        out1 = left_ls2.index(in1)
        in2 = right_ls1[out1]
        out2= left_ls1.index(in2)
        res += chr(out2 + ord('a'))
        if left_ls1[0] == 0:
            left_ls2, right_ls2 = left_ls2[1:] + left_ls2[:1], right_ls2[1:] + right_ls2[:1]
        left_ls1, right_ls1 = left_ls1[1:] + left_ls1[:1], right_ls1[1:] + right_ls1[:1]
    return res[::-1]

def crypt_decrypt_rotor_sentence(sentence, ls1, ls2, cryp=1):
    res = sentence
    for word in re.findall(r'[a-zA-Z]+', sentence):
        sub_res = crypt_rotor_one_word(word, ls1, ls2) if cryp == 1 \
                    else decrypt_rotor_one_word(word, ls1, ls2)
        res = re.sub('\\b' + word + '\\b', sub_res, res)
    return res