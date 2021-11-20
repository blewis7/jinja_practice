from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'brockisgood'
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return render_template('homepage.html', stories=stories.values())

@app.route('/questions')
def questions():
    story_id = request.args['story_id']
    story = stories[story_id]

    prompts = story.prompts

    return render_template('questions.html', title=story.title, prompts=prompts, story_id=story_id)

@app.route('/story')
def get_story():
    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template('story.html', title=story.title, text=text)

