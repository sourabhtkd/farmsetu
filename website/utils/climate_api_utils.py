import traceback

import requests

from farmsetu import constants
from farmsetu.type_class import OrderType


class Parser:
    """

    Parses data based on order type

    """
    __slots__ = ('ordering_type',)

    def __init__(self, ordering_type):
        self.ordering_type = ordering_type

    @staticmethod
    def get_parser(ordering_type):
        """
        returns parser object.

        .. note::
           Parser object can be instantiated directly this is implemented just for
           readability or in case different Parser classes are meant to be instantiated
           based on parameters

        """
        return Parser(ordering_type)

    def __parse_year_ordered_data(self, data):
        """
        Parses year ordered data

        """
        result_list = list()
        row_list = data.splitlines()[5:]
        field_list = row_list.pop(0)
        column_list = [f.strip() for f in field_list.split(' ') if f.strip() != ""]

        i = 0
        for row in row_list:
            row_values = [r.strip() for r in row.split(' ') if r.strip() != ""]
            result = dict(zip(column_list, row_values))
            if len(result) >= 12 and i == 0:
                data_list = row_values[1:13]
                # data_list = [float(d) for d in data_list]

            result_list.append(result)

        return result_list

    def __parse_rank_ordered_data(self, data):
        """
        Parses rank ordered data

        """
        result_list = list()
        row_list = data.splitlines()[5:]
        field_list = row_list.pop(0)
        column_list = [f.strip() for f in field_list.split(' ') if f.strip() != ""]

        for row in row_list:
            row_values = [r.strip() for r in row.split(' ') if r.strip() != ""]
            # prepared_list.append({'headers': column_list, "row": row_values})
            for start in range(0, len(row_values), 2):
                limit = start + 2
                related_col = column_list[start:limit]
                related_row = row_values[start:limit]
                result_list.append(
                    {
                        related_col[0]: related_row[0],
                        related_col[1]: related_row[1],
                    }
                )

        return result_list

    def parse(self, data):
        """
        Calls appropriate parser based on order type

        """
        func_dict = {
            OrderType.YEAR_ORDERED: self.__parse_year_ordered_data,
            OrderType.RANKED: self.__parse_rank_ordered_data,
        }
        callable_func = func_dict[self.ordering_type]
        return callable_func(data)


class Formatter:
    __slots__ = ('ordering_type',)

    def __init__(self, ordering_type):
        self.ordering_type = ordering_type

    @staticmethod
    def get_formatter(ordering_type):
        """
        :params ordering_type: values from :class:`farmsetu.type_class.OrderType`
        returns formatter object based on order type, implemented just for readability,
        in case different formatter classes are required those can be instantiated from here

        """
        return Formatter(ordering_type)

    def format(self, data):
        """
        calls approriate formatter based on order type

        """
        func_dict = {
            OrderType.YEAR_ORDERED: self.__format_year_ordered_data,
            OrderType.RANKED: self.__format_rank_ordered_data,
        }
        callable_func = func_dict[self.ordering_type]
        return callable_func(data)

    def __format_year_ordered_data(self, data_list):
        """
        Formats year ordered data

        """
        result = dict()

        for data in data_list:
            if data['year'] not in result:
                year = data.pop('year')
                result[year] = {}

            result[year]['months'] = {}
            result[year]['seasons'] = {}
            result[year][constants.ANNUAL_CONSTANT] = ""

            for k, v in data.items():
                try:
                    v = float(v)
                except (ValueError, TypeError) as ex:
                    v = None

                if str(k).lower() in constants.SHORT_MONTH_CONSTANT_LIST:
                    # result[year]['months'].append({k: v})
                    result[year]['months'][k] = v
                elif str(k).lower() in constants.UK_SEASON_CONSTANT_LIST:
                    # result[year]['seasons'].append({k: v})
                    result[year]['seasons'][k] = v
                elif str(k).lower() in constants.ANNUAL_CONSTANT:
                    result[year][constants.ANNUAL_CONSTANT] = v

        return result

    def __format_rank_ordered_data(self, data_list):
        """
        formats rank ordered data

        """
        result = dict()
        result['months'] = dict()
        result['seasons'] = dict()
        result[constants.ANNUAL_CONSTANT] = list()

        for data in data_list:
            if any(item in constants.SHORT_MONTH_CONSTANT_LIST for item in list(data.keys())):
                year = data.pop("year")
                month = list(data.keys())[0]
                val = data[month]

                try:
                    val = float(val)
                except (ValueError, TypeError) as ex:
                    val = None

                if month not in result['months']:
                    result['months'][month] = list()

                result['months'][month].append({year:val})

            elif any(item in constants.UK_SEASON_CONSTANT_LIST for item in list(data.keys())):
                year = data.pop("year")
                season = list(data.keys())[0]
                val = data[season]

                try:
                    val = float(val)
                except (ValueError, TypeError) as ex:
                    val = None

                if season not in result['seasons']:
                    result['seasons'][season] = list()
                result['seasons'][season].append({year: val})

            elif any(item in constants.ANNUAL_CONSTANT for item in list(data.keys())):
                year = data.pop("year")
                annual = list(data.keys())[0]
                val = data[annual]

                try:
                    val = float(val)
                except (ValueError, TypeError) as ex:
                    val = None

                if annual not in result[constants.ANNUAL_CONSTANT]:
                    result[constants.ANNUAL_CONSTANT].append({year: val})
                # row['seasons'][season].append({year: val})

        return result


class ClimateApiUtil:

    def __init__(self, parameter, ordering_type, region):
        self.message = ""
        self.errors = ""

        self.parameter = parameter
        self.ordering_type = ordering_type
        self.region = region
        self.__base_url = constants.BASE_API_URL

    def get_climate_data(self):
        """
        Forms url based on parameters and only calls api and returns climate api object.

        on success sets  _data and message and returns climate api object
        on failure sets errors(traceback for logging) and message then returns climate api object

        """
        try:
            self.__url = constants.API_RESULT_URL_FORMATTED.format(
                base_api_url=self.__base_url,
                parameter=self.parameter,
                ordering_type=self.ordering_type,
                region=self.region,
            )
            result = requests.get(self.__url, headers={'Accept': "application/json"})
            self._data = result.text
            self.message = "successfully fetched climate data"
            return self

        except requests.exceptions.RequestException as ex:
            self.message = "Error while fetching data from climate api"
            self.errors = traceback.format_exc()
            return self

    def is_valid(self):
        """
         will return true only if climate data api is fetched successfully.
         before returning true it will set __parser and parsed data in the
         current object

        """
        try:
            if not hasattr(self,'_data'):
                return False
            self.__parser = Parser.get_parser(self.ordering_type)
            self.parsed_data = self.__parser.parse(self._data)
            return True
        except Exception as ex:
            return False

    def get_formatted_data(self):
        """
         Gets proper formatter based on order type and formats data
        """
        if not hasattr(self, 'parsed_data'):
            raise Exception('call is valid before formatting data')

        if hasattr(self, 'parsed_data') and self.parsed_data is None:
            raise Exception('is_valid did not parsed data')

        self.__formatter = Formatter.get_formatter(self.ordering_type)
        self.formated_data = self.__formatter.format(self.parsed_data)

        return self.formated_data
