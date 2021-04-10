
import pickle

from flask import Flask, render_template, request
from flask_cors import cross_origin

#GP	PTS	FG%	3P%	FT%	REB	AST	STL	BLK	TOV
app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            GP=float(request.form['GP'])
            PTS =float(request.form['PTS'])
            FG =float(request.form['FG%'])
            P =float(request.form['3P%'])
            FT =float(request.form['FT%'])
            REB = float(request.form['REB'])
            AST = float(request.form['AST'])
            STL = float(request.form['STL'])
            BLK = float(request.form['BLK'])
            TOV = float(request.form['TOV'])

            def predict():
                filename = 'finalized_model.pickle'
                loaded_model = pickle.load(open(filename, 'rb'))
                return loaded_model
            # loading the model file from the storage
            a=predict()# predictions using the loaded model file
            prediction=a.predict([[GP,PTS,FG,P,FT,REB,AST,STL,BLK,TOV]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8006, debug=True)
	#app.run(debug=True) # running the app
    #36	2.001480	34.7	25.0	0.836062	2.024846	1.378405	0.632456	0.632456	0.262364