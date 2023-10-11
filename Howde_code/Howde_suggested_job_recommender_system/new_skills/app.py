from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
import re
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
app = Flask(__name__)




# Load your data
data = pd.read_csv("jobs.csv")  # Replace with the actual path to your CSV file
data = data.drop("Unnamed: 0",axis=1) 
data.isnull().sum()

text = " ".join(i for i in data["Key Skills"]) 
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, 
                      background_color="white").generate(text)
text = " ".join(i for i in data["Functional Area"])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
text = " ".join(i for i in data["Job Title"])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, 
                      background_color="white").generate(text)

feature = data["Key Skills"].tolist()




# Assuming data["Key Skills"] is a list of strings
feature = data["Key Skills"].tolist()

# Join the list of strings into a single document
all_skills = ' '.join(feature)

# Initialize the TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform the data
tfidf_matrix = tfidf.fit_transform([all_skills])

# Compute cosine similarity
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)



# Assuming you have the 'indices' and 'similarity' variables defined

feature = data["Key Skills"].tolist()
all_skills = ' '.join(feature)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(feature)
similarity = cosine_similarity(tfidf_matrix)

indices = pd.Series(data.index, index=data['Job Title']).drop_duplicates()
def jobs_recommendation(Title, similarity):
    index = indices[Title]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[::], reverse=True)
    similarity_scores = similarity_scores[0:5]
    newsindices = [i[0] for i in similarity_scores]
    return data[['Job Title', 'Job Experience Required', 
                 'Key Skills']].iloc[newsindices]
    # Add your existing function here
    # ...

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_title = request.form.get("job_title")
        recommendations = jobs_recommendation(job_title, similarity)
        return render_template("index.html", job_title=job_title, recommendations=recommendations.to_html())

    return render_template("index.html", job_title="", recommendations="")

if __name__ == "__main__":
    app.run(debug=True)
