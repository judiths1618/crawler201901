# coding=utf-8
from pyecharts import options as opts
from pyecharts.charts import Geo, Map
from pyecharts.globals import ChartType, SymbolType


# 读取城市数据
def city(file):
    cities = []
    with open(file, mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        for row in rows:
            if len(row.split(',')) == 5:
                cities.append(row.split(',')[2].replace('\n', ''), )
    return cities
city_data = city('..\\data_cleaning\\de_duplication.dat')


def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

# TODO: 城市数据-城市的地理位置信息不够明确，待完善
CITY=list(all_list(city_data))
VALUE=list(all_list(city_data).values())
print([list(z) for z in zip(CITY, VALUE)])
c = (
        Map()
        .add("《千与千寻》全国粉丝群众分布", [list(z) for z in zip(CITY, VALUE)], 'china')
        .set_global_opts (
            title_opts=opts.TitleOpts (title="Map-VisualMap（分段型）"),
            visualmap_opts=opts.VisualMapOpts (max_=200, is_piecewise=True),
        )
    ).render('Map.html')

