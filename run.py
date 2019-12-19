from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queens.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Queens
from sqlalchemy.sql import Insert

solutions = []
queen = [0 for c in range(8)]        #Row o f queen i n column c
rfree = [True for r in range(8)]     #Row rfree
du = [True for i in range(15)]       #Diagonal i = c + 7 − r
dd = [True for i in range(15)]       #Diagonal i = c + rfree

@app.route('/')
def index():   
    list_queen_obj = [] 
    solve(0)  
    for number, positions in enumerate(solutions):
        queen_obj = Queens(solution=number+1, positions=positions)
        list_queen_obj.append(queen_obj)
        #print('{} {}'.format(number, position))
    db.session.add_all(list_queen_obj)   
    db.session.commit()
    db.session.flush()
    return "{} solutions: {}".format(len(solutions), solutions)

def solve(c):
    global solutions
    if c == 8:
        positions = ''
        for r in range(8):
            positions += '{},'.format(queen[r] + 1)
        solutions.append(positions.rstrip(','))
    else:       
        for r in range(8):
            if rfree[r] and dd[c+r] and du[ c+7-r]:
                queen[c] = r
                rfree[r] = dd[c+r] = du[c+7-r] = False
                solve(c+1)
                rfree[r] = dd[c+r] = du[c+7-r] = True




