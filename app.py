from flask import Flask, render_template
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                                 user='gw2246fx',
                                 password='9Astronaut',
                                 db='gw2246fx_university',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
try:
    with connection.cursor() as cursor:
        #user_input = input("enter a student to search for: ")
        # Select all Students
        sql = "SELECT * from Student"
        
        # execute the SQL command
        cursor.execute(sql)
        data = cursor.fetchall()
        
finally:
    connection.close()
        
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/database')
def database():
    
            return render_template('database.html', data=data)
            
            # get the results
            #for result in cursor:
            
    
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='2246')
    
