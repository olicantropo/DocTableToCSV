import pandas as pd

def generate_result_csv(wixpt_path, cat_path, result_path):
    # Load tables
    wixpt = pd.read_csv(wixpt_path)
    cat = pd.read_csv(cat_path)
    
    # Create new dataframe with the number of rows matching B (Cat.csv)
    result = pd.DataFrame()
    result['collection'] = cat.iloc[:, 0].astype(str) + ';Python'
    
    # Generate 'name' column with 'Product' + increasing number
    result['name'] = [f'Product {i+1}' for i in range(len(result))]
    
    # Set 'price' column to 999.99
    result['price'] = 999.99
    
    # Set 'fieldType' column to 'Product'
    result['fieldType'] = 'Product'
    
    # Save result to CSV
    result.to_csv(result_path, index=False)
    print(f"Result.csv generated successfully at {result_path}")

# Example usage
generate_result_csv("WixPT.csv", "Cat.csv", "Result.csv")
