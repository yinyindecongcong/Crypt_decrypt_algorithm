import numpy as np

#初始置换
IP = np.array([57, 49, 41, 33, 25, 17,  9,  1,
               59, 51, 43, 35, 27, 19, 11,  3,
               61, 53, 45, 37, 29, 21, 13,  5,
               63, 55, 47, 39, 31, 23, 15,  7,
               56, 48, 40, 32, 24, 16,  8,  0,
               58, 50, 42, 34, 26, 18, 10,  2,
               60, 52, 44, 36, 28, 20, 12,  4,
               62, 54, 46, 38, 30, 22, 14,  6])
#逆初始置换
IP_1 = np.array([39,  7, 47, 15, 55, 23, 63, 31,
                 38,  6, 46, 14, 54, 22, 62, 30,
                 37,  5, 45, 13, 53, 21, 61, 29,
                 36,  4, 44, 12, 52, 20, 60, 28,
                 35,  3, 43, 11, 51, 19, 59, 27,
                 34,  2, 42, 10, 50, 18, 58, 26,
                 33,  1, 41,  9, 49, 17, 57, 25,
                 32,  0, 40,  8, 48, 16, 56, 24])

 #PC1置换
PC1 = np.array([57,49,41,33,25,17, 9,
                 1,58,50,42,34,26,18,
                10, 2,59,51,43,35,27,
                19,11, 3,60,52,44,36,
                63,55,47,39,31,23,15,
                 7,62,54,46,38,30,22,
                14, 6,61,53,45,37,29,
                21,13, 5,28,20,12, 4])
#PC2置换
PC2 = np.array([14,17,11,24, 1, 5, 3,28,
                15, 6,21,10,23,19,12, 4,
                26, 8,16, 7,27,20,13, 2,
                41,52,31,37,47,55,30,40,
                51,45,33,48,44,49,39, 0,
                34,53,46,42,50,36,29,32])
#每轮左移的位数
LFT=np.array([1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1])

def itobs(num, n=8): #整数转为bit数组，n为位数
    res = np.zeros(n, dtype=bool)
    bs = bin(num)[2:]
    for i in range(len(bs)):
        res[-i-1] = (bs[-i-1] == '1')
    return res

def bstoi(bs, n=8): #bit数组转为整数，n为位数
    res = 0
    for i in range(n):
        res = res * 2 + int(bs[i])
    return res

#64位密钥，8个字母
def get_data_64_bit(key):
    key_bitset = np.zeros(64,dtype=bool) #0表示最高位
    for i in range(len(key)):
        key_bitset[i * 8: (i + 1) * 8] = itobs(ord(key[i]), 8)
    return key_bitset

def substitute(sub_list, to_sub): #sub_list为置换表
    res = np.zeros(len(sub_list), dtype=bool)
    for i in range(len(sub_list)):
        res[i] = to_sub[sub_list[i]]
    return res

def left_shift_and_sub(key_bitset_after): #获得16个密钥
    res = []
    for i in range(len(LFT)):
        key_bitset_after = np.append(key_bitset_after[LFT[i]:], key_bitset_after[:LFT[i]])
        K_i = substitute(PC2, key_bitset_after)
        res.append(K_i)
    return res


# E扩展
E = np.array([31, 0, 1, 2, 3, 4,
              3, 4, 5, 6, 7, 8,
              7, 8, 9, 10, 11, 12,
              11, 12, 13, 14, 15, 16,
              15, 16, 17, 18, 19, 20,
              19, 20, 21, 22, 23, 24,
              23, 24, 25, 26, 27, 28,
              27, 28, 29, 30, 31, 0])
# P置换
P = np.array([16, 7, 20, 21, 29, 12, 28, 17,
              1, 15, 23, 26, 5, 18, 31, 10,
              2, 8, 24, 14, 0, 27, 3, 9,
              19, 13, 30, 6, 22, 11, 4, 25])
# S-盒
S_Box1 = np.array([[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                   [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                   [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                   [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]])

S_Box2 = np.array([[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                   [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                   [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                   [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]])

S_Box3 = np.array([[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                   [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                   [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                   [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]])

S_Box4 = np.array([[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                   [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                   [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                   [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]])

S_Box5 = np.array([[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                   [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                   [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                   [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]])

S_Box6 = np.array([[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                   [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                   [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                   [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]])

S_Box7 = np.array([[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                   [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                   [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                   [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]])

S_Box8 = np.array([[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                   [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                   [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                   [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]])

S_Box = np.array([S_Box1, S_Box2, S_Box3, S_Box4, S_Box5, S_Box6, S_Box7, S_Box8])

def S_Box_replace(E_i):
    res = np.zeros(32, dtype=bool)
    for i in range(8):
        start = i * 6
        row = E_i[start] * 2 + E_i[start+5]
        col = E_i[start+4] + E_i[start+3] * 2 + E_i[start+2]*4 + E_i[start + 1] * 8
        res[i * 4: (i + 1) * 4] = itobs(S_Box[i][row][col],n=4)
    return res

def XOR(A, B):
    res = np.zeros(len(A), dtype=bool)
    for i in range(len(A)):
        res[i] = A[i] ^ B[i]
    return res

def F(R_i, K_i):
    E_i = substitute(E, R_i) #E扩展
    E_out = XOR(E_i, K_i)    #异或
    S_out = S_Box_replace(E_out) #S盒代替
    res = substitute(P, S_out)#P置换
    return res

def DES_encryp_decryp_64(data, K_all, cryp=1):
    res = substitute(IP, data)       #初始置换
    for i in range(len(K_all)):      #16轮加密
        F_res = F(res[32:], K_all[i if cryp == 1 else 15 - i])
        R_next = XOR(F_res, res[:32])
        res[:32] = res[32:]
        res[32:] = R_next
    left32, right32 = res[:32].copy(), res[32:].copy()
    res[:32], res[32:] = right32, left32 #32位互换
    res = substitute(IP_1, res)
    return res

def cut_data(sentence):
    res = []
    i = 0
    while (i + 1) * 8 <= len(sentence):
        data = get_data_64_bit(sentence[i * 8: (i + 1) * 8])
        res.append(data)
        i += 1
    if i * 8 < len(sentence):
        sentence[i * 8:]
        data = get_data_64_bit(sentence[i * 8:])
        res.append(data)
    return res

def DES_encryp_decryp_sentence(sentence, key, cryp=1):
    K_all = get_K_all(key)
    data_all = cut_data(sentence)
    res = []
    for each in data_all:
        res.append(DES_encryp_decryp_64(each, K_all, cryp))
    res_sentence = ''
    for each in res:
        for i in range(8):
            a = chr(bstoi(each[i * 8: (i + 1) * 8]))
            if cryp == -1 and a == '\0': return res_sentence
            res_sentence += chr(bstoi(each[i * 8: (i + 1) * 8]))
    return res_sentence

def get_K_all(key):
    key_bitset = get_data_64_bit(key)
    key_bitset_after_sub = substitute(PC1, key_bitset)
    K_all = left_shift_and_sub(key_bitset_after_sub)
    return K_all

