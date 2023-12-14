class TextSplit:
    def character(text, character):
        return text.split(character)
    
    def subsplit(texts, character):
        return list(map(lambda text: text.strip().split(character), texts))