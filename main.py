from imdb import IMDb
import pandas as pd

a = IMDb()

result = a.search_movie("Il Padrino")

df = pd.DataFrame()



print(result)