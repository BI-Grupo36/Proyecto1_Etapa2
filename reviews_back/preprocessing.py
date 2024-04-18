from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

def data_cleaning(text):
    # Eliminar etiquetas HTML
    text = re.sub('<[^>]*>', '', text)
    
    # Eliminar tildes y otros caracteres especiales
    text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    
    # Convertir a minúsculas
    text = text.lower()
    
    # Encontrar emoticones
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    
    # Eliminar caracteres no alfanuméricos y agregar emoticones
    text = re.sub('[\W]+', ' ', text) + ' '.join(emoticons).replace('-', '')
    
    return text.split()
def remove_stopwords(text):
    stop = stopwords.words('spanish')
    tokenized = [w for w in text if w not in stop]
    return tokenized

def delete_rare_words(text):
    vocabulary = Counter()
    for review in text:
        vocabulary.update(review)
    rare_words = set(word for word, count in vocabulary.items() if count == 1)
    tokenized = [w for w in text if w not in rare_words]
    return tokenized

def stem_words(words):
    stemmer = SnowballStemmer('spanish')
    return [stemmer.stem(word) for word in words]

def final_preprocessor(data):
    df = pd.DataFrame(data, columns=['Review'])
    print("Limpiando reseñas...")
    df['Review'] = df['Review'].apply(data_cleaning)
    
    # print("Eliminando stopwords...")
    df['Review'] = df['Review'].apply(remove_stopwords)
    
    print("Aplicando stemming...")
    # Aplicar stemming y luego unir las palabras en una sola cadena
    df['Review'] = df['Review'].apply(stem_words)
    
    print("Eliminando palabras raras...")
    df['Review'] = df['Review'].apply(delete_rare_words)
    df['Review'] = df['Review'].apply(lambda x: ' '.join(x))
    

    print("Vectorizando reseñas...")
    X_str = df['Review']
    tfidf_vectorizer = TfidfVectorizer(max_features=10000,ngram_range=(1, 2))

    X_v = tfidf_vectorizer.fit_transform(X_str)

    return X_v