import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
import pickle
from nltk.corpus import stopwords

################################################################
movie_data = load_files(r"txt_sentoken")
X, y = movie_data.data, movie_data.target
# print(X)
# print(y)
print(X[0])
print(y[0])
# print(X[1])
# print(y[1])

################################################################

documents = []

from nltk.stem import WordNetLemmatizer

stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))
    
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
    
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    
    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)
    
    # Converting to Lowercase
    document = document.lower()
    
    # Lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    
    documents.append(document)
# print(documents)

################################################################

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()
print(X[0])

################################################################

from sklearn.feature_extraction.text import TfidfTransformer
tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()
print(X[0])

################################################################

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# print(X_test)

################################################################

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(X_train, y_train) 

################################################################

y_pred = classifier.predict(X_test)
# print(y_pred)

################################################################

print("============================================================")
print("")
print("             Eval Variable/Memory Model")
print("")
print("============================================================")
print("")

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
print("____________________________________________________________")

################################################################

with open('text_classifier', 'wb') as picklefile:
    pickle.dump(classifier,picklefile)

################################################################

with open('text_classifier', 'rb') as training_model:
    model = pickle.load(training_model)

################################################################

print("")
print("")
print("============================================================")
print("")
print("             Eval Saved Model")
print("")
print("============================================================")
print("")

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

y_pred2 = model.predict(X_test)

# print(confusion_matrix(y_test, y_pred2))
print(classification_report(y_test, y_pred2))
print(accuracy_score(y_test, y_pred2))
print("____________________________________________________________")

################################################################
