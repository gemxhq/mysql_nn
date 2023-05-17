import hashlib  # 导入hashlib模块



if __name__ == '__main__':

    md = hashlib.md5()  # 获取一个md5加密算法对象
    str1 = 'how to use md5 in hashlib?'.encode('utf-8')
    print(str1)
    md.update(str1)  # 制定需要加密的字符串
    print(md.hexdigest())  # 获取加密后的16进制字符串

    print(hashlib.md5(str1).hexdigest())
    print('------------------')
    md = hashlib.md5(str1)
    print(md.hexdigest())