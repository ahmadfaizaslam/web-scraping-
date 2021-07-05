# %%
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

df = pd.read_excel(r"final.xlsx")
print(df.dtypes)
# %%
df["scores"] = df["article"].apply(
    lambda article: analyzer.polarity_scores(article))

# %%
df.drop(columns=["link", "article"])
final = df[["scores"]]
# %%
final.head(20)

# %%
