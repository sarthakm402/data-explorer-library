# import pandas as pd
# import numpy as np
# def stat(doc, show_info=True, show_skew=True, show_kurtosis=True):
#     """
#     Provides an overview of the dataset, including structure, summary statistics, skewness, and kurtosis.
    
#     Parameters:
#         doc (str): The path to the CSV file to load.
#         show_info (bool): If True, displays basic information about the DataFrame (default: True).
#         show_skew (bool): If True, calculates and displays skewness for numerical columns (default: True).
#         show_kurtosis (bool): If True, calculates and displays kurtosis for numerical columns (default: True).
#     """
#     df = pd.read_csv(doc)
#     results = {}

#     # Data preview
#     results['head'] = df.head()

#     # Data structure
#     if show_info:
#         results['info'] = df.info()

#     # Summary statistics
#     results['describe'] = df.describe()

#     # Categorical and numerical columns
#     cat_col = df.select_dtypes(include=['object', 'category'])
#     num_col = df.select_dtypes(include=['int', 'float'])
#     results['cat_col'] = list(cat_col.columns)
#     results['num_col'] = list(num_col.columns)

#     # Skewness and kurtosis
#     if show_skew:
#         results['skew'] = df[num_col.columns].skew()
#     if show_kurtosis:
#         results['kurtosis'] = df[num_col.columns].kurtosis()

#     # Print and return results
#     for key, value in results.items():
#         print(f"{key}: \n{value}\n")
#     return results
# path=r"C:\Users\sarthak mohapatra\Downloads\archive\CountryHits240901.csv"
# stat(path)
# def graph(doc, num_col=None, cat_col=None, hist=True, box=True, QQ=True, corr=True, count=True):
#     # Importing libraries for plotting
#     import matplotlib.pyplot as plt
#     import seaborn as sns
#     from statsmodels.graphics.gofplots import qqplot 
#     import pandas as pd
    
#     # Read the CSV
#     df = pd.read_csv(doc)

#     # Filter num_col to ensure only numeric columns
#     num_col = [col for col in num_col if pd.api.types.is_numeric_dtype(df[col])]

#     # Plotting the distribution of numerical columns
#     if num_col:
#         for col in num_col:
#             plt.figure(figsize=(10, 6))
            
#             # Plot histogram
#             if hist:
#                 sns.histplot(data=df, x=col, kde=True)
#                 plt.title(f'Histogram of {col}')
#                 plt.show()

#             # Plot box plot
#             if box:
#                 plt.figure(figsize=(10, 6))
#                 sns.boxplot(data=df, x=col)
#                 plt.title(f'Box Plot of {col}')
#                 plt.show()

#             # Plot QQ plot for numeric columns only
#             if QQ:
#                 plt.figure(figsize=(10, 6))
#                 qqplot(df[col].dropna(), line='s')  # Drop NaN values for QQ plot
#                 plt.title(f'QQ Plot of {col}')
#                 plt.show()

#         # Optionally include correlation heatmap for numerical columns once
#         if corr and len(num_col) > 1:
#             plt.figure(figsize=(10, 8))
#             corr_matrix = df[num_col].corr()
#             sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
#             plt.title('Correlation Matrix Heatmap')
#             plt.show()

#     # Plotting for categorical columns
#     if cat_col:
#         for col in cat_col:
#             # Plot count plot for categorical columns
#             if count:
#                 plt.figure(figsize=(10, 6))
#                 sns.countplot(data=df, x=col)
#                 plt.title(f'Count Plot of {col}')
#                 plt.show()

# # Example usage
# cat_col = ['Track', 'Artist1', 'Artist2']
# num_col = ['Rank', 'Popularity']
# graph(path, num_col, cat_col)


#### THIS IS THE REAL IMPLEMENTATION OF ABOVE FUCTION IN A CLASS####
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot

class DataExplorer:
    def __init__(self, doc):
        """Initialize the DataExplorer with a CSV file path."""
        try:
            self.df = pd.read_csv(doc)
        except FileNotFoundError:
            print(f"File {doc} not found.")
            self.df = None
        except pd.errors.ParserError:
            print("Error parsing file. Check file format and structure.")
            self.df = None

    def data_info(self):
        """Provide basic data structure information."""
        if self.df is not None:
            return {
                'shape': self.df.shape,
                'memory_usage': self.df.memory_usage(deep=True),
                'dtypes': self.df.dtypes
            }

    def stat(self, show_info=True, show_skew=True, show_kurtosis=True):
        """Display dataset structure, summary statistics, skewness, and kurtosis."""
        if self.df is None:
            return "No data loaded."

        results = {}

        # Data preview
        results['head'] = self.df.head()

        # Data structure
        if show_info:
            results['info'] = self.data_info()

        # Summary statistics
        results['describe'] = self.df.describe()

        # Categorical and numerical columns
        cat_col = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        num_col = self.df.select_dtypes(include=['int', 'float']).columns.tolist()
        results['cat_col'] = cat_col
        results['num_col'] = num_col

        # Skewness and kurtosis
        if show_skew:
            results['skew'] = self.df[num_col].skew()
        if show_kurtosis:
            results['kurtosis'] = self.df[num_col].kurtosis()

        for key, value in results.items():
            print(f"{key}: \n{value}\n")
        return results

    def plot_histogram(self, col):
        """Plot histogram with KDE for a given column."""
        sns.histplot(data=self.df, x=col, kde=True)
        plt.title(f'Histogram of {col}')
        plt.show()

    def plot_box(self, col):
        """Plot box plot for a given column."""
        sns.boxplot(data=self.df, x=col)
        plt.title(f'Box Plot of {col}')
        plt.show()

    def plot_qq(self, col):
        """Plot QQ plot for a given column."""
        qqplot(self.df[col].dropna(), line='s')
        plt.title(f'QQ Plot of {col}')
        plt.show()

    def plot_count(self, col):
        """Plot count plot for a categorical column."""
        sns.countplot(data=self.df, x=col)
        plt.title(f'Count Plot of {col}')
        plt.show()

    def plot_correlation_heatmap(self, num_col):
        """Plot correlation heatmap for numerical columns."""
        corr_matrix = self.df[num_col].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
        plt.title('Correlation Matrix Heatmap')
        plt.show()

    def graph(self, num_col=None, cat_col=None, hist=True, box=True, QQ=True, corr=True, count=True):
        """Plot histograms, box plots, QQ plots, and correlation heatmaps for numerical columns,
           and count plots for categorical columns."""
        if self.df is None:
            return "No data loaded."

        # Filter numerical columns
        if num_col:
            num_col = [col for col in num_col if pd.api.types.is_numeric_dtype(self.df[col])]

            for col in num_col:
                if hist:
                    self.plot_histogram(col)
                if box:
                    self.plot_box(col)
                if QQ:
                    self.plot_qq(col)

            # Correlation heatmap
            if corr and len(num_col) > 1:
                self.plot_correlation_heatmap(num_col)

        # Plotting for categorical columns
        if cat_col:
            for col in cat_col:
                if count:
                    self.plot_count(col)


        



