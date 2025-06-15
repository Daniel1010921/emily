from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Step 1: Create a place to store blog posts
posts = []

@app.route("/")
def home():
    # Step 2: Return the template for home and pass posts
    return ...

@app.route("/post/<int:post_id>")
def post(post_id):
    # Step 3: Return single post using the ID
    return ...

@app.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        # Step 4: Get form data and save new post
        title = ...
        content = ...
        posts.insert(0, {"title": title, "content": content})
        return ...
    return ...

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    # Step 5: Remove post by ID
    if 0 <= post_id < len(posts):
        ...
    return ...

if __name__ == "__main__":
    app.run(debug=True)
