from flask_login import login_required,current_user
from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import Pitch, User,Comment,Upvote,Downvote
from .forms import PitchForm, CommentForm, UpvoteForm

from .. import db


# @main.route('/', methods = ['GET','POST'])
# def home():
   
#     return render_template('home.html')

@main.route('/', methods = ['GET','POST'])
def home():

    '''
    View root page function that returns the home page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    title = 'Home'
    pickuplines = Pitch.query.filter_by(category="pickuplines")
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
    promotionpitch = Pitch.query.filter_by(category = "promotionpitch")
    productpitch = Pitch.query.filter_by(category = "productpitch")

    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
    

    return render_template('home.html', title = title, pitch = pitch, pickuplines=pickuplines, interviewpitch= interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch, upvotes=upvotes)
    
    
@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    pitch = get_pitch(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_review = Review(pitch_id=pitch.id,pitch_title=title,pitch_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.pitch',id = pitch.id ))

    title = f'{pitch.title} review'
    return render_template('pitches.html',title = title, review_form=form, pitch=pitch)

# Views

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        # return redirect(url_for('.home'))
    return render_template('pitches.html',form=form)
    
@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch = pitch )

# @main.route('/pitch/downvote/<int:pitch_id>', methods = ['GET', 'POST'])
# @login_required
# def upvote(pitch_id):
#     pitch = Pitch.query.get(pitch_id)
#     user = current_user
#     pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
#     if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
#         return  redirect(url_for('.home'))


#     new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
#     new_upvote.save_upvotes()
#     return render_template('pitches.html')

# @main.route('/pitch/downvote/<int:pitch_id>', methods = ['GET', 'POST'])
# @login_required
# def downvote(pitch_id):
#     pitch = Pitch.query.get(pitch_id)
#     user = current_user
#     pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    
#     if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
#         return  redirect(url_for('.home'))


#     new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
#     new_downvote.save_downvotes()
#     return render_template('pitches.html')