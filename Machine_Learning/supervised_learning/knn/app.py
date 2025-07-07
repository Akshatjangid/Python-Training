from flask import Flask, request, jsonify, render_template, url_for

import joblib
scaler = joblib.load('scaler.lb')
kmeans = joblib.load('Crop_recommendation.lb')
df= joblib.load('crop_reco_df.lb')



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            N = float(request.form['nitrogen'])
            P = float(request.form['phosphorus'])
            K = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
            transformed_data = scaler.transform(input_data)
            prediction = kmeans.predict(transformed_data)[0]

            # Get crop frequency dictionary from the predicted cluster
            dt = dict(df[df["clusters_8"] == prediction]["label"].value_counts())

            # Optionally: filter crops with frequency ≥ 70
            top_crops = [k for k, v in dt.items() if v >= 70]

            return render_template("index.html", dt=dt, top_crops=top_crops)
        
        except Exception as e:
            return f"Something went wrong: {e}", 500

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         N = float(request.form['nitrogen'])
#         P = float(request.form['phosphorus'])
#         K = float(request.form['potassium'])
#         temperature = float(request.form['temperature'])
#         humidity = float(request.form['humidity'])
#         ph = float(request.form['ph'])
#         rainfall = float(request.form['rainfall'])

#         input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
#         transformed_data = scaler.transform(input_data)
#         prediction = kmeans.predict(transformed_data)[0]

#         print(prediction)

#         dt = dict(df[df["clusters_8"] == prediction]["label"].value_counts())
#         return render_template("index.html", dt = dt)
#         ls = []
#         for k,v in dt.items():
#             if v>=70:
#                 ls.append(k)
#         return jsonify(ls)
#         # recommended_crop = df[df["clusters_8"] == prediction]["label"].values[0]
        
#         # return render_template('index.html', prediction_text=f'Recommended Crop: {recommended_crop}')




if __name__ == '__main__':
    app.run(debug=True)