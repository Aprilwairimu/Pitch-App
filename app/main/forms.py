from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,PasswordField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
	title = StringField('Title', validators=[InputRequired()])
	description = TextAreaField("What would you like to pitch ?",validators=[InputRequired()])
	category = RadioField('Label', choices=[ ('promotionpitch','promotionpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')],validators=[InputRequired()])
	submit = SubmitField('Submit')

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Pitch review', validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()