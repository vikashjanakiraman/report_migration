import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
data1 = sns.load_dataset('iris')
data2 = sns.load_dataset('tips')
data3 = sns.load_dataset('mpg')

# Create subplots with 1 row and 3 columns
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Plot the first Seaborn plot
sns.scatterplot(data=data1, x='sepal_length', y='sepal_width', ax=axes[0])
axes[0].set_title('Plot 1')

# Plot the second Seaborn plot
sns.boxplot(data=data2, x='day', y='total_bill', ax=axes[1])
axes[1].set_title('Plot 2')

# Plot the third Seaborn plot
sns.barplot(data=data3, x='origin', y='mpg', ax=axes[2])
axes[2].set_title('Plot 3')

# Adjust spacing between subplots
plt.tight_layout()

# Display the plots using Streamlit
st.pyplot(fig)


# Display the raw data
st.header('Raw Data')

# Display the first dataset
st.subheader('Data 1')
st.dataframe(data1)

# Display the second dataset
st.subheader('Data 2')
st.dataframe(data2)

# Display the third dataset
st.subheader('Data 3')
st.dataframe(data3)


# Add download links for the raw data
st.header('Download Data')

# Download link for Data 1
st.subheader('Data 1')
data1_csv = data1.to_csv(index=False)
st.download_button('Download Data 1', data=data1_csv, file_name='data1.csv', mime='text/csv')

# Download link for Data 2
st.subheader('Data 2')
data2_csv = data2.to_csv(index=False)
st.download_button('Download Data 2', data=data2_csv, file_name='data2.csv', mime='text/csv')

# Download link for Data 3
st.subheader('Data 3')
data3_csv = data3.to_csv(index=False)
st.download_button('Download Data 3', data=data3_csv, file_name='data3.csv', mime='text/csv')





