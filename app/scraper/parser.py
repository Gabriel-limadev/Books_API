import pandas as pd


def parse_books(books_data: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(books_data)

    df['price'] = (
        df['price']
        .str.replace('£', '', regex=False)
        .astype(float)
    )

    df['rating'] = df['rating'].astype(int)

    return df
