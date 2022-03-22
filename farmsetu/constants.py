"""
CONSTANTS FOR THIS PROJECT

"""
#: base METOFFICE url
BASE_API_URL = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets'
#: replace parameters in this url to get meetoffice data
API_RESULT_URL_FORMATTED = "{base_api_url}/{parameter}/{ordering_type}/{region}.txt"

#: key for monthly data in meetoffice api, ignoring convention of keeping constants in UpperCase here
SHORT_MONTH_CONSTANT_LIST = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
#: objects keys for seasonwise data in meetoffice api
UK_SEASON_CONSTANT_LIST = ['win', "spr", "sum", "aut"]
#: object keys for annual data in meetoffice api
ANNUAL_CONSTANT = "ann"
