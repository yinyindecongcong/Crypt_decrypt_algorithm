---
typora-root-url: img
typora-copy-images-to: img
---

### Crypt_decrypt_algorithm

#### 古典密码

##### Caesar密码 

对字母表中的每个字母，用它之后的第三个字母代替。

##### Playfair密码（implement at 2018/11/10）（单表多字母代替密码）

给定一个密钥词，生成一个`5 x 5`的字母矩阵，生成过程为首先将密钥词去重后从左往右排列，再将剩余的字母从左往右填充至矩阵中，其中`I/J`算作一个字母，如monarchy生成如下矩阵。

>M O N A R
>
>C H Y B D
>
>E F G I/J K
>
>L P Q S T
>
>U V W X Z

对明文按如下规则加密：

1. 将明文分割成字母对，若字母对字母相同，在中间加一个填充字母，如x。`eg:balloon先变成ba,lx,lo,on`

2. 对每个字母对——
   * 若字母在矩阵的同一行，则每个字母由其右边的字母代替，`eg: AR->RM`
   * 若字母在矩阵的同一列，则每个字母由其下边的字母代替，`eg: MU->CM`
   * 否则对每个字母，其行为密文的所在行，另一字母的列为密文所在列，`eg:HS->BP`

##### Hill密码（单表多字母代替密码）

给定一个`m x m`的矩阵密钥，如`m = 3`，——

* 加密过程：$C = E(K,P) = PK \ mod \ 26$   
* 解密过程：$P = D(K,C)=PKK^{-1}\  mod \ 26$ 

##### Vigenere密码（多表代替密码）

* 最简单的多表代替密码，即使用不同的单表代替
* 代替表为 $m$ 个Caesar代替表，$m$ 的大小由密钥词决定 
* 加密过程为: $C_i = (p_i + k_{i\  mod \ m}) \ mod\  26$
* 解密过程为: $C_i = (p_i - k_{i\  mod \ m}) \ mod\  26$ 

##### 栅栏加密（置换密码）

一行一行写出单词，然后按列读出，但是把列的次序打乱，列的次序就是算法的密钥。

##### 转轮机（多次代替密码）

转轮机由多个圆筒组成，每个圆筒有26个输入引脚和26个输出引脚，分别表示26个字母。

考虑只有一个圆筒的转轮机，每输入一个字符，圆筒就旋转一个位置，内部连线相应改变，即为一个周期为26的多表代替密码。

多个圆筒时，每输入一个字符，第一个圆筒就旋转一个位置；当第一个圆筒旋转一周时，第二个圆筒旋转一个位置，以此类推。

#### 对称密码

##### 数据加密算法DEA（数据加密标准DES）

1. **Feistel密码**

输入为长为 $2w$ 的明文，分为下图的 $LE_0, RE_0$ ，密钥为 $K$，推出每一轮的密钥 $K_i$，算法加密解密如下，通过流程图可以看到加密和解密是完全相同的流程，区别只在于密钥的顺序。

<img src="https://s1.ax1x.com/2018/11/14/ijrxlq.png" width=450>

2. DEA的主体部分是Feistel密码，整个机制大致如下图：

<img src="https://s1.ax1x.com/2018/11/14/ijyQK0.png" width=700>

主要过程如下：

* 明文的初始置换与逆初始置换

* 轮密钥的生成：PC1置换->56位密钥、重复（循环移位、PC2置换->48位 $K_i$）

* 每一轮做F运算：每一轮的32位 $R_i$->E盒扩展(48位)->与48位 $K_i$异或 ->S盒代替(32位)->P盒置换(32位)
  * E盒扩展将32位输入扩展为48位，使得后面可以与密钥做异或，具体扩展如下图$\ ^{[2]}$：

<img src="https://img-blog.csdn.net/20160908111040111" width=400>

  * S盒代替将为48位数据分为8组，每组6位，分别输入到8个S盒中，每个输出4位，得到8 * 4 = 32位输出，以盒8为例$\ ^{[2]}$

<img src="https://img-blog.csdn.net/20160908123901711">

若第43-48位输入为110011，第1位和最后1位组成行，中间4位组成列，则对应（第11->4行第1001->9列），即12，所以输出为1100

