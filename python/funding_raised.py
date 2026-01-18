import polars as pl

class FundingRaised:
  @staticmethod
  def where(csv_path: str, options: dict, limit = -1):
    csv_data = FundingRaised._read_csv(csv_path)

    for key, value in options.items():
        csv_data = csv_data.filter(pl.col(key) == value)

    if limit != -1:
        csv_data = csv_data.head(limit)

    return csv_data.to_dicts()

  def _read_csv(csv_path: str):
    with open(csv_path, "rb") as f:   # or "r" if you want text mode
        return pl.read_csv(f, encoding="cp1252")

class RecordNotFound(Exception):
  pass
