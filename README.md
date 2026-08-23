# Ballpark Stats

A full-stack web app for exploring MLB player statistics — pulls live data from the MLB Stats API and lets you visualize it as bar charts or scatter plots, either for a single team or league-wide.

**Live site:** [https://mlb-stats-project-production.up.railway.app/]

<img width="691" height="421" alt="image" src="https://github.com/user-attachments/assets/185b35b6-0f4e-4c20-815a-9142d638fe1a" />

## Features

- **Team and league-wide views** — look up stats for a specific team's roster or every MLB player at once
- **Two chart types** — bar charts for ranking a single stat, or scatter plots for comparing two stats against each other (e.g. Batting Average vs. OPS), complete with league-average reference lines
- **Player highlighting** — search for a specific player to have them highlighted on the league-wide scatter plot
- **Configurable filters** — filter by year and minimum plate appearances to control who shows up in the results
- **Ranked, sortable results table** alongside every chart
- **Custom dark UI theme** — designed from scratch with a consistent color system and typography, rather than default Bootstrap styling
- **Responsive layout** — usable on both desktop and mobile
- **Graceful error handling** — invalid inputs are caught and shown a friendly error page instead of a raw stack trace

## Tech Stack

- **Backend:** Python, Flask
- **Data:** MLB Stats API
- **Visualization:** Matplotlib
- **Frontend:** HTML, CSS, JavaScript, Jinja2 templates, Animate.css, Bootstrap (base layout)
- **Deployment:** Railway

## How It Works

1. The user selects a team (or MLB-wide), year, minimum plate appearances, and chart type (bar or scatter) through the form.
2. Flask fetches the relevant player data from the MLB Stats API and processes it into the shape each chart type needs.
3. Matplotlib generates the chart, styled to match the site's theme, and renders it as a static image embedded directly in the page.
4. Results are displayed alongside a ranked table of the underlying stats.

## Screenshots

<!-- Add screenshots below -->

### Team View
<img width="290" height="606" alt="image" src="https://github.com/user-attachments/assets/8a1939b5-63f5-47c2-bb67-d3367fb94ebe" />


### MLB-Wide Bar Chart
<img width="804" height="608" alt="image" src="https://github.com/user-attachments/assets/7b9609c0-b9e9-40a6-be58-b05374f70249" />


### Scatter Plot Comparison
<img width="798" height="611" alt="image" src="https://github.com/user-attachments/assets/0e078720-aa2a-4c24-bbe7-859a743fa55b" />


## Running Locally

```bash
git clone https://github.com/dgasp24/MLB-Stats-project.git
cd MLB-Stats-project/mainSource
pip install -r requirements.txt
python app.py
```

The app will start on `http://localhost:5000`.

## Author

Dominic — [GitHub](https://github.com/dgasp24)
