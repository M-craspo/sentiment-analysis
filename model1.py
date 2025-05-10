import pandas as pd
import joblib

def analyze_sentiment_from_csv(input_csv_path, output_csv_path, text_column='text'):

    try:
        # 1. Load the sentiment analysis pipeline
        pipeline = joblib.load('sentiment_pipeline.joblib')
        print("Pipeline loaded successfully")
        
        # 2. Read the input CSV file
        df = pd.read_csv(input_csv_path)
        print(f"Loaded {len(df)} records from {input_csv_path}")
        
        # 3. Make predictions
        texts = df[text_column].tolist()
        predictions = pipeline.predict(texts)
        
        # 4. Add predictions to dataframe
        df['sentiment'] = predictions
        
        # 5. Save results
        df.to_csv(output_csv_path, index=False)
        print(f"Results saved to {output_csv_path}")
        
        return df
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except KeyError:
        print(f"Error: Column '{text_column}' not found in CSV file")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "/Users/mahmoudahmed/Downloads/GP depi/ouyput.csv"  # Your input CSV file
    output_file = "output_with_sentiment.csv"  # Output file
    
    # Specify which column contains the text (default is 'text')
    analyze_sentiment_from_csv(input_file, output_file, text_column='0')