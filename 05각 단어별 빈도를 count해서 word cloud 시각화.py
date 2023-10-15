import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
# 한국어 텍스트 입력 (예시)
text = """
 “사상 최고치! 대규모 경제성장!”

요즘 일본 경제가 좋다는 환호성이 들려온다. 그렇다면 지금이 일본에 ‘올인’할 타이밍일까? 천천히 생각해보자. 과장된 기사 제목들은 뿌리 깊은 이슈들을 숨기고 있다. 일본 주식은 선별적으로 보유하고, 지나친 투자는 피해야 한다.

올해 일본 증시는 쭉쭉 상승하며 기대감을 불러일으켰다. 지난 5월 토픽스와 닛케이평균은 모두 33년 만에 최고치를 기록했고, 토픽스는 9월에 이를 또 경신했다. 초여름의 흥분은 조금 가라앉았지만, 월가에서는 여전히 일본에 대한 낙관론이 높다.

올해 초 애널리스트들은 일본 주식 중간값이 올해 13.1% 상승할 것이라고 예측했다. 지금은 연말까지 4.5% 추가 상승을 포함, 무려 29.3%의 연간 상승을 예측하고 있다. 뱅크오브아메리카(BoA)의 글로벌 설문조사도 비슷하다. 8월 펀드매니저들의 일본 증시 투자 비율은 6% 증가했고, 이는 2022년 연말 6% 감소했던 것에서 상당히 상승한 수치다. 또한 연율 기준 6%를 기록한 일본의 2분기 GDP 성장률은 전망치인 3.1%와 1분기의 3.7%를 상회했다. 일각에서는 이러한 성장이 견고하게 지속될 것이라고 본다.

우려 사항도 있다. 우선, 이런 기록적인 고점은 일부 환율 왜곡에서 비롯됐다. 달러로 환산한 총수익률은 여전히 2021년 최고치에 한참 못 미치고, 2023년 8월까지 글로벌 주식 수익률에도 약간 뒤처진다. 일본 경제는 오랫동안 구조적인 문제로 골머리를 앓아 왔다. 일본의 GDP 성장은 수출에 크게 의존하고 있는데, 연율 기준 13.6%인 2분기 수출 성장률은 -2.2%의 저조한 소비 지출과 -16.2%의 수입 감소를 감추고 있다.  느린 개혁 과정도 별다른 위안을 주지 못한다. 한국의 재벌들처럼 일본의 대기업들도 글로벌 시장에서 상대적으로 낮은 가격에 거래된다. 새로운 상장 규제들이 기업 주주 가치 상승을 약속한다. 하지만 실행은 더디고 이미 널리 알려져 있으며, 아무것도 보장해주지 않는다. 재벌과 유사한 성장통을 예상할 수 있다. 채권 수익률 곡선 조정은 빈약한 대책일 뿐이다. 일본은 여전히 통화정책의 난관에 봉착해 있다.

따라서 지금은 일본에 집중할 때가 아니다. 물론 부분적인 투자는 괜찮다. 양질의 성장주를 찾고, 일본 내수 의존도가 낮은 수출 기업에 집중하는 것이 좋다. 특히, 반도체 및 반도체 장비 기업 등 테크 분야를 주목해야 한다. 이 분야의 높은 46%의 총이익은 재투자를 촉진한다. 알다시피 완화되는 한일 통상 관계도 도움이 된다.

하지만 테크는 일본 시장의 14%에 불과하다. 이에 비해 한국과 미국은 테크 시장의 비중이 더 크고, 대만도 마찬가지다. 그렇기에 일본 주식으로 포트폴리오를 다각화하되, 집착은 피해야 한다. 월가의 과도한 낙관론은 무시하고, 양질의 성장주를 찾는 것이 중요하다. 그곳이 한국이든, 일본이든, 어디든.
"""

# 정규식을 사용하여 한글 외 문자 제거
text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣ\s]', '', text)

# KoNLPy의 Okt 형태소 분석기를 사용하여 형태소 분석 수행
okt = Okt()
tokens = okt.morphs(text)

# 불용어 사전을 로드하고 불용어 제외한 단어 추출
stopwords = ["을", "를", "이", "가", "은", "는", "하다", "그", "에", "의"]
filtered_words = [word for word in tokens if word not in stopwords]

# 각 단어별 빈도수 계산
word_counts = Counter(filtered_words)

# filtered_words를 하나의 문자열로 합치기
text_for_wordcloud = ' '.join(filtered_words)

# Word cloud 생성
wordcloud = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumGothic.ttf', background_color='white', width=800, height=600)
wordcloud.generate(text_for_wordcloud)

# Word cloud 시각화
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

print(word_counts)