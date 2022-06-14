from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

project_path = Path(__file__).parent.parent.parent.resolve()
data_path = project_path / 'data' / 'test_data'
lahman_path = data_path / 'lahman' / 'baseballdatabank-2022.2'
output_path = project_path / 'baseball_data' / 'chapter_4'
matplotlib.use('Qt5Agg')


def get_teams(lahman_path: Path) -> pd.DataFrame:
    teams_path = lahman_path / 'core' / 'Teams.csv'
    teams_df = pd.read_csv(teams_path)
    int_fields = ['Ghome', 'BB', 'SO', 'SB', 'HBP', 'attendance']
    teams_df[int_fields] = teams_df[int_fields].fillna(0).astype(int)

    return teams_df


def plot_wpct_vs_run_diff(x, y, x_input, y_pred) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y)
    ax.set_xlabel("Run Differential")
    ax.set_ylabel("Win Pct")
    ax.plot(x_input, y_pred, 'k-', color='r')
    

def plot_residuals_vs_run_diff(x, y) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y)
    ax.set_xlabel("Run Differential")
    ax.set_ylabel("Win Pct Residuals")


# Analysis 1
teams_df = get_teams(lahman_path)
x_df = teams_df[['teamID', 'yearID', 'G', 'W', 'L', 'R', 'RA']]
x_df = x_df[x_df.yearID > 2001]
x_df['RD'] = x_df.R - x_df.RA
x_df['Wpct'] = x_df.W / (x_df.W + x_df.L)

model = LinearRegression()
x = x_df['RD'].values.reshape(-1, 1)
y = x_df['Wpct'].values.reshape(-1, 1)
model.fit(x, y)
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")
y_pred = model.predict(x)

plot_wpct_vs_run_diff(x_df['RD'], x_df['Wpct'], x, y_pred)

actual_data = y.reshape(-1)
pred_data = y_pred.reshape(-1)
residuals = actual_data - pred_data

plot_residuals_vs_run_diff(x_df['RD'], residuals)

total_count = len(residuals)
rmse = np.sqrt(np.mean(residuals ** 2))
within_one = sum(np.abs(residuals) < rmse)
within_two = sum(np.abs(residuals) < 2 * rmse)
pct_within_one = within_one / total_count
pct_within_two = within_two / total_count
print(f'Residuals within one: {pct_within_one} within two: {pct_within_two}')

plt.show()

# Analysis 2
x_df['PWpct'] = (x_df['R'] ** 2) / (x_df['R'] ** 2 + x_df['RA'] ** 2)
p_residuals = x_df['Wpct'] - x_df['PWpct']
x_df['residuals'] = p_residuals
p_total_count = len(p_residuals)
p_rmse = np.sqrt(np.mean(p_residuals ** 2))
p_within_one = sum(np.abs(p_residuals) < p_rmse)
p_within_two = sum(np.abs(p_residuals) < 2 * p_rmse)
p_pct_within_one = p_within_one / p_total_count
p_pct_within_two = p_within_two / p_total_count
print(f'Residuals within one: {p_pct_within_one} within two: {p_pct_within_two}')

output_csv = output_path / 'lahman_wpct.csv'
x_df.to_csv(output_csv)

import ipdb
ipdb.set_trace()