from flask import Flask, render_template,redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location On Google Maps (URL)', validators=[DataRequired(),URL()])
    opening = StringField('Opening Time', validators=[DataRequired()])
    closing = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[('☕️'),('☕️☕️'),('☕️☕️☕️'),('☕️☕️☕️☕️'),('☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strenght Rating', choices=[('✘'),('💪'),('💪💪'),('💪💪💪'),('💪💪💪💪'),('💪💪💪💪💪')], validators=[DataRequired()])
    power_rating = SelectField('Power Sockets Availability', choices=[('✘'),('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods =['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv',mode='a',newline='',encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},{form.location.data},{form.opening.data},{form.closing.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}")
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
