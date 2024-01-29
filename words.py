import nltk
from nltk.corpus import brown
from nltk import FreqDist
import random

nltk.download('brown')

def get_random_verbs(num_verbs=6):
    all_verbs = [word.lower() for word,pos in brown.tagged_words() if pos.startswith('VB')]
    verb_freq = FreqDist(all_verbs)
    common_verbs = [verb for verb, _ in verb_freq.most_common(1200)]
    random.shuffle(common_verbs)
    fuck_continuous = [word for word in common_verbs if not (word.endswith("ing") and word not in ["bring", "sing"])]
    todays_verbs = fuck_continuous[:num_verbs]
    return make_strings(todays_verbs)

def get_random_adjectives(num_adj=6):
    all_adj = [word.lower() for word,pos in brown.tagged_words() if pos.startswith('JJ')]
    adj_freq = FreqDist(all_adj)
    common_adj = [adj for adj, _ in adj_freq.most_common(1200)]
    random.shuffle(common_adj)
    todays_adj = common_adj[:num_adj]
    return make_strings(todays_adj)

def get_random_nouns(num_nouns=6):
    all_nouns = [word.lower() for word,pos in brown.tagged_words() if pos.startswith('NN')]
    nouns_freq = FreqDist(all_nouns)
    common_nouns = [noun for noun, _ in nouns_freq.most_common(1200)]
    todays_nouns = common_nouns[:num_nouns]
    return make_strings(todays_nouns)

def make_strings(my_list):
    output = ""
    for index, string in enumerate(my_list):
        output += string
        if index < len(my_list) - 1:
            output += "\n"
    return output
