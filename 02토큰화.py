#토큰화(단어)
from konlpy.tag import Okt

text = '형태소분석으로 문장을 분해해보자'
okt = Okt()
tokens = okt.morphs(text)
print()
print('형태소:', tokens)
print()
print('명사:', okt.nouns(text))
print()
print('품사:', okt.pos(text))
