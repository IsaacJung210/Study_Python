import re 

# data = """
# park 800905-1049118
# kim  700905-1059119
# """

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))

# p = re.compile('ab*')
# # m = p.match('abbbbbbbbbbbc')
# # print(m)
# m = p.search('cav')
# print(m.start())

#아이디@gmail.com
p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,}')
m = p.match('a1ae1@gmail.com')
print(m)