# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


print ("\nРешение Пункт A")
def remove_excl (text):
    return print (f"foo('{text}') -> '{text.replace('!','')}'")

remove_excl ("Hi! Hello")
remove_excl ("")
remove_excl ("Oh, no!!!")


# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


print ("\nРешение Пункт В")
def remove_excl_end (text):
  match text[-1]:
    case "!":
        return print (f"remove('{text}') == '{text[:-1]}'")
    case _:
        return print(f"remove('{text}') == '{text}'")

remove_excl_end ("Hi!")
remove_excl_end ("Hi!!!")
remove_excl_end ("!Hi")


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

print ("\nРешение Пункт C")
def remove_excl_w (text):
    l = text.split(' ')
    new_text = []
    for n in l:
        ch = list(n)
        if ch.count('!') != 1:
            new_text.append(n)
    return print(f"remove ('{text}') === '{''.join(new_text)}'")

remove_excl_w ("Hi!")
remove_excl_w ("Hi! Hi!")
remove_excl_w ("Hi! Hi! Hi!")
remove_excl_w("Hi Hi! Hi!")
remove_excl_w("Hi! !Hi Hi!")
remove_excl_w("Hi! Hi!! Hi!")
remove_excl_w("Hi! !Hi! Hi!")



