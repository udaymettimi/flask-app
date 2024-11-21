from flask import Flask, render_template


flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    dic ={"name":"uday","mobile":6361187989}

    return render_template('index.html', context=dic)



@flask_app.route('/about-us')
def about_us():
    return render_template('about.html')


@flask_app.route('/contact-us')
def contact_us():
    return render_template('contact.html')



if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )