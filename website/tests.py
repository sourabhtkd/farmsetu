class BaseApiTestCase(APITestCase):

    def setUp(self) -> None:
        self.app = Application.objects.create(
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            redirect_uris='',
            name='test'
        )

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

