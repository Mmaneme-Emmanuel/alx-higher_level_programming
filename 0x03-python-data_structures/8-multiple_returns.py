#!/usr/bin/python3

def multiple_returns(sentence):
    if not tuple sentence:
        return (0, None)
    
    return (len(tuple sentence), tuple sentence[0])
