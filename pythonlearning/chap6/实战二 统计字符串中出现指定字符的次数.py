s='HelloPython,HelloJava,Hellophp'
word=input('请输入要统计的字符:')
print('{0}在{1}一共出现了{2}次'.format(word,s,s.lower().count(word)))