from flask import Flask, render_template, request


app = Flask('app')

@app.route('/')
def hello():
    return '''<html><body><h1>Home Page</h1>
    <p>this is home page</p> <ol>
  <li>
    <a href="/products">products</a>
  </li>
  <li>
    <a href="/about">about us</a>
  </li>
  <li>
    <a href="/contacts">Contacts page</a>
  </li>
</ol> </body></html>'''
@app.route('/about')
def about():
    return'''<html>
    <body>
     <h1>About Page</h1>
     <p>this is the about page</p>
     <ol>
  <li>
    <a href="/products">products</a>
  </li>
  <li>
    <a href="/">main page</a>
  </li>
  <li>
    <a href="/contacts">Contacts page</a>
  </li>
</ol>    
     </body>
     </html>'''

@app.route('/contacts')
def contact():
    return '''<html>
    <body>
     <h1>Contacts Page</h1>
     <p>Here are our contact Info!</p>
     <ol>
  <li>
    <a href="/products">products</a>
  </li>
  <li>
    <a href="/">main page</a>
  </li>
  <li>
    <a href="/about">about us</a>
  </li>
</ol>    
     </body>
     </html>'''

@app.route('/products')
def products():
    return render_template('products.html')

@app.route(f'/products/<int:page>')
def product(page):
    ps = [
        {
            "name": "Fluent Python: Clear, Concise, and Effective Programming",
            "author": "Luciano Ramalho",
            "price": 39.95,
            "description": "Don't waste time bending Python to fit patterns you've learned in other languages. Python's simplicity lets you become productive quickly, but often this means you aren't using everything the language has to offer. With the updated edition of this hands-on guide, you'll learn how to write effective, modern Python 3 code by leveraging its best ideas. "
        },
        {
            "name": "Introducing Python: Modern Computing in Simple Packages",
            "author": "Bill Lubanovic",
            "price": 27.49,
            "description": "Easy to understand and fun to read, this updated edition of Introducing Python is ideal for beginning programmers as well as those new to the language. Author Bill Lubanovic takes you from the basics to more involved and varied topics, mixing tutorials with cookbook-style code recipes to explain concepts in Python 3. End-of-chapter exercises help you practice what you’ve learned."
        }
    ]
    return render_template('product.html',num =page,name = ps[page-1]['name'],author = ps[page-1]['author'],price=ps[page-1]['price'],description= ps[page-1]['description'])


app.run()