# user.text からﾃﾞｰﾀを読み込む

f = open('users.text',mode='r')

print(f)
print(type(f))

text = f.read()

print(text)

# text のﾃﾞｰﾀ型は？　typeで調べる
print(type(text)) # <class 'str'>

# ﾌｧｲﾙを空けたら閉める
f.close()
