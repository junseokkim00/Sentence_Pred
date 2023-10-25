import re
import openai
import time

# Set up your OpenAI API credentials
openai.api_key = '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'
txt_path = './generated_sents.txt'

def send_message(message):
    messages = [
        {"role": "system", "content": "너는 <A B.> 그런데 <B C.> 형태로 문장을 생성해. 다음은 <A B.> 그런데 <B C.>의 예시야 :\
         - <파이썬은 프로그래밍 언어이다.> 그런데 <프로그래밍 언어는 컴퓨터와 소통하는 도구이다.>\
         - <도서관은 책이 모여 있는 장소이다.> 그런데 <그러한 장소는 지식과 상상력을 키워주는 보물창고와도 같다.>\
         - <나는 친구와 함께 영화를 보러 갔다.> 그런데 <영화를 보러 가는 것은 은근히 힘이 드는 일이다.> \
         - <이것은 향수이다.> 그런데 <향수는 향과 알코올, 용기 등으로 만든다.> \
         - <나는 친구와 함께 쇼핑을 하러 갔다.> 그런데 <쇼핑은 돈과 시간, 취향 등을 필요로 한다.>\
         - <생물학계에서는 인류의 미래에 대한 로렌츠의 낙관적인 전망을 소개하였다.> 그런데 <이러한 로렌츠의 낙관적인 전망을 많은 생물학자들은 인류의 미래를 어떻게 보아야 할 것인가 하는 문제의 중요한 해결 방안들 중의 하나로 생각하고 있다.>\
         - <이것은 비행기이다.> 그런데 <비행기는 공기역학의 원리에 따라 날 수 있다.>"},
        {"role": "user", "content": " 주어진 \"문장\"을 <A,B> 라고 할 때, <B,C>로 가능한 문장을 4개 출력해줘."} # <A B.> 그런데 <B C.> 형태의 문장을 30개 생성해줘.
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )

    return response

def text_save(file_path, sentences) :
    file = open(file_path, "a")
    file.write('\n')
    for sen in sentences:
        file.write(sen)
    file.close()

# '''
# main
# '''
# print("Processing")
# while True:
    
#     start = time.time()

#     response = send_message('')
#     text_save(txt_path, response['choices'][0]['message']['content'])
#     print('prompt_tokens : ', response['usage']['prompt_tokens'])
#     print('completion_tokens : ', response['usage']['completion_tokens'])
#     print('total_tokens : ', response['usage']['total_tokens'])

#     end = time.time()

#     print(f"30 sentences generated. {end - start:.5f} sec")
