#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence = None
        tuple_result = (0, sentence)
        return tuple_result
    else:
        count = len(sentence)
        tuple_result = (count, sentence[0])
        return tuple_result
