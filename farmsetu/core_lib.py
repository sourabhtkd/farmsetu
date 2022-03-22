"""
Core library functions which are expected to be used in all over the project
eg:- Object ids, image related functions, s3 upload functions

"""
import bson


class CoreUtils:

    @staticmethod
    def get_bson_object_id():
        """
        Bson object id for database(instead of default integer ids)

        """
        return bson.objectid
