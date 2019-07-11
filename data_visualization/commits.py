# coding=utf-8
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


comment = []
with open('..\\data_cleaning\\de_duplication.dat', 'r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            comment.append(row.split(',')[4].replace('\n', ''))

comment_after_split = jieba.cut(str(comment).encode('utf-8'), cut_all=False)

print(comment_after_split)
wl_space_split = " ".join(comment_after_split)
# print(wl_space_split)

# 导入背景图
backgroud_Image = plt.imread('1.jpg')

# 屏蔽词汇
stopwords = STOPWORDS.copy()
# 可以加多个屏蔽词
stopwords.add ("这样")
stopwords.add ("一个")
stopwords.add ("还行")
stopwords.add ("就是")
stopwords.add ("真的")
stopwords.add ("一样")
stopwords.add ("希望")
stopwords.add ("应该")
stopwords.add ("感觉")
stopwords.add ("终于")
stopwords.add ("这部")
stopwords.add ("不知道")
stopwords.add ("超级")
stopwords.add ("自己")
stopwords.add('非常')
stopwords.add ("每次")
stopwords.add('可以')
stopwords.add('呵呵')
stopwords.add('电影')
stopwords.add('不能')
stopwords.add('有点')

# 设置词云参数
# 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
wc = WordCloud(width=464, height=644, background_color='WHITE',
                mask=backgroud_Image, font_path='STLITI.TTF',stopwords=stopwords, max_font_size=600,
                random_state=50)
# print(wl_space_split.encode('utf-8'))
wc.generate_from_text(wl_space_split)
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
# print(wc)
plt.imshow(wc)
plt.axis('off')  # 不显示坐标轴
plt.show ()

# 保存结果到本地
wc.to_file ('wordcloud.jpg')
