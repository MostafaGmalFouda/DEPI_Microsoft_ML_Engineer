import pandas as pd 
import plotly.express as px
from dash import Dash,dcc,html,Input,Output

df = pd.read_excel(r"D:\Gemy Study\DEPI\Machine learning DEPI round_4\TEC\Amit-1\src\ML\data-analysis\session_4\Code\Dash.xlsx")
df.head()
num_cols = df.select_dtypes(include='number').columns

app = Dash()

app.title = "Interactive Dashboard"
app.layout = html.Div([html.H1("Interactive Dashboard with pie plot"),
                       html.Label("select a value to show in the pie chart"),
                       dcc.Dropdown(id='column-dropdown',
                       options = [{'label':col,'value':col} for col in num_cols],
                       value = num_cols[0]),
                       dcc.Graph(id='pie-chart')

                       
                        ])
@app.callback(Output('pie-chart','figure'),Input('column-dropdown','value'))
def update_pie(select_col):
    grouped = df.groupby('Area')[select_col].sum().reset_index()
    fig =px.pie(grouped,names ="Area",values = select_col,title = f"distribution of {select_col} by Area",hole=.4,color_discrete_sequence=px.colors.qualitative.Set2)
    return fig

if __name__ == '__main__':
    app.run(debug=True)
































# from dash import Dash,html,dcc,Input
# from dash.dependencies import Input, Output

# app = Dash(__name__)

# app.layout = html.Div([
#     html.Button('Submit',id = 'number'),
#     dcc.Input(placeholder = "Enter a Valid number",
#               id = 'Data',type ='number'),
#     html.H1(id='Result')

# ])
# @app.callback(Output('Result','children'),
#               Input('number','n_clicks'))
# def play_data(n,data):
#     if n:
#         return f"your enter:{data}"
#     return ""
    
# app.run(debug=True)