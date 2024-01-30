import nltk
from nltk.corpus import brown
from nltk import FreqDist
from translate import Translator
import random

nltk.download('brown')

sentence_list = ["Good morning!",
"How are you?",
"What’s up?",
"How was your day?",
"How’s it going?",
"Nice to meet you.",
"What’s your name?",
"My name is _______.",
"Where are you from?",
"I’m from _______.",
"What do you do for a living?",
"Can you help me, please?",
"Thank you very much!",
"You’re welcome.",
"Excuse me, do you have the time?",
"Sorry, I didn’t catch that.",
"No problem.",
"Have a good day!",
"How old are you?",
"What’s your favorite color?",
"What’s your favorite food?",
"How do you say _______ in English?",
"Do you speak English?",
"Yes, I do.",
"No, I don’t.",
"I don’t understand.",
"Can you repeat that, please?",
"Can you speak slower, please?",
"How much does it cost?",
"Where is the bathroom?",
"Can you show me on the map?",
"Let’s grab some lunch.",
"What are your plans for the weekend?",
"That sounds like a great idea.",
"I’m not sure about that.",
"Let me think about it.",
"I’m sorry for being late.",
"I’m sorry, I can’t make it.",
"Would you like to join me for dinner?",
"What time is it?",
"I need to take a break.",
"What’s the weather like today?",
"How do I get to _______?",
"Can you recommend a good restaurant?",
"Do you have any siblings?",
"I’m an only child.",
"I have two brothers and a sister.",
"What’s your favorite hobby?",
"I enjoy reading and hiking.",
"What kind of music do you like?",
"I like all kinds of music.",
"Let’s stay in touch.",
"How long have you lived here?",
"What’s the best way to get around the city?",
"Can you tell me more about your job?",
"What do you like to do in your free time?",
"I’m a big fan of sports.",
"Do you have any pets?",
"I have a dog and a cat.",
"What’s your favorite movie?",
"My favorite movie is _______.",
"How do you spell your name?",
"What’s your favorite book?",
"I’m currently reading _______.",
"How far is it to _______?",
"Can I borrow a pen, please?",
"I’m sorry, I forgot my wallet.",
"How was your weekend?",
"That’s a great story.",
"What do you think about _______?",
"I’m not sure, let me check.",
"What’s the best way to contact you?",
"My phone number is _______.",
"Let me give you my email address.",
"I’ll send you an email.",
"It was nice meeting you.",
"What’s your favorite TV show?",
"I’m a big fan of _______.",
"Can you recommend a good hotel?",
"What’s your favorite holiday?",
"My favorite holiday is Christmas.",
"What’s your favorite season?",
"I love the fall season.",
"What’s your favorite sports team?",
"I’m a big fan of the Lakers.",
"Do you have any travel plans coming up?",
"I’m planning a trip to Europe next year.",
"How was your vacation?",
"It was amazing!",
"What’s your favorite type of cuisine?",
"I love Italian food.",
"How do you take your coffee?",
"I take it with cream and sugar.",
"What’s your favorite type of tea?",
"I like green tea.",
"How do you like your steak cooked?",
"I like it medium-rare.",
"Can you recommend a good place to go hiking?",
"What’s the best beach around here?",
"Do you prefer the mountains or the beach?",
"I love both!",
"What’s your favorite type of exercise?",
"I enjoy yoga and running.",
"Can you recommend a good book to read?",
"Have you seen the latest movie?",
"Let’s go see a movie together.",
"What’s your favorite type of art?",
"I love impressionist paintings.",
"Do you like to dance?",
"I’m not a great dancer, but I enjoy it.",
"What’s your favorite type of dessert?",
"I love chocolate cake.",
"Do you have any allergies?",
"I’m allergic to peanuts.",
"What’s your favorite type of flower?",
"I love roses.",
"Can you recommend a good hair salon?",
"I need to find a good mechanic for my car.",
"What’s your favorite type of fruit?",
"I love strawberries.",
"What’s your favorite type of vegetable?",
"I enjoy broccoli.",
"Can you recommend a good wine?",
"What’s your favorite type of beer?",
"I enjoy a good IPA.",
"What’s your favorite type of whiskey?",
"I like bourbon.",
"Do you prefer sweet or savory foods?",
"I like both, depending on my mood.",
"What’s your favorite type of cheese?",
"I love brie.",
"Can you recommend a good restaurant for a romantic dinner?",
"Let’s go out for a drink.",
"What’s your favorite type of cocktail?",
"I like a good margarita.",
"Do you like spicy foods?",
"I love spicy foods.",
"What’s your favorite type of soup?",
"I enjoy tomato soup.",
"Can you recommend a good place to buy groceries?",
"What’s your favorite type of bread?",
"I like sourdough bread.",
"What’s your favorite type of pasta?",
"I love spaghetti carbonara.",
"Can you recommend a good place to buy shoes?",
"What’s your favorite type of shoe?",
"I love sneakers.",
"Can you recommend a good tailor?",
"What’s your favorite type of fabric?",
"I like cotton.",
"Do you prefer to dress casually or formally?",
"It depends on the occasion.",
"What’s your favorite type of hat?",
"I like baseball caps.",
"What’s your favorite type of jewelry?",
"I like earrings.",
"Can you recommend a good place to buy a watch?",
"What’s your favorite type of watch?",
"I like classic leather watches.",
"Can you recommend a good place to buy a handbag?",
"What’s your favorite type of handbag?",
"I like crossbody bags.",
"What’s your favorite color?",
"I love the color blue.",
"What’s your favorite type of music?",
"I enjoy listening to pop music.",
"Can you recommend a good place to buy a camera?",
"What’s your favorite type of photography?",
"I enjoy landscape photography.",
"What’s your favorite type of animal?",
"I love dogs.",
"Do you have any pets?",
"Yes, I have a cat.",
"What’s your favorite type of movie?",
"I love action movies.",
"Can you recommend a good television show to watch?",
"What’s your favorite genre of television?",
"I enjoy watching comedies.",
"What’s your favorite type of video game?",
"I love playing first-person shooters.",
"Can you recommend a good place to buy video games?",
"What’s your favorite type of board game?",
"I enjoy playing chess.",
"Do you have any hobbies?",
"Yes, I enjoy playing the guitar.",
"What’s your favorite type of instrument?",
"I love the piano.",
"Can you recommend a good place to take music lessons?",
"What’s your favorite type of song?",
"I love ballads.",
"What’s your favorite type of musical artist?",
"I’m a big fan of Taylor Swift.",
"Do you like going to concerts?",
"Yes, I love live music.",
"Can you recommend a good place to buy concert tickets?",
"What’s your favorite type of museum?",
"I love art museums.",
"Can you recommend a good place to go shopping?",
"What’s your favorite type of clothing?",
"I enjoy wearing comfortable and casual clothing.",
"Can you recommend a good place to buy home decor?",]
target_language="de"

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
    random.shuffle(common_nouns)
    todays_nouns = common_nouns[:num_nouns]
    return make_strings(todays_nouns)

def make_strings(my_list):
    translated_list = translate_list(my_list)
    output= ""
    for original, translated in zip(my_list,translated_list):
        output += f"{original} = {translated}\n"
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
    random.shuffle(sentence_list)
    translator = Translator(to_lang=target_language)
    translation = translator.translate(sentence_list[0])
    return translation
