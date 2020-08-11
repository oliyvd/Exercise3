from flask import Flask
import nltk
from nltk import FreqDist

nltk.download('gutenberg')
from nltk.corpus import gutenburg

app = Flask(__name__)

@app.route("/")
def count_words():
    tokens = gutenberg.words('austen-sense.txt')
    tokens = [word.lower() for word in tokens if word.isalpha()]
    fdist = FreqDist(tokens)
    common = fdist.most_common(500)
    words = []
    for word, frequency in common:
        words.append(word)
    words.sort()
    highCount = common[0][1]
    htmlSpan = ''

    for word, in words:
        size = str(int(15 + fdist[word] / float(highCount) * 150))
        colour = str(hex(int(0.8 * fdist[word] / \
                            float(highCount) * 256**3)))
        colour = colour[-(len(colour) - 2):]
        while len(colour) < 6:
            colour = "0" + colour
        htmlSpan = htmlSpan + '<span style="font-size: 16px; color: #017e22">' + word + '</span>'
    html = '<html><head><body><h1>'+html+'</h1></body></head></html>'
    return html
    
    

if __name__ == "__main__":
    app.run()