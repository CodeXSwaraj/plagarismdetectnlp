from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(doc1, doc2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([doc1, doc2])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix[0, 1]

def detect_plagiarism(new_document, database_documents):
    similarities = []
    for doc in database_documents:
        similarity = calculate_similarity(new_document, doc['content'])
        similarities.append((doc['id'], similarity))
    return sorted(similarities, key=lambda x: x[1], reverse=True)
