from flask import Flask, render_template, request
from few_shot import FewShotPosts
from post_generator import generate_post

app = Flask(__name__)

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


@app.route('/', methods=['GET', 'POST'])
def index():
    fs = FewShotPosts()
    tags = fs.get_tags()

    # Handle form submission
    if request.method == 'POST':
        selected_tag = request.form.get('tag')
        selected_length = request.form.get('length')
        selected_language = request.form.get('language')

        # Generate the post
        try:
            post = generate_post(selected_length, selected_language, selected_tag)
            return render_template('index.html', tags=tags, length_options=length_options,
                                   language_options=language_options, post=post,
                                   selected_tag=selected_tag, selected_length=selected_length,
                                   selected_language=selected_language)
        except Exception as e:
            error_message = f"Error generating post: {str(e)}"
            return render_template('index.html', tags=tags, length_options=length_options,
                                   language_options=language_options, error_message=error_message)
    return render_template('index.html', tags=tags, length_options=length_options,
                           language_options=language_options)


if __name__ == '__main__':
    app.run(debug=True)
