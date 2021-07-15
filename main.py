import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("data.csv")
data= df["temp"].tolist()

fig=ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()