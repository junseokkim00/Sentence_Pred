
def sen_processing(gen_sen, user_input):
    processed_sen = gen_sen.replace('\'','<','>')
    # processed_sen = processed_sen[:len(gen_sen)]

    return processed_sen