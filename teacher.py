from front import generate_layout,populate_section
from words import get_random_verbs,get_random_adjectives,get_random_nouns, get_random_sentence

root,frames = generate_layout("teacher")

populate_section(frames["nouns"], get_random_nouns(5))
populate_section(frames["verbs"], get_random_verbs(5))
populate_section(frames["adjectives"], get_random_adjectives(5))
populate_section(frames["sentences"], get_random_sentence())

root.mainloop()