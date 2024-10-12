from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', submission_message='')

@app.route('/submit_user_info', methods=['POST'])
def submit_user_info():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    mobile_number = request.form.get('mobile_number')
    gender = request.form.get('gender')


    # a submission message rendered after form submition 
    submission_message = f"Thank you, {name}! Your information has been submitted."

    return render_template('index.html', submission_message=submission_message)

if __name__ == '__main__':
    app.run(debug=True)
