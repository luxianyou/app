
"""
@author: gwu
@software: PyCharm
@time: 2017/3/7 0007 18:11
"""

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

__basePath = '../data/'
__fileNamePath = u'../data/wordcloud/love.txt'
__stopWordPath = u'../data/dict/stopword/stopwords.txt'
__imagePath = u'../data/image/danan.jpeg'
__ttfPath = u'../data/font/FangZhengShuSongJianTi-1.ttf'

if __name__ == '__main__':
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, __fileNamePath)).read()

    # read the mask / color image
    # taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    alice_coloring = imread(path.join(d, __imagePath))

    wc = WordCloud(font_path=__ttfPath,background_color="black", max_words=2000, mask=alice_coloring,
               stopwords=STOPWORDS.add("said"),
               max_font_size=100, random_state=42)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    plt.imshow(wc)
    plt.axis("off")
    plt.figure()
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()