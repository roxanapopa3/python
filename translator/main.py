from translate import Translator

translator=Translator(to_lang="fr")
try:
    with open('./test.txt', mode="r") as my_file:
        text=my_file.read()
        translation=translator.translate(text)
        with open('./test2.txt',mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Give a correct file path')