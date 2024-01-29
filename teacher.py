from front import generate_layout,populate_section
from words import get_random_verbs,get_random_adjectives,get_random_nouns

root,frames = generate_layout("teacher")
noun_list = get_random_nouns(5)
verb_list = get_random_verbs(5)
adj_list = get_random_adjectives(5)

populate_section(frames["nouns"], noun_list)
populate_section(frames["verbs"], verb_list)
populate_section(frames["adjectives"], adj_list)
# populate_section(frames["sentences"], noun_list)
# populate_section(frames["to_translate"], noun_list)
# populate_section(frames["translated"], noun_list)

root.mainloop()