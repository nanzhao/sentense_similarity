from sklearn.feature_extraction.text import  TfidfVectorizer

corpus = ['This is the first document.',
      'This is the second second document.',
      'And the third one.',
      'Is this the first document?',]

vectorizer = TfidfVectorizer(min_df=1)

vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())

print (vectorizer.fit_transform(corpus).toarray())


