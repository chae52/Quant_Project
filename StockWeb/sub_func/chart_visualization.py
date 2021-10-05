import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from datetime import date, datetime, timedelta

def stock_chart(stock_num, abnormal,pred_rate=0.05):
    time = pd.read_csv(
        "../static/stock_data/000270.csv",
        parse_dates=["Date"],
        index_col="Date"
    )
    time = time.reset_index()[['Date', 'price']]
    time.columns = ['date', 'released']


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time['date'], y=time['released'], name="Stock Price"))

    fig.add_trace(go.Scatter(x=pd.Series(time.loc[[len(time)-2,len(time)-1],'date']) + timedelta(days=1), y=pd.concat([pd.Series(time.loc[len(time)-2, 'released']),pd.Series(time.loc[len(time)-1,'released'] *( 1+ pred_rate))]), name="Predict"))

    fig.update_layout(plot_bgcolor='#f6f5fc')

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#f6f5fc",
    )

    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,

    ))

    # input_abnormal_detect_date
    for i in abnormal:
        fig.add_vrect(x0=i[0], x1=i[1], fillcolor="green", opacity=0.25, line_width=0)

    a = fig.to_json()
    return a, fig

stock_name = '000270'
abnormal = [['2012-04-06', '2012-04-10'],
 ['2012-10-30', '2012-11-16'],
 ['2018-12-03', '2018-12-27'],
 ['2019-04-17', '2019-04-22'],
 ['2020-04-10', '2020-05-15'],
 ['2020-05-20', '2020-05-21'],
 ['2020-05-28', '2020-06-12'],
 ['2020-07-31', '2020-08-18'],
 ['2020-11-13', '2020-11-20'],
 ['2020-12-07', '2020-12-09'],
 ['2021-01-14', '2021-03-03'],
 ['2021-06-08', '2021-06-14']]
#
a,fig = stock_chart(stock_name,abnormal)
fig.show()
print(a)