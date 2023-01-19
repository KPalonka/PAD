from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#9c9797',
    'text': '#000000'
}

df = pd.read_csv('C:\Python\AAA studia pjatk\PAD\cwiczenie 6\winequelity.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])




app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Dash program with table and graphs',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div([
    html.H3(children='Wine Quality'),
    generate_table(df),
    ]),


    html.Label('Select type of graph'),
    html.Div([
        dcc.Dropdown(['Classification', 'Reggresion'], id='dropdown', style={'width': '60%', 'display': 'block'})]),
        dcc.RadioItems(
                df.columns.tolist(),
                id='yaxis-type',
                inline=True),
    html.Div([
        dcc.Graph(id='scatter')], style={'width': '80%', 'display': 'centre', 'padding': '0 20'}),
])



@app.callback(
    Output('scatter', 'figure'),
    Input('dropdown', 'value'),
    Input('yaxis-type', 'value'),
    )

def update_graph(dropdown_value, user_choice):
    if dropdown_value == 'Reggresion':
        
        fig = px.scatter(df, x='pH', y=user_choice)
    elif dropdown_value == 'Classification':

        fig = px.box(df, x='target', y=user_choice)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
