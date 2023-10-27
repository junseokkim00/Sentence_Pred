import re
import openai
import time
from apikey import OPENAI_KEY

openai.api_key = OPENAI_KEY


def send_message_2_1(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <B> <C.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <B> <C.>의 예시야 :\
         - <파이썬은> <프로그래밍 언어이다.> 그런데 <프로그래밍 언어는> <컴퓨터와 소통하는 도구이다.>\
         - <도서관은> <책이 모여 있는 장소이다.> 그런데 <그러한 장소는> <지식과 상상력을 키워주는 보물창고와도 같다.>\
         - <나는> <친구와 함께 영화를 보러 갔다.> 그런데 <영화를 보러 가는 것은> <은근히 힘이 드는 일이다.> \
         - <이것은> <향수이다.> 그런데 <향수는> <향과 알코올, 용기 등으로 만든다.> \
         - <나는> <친구와 함께 쇼핑을 하러 갔다.> 그런데 <쇼핑은> <돈과 시간, 취향 등을 필요로 한다.>\
         - <생물학계에서는> <인류의 미래에 대한 로렌츠의 낙관적인 전망을 소개하였다.> 그런데 <이러한 로렌츠의 낙관적인 전망을> <많은 생물학자들은 인류의 미래를 어떻게 보아야 할 것인가 하는 문제의 중요한 해결 방안들 중의 하나로 생각하고 있다.>\
         - <이것은> <비행기이다.> 그런데 <비행기는> <공기역학의 원리에 따라 날 수 있다.>"},
        {"role": "user", "content": f'\'{message} 그런데\' 뒤에 나올 문장을 끊지 말고 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

def send_message_2_2(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <C> <B.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <C> <B.>의 예시야 :\
         - <지금은> <농번기이다.> 그런데 <현재 우리나라에서는 모낼 때, 논맬 때, 추수할 때가> <이러한 농번기이다.>\
         - <이곳은> <공항이다.> 그런데 <현재 우리나라에서는 항공 수송을 위하여 사용하는 공공용 비행장이> <이러한 공항이다.>\
         - <이것은> <식탁이다.> 그런데 <지금 음식들을 차려놓는 탁자가> <이러한 식탁이다.> \
         - <영수는> <투자자이다.> 그런데 <소득 창출 자산을 신중하게 선택하여 구입하는 사람이> <이러한 투자자이다.> \
         - <영희는> <사회 복지사이다.> 그런데 <요즘 많은 사람들의 존경을 받는 전문가들 중의 하나가> <이러한 사회 복지사이다.>"},
        {"role": "user", "content": f'\'{message} 그런데\' 뒤에 나올 문장을 끊지 말고 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response


def send_message_2_3(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <A> <C.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <A> <C.>의 예시야 :\
         - <영수는> <영화 평론가이다.> 그런데 <이러한 영수는> <영화 한 편을 여러 번 감상하는 습관이 있다.>\
         - <그것은> <탄산음료이다.> 그런데 <그것은> <영수가 밥을 먹은 뒤에 마시려고 편의점에서 사 온 것이다.>\
         - <저것은> <무지개이다.> 그런데 <저것은> <간절하게 원하는 사람들의 소망을 이루어 준다고 한다.> \
         - <이것은> <의자이다.> 그런데 <이것은> <일반적으로 사람들이 앉아서 휴식을 취하거나 일을 하는 데에 쓰이는 기구이다.> \
         - <지금은> <가을철이다.> 그런데 <지금은> <벼를 수확하고 있다.>"},
        {"role": "user", "content": f'\'{message} 그런데\' 뒤에 나올 문장을 끊지 말고 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

def send_message_2_4(message):
    messages = [
        {"role": "system", "content": "너는 <A> <B.> 그런데 <C> <A.> 형태로 문장을 생성해. 다음은 <A> <B.> 그런데 <C> <A.>의 예시야 :\
         - <영희는> <학생이다.> 그런데 <얼마 전 인공 지능의 자연어 처리 논문을 발표하였던 사람이> <이러한 영희이다.> \
         - <영수는> <농부이다.> 그런데 <작년에 박사 학위를 취득했던 사람이> <이러한 영수이다.>\
         - <이것은> <침대이다.> 그런데 <하루 일과를 마친 현대인들에게 필요한 것이> <이것이다.>\
         - <지금은> <한밤중이다.> 그런데 <현재 우리나라에서 깊은 밤이> <지금이다.>\
         - <이것은> <기린이다.> 그런데 <동물원에서 아이들이 좋아하는 동물들 중의 하나가> <이것이다.>"},
        {"role": "user", "content": f'\'{message} 그런데\' 뒤에 나올 문장을 끊지 말고 생성해줘.'}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

utils2_list = [send_message_2_1, send_message_2_2, send_message_2_3, send_message_2_4]
