"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'u fugly', 'you have the personality of printer paper',
  'smell u later', 'you look like i need a drink', 'ya basic', 
  'what are you looking at, four eyes!', 'take a picture it\'ll last longer',
  'stop trying to make fetch happen. it\'s not going to happen.']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <p>Hi! This is the home page. This is another change.</p>
      <a href="/hello">Hello</a>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    options = []
    for compliment in AWESOMENESS:
      options.append(f'<option value="{compliment}">{compliment.capitalize()}</option>')

    actual_options = "\n".join(options)


    # we're just returning a string! so we can use an f method
    return f"""     
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"></br>
          Choose a compliment: <select name="compliment">
            {actual_options}
          </select></br>
          <input type="submit" value="Submit">
        </form></br>
        <form action="/diss">
          Do you have a thick skin? 
            <input type="radio" name="thickskin" value="yes" />Yes
            <input type="radio" name="thickskin" value="no" />No </br>
            <input type="submit" value="Play">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get('compliment')

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss")
def diss_person():
    """Give a user a random insult"""

    diss = choice(INSULTS)

    if request.args.get('thickskin') == 'yes':
      intro = "(You can handle it)"
    else:
      intro = "(Go cry about it, nerd!)"

    # y = x

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        {diss}!</br>
        {intro}
      </body>
    </html>
    """


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
