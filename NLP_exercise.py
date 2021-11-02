import imageio
from nltk import text
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob, blob
from pathlib import Path

import textblob

# nltk.download("stopwords")

stops = stopwords.words("english")

text = TextBlob(Path("book of John text.txt").read_text())


more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]

stops += more_stops
# text = TextBlob(Path('book of John text.txt').read_text())
# print(stops)

blob1 = []
blob1 += text.noun_phrases
items = text.word_counts.items()
# print(items)
from operator import itemgetter

cleanitems = [i for i in items if i[0] in blob1 and i[0] not in stops]
sorted_list = sorted(cleanitems, key=itemgetter(1), reverse=True)

# print(text.noun_phrases)

top = sorted_list[:15]


top15 = " "
for i in top:
    top15 += i[0]
    top15 += " "


# mask_image = imageio.imread("mask_oval.png")

wordcloud = WordCloud(colormap="prism", background_color="grey")

wordcloud = wordcloud.generate(top15)

wordcloud = wordcloud.to_file("book of John text_oval.png")

print("Done")
