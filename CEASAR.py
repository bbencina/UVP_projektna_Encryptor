TABLE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '0', '1', '2', '3',
         '4', '5', '6', '7', '8', '9']

check_table = set(TABLE)
table_len = len(TABLE)

def encrypt(char, passwd):
    indent = TABLE.index(passwd)
    char_i = TABLE.index(char)
    return TABLE[(char_i + indent) % table_len]

def decrypt(char, passwd):
    char_i = TABLE.index(char)
    indent = TABLE.index(passwd)
    return TABLE[(table_len + char_i - indent) % table_len]
