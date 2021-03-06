import numpy as np

def GF_sum(num1, num2):
    return num1 ^ num2

def GF_mul(num1, num2):
    res, tmp = 0, num1
    i = 1
    while i <= 128:
        res = res ^ (0 if (num2 & i) == 0 else tmp)
        i *= 2
        if tmp & 0b10000000: tmp = (tmp * 2) % 256 ^ 0b00011011
        else: tmp = (tmp * 2) % 256
    return res

#字节代替
S_box = np.array([
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16])

S_box_1 = np.array([
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d])

def byte_sub(to_sub, cryp=1, key_extend=0): #1表示加密，即正向字节代替
    res = to_sub.copy()
    S = S_box if cryp == 1 else S_box_1
    if key_extend:
        for i in range(len(to_sub)):
            res[i] = S[int(to_sub[i] & 0b11110000) + int(to_sub[i] & 0b00001111)]
    else:
        for i in range(len(to_sub)):
            for j in range(len(to_sub[0])):
                res[i,j] = S[int(to_sub[i,j] & 0b11110000) + int(to_sub[i,j] & 0b00001111)]
    return res

def show_in_hex(a,s = 1):
    if s == 1:
        for i in range(4):
            for j in range(4):
                print('%.2x'%a[i,j], end=' ')
            print(' ')
    else:
        for i in range(len(a)):
            print('%.2x'%a[i], end=' ')
        print(' ')

#行移位
def row_shift(to_shift, cryp=1): #1表示加密，即正向行移位
    res = to_shift.copy()
    for i in range(1,4):
        if cryp == 1:
            res[i] = np.append(to_shift[i][i:], to_shift[i][:i])
        else:
            res[i] = np.append(to_shift[i][4-i:], to_shift[i][:4-i])
    return res

#列混淆
matrix = np.array([[2,3,1,1],
                   [1,2,3,1],
                   [1,1,2,3],
                   [3,1,1,2]],dtype=int)
matrix_1 =np.array([[0X0E,0X0B,0X0D,0X09],
                    [0X09,0X0E,0X0B,0X0D],
                    [0X0D,0X09,0X0E,0X0B],
                    [0X0B,0X0D,0X09,0X0E]],dtype=int)

def col_mix(to_mix, cryp=1):
    res = np.zeros((4,4),dtype=int)
    M = matrix if cryp == 1 else matrix_1
    for i in range(4):
        for j in range(4):
            for k in range(4):
                t =  GF_sum(res[i,j], GF_mul(M[i,k], to_mix[k,j]))
                res[i,j] = GF_sum(res[i,j], GF_mul(M[i,k], to_mix[k,j]))
    return res

#轮密钥加
def key_add(data1, data2, key_extend=0):
    res = data1.copy()
    if key_extend:
        for i in range(len(data1)):
            res[i] = data1[i] ^ data2[i]
    else:
        for i in range(len(data1)):
            for j in range(len(data1)):
                res[i,j] = data1[i,j] ^ data2[i,j]
    return res

#密钥扩展
RC = np.array([0x01, 0x02, 0x04, 0x08,0x10,
               0x20,0x40, 0x80,0x1b, 0x36])
def key_extend(key): #key是一个4*4的矩阵
    res = np.zeros((44,4), dtype=int)
    res[:4] = key.T
    for i in range(4,44):
        temp = res[i - 1]
        if i % 4 == 0:
            temp = np.append(res[i - 1][1:], res[i - 1][0])
            temp = byte_sub(temp,key_extend=1)
            temp[0] = temp[0] ^ RC[i // 4 - 1]
        res[i] = key_add(temp, res[i - 4], key_extend=1)
    return res

#AES加密解密
def AES_cryp(data, key_all, cryp=1):
    '''
    data是4*4矩阵，key_all是11个密钥，shape=(44,4)，使用时要转置
    '''
    start = 0 if cryp == 1 else 40
    key0 = key_all[start: start + 4].T
    res = key_add(data, key0)
    for i in range(1,10):
        start = 4 * i if cryp == 1 else 40 - 4 * i
        key_i = key_all[start:start+4].T
        if cryp == -1:
            key_i = col_mix(key_i, cryp) #若是解密，先对密钥进行逆向列混淆，才可以交换列混淆和轮密钥加的顺序
        res = byte_sub(res,cryp)
        res = row_shift(res, cryp)
        res = col_mix(res,cryp)
        res = key_add(res,key_i)
    start = 40 if cryp == 1 else 0
    key_10 = key_all[start:start+4].T
    res = byte_sub(res,cryp)
    res = row_shift(res, cryp)
    res = key_add(res,key_10)
    return res

def get_data_16_byte(s): #把16字节的字符串转为4*4的矩阵
    res = np.zeros((4,4), dtype=int)
    for i in range(len(s)):
        res[i % 4, i // 4] = ord(s[i])
    return res

def cut_data_16(sentence):
    res = []
    i = 0
    while (i + 1) * 16 <= len(sentence):
        data = get_data_16_byte(sentence[i * 16: (i + 1) * 16])
        res.append(data)
        i += 1
    if i * 16 < len(sentence):
        data = get_data_16_byte(sentence[i * 16:])
        res.append(data)
    return res

def AES_encryp_decryp_sentence(sentence, key, cryp=1):
    key_ = get_data_16_byte(key)
    key_all = key_extend(key_)
    data_all = cut_data_16(sentence)
    res = []
    for each in data_all:
        res.append(AES_cryp(each,key_all,cryp))
    res_sentence = ''
    for each in res:
        for i in range(4):#把4*4的矩阵转为16字节的字符串
            for j in range(4):
                res_sentence += chr(each[j,i])
                if cryp == -1 and each[j,i] == '\0': return res_sentence[:-1]
    return res_sentence
