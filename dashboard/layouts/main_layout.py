import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container(
    [
        html.H1("Bitget Scalping Bot Dashboard"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div("Trading View"), md=8),
                dbc.Col(html.Div("Controls"), md=4),
            ]
        ),
    ],
    fluid=True,
)