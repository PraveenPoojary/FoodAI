
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
# Food Nutritionist, Recipe Expert, and Market Price Analyst
st.title("AI Foodbot")

requirement = st.text_area(
    "Enter the Food name:"
)
# Generate functional, negative and edge test cases for:
if st.button("Submit"):
    prompt = f""" 
Food Name: {requirement}

Generate a comprehensive report for the given food item with the following sections:

### 1. Food Overview

* Brief introduction of the food.
* Origin and common usage.

### 2. Detailed Recipe

Provide:

* Ingredients with quantities.
* Preparation time.
* Cooking time.
* Step-by-step preparation instructions.
* Serving size.

### 3. Nutritional Information

Provide estimated nutritional values per serving in a table:

* Calories
* Protein
* Carbohydrates
* Fat
* Fiber
* Sugar
* Vitamins
* Minerals

### 4. Health Benefits

Explain:

* Protein benefits
* Energy benefits
* Muscle-building benefits
* Digestive benefits
* Immunity benefits
* Any other important nutritional advantages

### 5. Advantages

Provide at least 5 advantages of consuming this food.

### 6. Disadvantages

Provide at least 5 disadvantages or precautions including:

* Allergies
* Excess consumption risks
* Dietary restrictions

### 7. Bangalore Grocery Price Estimation

Estimate ingredient prices in Bangalore based on common grocery platforms such as:

* Blinkit
* Zepto
* Instamart
* Amazon Fresh

Generate a comparison table containing:
| Ingredient | Quantity | Blinkit (₹) | Zepto (₹) | Instamart (₹) | Amazon Fresh (₹) |

Use realistic estimated prices when exact prices are unavailable.
 

### 8. Recommendation

Provide:

* Who should eat this food.
* Who should avoid or limit this food.
* Best time to consume.
* Frequency recommendation.

Format the response professionally using headings, tables, and bullet points. :
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.write(response.text)