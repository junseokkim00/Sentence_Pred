import re
import openai
import time


openai.api_key = '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'

def send_message_1(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그러나 <A> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그러나 <A> <B 부정.>의 예시야 :\
         - <나는 밥을> <먹어야 한다.> 그러나 <나는 밥을> <먹지 않는다.>\
         - <세상에는> <희망이 없다고 한다.> 그러나 <세상에는> <희망이 있다.>\
         - <어느 모임에는> <구성원들이 있다.> 그러나 <어느 모임에는> <구성원들이 없다.>\
         - <역사학에서는> <사료를 중요시한다고 한다.> 그러나 <역사학에서는> <사료를 중요시하지 않는다.>\
         - <채소는> <땅에서 자라지 않는다고 한다.> 그러나 <채소는> <땅에서 자란다.>\
         - <여학생들은> <부정적인 태도를 가지고 있다고 알려져 있다.> 그러나 <여학생들은> <부정적인 태도를 안 가지고 있다.>"},
        {"role": "user", "content": f'\'{message} 그러나\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
        # {"role" : "user", "content" : message}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

def send_message_2(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A 부정> <B.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A 부정> <B.>의 예시야 :\
         - <남자가> <학교에 가려고 했다.> 그러나 <여자가> <학교에 갔다.>\
         - <내연 기관 자동차가> <많지 않다.> 그러나 <전기 자동차도> <많지 않다.>\
         - <큰 기업들도> <문을 닫고 있다고 한다.> 그러나 <작은 기업들만> <문을 닫고 있다.>\
         - <알려진 것에 의하면 최근 가장 주목을 받고 있는 사람들이> <선행을 베푸는 사람들이다.> 그러나 <사실 최근 가장 주목을 받지 않고 있는 사람들이> <선행을 베푸는 사람들이다.>\
         - <비공식적인 자리에도> <사람들을 초청하였다고 한다.> 그러나 <공식적인 자리에만> <사람들을 초청하였다.>\
         - <알려진 것에 의하면 남성 학자들이> <인공 지능 개발을 중지해야 한다고 주장하고 있다.> 그러나 <사실 여성 학자들이> <인공 지능 개발을 중지해야 한다고 주장하고 있다.>"},
        {"role": "user", "content": f'\'{message} 그러나나\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
        # {"role" : "user", "content" : message}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

def send_message_3(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A 부정> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A 부정> <B 부정.>의 예시야 :\
            - <과거에는> <나쁜 영화들이 있었다.> 그러나 <현재는> <나쁜 영화들이 없다.>\
            - <과거에는> <개업하는 사람들도 있었다.> 그러나 <현재는> <폐업하는 사람들만 있다.>\
            - <남자들은> <매운 국수를 좋아한다.> 그러나 <여자들은> <맵지 않은 국수를 좋아한다.>\
            - <피고는> <사건을 확대했다.> 그러나 <원고는> <사건을 축소했다.>\
            - <농촌은> <동물이 서식하기 좋은 환경이 된다.> 그러나 <도시는> <동물이 서식하기 좋은 환경이 못 된다.>"},
        {"role": "user", "content": f'\'{message} 그러나나\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
        # {"role" : "user", "content" : message}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

utils1_list = [send_message_1, send_message_2, send_message_3]

# def send_message_4(message):
#     messages = [
#         {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 부정.>의 예시야 :\
#          - <세상에는> <절망만 있다고 한다.> 따라서 <세상에는> <희망이 있다고 알릴 필요가 있다.>\
#          - <원고와 피고는> <오해를 풀지 않았다.> 따라서 <원고와 피고는> <오해를 풀어야 한다.>\
#          - <농촌에서는> <동물들이 살기에 좋은 서식지를 만들지 않고 있다.> 따라서 <농촌은> <동물들이 살기에 좋은 서식지를 만들어야 한다.>\
#          - <왕과 왕비는> <백성들을 보살피지 않는다.> 따라서 <왕과 왕비는> <백성들을 보살피지 않는 것을 반성해야 한다.>\
#          - <그녀는> <자신의 연구 성과를 알리고 싶어 하지 않는다.> 따라서 <그녀는> <연구 성과를 알리기 위한 공식적인 자리를 마련하라는 충고를 거절해야 한다.>"},
#         {"role": "user", "content": f'\'{message}\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
#         # {"role" : "user", "content" : message}
#         ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=messages
#     )

#     return response

# def send_message_8(message):
#     messages = [
#         {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 부정.>의 예시야 :\
#          - <세상에는> <절망만 있다고 한다.> 따라서 <세상에는> <희망이 있다고 알릴 필요가 있다.>\
#          - <원고와 피고는> <오해를 풀지 않았다.> 따라서 <원고와 피고는> <오해를 풀어야 한다.>\
#          - <농촌에서는> <동물들이 살기에 좋은 서식지를 만들지 않고 있다.> 따라서 <농촌은> <동물들이 살기에 좋은 서식지를 만들어야 한다.>\
#          - <왕과 왕비는> <백성들을 보살피지 않는다.> 따라서 <왕과 왕비는> <백성들을 보살피지 않는 것을 반성해야 한다.>\
#          - <그녀는> <자신의 연구 성과를 알리고 싶어 하지 않는다.> 따라서 <그녀는> <연구 성과를 알리기 위한 공식적인 자리를 마련하라는 충고를 거절해야 한다.>"},
#         {"role": "user", "content": f'\'{message}\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
#         # {"role" : "user", "content" : message}
#         ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=messages
#     )

#     return response

# def send_message_9(message):
#     messages = [
#         {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 부정.>의 예시야 :\
#          - <세상에는> <절망만 있다고 한다.> 따라서 <세상에는> <희망이 있다고 알릴 필요가 있다.>\
#          - <원고와 피고는> <오해를 풀지 않았다.> 따라서 <원고와 피고는> <오해를 풀어야 한다.>\
#          - <농촌에서는> <동물들이 살기에 좋은 서식지를 만들지 않고 있다.> 따라서 <농촌은> <동물들이 살기에 좋은 서식지를 만들어야 한다.>\
#          - <왕과 왕비는> <백성들을 보살피지 않는다.> 따라서 <왕과 왕비는> <백성들을 보살피지 않는 것을 반성해야 한다.>\
#          - <그녀는> <자신의 연구 성과를 알리고 싶어 하지 않는다.> 따라서 <그녀는> <연구 성과를 알리기 위한 공식적인 자리를 마련하라는 충고를 거절해야 한다.>"},
#         {"role": "user", "content": f'\'{message}\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
#         # {"role" : "user", "content" : message}
#         ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=messages
#     )

#     return response

# def send_message_10(message):
#     messages = [
#         {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <B 부정.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <B 부정.>의 예시야 :\
#          - <세상에는> <절망만 있다고 한다.> 따라서 <세상에는> <희망이 있다고 알릴 필요가 있다.>\
#          - <원고와 피고는> <오해를 풀지 않았다.> 따라서 <원고와 피고는> <오해를 풀어야 한다.>\
#          - <농촌에서는> <동물들이 살기에 좋은 서식지를 만들지 않고 있다.> 따라서 <농촌은> <동물들이 살기에 좋은 서식지를 만들어야 한다.>\
#          - <왕과 왕비는> <백성들을 보살피지 않는다.> 따라서 <왕과 왕비는> <백성들을 보살피지 않는 것을 반성해야 한다.>\
#          - <그녀는> <자신의 연구 성과를 알리고 싶어 하지 않는다.> 따라서 <그녀는> <연구 성과를 알리기 위한 공식적인 자리를 마련하라는 충고를 거절해야 한다.>"},
#         {"role": "user", "content": f'\'{message}\' 뒤에 나올 문장을 끊지 말고 하나 생성해줘.'}
#         # {"role" : "user", "content" : message}
#         ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=messages
#     )

#     return response
