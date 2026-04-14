import requests
import json
import sys

def fetch_and_save_products():
    """
    Invoke REST API and write products data into a new JSON file
    """
    try:
        # Make the API request with timeout
        print("Fetching product data from API...")
        resp = requests.get('https://dummyjson.com/products', timeout=10)
        
        # Raise an exception for bad status codes (4xx, 5xx)
        resp.raise_for_status()
        
        # Parse JSON response
        product_data = resp.json()
        products = product_data.get('products', [])
        
        if not products:
            print("Warning: No products found in the API response")
            return
        
        print(f"Successfully fetched {len(products)} products")
        
        # Write products to JSON file
        print("Writing data to product.json...")
        with open('product.json', 'w') as fp:
            json.dump(products, fp, indent=2)  # Added indent for better readability
        
        print("✅ New JSON File created successfully: product.json")
        print(f"   File contains {len(products)} products")
        
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out. The API took too long to respond.")
        sys.exit(1)
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Failed to connect to the API. Please check your internet connection.")
        sys.exit(1)
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error occurred: {e}")
        if resp.status_code == 404:
            print("   The API endpoint was not found.")
        elif resp.status_code == 500:
            print("   The server encountered an internal error.")
        else:
            print(f"   Status code: {resp.status_code}")
        sys.exit(1)
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error making API request: {e}")
        sys.exit(1)
        
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON response: {e}")
        print("   The API response was not valid JSON.")
        sys.exit(1)
        
    except IOError as e:
        print(f"❌ Error writing to file: {e}")
        print("   Please check if you have write permissions in the current directory.")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print(f"   Error type: {type(e)._name_}")
        sys.exit(1)

# Run the function
if __name__ == "_main_":
    fetch_and_save_products()