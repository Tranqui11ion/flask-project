from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello,World',
        'content': 'This is my first blog post'
    }
}

@app.route('/')
def home():
    return ('Hello, world!')

@app.route('/post/<int:post_id>') #/post/0
def posy(post_id):
    post = posts.get(post_id)
    return render_template('post.html')


if __name__== '__main__':
    app.run(debug=True)