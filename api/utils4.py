import re
def sen_processing(gen_sen):
    processed_sen = re.sub("\'|<|>", "", gen_sen)
    # processed_sen = processed_sen[:len(gen_sen)]

    return processed_sen