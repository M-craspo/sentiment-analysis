import streamlit as st
import pandas as pd
import joblib
from scrape import main_url, options, webdriver, time, BeautifulSoup
from model1 import analyze_sentiment_from_csv
import os

# Set up the Streamlit app
st.set_page_config(page_title="Product Review Analyzer", layout="wide")

def main():
    st.title("Product Review Sentiment Analysis")
    st.write("This app scrapes product reviews from ePay and analyzes their sentiment.")
    
    # Create tabs for different functionalities
    tab1, tab2 = st.tabs(["Scrape Reviews", "Analyze Sentiment"])
    
    with tab1:
        st.header("Scrape Product Reviews")
        url = st.text_input("Enter ePay Product URL:", value="")
        
        if st.button("Scrape Reviews"):
            if not url:
                st.warning("Please enter a valid URL")
            else:
                with st.spinner("Scraping reviews..."):
                    try:
                        # Run the scraping code
                        driver = webdriver.Chrome(options=options)
                        driver.get(url)
                        time.sleep(3)
                        html = driver.page_source
                        url_soup = BeautifulSoup(html, "lxml")
                        divs = url_soup.find_all("div", class_="fdbk-container__details__comment")
                        
                        arr = []
                        for div in divs:
                            arr.append(div.get_text().strip())
                        
                        if arr:
                            df = pd.DataFrame(arr, columns=['review'])
                            df.to_csv("scraped_reviews.csv", index=False)
                            st.success(f"Successfully scraped {len(df)} reviews!")
                            st.dataframe(df)
                        else:
                            st.warning("No reviews found on this page.")
                            
                        driver.quit()
                    except Exception as e:
                        st.error(f"Error during scraping: {str(e)}")
    
    with tab2:
        st.header("Analyze Review Sentiment")
        
        # Option to upload CSV or use scraped file
        option = st.radio("Choose input source:", 
                         ("Use scraped reviews", "Upload your own CSV file"))
        
        if option == "Upload your own CSV file":
            uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
            if uploaded_file:
                df = pd.read_csv(uploaded_file)
                st.write("Preview of uploaded data:")
                st.dataframe(df.head())
                
                text_column = st.selectbox("Select the column containing reviews", df.columns)
                
                if st.button("Analyze Sentiment"):
                    with st.spinner("Analyzing sentiment..."):
                        try:
                            # Create temp file for analysis
                            temp_path = "temp_upload.csv"
                            df.to_csv(temp_path, index=False)
                            
                            # Run analysis
                            result = analyze_sentiment_from_csv(
                                temp_path, 
                                "sentiment_results.csv", 
                                text_column=text_column
                            )
                            
                            # Display results
                            st.success("Analysis complete!")
                            st.dataframe(result)
                            
                            # Show sentiment distribution
                            st.subheader("Sentiment Distribution")
                            sentiment_counts = result['sentiment'].value_counts()
                            st.bar_chart(sentiment_counts)
                            
                            # Download button
                            st.download_button(
                                label="Download Results",
                                data=result.to_csv(index=False),
                                file_name="sentiment_analysis_results.csv",
                                mime="text/csv"
                            )
                            
                            # Clean up temp file
                            os.remove(temp_path)
                            
                        except Exception as e:
                            st.error(f"Error during analysis: {str(e)}")
        
        else:  # Use scraped reviews
            if os.path.exists("scraped_reviews.csv"):
                if st.button("Analyze Scraped Reviews"):
                    with st.spinner("Analyzing sentiment..."):
                        try:
                            result = analyze_sentiment_from_csv(
                                "scraped_reviews.csv", 
                                "sentiment_results.csv", 
                                text_column='review'
                            )
                            
                            st.success("Analysis complete!")
                            st.dataframe(result)
                            
                            # Show sentiment distribution
                            st.subheader("Sentiment Distribution")
                            sentiment_counts = result['sentiment'].value_counts()
                            st.bar_chart(sentiment_counts)
                            
                            # Download button
                            st.download_button(
                                label="Download Results",
                                data=result.to_csv(index=False),
                                file_name="sentiment_analysis_results.csv",
                                mime="text/csv"
                            )
                            
                        except Exception as e:
                            st.error(f"Error during analysis: {str(e)}")
            else:
                st.warning("No scraped reviews found. Please scrape reviews first.")

if __name__ == "__main__":
    main()