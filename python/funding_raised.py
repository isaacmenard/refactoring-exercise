import polars as pl

class FundingRaised:
  @staticmethod
  def where(csv_path: str, options: dict):
    csv_data = FundingRaised._read_csv(csv_path)
    for key, value in options.items():
        csv_data = csv_data.filter(pl.col(key) == value)
    return csv_data.to_dicts()

  @staticmethod
  def find_by(csv_path: str, options = {}):
    csv_data = FundingRaised._read_csv(csv_path)

    if 'company_name' in options:
      for row in csv_data:
        if row[1] == options['company_name']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'city' in options:
      for row in csv_data:
        if row[4] == options['city']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'state' in options:
      for row in csv_data:
        if row[5] == options['state']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'round' in options:
      for row in csv_data:
        if row[9] == options['round']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    raise RecordNotFound


  def _read_csv(csv_path: str):
    with open(csv_path, "rb") as f:   # or "r" if you want text mode
        return pl.read_csv(f, encoding="cp1252")

class RecordNotFound(Exception):
  pass
