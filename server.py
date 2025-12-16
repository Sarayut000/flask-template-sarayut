from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)


@app.route('/about')
def about():
    title = 'About Page'
    name = 'sarayut'
    email = 'std.67122420311@ubru.ac.th'
    mobile = '093-542-6340'
    age = 21
    return render_template('about.html', title=title, name=name, email=email, mobile=mobile,age=age)


@app.route('/favorite/foods')
def favorite_foods():
    title= 'Favorite Foods Page'
    foods = ['ส้มตำไก่ย่าง', 'สามชั้นทอดน้ำปลา', 'กระเพราหมูกรอบไข่ดาว']
    return render_template('favorite_foods.html', title=title, foods=foods)


@app.route('/favorite/sports')
def favorite_sports():
    title= 'Favorite Sprots Page'
    sports = ['ฟุตบอล', 'บาสเกตบอล', 'แบดมินตัน']
    return render_template('favorite_sports.html', title=title, sports=sports)

