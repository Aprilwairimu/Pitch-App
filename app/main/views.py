from flask_login import login_required

# @main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
#     form = ReviewForm()
#     pitch = get_pitch(id)
#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data

#         # Updated review instance
#         new_review = Review(pitch_id=pitch.id,pitch_title=title,pitch_review=review,user=current_user)

#         # save review method
#         new_review.save_review()
#         return redirect(url_for('.pitch',id = pitch.id ))

#     title = f'{pitch.title} review'
#     return render_template('new_review.html',title = title, review_form=form, pitch=pitch)