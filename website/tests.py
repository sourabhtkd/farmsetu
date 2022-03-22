from rest_framework.test import APITestCase

from farmsetu.type_class import RegionType, ParameterType, OrderType


class BaseApiTestCase(APITestCase):

    # def setUp(self) -> None:
    #     self.app = Application.objects.create(
    #         client_type=Application.CLIENT_CONFIDENTIAL,
    #         authorization_grant_type=Application.GRANT_PASSWORD,
    #         redirect_uris='',
    #         name='test'
    #     )

    def assertEqualsForTwoDicts(self, response_data_dict, expected_data_dict):
        """
         response_data_dict: response got after calling api
         expected_data_dict: Values we want to match
         eg:
          response_data{
             "name":"vishal shekhar",
             "age":20
          }

          expected_data_dict = {
             "name":"aman saxena"
          }

          this will match name of expected data with name key of response_data
        """
        if not response_data_dict or type(response_data_dict) is not dict:
            raise Exception('expected dict for response_data_dict got {}'.format(type(response_data_dict)))

        if not expected_data_dict or type(expected_data_dict) is not dict:
            raise Exception('Expected dict for expected_data_dict but got {}'.format(type(expected_data_dict)))

        for key, value in expected_data_dict.items():
            self.assertEqual(response_data_dict[key], expected_data_dict[key],
                             msg='error in {} expected {}:type {} found {}:type {}'
                                 ''.format(key,
                                           expected_data_dict[key],
                                           type(expected_data_dict[key]),
                                           response_data_dict[key],
                                           type(response_data_dict[key])
                                           ))

    def assertKeyListInDict(self, response_dict, key_list):
        """
        checks if given list of keys exist in provided dictionary
        """
        if not key_list or type(key_list) is not list:
            raise Exception('Expected key_list as list but got {}'.format(type(key_list)))

        if not response_dict or type(response_dict) is not dict:
            raise Exception('Expected response_dict as dict but got {}'.format(type(response_dict)))

        for key in key_list:
            self.assertIn(key, response_dict)


class ClimateBaseTestCase(BaseApiTestCase):

    def setUp(self):
        self.url = "http://localhost:8000/"
        self.regions = [c[0] for c in RegionType.choices]
        self.parameters = [p[0] for p in ParameterType.choices]

    def test_success_rank_ordered_data(self):
        payload = dict()
        payload["order"] = OrderType.RANKED

        for region in self.regions:
            for parameter in self.parameters:
                payload['region'] = region
                payload['parameter'] = parameter
                headers = {
                    "Content-Type": "Application/json",
                    "Accept": "Application/json",
                }
                print("calling {}".format(payload))
                response = self.client.post(self.url, data=payload, headers=headers)
                self.assertEqual(response.status_code, 200)

                json_response = response.json()

                self.assertKeyListInDict(json_response, ['order', 'region', 'parameter', 'data'])
                self.assertKeyListInDict(json_response['data'], ['months', 'seasons', 'ann'])

                month_data = json_response['data']['months']
                self.assertEqual(type(month_data), dict)
                for month, v in month_data.items():
                    self.assertEqual(type(v), list)
                    for value in v:
                        self.assertEqual(type(value), dict)

                season_data = json_response['data']['seasons']
                self.assertEqual(type(season_data), dict)
                for season, v in season_data.items():
                    self.assertEqual(type(v), list)
                    for value in v:
                        self.assertEqual(type(value), dict)

                annual_data = json_response['data']['ann']
                self.assertEqual(type(annual_data), list)
                for data in annual_data:
                    self.assertEqual(type(data), dict)

    def test_success_year_ordered_data(self):
        payload = dict()
        payload["order"] = OrderType.YEAR_ORDERED

        for region in self.regions:
            for parameter in self.parameters:
                payload['region'] = region
                payload['parameter'] = parameter
                headers = {
                    "Content-Type": "Application/json",
                    "Accept": "Application/json",
                }
                print("calling {}".format(payload))
                response = self.client.post(self.url, data=payload, headers=headers)
                self.assertEqual(response.status_code, 200)

                json_response = response.json()

                self.assertKeyListInDict(json_response, ['order', 'region', 'parameter', 'data'])

                data = json_response['data']
                self.assertEqual(type(data),dict)

                for year, value in data.items():
                    # in wrong data Valuerror should be raised
                    self.assertEqual(type(int(year)), int)
                    self.assertEqual(len(year), 4)

                    self.assertEqual(type(value), dict)
