import pymupdf

pdf="Endline.pdf"
new="newPdf.txt"

doc=pymupdf.open(pdf)
d=open(new,"wb")
for pages in doc:
    text=pages.get_text().encode("utf8")
    d.write(text)
    d.write(bytes((10,)))
    
d.close()
"""
1.Count words
2.count characters
3.create a list of maximum 10 words from the document
4.count the number of times the word "the" appears in the document
5.list out the words that end with "ound"
"""

print("\n 1.count words")
with open(new,"r") as f:
    words=f.read()
    words=words.split()
    print("Number of words:",len(words))
print("2.count characters") 
with open(new,"r") as f:
    characters=f.read()
    print("Number of characters:",len(characters))

print("3.create a list of maximum 10 words from the document")
with open(new,"r") as f:
    words=f.read().split()
    max_words=words[:10]
    print("Maximum 10 words:", max_words)
    

print("4.count the number of times the word \"the\" appears in the document")
with open(new,"r") as f:
    text=f.read().lower()
    count_the=text.count("the")
    print("The word 'the' appears:", count_the, "times")

print("5.list out the words that end with \"ound\"")

with open(new,"r") as f:
    words=f.read().split()
    words_ending_with_ound=[word for word in words if word.endswith("ound")]
    print("Words ending with 'ound':", words_ending_with_ound)
