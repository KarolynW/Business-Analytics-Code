import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

# Load the dataset
input_path = "Lecture 3/Example Python Visualisations/Data_Visualisation_Tools_Example_Dataset.xlsx"
data = pd.read_excel(input_path)

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Layout of the dashboard
app.layout = dbc.Container([
    html.Div([
        html.H1("Sales Dashboard", className="text-center text-primary mb-4"),
        html.Hr(),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.Label("Select Region:", className="text-primary fw-bold"),
            dcc.Dropdown(
                id="region-dropdown",
                options=[{"label": region, "value": region} for region in data["Region"].unique()],
                value=data["Region"].unique()[0],
                clearable=False,
                className="mb-3",
            )
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Key Performance Indicators (KPIs)", className="bg-primary text-white text-center"),
                dbc.CardBody([
                    html.Div(id="kpi-display", style={"font-size": "18px", "text-align": "center"})
                ])
            ])
        ], width=9)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Sales Over Time", className="bg-primary text-white text-center"),
                dbc.CardBody([
                    dcc.Graph(id="sales-trend-chart")
                ])
            ])
        ], width=6),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Sales by Category", className="bg-primary text-white text-center"),
                dbc.CardBody([
                    dcc.Graph(id="category-sales-bar")
                ])
            ])
        ], width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Profit vs Advertising Spend", className="bg-primary text-white text-center"),
                dbc.CardBody([
                    dcc.Graph(id="profit-advertising-scatter")
                ])
            ])
        ], width=6),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Customer Satisfaction vs Sales", className="bg-primary text-white text-center"),
                dbc.CardBody([
                    dcc.Graph(id="satisfaction-sales-bar")
                ])
            ])
        ], width=6)
    ])
], fluid=True)

# Callbacks for interactivity
@app.callback(
    [
        Output("sales-trend-chart", "figure"),
        Output("category-sales-bar", "figure"),
        Output("profit-advertising-scatter", "figure"),
        Output("satisfaction-sales-bar", "figure"),
        Output("kpi-display", "children")
    ],
    [Input("region-dropdown", "value")]
)
def update_dashboard(selected_region):
    filtered_data = data[data["Region"] == selected_region]

    # Sales Trend Line Chart
    sales_trend_fig = px.line(
        filtered_data, x="Date", y="Sales",
        title=f"Sales Over Time in {selected_region}",
        labels={"Sales": "Sales ($)", "Date": "Date"}
    )
    sales_trend_fig.update_layout(title_font_size=16, margin={"l": 20, "r": 20, "t": 50, "b": 20},
                                  plot_bgcolor="#f9f9f9")

    # Category Sales Bar Chart
    category_sales_fig = px.bar(
        filtered_data.groupby("Category")["Sales"].sum().reset_index(),
        x="Category", y="Sales", color="Category",
        title=f"Sales by Category in {selected_region}",
        labels={"Sales": "Total Sales ($)", "Category": "Category"}
    )
    category_sales_fig.update_layout(title_font_size=16, margin={"l": 20, "r": 20, "t": 50, "b": 20},
                                      plot_bgcolor="#f9f9f9")

    # Profit vs Advertising Spend Scatter Plot
    scatter_fig = px.scatter(
        filtered_data, x="AdvertisingSpend", y="Profit", color="Category",
        size="Sales", hover_data=["StoreID"],
        title=f"Profit vs Advertising Spend in {selected_region}",
        labels={"AdvertisingSpend": "Advertising Spend ($)", "Profit": "Profit ($)"}
    )
    scatter_fig.update_layout(title_font_size=16, margin={"l": 20, "r": 20, "t": 50, "b": 20},
                               plot_bgcolor="#f9f9f9")

    # Customer Satisfaction vs Sales Bar Chart
    satisfaction_fig = px.bar(
        filtered_data.groupby("CustomerSatisfaction")["Sales"].sum().reset_index(),
        x="CustomerSatisfaction", y="Sales", color="CustomerSatisfaction",
        title=f"Customer Satisfaction vs Sales in {selected_region}",
        labels={"Sales": "Sales ($)", "CustomerSatisfaction": "Satisfaction Level"}
    )
    satisfaction_fig.update_layout(title_font_size=16, margin={"l": 20, "r": 20, "t": 50, "b": 20},
                                    plot_bgcolor="#f9f9f9")

    # KPI Display
    total_sales = filtered_data["Sales"].sum()
    avg_profit = filtered_data["Profit"].mean()
    avg_satisfaction = filtered_data["CustomerSatisfaction"].mean()

    kpi_text = (
        f"Total Sales: ${total_sales:,.2f} | "
        f"Average Profit: ${avg_profit:,.2f} | "
        f"Avg. Satisfaction: {avg_satisfaction:.1f}/5"
    )

    return sales_trend_fig, category_sales_fig, scatter_fig, satisfaction_fig, kpi_text

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)