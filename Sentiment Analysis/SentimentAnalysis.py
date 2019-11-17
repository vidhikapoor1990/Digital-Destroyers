#import libraries
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from Stopwords import words as english_stopwords

# def getResult(sentence):

names = ['comments','type']

#loading data
data = pd.read_table('amazon_cells_labelled.txt',sep="\t",names = names)

#make it as a data frame
df = pd.DataFrame(data)

#Features
X = df['comments']
y = df['type']

#change text lower cases and white spaces removal
lower_text = []
for i in range(0,len(X)):
    s = str(X[i])
    s1 = s.strip()
    lower_text.append(s1.lower())

#Remove punctuation
punc_text = []
for i in range(0,len(lower_text)):
    s2 = (lower_text[i])
    s3 = re.sub(r'-'," ",s2)
    s3 = re.sub(r'[^\w\s]',"",s3)
    punc_text.append(s3)

#Word vectorization
#Initialize the TF-IDF vectorizer
tfidf = TfidfVectorizer(ngram_range=(1, 2), stop_words=english_stopwords)

#transform independent variable using TF-IDF vectorizer
X_tfidf = tfidf.fit_transform(punc_text)

#Split the data into train and testing
X_train, X_test, Y_train, Y_test = train_test_split(X_tfidf, y, test_size=0.10, random_state=0)

#Build the Naive_bayes model
clf = MultinomialNB()

#Fit train and test into the model
clf.fit(X_train, Y_train)

#Predict the result
y_pred = clf.predict(X_test)

print("Accuracy : ",accuracy_score(Y_test,y_pred)*100)



def getResult(sentence):

    vectorised_sentence = tfidf.transform([sentence])
    prediction = clf.predict(vectorised_sentence)

    if prediction == 1:
        return "Positive Comment"
    elif prediction == 0:
        return"Negative Comment"