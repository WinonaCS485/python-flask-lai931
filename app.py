from flask import Flask, render_template

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

@app.route('database')
def database():
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
            
            # get the results
            for result in cursor:
                print (result)
            
          
            # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
            # So you must commit to save your changes. 
            # connection.commit()
            

    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
