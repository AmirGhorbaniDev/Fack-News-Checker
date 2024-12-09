import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# Load the saved model and vectorizer
model = joblib.load('fake_news_model.joblib')
tfidf = joblib.load('tfidf_vectorizer.joblib')

# Function to predict
def predict_news(title):
    # Transform the title
    title_tfidf = tfidf.transform([title])
    # Get prediction and probability
    prediction = model.predict(title_tfidf)[0]
    proba = model.predict_proba(title_tfidf)[0]
    return prediction, proba

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", layout="wide")

# Title and Description
st.title("📰 Fake News Detection Dashboard")
st.markdown("""
This dashboard helps you detect fake news using machine learning.
Simply enter a news title and get instant predictions!
""")

# Create two columns
col1, col2 = st.columns([2, 1])

with col1:
    # Input text box
    news_title = st.text_area("Enter News Title", height=100)
    
    if st.button("Predict"):
        if news_title:
            # Get prediction
            prediction, proba = predict_news(news_title)
            
            # Create columns for results
            res_col1, res_col2 = st.columns(2)
            
            with res_col1:
                # Display result with colored box
                if prediction == 1:
                    st.success("This appears to be Real News!")
                else:
                    st.error("This appears to be Fake News!")
            
            with res_col2:
                # Display confidence
                confidence = proba[1] if prediction == 1 else proba[0]
                st.metric("Confidence Score", f"{confidence*100:.2f}%")
            
            # Show probability chart
            prob_df = pd.DataFrame({
                'Category': ['Fake News', 'Real News'],
                'Probability': [proba[0], proba[1]]
            })
            fig = px.bar(prob_df, x='Category', y='Probability',
                        color='Category', color_discrete_map={
                            'Fake News': 'red',
                            'Real News': 'green'
                        })
            st.plotly_chart(fig)
        else:
            st.warning("Please enter a news title!")

with col2:
    # Add some statistics or information
    st.subheader("About the Model")
    st.markdown("""
    - Uses TF-IDF Vectorization
    - Trained on over 24,000 news articles
    - Logistic Regression classifier
    - Evaluates news titles for authenticity
    """)
    
    # Add some tips
    st.subheader("Tips for Use")
    st.markdown("""
    - Enter complete news titles
    - Check confidence scores
    - Higher confidence means more reliable prediction
    - Consider context and sources
    """)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit • ML Model: Logistic Regression")