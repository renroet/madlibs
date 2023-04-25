from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'asdf'

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('begin.html', STORY=story)

@app.route('/story')
def story_page():
    your_story = story.generate(request.args)
    return render_template('story.html', your_story=your_story)