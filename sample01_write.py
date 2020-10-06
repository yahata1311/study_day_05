# user02.text へﾃﾞｰﾀを書き込む
f = open('users02.text',mode='w')

f.write('りんご')
f.write('ﾒﾛﾝ')
f.write('みかん')

f.write('りんご\n') # \n は改行の意味
f.write('ﾒﾛﾝ\n')
f.write('みかん\n')

f.close()

