print("This Project Is Made By Tal Moshel and Ron Nudle ")
def EN_HE(text):
    d={" ":" ","/":"q","'":"w","ק":"e","ר":"r","א":"t","ט":"y","ו":"u","ן":"i","ם":"o","פ":"p","ש":"a","ד":"s","ג":"d","כ":"f","ע":"g","י":"h","ח":"j","ל":"k","ך":"l","ז":"z","ס":"x","ב":"c","ה":"v","נ":"b","מ":"n","צ":"m"}
    final = ""
#The swapping
    for letter in text:
        final += d[letter]
#The text printing
    return(final)
def HE_EN(text):
    d2={" ": " ","e":"ק","r":"ר","t":"א","y":"ט","u":"ו","i":"ן","o":"ם","p":"פ","a":"ש","s":"ד","d":"ג","f":"כ","g":"ע","h":"י","j":"ח","k":"ל","l":"ך",";":"ף","z":"ז","x":"ס","c":"ב","v":"ה","b":"נ","n":"מ","m":"צ",",":"ת",".":"ץ"}
    final = ""
#The swapping
    for letter in text:
        final += d2[letter]
#The text printing
    return(final)
