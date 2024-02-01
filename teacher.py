from front import generate_layout,populate_section, read_config
from words import get_random_verbs,get_random_adjectives,get_random_nouns, get_random_sentence, generate_seed


read_config()

root,frames = generate_layout("")
generate_seed()


populate_section(frames["nouns"], get_random_nouns(5))
populate_section(frames["verbs"], get_random_verbs(5))
populate_section(frames["adjectives"], get_random_adjectives(5))
populate_section(frames["sentences"], "-"+get_random_sentence()+"\n-"+get_random_sentence())

root.mainloop()