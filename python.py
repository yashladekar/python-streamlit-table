import streamlit as st
import pandas as pd

# Sample data for the initial table
data = {
    'Item': ['Item A', 'Item B', 'Item C'],
    'Price': [200, 300, 250],
    'Stock': [5, 3, 10]
}

# DataFrame for the main table
df = pd.DataFrame(data)

# Function to get additional details based on item
def get_item_details(item):
    # Additional data can be fetched from databases or any other source here
    details = {
        'Item A': {'Description': 'Description of Item A', 'Supplier': 'Supplier A'},
        'Item B': {'Description': 'Description of Item B', 'Supplier': 'Supplier B'},
        'Item C': {'Description': 'Description of Item C', 'Supplier': 'Supplier C'},
    }
    return details.get(item, {})

# Streamlit app
st.title("Interactive Data Table")

# Display the main table
selected_row = st.dataframe(df)

# Capture the selected item from the table
if 'selected_item' not in st.session_state:
    st.session_state.selected_item = None   

def update_selected_item(item):
    st.session_state.selected_item = item

# Add clickable cells for the 'Item' column
for index, row in df.iterrows():
    st.button(row['Item'], key=row['Item'], on_click=update_selected_item, args=(row['Item'],))

# Display details of the selected item
if st.session_state.selected_item:
    item_details = get_item_details(st.session_state.selected_item)
    st.subheader(f"Details of {st.session_state.selected_item}")
    details_df = pd.DataFrame(item_details.items(), columns=['Attribute', 'Value'])
    st.table(details_df)