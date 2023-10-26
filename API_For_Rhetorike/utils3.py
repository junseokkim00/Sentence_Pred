import re
import openai
import time


openai.api_key = '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'

def send_message_1(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 강조.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 강조.>의 예시야 :\
         - <우리는> <희망을 쉽게 찾는다.> 따라서 <우리는> <희망을 쉽게 찾는 것을 바꾸지 않아야 한다.>\
         - <나는> <밥을 알맞게 먹기 때문에 건강하다.> 따라서 <나는> <건강한 상태를 유지하기 위해서 밥을 알맞게 먹어야 한다.>\
         - <우리는> <희망을 쉽게 찾는다.> 따라서 <우리는> <희망을 쉽게 찾는 것을 바꾸지 않는 것이 중요하다.>\
         - <세상에 절망은 없다><고 한다.> 따라서 <세상에 절망은 없다고 알리는 것이> <중요하다.>\
         - <채소는> <땅에서 자란다.> 따라서 <채소는> <땅에서 키우는 것이 중요하다.>"},
        {"role": "user", "content": f'\'{message}\' 뒤에 나올 문장을 끊지 말고 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )
    return response

def send_message_2(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 부정.>의 예시야 :\
         - <세상에는> <절망만 있다고 한다.> 따라서 <세상에는> <희망이 있다고 알릴 필요가 있다.>\
         - <원고와 피고는> <오해를 풀지 않았다.> 따라서 <원고와 피고는> <오해를 풀어야 한다.>\
         - <농촌에서는> <동물들이 살기에 좋은 서식지를 만들지 않고 있다.> 따라서 <농촌은> <동물들이 살기에 좋은 서식지를 만들어야 한다.>\
         - <왕과 왕비는> <백성들을 보살피지 않는다.> 따라서 <왕과 왕비는> <백성들을 보살피지 않는 것을 반성해야 한다.>\
         - <그녀는> <자신의 연구 성과를 알리고 싶어 하지 않는다.> 따라서 <그녀는> <연구 성과를 알리기 위한 공식적인 자리를 마련하라는 충고를 거절해야 한다.>"},
        {"role": "user", "content": f'\'{message}\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

utils3_list = [send_message_1, send_message_2]