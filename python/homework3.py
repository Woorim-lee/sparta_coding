from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("sister.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[2:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('너무', '').replace('마자', '').replace('근데', '').replace('저도', '').replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '').replace('이모티콘\n', '').replace('사진\n', '').replace('삭제된 메세지입니다', '')

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/malgunbd.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked2.png")