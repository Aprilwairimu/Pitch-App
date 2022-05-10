from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired,Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Pitch review', validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')