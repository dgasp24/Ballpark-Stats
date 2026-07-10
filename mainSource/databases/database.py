import sqlite3
import os

db_folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(db_folder, "player_stats.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS player_stats (
        team_id INTEGER,
        season INTEGER,
        last_name TEXT,
        full_name TEXT,
        avg TEXT,
        home_runs INTEGER,
        games_played INTEGER,
        ops TEXT,
        plate_appearances INTEGER,
        PRIMARY KEY (team_id, season, last_name)
    )
""")
conn.commit()


def get_cached_team_stats(team_id, season):
    cursor.execute("""
        SELECT last_name, full_name, avg, home_runs, games_played, ops, plate_appearances
        FROM player_stats
        WHERE team_id = ? AND season = ?
    """, (team_id, season))
    return cursor.fetchall()


def save_player_stat(team_id, season, last_name, full_name, avg, home_runs, games_played, ops, plate_appearances):
    cursor.execute("""
        INSERT OR REPLACE INTO player_stats
        (team_id, season, last_name, full_name, avg, home_runs, games_played, ops, plate_appearances)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (team_id, season, last_name, full_name, avg, home_runs, games_played, ops, plate_appearances))
    conn.commit()