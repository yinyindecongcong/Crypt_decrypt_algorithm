import numpy as np
import re

# 使用字典存储
alphabet = 'abcdefghiklmnopqrstuvwxyz'


def create_matrix(word):
    res = {}  # key为字母/下标，value为下标/字母
    count = 0
    for each in word.lower() + alphabet:
        if each == 'j': each = 'i'
        if res.get(each, -1) == -1:
            res[each] = count
            res[count] = each
            count += 1
    return res


def crypt_one_word(word, mat):
    word = re.sub(r'j', 'i', word.lower())
    cut, res = word[0], ''
    for i in range(1, len(word)):
        cut += word[i] if len(cut) % 2 == 0 or word[i] != cut[-1] else 'x' + word[i]
    if len(cut) % 2: cut += 'x'
    for i in range(0, len(cut), 2):
        pos1, pos2 = mat[cut[i]], mat[cut[i + 1]]
        if pos1 // 5 == pos2 // 5:  #同一行
            res += mat[pos1 // 5 * 5 + (pos1 + 1) % 5] + mat[pos2 // 5 * 5 + (pos2 + 1) % 5]
        elif pos1 % 5 == pos2 % 5: #同一列
            res += mat[(pos1 // 5 + 1) % 5 * 5 + pos1 % 5] + mat[(pos2 // 5 + 1) % 5 * 5 + pos1 % 5]
        else:
            res += mat[pos1 // 5 * 5 + pos2 % 5] + mat[pos2 // 5 * 5 + pos1 % 5]
    return res


def crypt_sentence(sentence, key):
    mat = create_matrix(key)
    res = sentence
    for word in re.findall(r'[a-zA-Z]+', sentence):
        res = re.sub('\\b' + word + '\\b', crypt_one_word(word, mat), res)
    return res


def decrypt_one_word(word, mat):
    res = ''
    for i in range(0, len(word), 2):
        pos1, pos2 = mat[word[i]], mat[word[i + 1]]
        if pos1 // 5 == pos2 // 5:
            res += mat[pos1 // 5 * 5 + (pos1 - 1) % 5] + mat[pos2 // 5 * 5 + (pos2 - 1) % 5]
        elif pos1 % 5 == pos2 % 5:
            res += mat[(pos1 // 5 - 1) % 5 * 5 + pos1 % 5] + mat[(pos2 // 5 - 1) % 5 * 5 + pos1 % 5]
        else:
            res += mat[pos1 // 5 * 5 + pos2 % 5] + mat[pos2 // 5 * 5 + pos1 % 5]
    return res


def decrypt_sentence(sentence, key):
    mat = create_matrix(key)
    res = sentence
    for word in re.findall(r'[a-zA-Z]+', sentence):
        res = re.sub('\\b' + word + '\\b', decrypt_one_word(word, mat), res)
    return res