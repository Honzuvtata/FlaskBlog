from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

posts = [
	{
		'author': 'Honza Švehla',
		'title': 'blog post 1',
		'content': 'first post contetnt',
		'date_posted': 'April 20, 2018',
	},
	{
		'author': 'kuba Švehla',
		'title': 'blog post 2',
		'content': 'second post contetnt',
		'date_posted': 'April 21, 2018',
	}
 ]




@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
	return render_template('about.html', title= 'About')



@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='rRegister', form=form)



@app.route('/login')
def login():
	form = LoginForm()
	return render_template('register.html', title='Login', form=form)


if __name__=='__main__':
	app.run(debug=True)