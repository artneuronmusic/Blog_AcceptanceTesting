from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []


@app.route('/') #its show the homepage after url
def homepage():
    return render_template('home.html')  #will return the page: home.html


@app.route('/blog') #now in blog page
def blog_page():
    return render_template('blog.html', posts=posts) #it might have posts after adding it later


@app.route('/post', methods=['GET', 'POST']) #go to the create page which is entitled with post, in this one, the server needs to receive input and post it.
def add_post():
    if request.method == 'POST':          #if the request of the func is equal to "POST, then input the forms for title and content
        title = request.form['title']
        content = request.form['content']
        global posts                      #why need global? we have posts in the beginning.

        posts.append({                    #add materials in posts
            'title': title,
            'content': content
        })

        return redirect(url_for('blog_page')) #everytime return to the blog_page, not blog
    return render_template('new_post.html') #create a new page for new_post


@app.route('/post/<string:title>')  #in the post section, we have the data of the new input
def see_post(title):
    global posts                   #the collection

    for post in posts:             # among those posts, if the one u want is found, then show the page
        if post['title'] == title:
            return render_template('post.html', post=post)

    return render_template('post.html', post=None)  #otherwise, show nothing


if __name__ == '__main__':
    app.run()
