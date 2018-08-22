import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression,SGDClassifier

data = pd.read_csv("/Users/prudhvi/Downloads/code_mix_final_thu.csv")

docs = list(data['Tweet'])
vec = CountVectorizer()
X = vec.fit_transform(docs)
df = pd.DataFrame(X.toarray(),columns=vec.get_feature_names())
tfidf_transformer = TfidfTransformer()
X = tfidf_transformer.fit_transform(df)
y = data[['Neutral','Positive','Negative']].as_matrix()
y = np.argmax(y, axis=1)
model = LogisticRegression()
model.fit(X_train_tfidf,y)
y_pr = model.predict(X_train_tfidf)
accuracy_score(y,y_pr)
