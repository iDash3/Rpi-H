from flask import Flask,render_template, redirect
from l1 import Lights

app = Flask(__name__)
DASH_LIGHTS = Lights()

@app.route("/")
def main():
    return render_template("index.html", name='index')

@app.route("/l1_on")
def l1_on():
	DASH_LIGHTS.lights_on()
	return redirect("/") 

@app.route("/l1_off")
def l1_off():
	DASH_LIGHTS.lights_off()
	return redirect("/") 

if __name__ == '__main__':
    print('Server setup...')
    # DASH_LIGHTS.lights_on()
    app.debug = True
    app.run(host='0.0.0.0')