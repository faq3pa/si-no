from flask import Flask, render_template
import random

def randomic():
    response = ["Si","No","Si","No","Si","No","si","no","NO","SI"]
    end_sentence = ["","","","","","","",".","!","?"]
    text_format = [("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("<b>","</b>"),("<i>","</i>")]
    random_response = random.choice(response)
    random_end_sentence = random.choice(end_sentence)
    random_text_format = random.choice(text_format)
    random_sentence = "%s" % (random_text_format)[0]+"%s" % (random_response)+"%s" % (random_end_sentence)+"%s" % (random_text_format)[1]
    return random_sentence

def randomic_background():
    background_font = [
        ("#FCE77D","#F96167"),
        ("#292826","#F9D342"),
        ("#3D155F","#DF678C"),
        ("#4831D4","#CCF381"),
        ("#F0A07C","#4A274F"),
        ("#3C1A5B","#FFF748"),
        ("#FBEAEB","#2F3C7E"),
        ("#1D1B1B","#EC4D37"),
        ("#8AAAE5","#FFFFFF"),
        ("#FFE67C","#295F2D")
        ]
    random_background_font = random.choice(background_font)
    return random_background_font

def randomic_font():
    fonts = [
        ("""link href='https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap' rel='stylesheet'""","font-family: 'Roboto Slab', serif;"),
        ("""link href='https://fonts.googleapis.com/css2?family=Lora&display=swap' rel='stylesheet'""","font-family: 'Lora', serif;"),
        ("""link href='https://fonts.googleapis.com/css2?family=Work+Sans&display=swap' rel='stylesheet'""","font-family: 'Work Sans', sans-serif;"),
        ("""link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap" rel='stylesheet'""","font-family: 'Josefin Sans', sans-serif;"),
        ("""link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz&display=swap" rel='stylesheet'""","font-family: 'Yanone Kaffeesatz', sans-serif;"),
        ("""link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel='stylesheet'""","font-family: 'Dancing Script', cursive;"),
        ("""link href="https://fonts.googleapis.com/css2?family=Rokkitt&display=swap" rel='stylesheet'""","font-family: 'Rokkitt', serif;"),
        ("""link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel='stylesheet'""","font-family: 'Orbitron', sans-serif;")
        ]
    random_font = random.choice(fonts)
    return random_font

app = Flask(__name__)

@app.route('/')
def index():
    webresult = randomic()
    webbackgroundfont = randomic_background()
    webfontfam = randomic_font()
    return render_template('index.html', time=webresult, backgroundcolor=webbackgroundfont[0], fontcolor=webbackgroundfont[1], fontfam=webfontfam[0],fontstyle=webfontfam[1])

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(debug=True, host='192.168.0.145', port=5000)