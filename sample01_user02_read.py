# user02.text からﾃﾞｰﾀを読み込む

f = open('users02.text',mode='r')

print(f)
print(type(f))

text = f.read()

print(text)

# text のﾃﾞｰﾀ型は？　typeで調べる
print(type(text)) # <class 'str'>

# ﾌｧｲﾙを空けたら閉める
f.close()

# 出力結果
# りんごﾒﾛﾝみかんりんご
# ﾒﾛﾝ
# みかん
