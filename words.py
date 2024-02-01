import nltk
from nltk.corpus import brown
from nltk import FreqDist
from translate import Translator
import random
from datetime import datetime
import configparser
import os
import json


config = configparser.ConfigParser()
# config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))
config.read('config.ini')

today_seed=0 
target_language=config.get('settings', 'language')

def generate_seed():
    global today_seed
    
    now = datetime.now()
    seed_components = [
    now.year,
    now.month,
    now.day
    ]
        
    today_seed = int("".join(map(str, seed_components)))
    random.seed(today_seed)

def get_random_verbs(num_verbs=6):
    common_verbs=""
    with open("verbs.json", 'r') as json_file:
        common_verbs = json.load(json_file)
        
    random.shuffle(common_verbs)
    fuck_continuous = [word for word in common_verbs if not (word.endswith("ing") and word not in ["bring", "sing"])]
    todays_verbs = fuck_continuous[:num_verbs]
    return make_strings(todays_verbs)

def get_random_adjectives(num_adj=6):
    common_adj=""
    with open("adj.json", 'r') as json_file:
        common_adj = json.load(json_file)
        
    random.shuffle(common_adj)
    todays_adj = common_adj[:num_adj]
    return make_strings(todays_adj)

def get_random_nouns(num_nouns=6):
    common_nouns=""
    with open("nouns.json", 'r') as json_file:
        common_nouns = json.load(json_file)
    
    random.shuffle(common_nouns)
    todays_nouns = common_nouns[:num_nouns]
    return make_strings(todays_nouns)

def make_strings(my_list):
    translated_list = translate_list(my_list)
    output= ""
    for original, translated in zip(my_list,translated_list):
        output += f"-{original} = {translated}\n"
    return output

def translate_text(text):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def translate_list(list):
    translator = Translator(to_lang=target_language)
    all_words=""
    for index, item in enumerate(list):
        all_words += item
        if index < len(list) - 1:
            all_words += "<>"
    
    translated=translator.translate(all_words)
    translated_list = translated.split("<>")
    
    return translated_list

def get_random_sentence():
    sentence_list=""
    with open("sentence.json", 'r') as json_file:
        sentence_list = json.load(json_file)
        
    random.shuffle(sentence_list)
    translator = Translator(to_lang=target_language)
    translation = translator.translate(sentence_list[0])
    return translation