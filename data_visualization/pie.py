# coding=utf-8
from pyecharts.charts import ThemeRiver
from pyecharts import options as opts

rate = []
with open ('..\\data_cleaning\\de_duplication.dat', 'r', encoding='utf-8') as f:
    rows = f.readlines ()
    for row in rows:
        if len (row.split (',')) == 5:
            rate.append (row.split (',')[3].replace ('\n', ''))
v1 = []
v1.append(rate.count ('5') + rate.count ('4.5'))
v1.append(rate.count ('4') + rate.count ('3.5'))
v1.append(rate.count ('3') + rate.count ('2.5'))
v1.append(rate.count ('2') + rate.count ('1.5'))
v1.append(rate.count ('1') + rate.count ('0.5'))

# 饼状图
from pyecharts.charts import Pie

attr = ["五星", "四星", "三星", "二星", "一星"]
print(v1)
# 分别代表各星级评论数
# v1 = [3324, 1788, 1293, 553, 1653]
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(attr, v1)],
        radius=["30%", "75%"],
        center=["25%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add(
        "",
        [list(z) for z in zip(attr, v1)],
        radius=["30%", "75%"],
        center=["75%", "50%"],
        rosetype="area",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-星级玫瑰图示例"))
).render('Pie.html')

