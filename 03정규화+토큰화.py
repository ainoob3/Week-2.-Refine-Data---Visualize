#03정규화+토큰화
from konlpy.tag import Okt

# 한국어 텍스트 입력
text = "이 몸이 죽고 죽어,일백 번 고쳐죽어,백골이 진토 되어,넋이라도 있고 없고, 임 향한 일편단심이야, 가실 줄이 있으랴."

# KoNLPy의 Okt 형태소 분석기를 사용하여 형태소 분석 수행
okt = Okt()

# 첫 번째 텍스트에 대한 형태소 분석
tokens = okt.morphs(text)

# 정규화된 텍스트 생성
normalized_text = ' '.join(tokens)

# 출력
print(normalized_text)
print()

# 두 번째 텍스트에 대한 형태소 분석
print('형태소:', tokens)
print('명사:', okt.nouns(text))
print('품사:', okt.pos(text))
