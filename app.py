#!/usr/bin/env python
# coding: utf-8
# In[25]:
import pandas as pd
import flask 
import pickle

# Use pickle to load in the pre-trained model.
with open(f'model/transformeter.pkl', 'rb') as f:
    model = pickle.load(f)
    app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return(flask.render_template('Main-Dashboard.html'))
@app.route('/Main-Dashboard.html')
def main2():
    return(flask.render_template('Main-Dashboard.html'))
@app.route('/Machine-Learning.html')
def machine():
    return(flask.render_template('Machine-Learning.html'))
@app.route('/Try-Model.html', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return(flask.render_template('Try-Model.html'))
    if flask.request.method == 'POST':
        Temperature = flask.request.form['temperature']
        Humidity = flask.request.form['humidity']
        input_variables = pd.DataFrame([[Temperature, Humidity]],
                                       columns=['temperature', 'humidity'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('Try-Model.html',
                                     original_input={'Temperature':Temperature,
                                                     'Humidity':Humidity},
                                     result=prediction,
                                     )
app.run()

# In[ ]:





# In[ ]:




