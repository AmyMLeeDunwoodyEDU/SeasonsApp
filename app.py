from flask import Flask, render_template, request
from datetime import datetime
import random

print("Content-Type: text/html\n")

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime("%B")
    return render_template("index.html", year=current_year, month=current_month)

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    
    global default_die
    global default_sides
    
    default_die = int(1)
    default_sides = int(6)
    
    global num_dice
    global num_sides
    global num_sides1
    global num_dice1
    global total
    global results
    
    global ency_data
    global result_data
    global sides_data
    global dice_data
    global total_data
    
    num_dice = num_sides = num_dice1 = num_sides1 = total = None
    results = result_data = []
    dice_data = sides_data = total_data = ""
    ency_data = ['Empty']
    
    if request.method == 'POST':
        num_dice = request.form.get('amt_dice')
        num_sides = request.form.get('amt_sides')

        if num_dice:
            num_dice1 = int(num_dice)
            ency_data.remove('Empty')
            try:
                if isinstance(num_dice1, int) == True:
                    if num_dice1 == 1:
                        dice_data = (f"You rolled: {num_dice1} die")
                        ency_data.append("Dices")
                    if num_dice1 > 1:
                        dice_data = (f"You rolled: {num_dice1} dices")
                        ency_data.append("Dices")
            except ValueError:
                if num_dice1 < 1:
                    ency_data.append("Dices")
                    dice_data = (f"You cannot have less than 1 die.")

        if not num_dice:
             num_dice1 = default_die
             ency_data.remove('Empty')
             try:
                 if isinstance(num_dice1, int) == True:
                     if num_dice1 == 1:
                         dice_data = (f"You rolled: {num_dice1} die")
                         ency_data.append("Dices")
                     if num_dice1 > 1:
                         dice_data = (f"You rolled: {num_dice1} dices")
                         ency_data.append("Dices")
             except ValueError:
                 if num_dice1 < 1:
                     ency_data.append("Dices")
                     dice_data = (f"You cannot have less than 1 die.")

        if num_sides:
            num_sides1 = int(num_sides)
            try:
                if isinstance(num_sides1, int) == True:
                    if num_sides1 == 1:
                        sides_data = (f"With {num_sides1} side")
                        ency_data.append("Sides")
                    if num_sides1 > 1:
                        sides_data = (f"With {num_sides1} sides")
                        ency_data.append("Sides")
            except ValueError:
                if num_dice1 == 1 and num_sides < 1:
                    ency_data.append("Sides")
                    sides_data = (f"You cannot have a die with less than 1 side.")
        
        if not num_sides:
             num_sides1 = default_sides
             try:
                 if isinstance(num_sides1, int) == True:
                     if num_sides1 == 1:
                         sides_data = (f"With {num_sides1} side")
                         ency_data.append("Sides")
                     if num_sides1 > 1:
                         sides_data = (f"With {num_sides1} sides")
                         ency_data.append("Sides")
             except ValueError:
                     if num_dice1 == 1 and num_sides < 1:
                         ency_data.append("Sides")
                         sides_data = (f"You cannot have a die with less than 1 side.")
        
        if isinstance(num_dice1, int) == True and isinstance(num_sides1, int) == True:
            results = [random.randint(1, num_sides1) for _ in range(num_dice1)]
            if len(results) > 1:
                total = sum(results)
                result_data = (f"The independant values of your dices are: {results}")
                total_data = (f"The the total value of your dices is: {total}")
                ency_data.append("Results")
                ency_data.append("Total")
            if len(results) == 1:
                result_data = (f"The total value of your die is: {results}")
                ency_data.append("Results")
                ency_data.append("Total")
    
    return render_template('dice.html', results=results, total=total, dice_data=dice_data, sides_data=sides_data, result_data=result_data, total_data=total_data, ency_data=ency_data, num_dice=num_dice1, num_sides=num_sides1)