##### 【参考文章】
[1.DES算法原理与Java实现](https://blog.csdn.net/android_jiangjun/article/details/79654940)

[2.DES算法原理完整版](https://blog.csdn.net/qq_27570955/article/details/52442092)

##### AES-128

明文：16字节，密钥16字节，轮数10，AES的运算是定义在$GF(2^8)$上的，其中乘法和加法操作如下：

* 加法：按位异或
* 乘法：num乘以00000010左移一位，若num最高位为1，则移位的结果再与00011011异或；更高次可重复使用上述过程得到结果。

1. **加密流程**

第0轮：明文与第0轮密钥做加密操作（轮密钥加）

第1-9轮：明文与第1-9轮密钥做加密操作（字节代替、行移位、列混淆、轮密钥加）

第10轮：明文与第10轮密钥做加密操作（字节代替、行移位、列混淆）

2. **密钥的扩展**

密钥被扩展为11个16字节的轮密钥，各用于每一轮的加密

3. **明文与密钥的表示**

16个字节按列排列为4 * 4的字节矩阵

4. **各个加密操作**

* 字节代替变换——
  * S盒变换：对状态中的每个字节，高四位作为行，低四位作为列，从S盒中去对应字节作为输出
  * 逆S盒变换类似，代替表不同
  * S盒的构造

* 行移位变换——
  * 正向行移位：状态第一、二、三、四行分别循环左移0、1、2、3个字节
  * 逆向则相反，即循环右移

* 列混淆变换——
  * 正向列混淆：对每列独立的进行操作，如图，其中乘法与加法都是定义在GF(2^8)上的。

  <img src="https://s1.ax1x.com/2018/11/15/ivImyF.md.png" width=450>

  * 逆向列混淆类似，矩阵如下：

  <img src="https://s1.ax1x.com/2018/11/15/ivI3Jx.md.png" width=450>

* 轮密钥加变换——

  * 正向/逆向：128位的状态按位与128位的轮密钥异或

5. 密钥扩展算法

* 用输入密钥（16个字节，4个字）直接作为扩展密钥数组的前4个字

* 对之后的每个字$w[i]$，依赖于$w[i-1]$和$w[i-4]$
  * 若 $i \ mod \ 4 \ne 0$ ， 则$w[i] = w[i-1] ⊕ w[i-4]$
  * 否则，$w[i] = G(w[i-1])⊕w[i-4]$ 

  其中，G的操作如下：
  * 字循环：把四个字节循环左移一个字节
  * 字代替：使用S盒代替4个字节
  * 字代替的结果与轮常量$RC[j]$异或得到输出，其中轮常量是一个字，右边三个字节为0。$RC[j]$每轮都不同，$RC[j] = 2 * RC[j-1],RC[1]=1​$

#### 公钥加密算法

五维组（明文，加密算法，密文，公钥与私钥，解密算法）

每个用户生成一对公钥与私钥，公钥所有人可见，私钥仅自己可见，且从公钥获得私钥在计算上不可行。

* 用于加密，如下：

$$
Y=E(PU_B,X)\\
X=D(PR_B,Y)
$$

* 用于数字签名，如下：(由于任何人都可以解密，不安全)

$$
Y=E(PR_A,X)\\
X=D(PU_A,Y)
$$

* 使用两次公钥算法，提供认证与保密功能，如下：

$$
Z=E(PU_B,E(PR_A,X))\\
X=D(PU_A,D(PR_B,Z))
$$

##### RSA

五维组——

* 明文：`0`到某`n-1`之间的整数，通常n为1024bit的二进制数（309位十进制数）

* 加密算法：乘方取模

* 密文：`0`到某`n-1`之间的整数，通常n为1024bit的二进制数（309位十进制数）

* 公钥与私钥

* 解密算法：乘方取模

RSA是一种分组密码，在实际应用中，分组大小为 $i$，其中 $2^i < n \le 2^{i+1}$，加密解密过程如下：
$$
\begin{align}
C &= M^e \ mod \ n\\
M &= C^d \ mod \ n = (M^e)^d \ mod \ n=M^{ed}\ mod \ n
\end{align}
$$
