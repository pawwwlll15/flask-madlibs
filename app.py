from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
debug = DebugToolbarExtension(app)


@app.route('/home')
def home_page():
    return render_template('home.html')

story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """I came from a place called {place}, I was the {adjective} out of all the {noun}. People loved it when I {verb} {plural_noun}."""
)
story3 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """I hate it here in {place}, Everyone is so {adjective} {verb}. But I do love {noun} and {plural_noun}. """
)


@app.route('/prompt')
def prompt_page():
    prompts = list(story1.__dict__.keys())[0]
    words = getattr(story1,prompts)
    return render_template('prompt.html',words = words)

@app.route('/story')
def story_page():
    #I am figuring out how to retrieve the data that is sent over by the form on the home page
    ans = request.args
    story = request.args['story_choices']
    if story == 'Story 1':
        phrase = story1.generate(ans)
    elif story == 'Story 2':
        phrase = story2.generate(ans)
    elif story == 'Story 3':
        phrase = story3.generate(ans)
    
    
    

    return render_template('story.html',phrase = phrase, ans = ans)



#ask Sonia how I would call a request args in on view function and then also pass the query information on to the next route
    
    
    

   


    
    
