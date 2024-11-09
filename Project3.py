import streamlit as st
import matplotlib.pyplot as plt

# Sample sales data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales = [150, 200, 250, 300, 350, 400, 450]

# Function to plot graphs
def plot_graph(graph_type):
    if graph_type == 'All Graphs':
        fig, axs = plt.subplots(3, 2, figsize=(15, 15))
        fig.suptitle('Cafe Sales Data Visualization', fontsize=16)
        
        # Bar Graph
        axs[0, 0].bar(days, sales, color='skyblue')
        axs[0, 0].set_title('Bar Graph: Sales per Day', fontsize=12)
        axs[0, 0].set_xlabel('Days', fontsize=10)
        axs[0, 0].set_ylabel('Sales', fontsize=10)
        axs[0, 0].tick_params(axis='x', rotation=45)
        plt.subplots_adjust(wspace=0.4, hspace=0.6)  # Adjusting space between subplots

        # Line Graph
        axs[0, 1].plot(days, sales, marker='o', color='green', linestyle='dashed')
        axs[0, 1].set_title('Line Graph: Sales Trend Over Time', fontsize=12)
        axs[0, 1].set_xlabel('Days', fontsize=10)
        axs[0, 1].set_ylabel('Sales', fontsize=10)
        axs[0, 1].tick_params(axis='x', rotation=45)

        # Scatter Plot
        axs[1, 0].scatter(days, sales, color='red')
        axs[1, 0].set_title('Scatter Plot: Sales per Day', fontsize=12)
        axs[1, 0].set_xlabel('Days', fontsize=10)
        axs[1, 0].set_ylabel('Sales', fontsize=10)
        axs[1, 0].tick_params(axis='x', rotation=45)

        # Pie Chart
        axs[1, 1].pie(sales, labels=days, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(days))))
        axs[1, 1].set_title('Pie Chart: Distribution of Sales by Day', fontsize=12)

        # Histogram
        axs[2, 0].hist(sales, bins=7, color='purple', edgecolor='black')
        axs[2, 0].set_title('Histogram: Sales Distribution', fontsize=12)
        axs[2, 0].set_xlabel('Sales', fontsize=10)
        axs[2, 0].set_ylabel('Frequency', fontsize=10)

        # Box Plot
        axs[2, 1].boxplot(sales)
        axs[2, 1].set_title('Box Plot: Sales Distribution', fontsize=12)
        axs[2, 1].set_xlabel('Days', fontsize=10)
        axs[2, 1].set_ylabel('Sales', fontsize=10)

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        st.pyplot(fig)
    else:
        plt.figure(figsize=(10, 5))
        if graph_type == 'Bar Graph':
            plt.bar(days, sales, color='skyblue')
            plt.title('Bar Graph: Sales per Day')
        elif graph_type == 'Line Graph':
            plt.plot(days, sales, marker='o', color='green', linestyle='dashed')
            plt.title('Line Graph: Sales Trend Over Time')
        elif graph_type == 'Scatter Plot':
            plt.scatter(days, sales, color='red')
            plt.title('Scatter Plot: Sales per Day')
        elif graph_type == 'Pie Chart':
            plt.pie(sales, labels=days, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(days))))
            plt.title('Pie Chart: Distribution of Sales by Day')
        elif graph_type == 'Histogram':
            plt.hist(sales, bins=7, color='purple', edgecolor='black')
            plt.title('Histogram: Sales Distribution')
        elif graph_type == 'Box Plot':
            plt.boxplot(sales)
            plt.title('Box Plot: Sales Distribution')

        st.pyplot(plt)

# Streamlit app
st.title('Interactive Sales Data Visualization')
graph_type = st.selectbox('Select Graph Type', ['All Graphs', 'Bar Graph', 'Line Graph', 'Scatter Plot', 'Pie Chart', 'Histogram', 'Box Plot'])
plot_graph(graph_type)
