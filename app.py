from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('image.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method =='POST':
        district=request.form['district']
        C_floor = request.form['C_floor']
        roomnum = request.form['roomnum']
        hall = request.form['hall']
        AREA = request.form['AREA']
        school=request.form['school']
        subway=request.form['subway']
        # print(school,subway)
        data =[[int(district),int(C_floor),int(roomnum),int(hall),float(AREA),int(school),int(subway)]]
        SZFj = pickle.load(open('finalized_model(0.9428).pkl','rb'))
        prediction =SZFj.predict(data)
        a = ('%.2f' % prediction)
    return render_template('image.html',prediction=a)


if __name__ == '__main__':
    app.run()
