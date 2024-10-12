import pandas as pd
from pandas._libs.algos import diff_2d

sample_data = [
    {
        "title": "Mystery of the Lost City",
        "actor1": "John Doe",
        "actor2": "Jane Smith",
        "actor3": "Emily Johnson",
        "age1": 45,
        "age2": 39,
        "age3": 28,
    },
    {
        "title": "Skyward Journey",
        "actor1": "Chris Evans",
        "actor2": "Scarlett Johansson",
        "actor3": "Tom Holland",
        "age1": 38,
        "age2": 36,
        "age3": 27,
    },
    {
        "title": "Digital Fortress",
        "actor1": "Denzel Washington",
        "actor2": "Morgan Freeman",
        "actor3": "Anne Hathaway",
        "age1": 65,
        "age2": 83,
        "age3": 40,
    },
    {
        "title": "Ocean's Melody",
        "actor1": "Ryan Gosling",
        "actor2": "Emma Stone",
        "actor3": "Mahershala Ali",
        "age1": 42,
        "age2": 34,
        "age3": 49,
    },
    {
        "title": "Time Traveler's Log",
        "actor1": "Robert Downey Jr.",
        "actor2": "Jeremy Renner",
        "actor3": "Zoe Saldana",
        "age1": 58,
        "age2": 52,
        "age3": 45,
    },
]

df = pd.DataFrame(sample_data)
df = df.melt(
    id_vars=["title"],
    value_vars=["actor1", "actor2", "actor3", "age1", "age2", "age3"],
    var_name="variable",
    value_name="value",
)

df["actor"] = df.apply(
    lambda row: row["value"] if "actor" in row["variable"] else None, axis=1
)

df["age"] = df.apply(
    lambda row: row["value"] if "age" in row["variable"] else None, axis=1
)

actor = pd.DataFrame(["actor"])
age = pd.DataFrame(df["age"])

# drop rows with NaN values and reset index
# actor = actor.dropna().reset_index(drop=True)
age = age.dropna().reset_index(drop=True)

# split a DataFrame in half by dividing the length of the DataFrame by 2
# or the number of colums attributes that pertain to movies (e.g. actor, age)
df = df.iloc[: len(df) // 2]
del df["value"]
del df["variable"]
del df["age"]
df = pd.merge(df, age, left_index=True, right_index=True)

print(df)
