# import tkinter as tk

# def create_section(root, color, row, column, width, height, rowspan=1, columnspan=1):
#     section = tk.Frame(root, bg=color, width=width, height=height)
#     section.grid(row=row, column=column, padx=1, pady=1, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
#     return section

# def populate_section(section, text):
#     label = tk.Label(section, text=text, background=section['bg'], justify="left")
#     label.pack()

# root = tk.Tk()
# root.title("Three Sections Example")

# noun_section = create_section(root, "white", 0, 0, 75, 75)
# verb_section = create_section(root, "white", 0, 1, 75, 75)
# adjective_section = create_section(root, "white", 1, 0, 75, 75)
# sentence_section = create_section(root, "white", 1, 1, 75, 75)

# to_translate_section = create_section(root, "light gray", 2, 0, 150, 50, columnspan=2)
# translated_section = create_section(root, "light gray", 3, 0, 150, 50, columnspan=2)

# noun_list = "sd das daa"

# populate_section(noun_section, noun_list)
# populate_section(verb_section, noun_list)
# populate_section(adjective_section, noun_list)
# populate_section(sentence_section, noun_list)
# populate_section(to_translate_section, noun_list)
# populate_section(translated_section, noun_list)

# root.mainloop()

# import nltk
# from nltk.corpus import brown
# from nltk import FreqDist

# # Download the Brown Corpus data (you only need to do this once)
# nltk.download('brown')

# def get_common_verbs(num_verbs=1000):
#     # Get all verbs from the Brown Corpus
#     all_verbs = [word.lower() for word, pos in brown.tagged_words() if pos.startswith('VB')]

#     # Calculate the frequency distribution of verbs
#     verb_freq = FreqDist(all_verbs)

#     # Get the most common verbs
#     common_verbs = [verb for verb, _ in verb_freq.most_common(num_verbs)]

#     return common_verbs

# # Get common verbs
# common_verbs = get_common_verbs()

# # Print the length of the list
# print("Length of Common Verbs List:", len(common_verbs))

# # Print the common verbs
# print("Common Verbs:", common_verbs)

# from translate import Translator

# def translate_text(text, target_language):
#     translator = Translator(to_lang=target_language)
#     translation = translator.translate(text)
#     return translation

# # Example usage
# text_to_translate = "toy"
# target_language = "no"  # French

# translated_text = translate_text(text_to_translate, target_language)
# print(f"Source text: {text_to_translate}")
# print(f"Translation: {translated_text}")
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsBlurEffect, QGraphicsOpacityEffect, QGraphicsScene, QGraphicsView, QLabel, QGraphicsWidget

class FrostedGlassWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Set up the QGraphicsScene
        scene = QGraphicsScene(self)
        self.setScene(scene)

        # Create a QGraphicsWidget for the frosted glass effect
        frosted_widget = QGraphicsWidget()
        frosted_widget.setGeometry(50, 50, 300, 200)

        # Apply a blur effect to the QGraphicsWidget
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(10)
        frosted_widget.setGraphicsEffect(blur_effect)

        # Create a QLabel for the text
        text_label = QLabel("Crystal Clear Text")
        text_label.setStyleSheet("color: black; font-size: 16px; font-weight: bold;")

        # Apply an opacity effect to the text label
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(1.0)
        text_label.setGraphicsEffect(opacity_effect)

        # Add the text label to the frosted widget
        frosted_widget.layout().addWidget(text_label)

        # Add the frosted widget to the scene
        scene.addItem(frosted_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FrostedGlassWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
