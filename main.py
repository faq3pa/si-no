from flask import Flask, render_template
import random

def randomic():
    response = ["Si","No","si","no","NO","SI"]
    end_sentence = ["","","","","","","",".","!","?"]
    text_format = [("",""),("",""),("",""),("<b>","</b>"),("<i>","</i>")]
    random_response = random.choice(response)
    random_end_sentence = random.choice(end_sentence)
    random_text_format = random.choice(text_format)
    random_sentence = "%s" % (random_text_format)[0]+"%s" % (random_response)+"%s" % (random_end_sentence)+"%s" % (random_text_format)[1]
    return random_sentence

def randomic_background():
    background_font = [("red","yellow"),("orange","black"),("yellow","blue"),("green","grey"),("blue","white")]
    random_background_font = random.choice(background_font)
    return random_background_font

app = Flask(__name__)

@app.route('/')
def index():
    webresult = randomic()
    webbackgroundfont = randomic_background()
    return render_template('index.html', time=webresult, backgroundcolor=webbackgroundfont[0], fontcolor=webbackgroundfont[1])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run(debug=True, host='192.168.0.252', port=5009)