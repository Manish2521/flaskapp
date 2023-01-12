from flask import Flask, render_template, request, redirect, apikey
from newsapi import NewsApiClient


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')



# @app.route("/news")
# def news():
#     newsapi = NewsApiClient(api_key="2d50871e7a3244c6a7ef19011b2192ba")
#     topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    
#     articles = topheadlines['articles']
    
#     desc = []
#     news = []
#     img = []
#     for i in range(len(articles)):
#         myarticles = articles[i]
#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
        
        
        
    # mylist = zip(news, desc , img)
    
    
    # return render_template('news.html', context= mylist)



@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

@app.route('/sharemarket')
def sharemarket():
    return render_template('sharemarket.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/cryptocurrency')
def cryptocurrency():
    return render_template('cryptocurrency.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()