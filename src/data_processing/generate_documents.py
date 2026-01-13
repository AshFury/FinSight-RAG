import pandas as pd
from pathlib import Path

input_path = "data/processed/mcdonalds_financials_clean.csv"
output_dir = Path("data/docs")
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_path)

cols = {
    "year": "year",
    "revenue": "revenue_($b)",
    "net_income": "earnings_($b)",
    "market_cap": "market_cap_($b)",
    "profit_margin": "operating_margin_(%)",
}

for k, v in cols.items():
    assert v in df.columns, f"Missing required column: {v}"

documents = []

for _, row in df.iterrows():
    content = f"""
Year: {int(row[cols['year']])}
Revenue: ${row[cols['revenue']]:.2f}B
Net Income: ${row[cols['net_income']]:.2f}B
Operating Margin: {row[cols['profit_margin']]:.2f}%
Market Capitilization: ${row[cols['market_cap']]:.2f}B
""".strip()

    documents.append({
        "doc_type": "yearly_snapshot",
        "year": int(row[cols["year"]]),
        "content": content
    })

pd.DataFrame(documents).to_json(
    output_dir / "yearly_snapshots.json",
    orient="records",
    indent=2
)

print("Yearly financial snapshot documents generated")


ratio_docs = []

for _, row in df.iterrows():
    year = int(row[cols["year"]])
    margin = row[cols["profit_margin"]]

    interpretations = []

    if margin < 15:
        interpretations.append("operating profitability was relatively weak")
    elif margin > 25:
        interpretations.append("operating profitability was strong")
    
    summary = (
        f"In {year}, McDonald's {', '.join(interpretations)}."
        if interpretations
        else f"In {year}, McDonald's operating margins remained stable."
    )

    ratio_docs.append({
        "doc_type": "ratio_summary",
        "year": year,
        "content": summary
    })

    pd.DataFrame(ratio_docs).to_json(
        output_dir / "ratio_summaries.json",
        orient="records",
        indent=2
    )

    print("Ratio interpretation documents generated")

trend_docs = []
win = 3

for i in range(len(df) - win + 1):
    window = df.iloc[i:i+win]
    start_year = int(window.iloc[0][cols["year"]])
    end_year = int(window.iloc[-1][cols["year"]])

    revenue_change = window[cols["revenue"]].iloc[-1] - window[cols["revenue"]].iloc[0]
    earnings_change = window[cols["net_income"]].iloc[-1] - window[cols["net_income"]].iloc[0]

    content = f"""
    Between {start_year} and {end_year}, McDonald's financial performance showed the following trends:
    - Revenue changed by {revenue_change:.2f}B USD.
    - Earnings changes by {earnings_change:.2f}B USD.
    """.strip()

    trend_docs.append({
        "doc_type": "trend_summary",
        "period": f"{start_year}-{end_year}",
        "content": content
    })
    
pd.DataFrame(trend_docs).to_json(
    output_dir / "trend_summaries.json",
    orient="records",
    indent=2
)

print("Multi-year trend summaries generated")