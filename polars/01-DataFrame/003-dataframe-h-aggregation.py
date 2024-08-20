import polars as pl

df = pl.read_csv(
    "https://raw.githubusercontent.com/oscarito-taquito/yt-examples/main/data/movie_metadata.csv"
)

df = df.with_columns(
    df["actor_1_facebook_likes", "actor_2_facebook_likes", "actor_3_facebook_likes"]
    .mean_horizontal()
    .alias("mean_fb_likes")
    .round(0)
    .cast(pl.Int64)
)

cols = ["director_name", "mean_fb_likes", "imdb_score"]

# avg_fb_likes = df.select(cols).sort("imdb_score", descending=True)
# print(avg_fb_likes.head(10))
print(df[cols].head())
