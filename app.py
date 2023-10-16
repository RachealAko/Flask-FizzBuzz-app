from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/fizzbuzz')
def fizzbuzz():
    return render_template('fizzbuzz.html')

if __name__ == '__main__':
    app.run(debug=True)