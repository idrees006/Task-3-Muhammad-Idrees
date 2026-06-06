import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =====================================================================
# STEP 1: INPUT PHASE (Item Metadata Setup & User Profile Initialization)
# =====================================================================
print("=== [1/3] INPUT PHASE ===")

# Item Corpus: Intrinsic course attributes representing item profiles
course_data = {
    'course_id': [101, 102, 103, 104, 105, 106],
    'title': [
        'Advanced Python & Cloud Automation',
        'Frontend Web Development Frameworks',
        'Introduction to Machine Learning & Neural Networks',
        'Cloud Infrastructure & DevOps Pipelines',
        'UI/UX Design Patterns & Prototyping',
        'Deep Learning and Tensor Optimization'
    ],
    # The Shared Vocabulary Tags
    'metadata': [
        'python cloud automation backend engineering scripts software',
        'frontend web design framework javascript html css react development',
        'python machine learning neural networks artificial intelligence data math optimization',
        'cloud devops pipelines aws docker automation infrastructure engineering',
        'uiux design patterns prototyping figma frontend web web-design user-experience',
        'python neural networks deep learning tensors optimization artificial intelligence'
    ]
}

# Constructing our structured asset framework
df_items = pd.DataFrame(course_data)
print("✔ Item Metadata Corpus successfully loaded into shared vocabulary space.")
print(df_items[['course_id', 'title']])

# Simulating explicit user intent choice input sequence
# Scenario: A user profiles themselves with an interest in Python, Cloud systems, and Automation
user_choices = "python cloud automation backend"
print(f"\n• Capturing Explicit User Interaction State Profile Tags:")
print(f"  --> User Preferences Vector Input: \"{user_choices}\"\n")


# =====================================================================
# STEP 2: PROCESS PHASE (TF-IDF Term Penalization & Cosine Similarity Map)
# =====================================================================
print("=== [2/3] PROCESS PHASE ===")

# The TF-IDF Engine: Automatically rewards rare, descriptive tags
# and penalizes generic high-frequency terms.
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the corpus text data into spatial coordinate matrices
tfidf_matrix = tfidf_vectorizer.fit_transform(df_items['metadata'])
print(f"• Spatial Grid Mapping Complete. Vocabulary Size: {len(tfidf_vectorizer.get_feature_names_out())} unique tokens.")

# Vector Mapping: Transform the user preference text using the exact same vocabulary index map
user_vector = tfidf_vectorizer.transform([user_choices])
print("✔ Structural Vector Mapping: User intent safely projected into item vector field.")

# Similarity Engine Math: Compute Cosine Similarity between user vector and all item vectors
# Cosine Distance targets the angular trajectory alignment rather than coordinate scale size.
similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
print("✔ Linear Algebra Calculations Complete (Angular Proximity Vectors Generated).\n")


# =====================================================================
# STEP 3: OUTPUT PHASE (Generating Top-N Recommendations List)
# =====================================================================
print("=== [3/3] OUTPUT PHASE (CURATED TOP-N MATCHES) ===")

# Append the scores back into our data structure framework
df_items['alignment_score'] = similarity_scores

# Generate Top-N Recommendation Matrix (Top 3 highest matching content profiles)
top_n = 3
recommended_items = df_items.sort_values(by='alignment_score', ascending=False).head(top_n)

print(f"\n🚀 SUCCESS: Top {top_n} Personalization Matrix Suggestions generated for user profile:")
print("-" * 85)
for index, row in recommended_items.iterrows():
    print(f"🏅 Match Rank: Course #{row['course_id']} - {row['title']}")
    print(f"   📐 Alignment Fit Match Score: {row['alignment_score'] * 100:.2f}%")
    print(f"   🏷️ Content Fingerprint: {row['metadata']}")
    print("-" * 85)