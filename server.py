from flask import Flask
import random

app = Flask(__name__)

guessed_number = random.randint(0, 10)
print(guessed_number)


@app.route("/")
def home():
    return f"<h1 style=color:blue; > Guess a number between 0 and 9.</h1>"\
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:number>")
def play(number):
    if number < guessed_number:
        return f"<h1 style=color:red;>Too Low, Try Again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > guessed_number:
        return f"<h1 style=color:green; >Too High, Try Again!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    else:
        return f"<h1 style=color:purple;>You Found Me.</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
