## Scanner function
## Used some list comprehension for tuples from here -
## https://bytes.com/topic/python/answers/521450-how-reverse-tuples-list

def scan(sentence):

    lexicon_tuples = [('direction', 'north'), ('direction','south'), ('direction', 'east'),
        ('direction', 'west'), ('direction', 'down'), ('direction', 'up'), ('direction', 'left'), ('direction', 'right'), ('direction', 'back'),
        ('verb', 'go'), ('verb', 'stop'), ('verb', 'kill'), ('verb', 'eat'),
        ('stop', 'the'), ('stop', 'in'), ('stop', 'of'), ('stop','from'), ('stop','at'), ('stop', 'it'),
        ('noun', 'door'), ('noun', 'bear'),('noun', 'princess'),('noun', 'cabinet')]

    words = sentence.split()

    ## List to store output
    result = []

    inv_lexicon_tuples = [(b,a) for a, b in lexicon_tuples]
    inv_lexicon_tuples = dict(inv_lexicon_tuples)

    for i in range(0, len(words)):
        is_num = ConvertToNum(words[i])
        if is_num == False and words[i] in inv_lexicon_tuples:
            result.append((inv_lexicon_tuples.get(words[i]), words[i]))
        elif is_num == False and words[i] not in inv_lexicon_tuples:
            result.append(('error', words[i]))
        else:
            result.append(('number', is_num))

    return result

def ConvertToNum(n):
    try:
        return int(n)
    except ValueError:
        return False

## All tests were passed
