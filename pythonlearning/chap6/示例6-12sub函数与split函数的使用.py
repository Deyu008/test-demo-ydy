import re
pattern=r'黑客|破解|反爬'
s='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
# re.sub是替换
new_s=re.sub(pattern,'XXX',s)  # 遇到pattern中的词,就替换成'XXX'
print(new_s)

s2='https://www.baidu.com/s?wd=ysj&rsv_spt=1'
pattern2='[?|&]'
# re.split是分隔
lst=re.split(pattern2,s2)
print(lst)

