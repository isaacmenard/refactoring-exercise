from funding_raised import FundingRaised
import polars as pl

csv_path = "../startup_funding.csv"

def test_where_returns_events():
  assert len(FundingRaised.where(csv_path, {'company_name': 'Facebook'})) == 7

def test_where_returns_correct_keys():
  row_test = {'permalink': 'facebook', 'company_name': 'Facebook', 'number_employees': 450, 'category': 'web', 'city': 'Palo Alto', 'state': 'CA', 'funded_date': '1-Sep-04', 'raised_amount': 500000, 'raised_currency': 'USD', 'round': 'angel'}
  row = FundingRaised.where(csv_path, {'company_name': 'Facebook'})[0]
  assert row == row_test

def test_where_returns_events_by_city():
  assert len(FundingRaised.where(csv_path, {'city': 'Tempe'})) == 3

def test_where_returns_events_by_state():
  assert len(FundingRaised.where(csv_path, {'state': 'CA'})) == 873

def test_where_returns_events_by_company():
  assert len(FundingRaised.where(csv_path, {'company_name': 'Facebook', 'round': 'a'})) == 1

def test_where_returns_events_by_type():
  assert len(FundingRaised.where(csv_path, {'round': 'a'})) == 582

def test_where_returns_no_events():
  assert len(FundingRaised.where(csv_path, {'company_name': 'NotFacebook'})) == 0

def test_find_by_event_by_company_name():
  row = FundingRaised.where(csv_path, {'company_name': 'Facebook'}, 1)
  row_test = {'permalink': 'facebook', 'company_name': 'Facebook', 'number_employees': 450, 'category': 'web', 'city': 'Palo Alto', 'state': 'CA', 'funded_date': '1-Sep-04', 'raised_amount': 500000, 'raised_currency': 'USD', 'round': 'angel'}
  assert len(row) == 1
  assert row[0] == row_test

def test_find_by_event_by_state():
  row = FundingRaised.where(csv_path, {'state': 'CA'}, limit=1)
  row_test = {'permalink': 'digg', 'company_name': 'Digg', 'number_employees': 60, 'category': 'web', 'city': 'San Francisco', 'state': 'CA', 'funded_date': '1-Dec-06', 'raised_amount': 8500000, 'raised_currency': 'USD', 'round': 'b'}
  assert len(row) == 1
  assert row[0] == row_test

test_where_returns_events()
test_where_returns_correct_keys()
test_where_returns_events_by_city()
test_where_returns_events_by_state()
test_where_returns_events_by_company()
test_where_returns_events_by_type()
test_where_returns_no_events()
test_find_by_event_by_company_name()
test_find_by_event_by_state()
