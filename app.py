from flask import Flask, render_template, request
from yieldCalculator import YieldCalculator
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/SubmitForm')
def submitForm():
    return render_template('submit_form.html')

@app.route('/CalculateYield')
def calculateYield():
    return 0

@app.route('/thankyou', methods=['POST'])
def thankyou():
    area = request.form.get('area')
    areaInAcreasOrHectares = request.form.get('areaInAcreasOrHectares')
    cropType = request.form.get('cropType')
    expectedYieldPerUnitArea = request.form.get('expectedYieldPerUnitArea')
    totalYield = YieldCalculator(cropType, areaInAcreasOrHectares, area, expectedYieldPerUnitArea)
    output = totalYield.yieldCalc()

    return render_template('thankyou.html',
                           area=area,
                           areaInAcreasOrHectares=areaInAcreasOrHectares,
                           cropType=cropType,
                           expectedYieldPerUnitArea=expectedYieldPerUnitArea,
                           output=output)


if __name__ == '__main__':
    app.run(debug=True, port=5000)