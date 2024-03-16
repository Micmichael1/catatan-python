message=input(">")
# Memisah setiap kata dalam kalimat dan memasukkannya dalam list
words = message.split(" ")
print(words)
emojis = {
    ":)":"😁",
    ":(":"😥"
}
pesan = ""
for dummy in words:
    pesan += emojis.get(dummy,dummy)+" "
print(pesan)