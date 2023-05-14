def str_upper(string):
    """Возвращает строку большими буквами"""
    return string.upper()

def title_word(string):
    """Делает заглавными первые буквы каждого слова в строке, поступившей на вход функции"""
    title_words = []
    for word in string.split():
        title_words.append(word.title())
    return " ".join(title_words)