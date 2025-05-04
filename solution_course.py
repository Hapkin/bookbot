def get_num_words(text):
    words = text.split()
    return len(words)


#het verschil met mijn code is dat men hier elk teken 1maal zoekt en tijdelijk in een nieuwe dictionairy zet
#wanneer het geteld is wordt het in het resultaat geappend

#mijn oplossing ging bij elk char volledig de lijst af op zoek naar het char om het nummer +1 te kunnen doen
#dus veel meer keren door de lijst met dictionairies...

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#sort_on is een specialleke
#hier geef je extra optie aan de functie .sort()
#---
#sorted_list.sort(reverse=True, key=sort_on)
#met deze functie bepaal je dus op wat je de lijst wil sorteren
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list