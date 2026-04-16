#!/usr/bin/env python3
import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. 首页 Herro 标语
html = html.replace('让有机走进每个社区', '一起种地、一起做饭、把收获分享出去')

# 2. 品牌介绍
html = html.replace('认地人致力于打造社区共享有机菜园', '认地人致力于推动社区（社群）共享菜园')
html = html.replace('我们坚持有机种植', '我们坚持按有机方式种植')
html = html.replace('连接农场与社区，共建邻里共享的新生活方式', '推动社群自主对接农场与农户，共建邻里共享的新生活方式')

# 3. 会员福利 - "享受全年有机蔬菜供应"
html = html.replace('认领专属一米菜园，享受全年有机蔬菜供应', '你种一块、我种一块、互相分享、把收获分享出去')

# 4. 会员价修改做成字典
price_map = {
    '糙米</td><td>¥9.5/斤</td><td>¥17/斤</td>':        '糙米</td><td>¥10.8/斤</td><td>¥17/斤</td>',
    '现碾胚芽米</td><td>¥10/斤</td><td>¥18/斤</td>':   '现碾胚芽米</td><td>¥13/斤</td><td>¥18/斤</td>',
    '豆皮</td><td>¥6/斤</td><td>¥12/斤</td>':           '豆皮</td><td>¥9.8/斤</td><td>¥12/斤</td>',
    '豆翅</td><td>¥12/斤</td><td>¥22/斤</td>':          '豆翅</td><td>¥12.8/斤</td><td>¥22/斤</td>',
    '黄豆</td><td>¥7/斤</td><td>¥13/斤</td>':           '黄豆</td><td>¥4.5/斤</td><td>¥13/斤</td>',
    '芝麻油</td><td>¥25/瓶</td><td>¥42/瓶</td>':        '芝麻油</td><td>¥33/瓶</td><td>¥42/瓶</td>',
    '红枣</td><td>¥15/斤</td><td>¥28/斤</td>':           '红枣</td><td>¥18/斤</td><td>¥28/斤</td>',
    '红糖</td><td>¥10/斤</td><td>¥18/斤</td>':           '红糖</td><td>¥29/斤</td><td>¥38/斤</td>',
    '花生</td><td>¥8/斤</td><td>¥15/斤</td>':            '带壳花生</td><td>¥18/斤</td><td>¥15/斤</td>',
    '木耳</td><td>¥35/斤</td><td>¥60/斤</td>':           '木耳</td><td>¥38/半斤</td><td>¥60/斤</td>',
    '海带</td><td>¥12/斤</td><td>¥22/斤</td>':           '海带</td><td>¥38/斤</td><td>¥22/斤</td>',
    '藕粉</td><td>¥20/斤</td><td>¥35/斤</td>':           '藕粉</td><td>¥32.8/半斤</td><td>¥35/斤</td>',
    '肉桂粉</td><td>¥18/瓶</td><td>¥32/瓶</td>':         '肉桂粉</td><td>¥18/瓶</td><td>¥32/瓶</td>',
    '辣椒粉</td><td>¥15/瓶</td><td>¥26/瓶</td>':         '辣椒粉</td><td>¥16/瓶</td><td>¥26/瓶</td>',
    '五香粉</td><td>¥12/瓶</td><td>¥22/瓶</td>':         '五香粉</td><td>¥18/瓶</td><td>¥22/瓶</td>',
    '咖喱粉</td><td>¥18/瓶</td><td>¥32/瓶</td>':         '咖喱粉</td><td>¥18/瓶</td><td>¥32/瓶</td>',
    '茶籽粉</td><td>¥10/斤</td><td>¥18/斤</td>':         '茶籽粉</td><td>¥29.9元/5斤</td><td>¥18/斤</td>',
}

for old, new in price_map.items():
    if old in html:
        html = html.replace(old, new)
        print(f'✅ 替换: {old[:30]}...')
    else:
        print(f'❌ 未找到: {old[:30]}...')

# 5. 自提点
html = html.replace(
    '<strong>📍 朱家角古镇站</strong><br>\n          上海市青浦区朱家角古镇菜园基地<br>\n          营业时间：每日 8:00 - 18:00',
    '<strong>📍 朱家角古镇共享厨房</strong><br>\n          上海市青浦区大新街84弄13号<br>\n          营业时间：每日 8:00 - 18:00'
)

with open('index.html', 'w') as f:
    f.write(html)

print('\n✅ 所有修改完成！')
