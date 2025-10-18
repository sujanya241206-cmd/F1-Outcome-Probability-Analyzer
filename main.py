import pandas as pd


def create_f1_dataset():
    data = {
        "Driver": [
            "Max Verstappen",
            "Liam Lawson",
            "Yuki Tsunoda",
            "Charles Leclerc",
            "Lewis Hamilton",
            "Lando Norris",
            "Oscar Piastri",
            "George Russell",
            "Kimi Antonelli",
            "Fernando Alonso",
            "Lance Stroll",
            "Pierre Gasly",
            "Franco Colapinto",
            "Oliver Bearman",
            "Esteban Ocon",
            "Nico Hulkenberg",
            "Gabriel Bortoleto",
            "Alex Albon",
            "Carlos Sainz",
            "Isack Hadjar",
        ],
        "Team": [
            "Red Bull",
            "Red Bull",
            "Racing Bulls",
            "Ferrari",
            "Ferrari",
            "McLaren",
            "McLaren",
            "Mercedes",
            "Mercedes",
            "Aston Martin",
            "Aston Martin",
            "Alpine",
            "Alpine",
            "Haas",
            "Haas",
            "Sauber",
            "Sauber",
            "Williams",
            "Williams",
            "Racing Bulls",
        ],
        "Races": [22] * 20,
        "Wins": [12, 1, 0, 3, 2, 2, 5, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        "Podiums": [18, 5, 3, 11, 10, 9, 12, 8, 4, 6, 4, 6, 3, 2, 3, 1, 2, 2, 7, 3],
        "Poles": [10, 1, 0, 6, 5, 3, 4, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0],
        "Fastest Laps": [8, 0, 1, 3, 2, 2, 3, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        "Weather": [
            "Sunny",
            "Cloudy",
            "Rainy",
            "Sunny",
            "Cloudy",
            "Sunny",
            "Sunny",
            "Cloudy",
            "Sunny",
            "Sunny",
            "Cloudy",
            "Cloudy",
            "Rainy",
            "Cloudy",
            "Sunny",
            "Cloudy",
            "Sunny",
            "Rainy",
            "Cloudy",
            "Sunny",
        ],
        "Track": [
            "Monza",
            "Spa",
            "Suzuka",
            "Monaco",
            "Silverstone",
            "Montreal",
            "Interlagos",
            "Baku",
            "Miami",
            "Barcelona",
            "Jeddah",
            "Zandvoort",
            "Imola",
            "Austin",
            "Hungaroring",
            "Monaco",
            "Baku",
            "Singapore",
            "Zandvoort",
            "Silverstone",
        ],
    }
    df = pd.DataFrame(data)
    df.to_csv("f1_data_raw.csv", index=False)
    print("Raw dataset 'f1_data_raw.csv' created successfully.")
    return df


def clean_f1_data(df):
    df = df.dropna().copy()
    df["Driver"] = df["Driver"].str.title().str.strip()
    df["Team"] = df["Team"].str.title().str.strip()
    df["Weather"] = df["Weather"].str.capitalize().str.strip()
    df["Track"] = df["Track"].str.title().str.strip()
    df.drop_duplicates(inplace=True)
    for col in ["Races", "Wins", "Podiums", "Poles", "Fastest Laps"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Races", "Wins", "Podiums"])
    df = df[(df["Races"] >= df["Wins"]) & (df["Podiums"] >= df["Wins"])]
    df["Win Rate (%)"] = (df["Wins"] / df["Races"]) * 100
    df.to_csv("f1_data_cleaned.csv", index=False)
    print("Cleaned dataset saved as 'f1_data_cleaned.csv'.")
    return df


def analyze_data(df):
    top5 = df.sort_values(by="Win Rate (%)", ascending=False).head(5)
    print("\nTop 5 Drivers by Win Rate:")
    print(top5[["Driver", "Team", "Win Rate (%)"]])
    return top5


if __name__ == "__main__":
    print("Starting F1 Data Preprocessing Module...\n")
    raw_df = create_f1_dataset()
    clean_df = clean_f1_data(raw_df)
    analyze_data(clean_df)
    print("\nProcess completed successfully!")
    print(clean_df.head())
