from  library import DataExplorer
path=r"C:\Users\sarthak mohapatra\Downloads\archive\CountryHits240901.csv"
model=DataExplorer(path)
model.stat()
cat_col=['Track', 'Artist1']
num_col=['Rank', 'Popularity', 'Duration']
model.graph(num_col,cat_col)
