
from flask import Flask, render_template_string
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Example dummy metrics
    metrics = {
        "Forecast Accuracy": "88%",
        "Coupon Redemption Lift": "+17%",
        "CTR Increase (LLM Coupons)": "+9%",
        "ROI from Targeted Campaign": "22%"
    }

    df = pd.DataFrame({
        'Week': ['2025-01-01', '2025-01-08', '2025-01-15', '2025-01-22'],
        'Forecasted': [100, 120, 130, 110],
        'Actual': [95, 125, 135, 108]
    })

    fig = px.line(df, x='Week', y=['Forecasted', 'Actual'], title="SKU Weekly Forecast")

    return render_template_string("""
    <html>
    <head><title>mPerks Dashboard</title></head>
    <body>
        <h1>mPerks AI Dashboard</h1>
        {% for k, v in metrics.items() %}
        <p><strong>{{ k }}:</strong> {{ v }}</p>
        {% endfor %}
        <div>{{ plot_div|safe }}</div>
    </body>
    </html>
    """, metrics=metrics, plot_div=fig.to_html(full_html=False))

if __name__ == '__main__':
    app.run(debug=True)
