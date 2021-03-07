from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')
  

@app.route('/froyo_results', method=['GET'])
def show_froyo_results():
    context = {
        'users_froyo_flavor': request.args.get("flavor")
        'users_froyo_toppings': request.args.get("toppings")
    }
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo and added the toppings {user_froyo_toppings}!'


@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return render_template('favorite_form.html')

@app.route('/favorites_results', method=['GET'])
def favorites_results():
    """Shows the user a nice message using their form results."""
    context = {
        'users_favorite_color': request.args.get("color")
        'users_favorite_animal': request.args.get("animal")
        'users_favorite_city': request.args.get("city")
    }
    return f'Wow, I didnt know {users_favorite_color} {users_favorite_animal} lived in {users_favorite_city}!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return render_template('secret_message_form.html')

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    context = {
        'users_input_message': request.form.get("message")
        'users_secret_list': sorted("users_input_message")
    return request.sort_letters(message_results) 

    }

    


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')
    

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    context = {
        'operand1' : int(request.args.get('operand1')),
        'operand2' : int(request.args.get('operand2')),
        'operation' : request.args.get('operation'),
    }
    return render_template('calculator_results.html', **context)


@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
   
    context = {
        'users_horoscope_sign': request.args.get("horoscope_sign")
        'users_personality': request.args.get("users_personality") 
        'users_lucky_number': request.args.get("lucky_number")
    }

    return render_template('horoscope_results.html', **context)
   

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = ''

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = ''

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 100)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
