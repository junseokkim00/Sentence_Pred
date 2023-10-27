import re
import openai
import time
from apikey import OPENAI_KEY


openai.api_key = OPENAI_KEY

# 긍정 - 유지
def send_message_1(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 강조.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 강조.>의 예시야 :\
         - <우리는> <희망을 쉽게 찾는다.> 따라서 <우리는> <희망을 쉽게 찾는 것을 바꾸지 않아야 한다.>\
         - <나는> <밥을 알맞게 먹기 때문에 건강하다.> 따라서 <나는> <건강한 상태를 유지하기 위해서 밥을 알맞게 먹어야 한다.>\
         - <우리는> <희망을 쉽게 찾는다.> 따라서 <우리는> <희망을 쉽게 찾는 것을 바꾸지 않는 것이 중요하다.>\
         - <세상에 절망은 없다><고 한다.> 따라서 <세상에 절망은 없다고 알리는 것이> <중요하다.>\
         - <채소는> <땅에서 자란다.> 따라서 <채소는> <땅에서 키우는 것이 중요하다.>"},
        {"role": "user", "content": f'\'{message} 따라서\' 뒤에 나올 문장을 끊지 말고 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )
    return response

# 부정 - 개선
def send_message_2(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 부정.>의 예시야 :\
         - <세상에는> <절망만 있다고 한다.> 따라서 <세상에는> <희망이 있다고 알릴 필요가 있다.>\
         - <원고와 피고는> <오해를 풀지 않았다.> 따라서 <원고와 피고는> <오해를 풀어야 한다.>\
         - <농촌에서는> <동물들이 살기에 좋은 서식지를 만들지 않고 있다.> 따라서 <농촌은> <동물들이 살기에 좋은 서식지를 만들어야 한다.>\
         - <왕과 왕비는> <백성들을 보살피지 않는다.> 따라서 <왕과 왕비는> <백성들을 보살피지 않는 것을 반성해야 한다.>\
         - <그녀는> <자신의 연구 성과를 알리고 싶어 하지 않는다.> 따라서 <그녀는> <연구 성과를 알리기 위한 공식적인 자리를 마련하라는 충고를 거절해야 한다.>"},
        {"role": "user", "content": f'\'{message} 따라서\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

# 긍정 - 현재상황
def send_message_3(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 관련 현재상황.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 관련 현재상황.>의 예시야 :\
         - <나는> <세상에 희망이 많이 남아있다는 말을 믿는다.> 따라서 <나는> <그러한 희망을 붙잡을 준비를 하고 있다.>\
         - <아버지께서는> <어머니와 잘 지내시는 걸 좋아한다.> 따라서 <아버지께서는> <어머니와 잘 지내기 위해 노력하고 계신다.>\
         - <우리 정부는> <인공지능 사업의 잠재 가치를 확인했다.> 따라서 <우리 정부는> <인공지능 연구를 위해 예산을 확보하고 있다.>\
         - <노트북은> <인간 삶에 꼭 필요하다.> 따라서 <노트북은> <인간 삶의 편의를 위해 더욱 발전하고 있다.>\
         - <음악은> <사람들에게 힘을 불어넣는다.> 따라서 <음악은> <사람들에게 도움을 주고 있다.>"},
        {"role": "user", "content": f'\'{message} 따라서\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

# 부정 - 현재상황
def send_message_4(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 관련 현재상황.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 관련 현재상황.>의 예시야 :\
         - <나는> <절망뿐인 일에 사로잡혔다.> 따라서 <나는> <절망을 없애기 위해 노력하고 있다.>\
         - <원고와 피고는> <오해가 계속 있었다.> 따라서 <원고와 피고는> <오해를 풀고 있다.>\
         - <농촌에서는> <동물들이 살기에 좋은 서식지를 만들지 않았었다.> 따라서 <농촌은> <동물들이 살기에 좋은 서식지가 아니게 되고 있다.>\
         - <왕과 왕비는> <백성들을 보살피지 않는다.> 따라서 <왕과 왕비는> <백성들에게 반감을 사고 있다.>\
         - <그녀는> <자신의 연구 성과를 알리고 싶어 하지 않는다.> 따라서 <그녀는> <연구 성과를 알리기 위한 공식적인 자리를 마련하라는 충고를 거절하고 있다.>"},
        {"role": "user", "content": f'\'{message} 따라서\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

utils3_list = [send_message_1, send_message_2, send_message_3, send_message_4]
