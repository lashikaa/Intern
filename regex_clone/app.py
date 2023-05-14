from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def index_page():
    
    if request.method == 'POST':
        #Capturing the data from the frontend
        reg_exp = request.form['reg_exp']  
        txt = request.form['txt']
        count = 0
        matches = []

        for i in re.finditer(reg_exp,txt):
            stmt = ""
            count +=1
            stmt = stmt+"{}) {} ".format(count,i.group())
            matches.append(stmt) 
        return render_template('regex.html', count = count, matches = matches, text = txt, reg = reg_exp)
    return render_template('regex.html', count = -1)


if __name__ == '__main__':
    app.run(debug=True)

