def emoji_converter(kalimat):
    words = kalimat.split(" ")
    emojis = {
        ":)": "😁",
        ":(": "😥",
        "m":"Michael"
    }
    pesan = ""
    for dummy in words:
        pesan += emojis.get(dummy, dummy) + " "
    return pesan
kalimat=input(">")
print(emoji_converter(kalimat))