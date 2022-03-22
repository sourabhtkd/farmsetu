"""
This file contains choice fields of databases and forms, though it makes application a bit of tight coupled and is
more relevant approach in monolithic applications but here we have only one application so this
is fine

"""


class OrderType:
    """
    options for order field in meetoffice api
    """
    #: to get rank ordered data from meetoffice api
    RANKED = 'ranked'
    #: to get year ordered data from meetoffice api
    YEAR_ORDERED = 'date'

    choices = (
        (RANKED, 'Ranked Ordered'),
        (YEAR_ORDERED, 'Year Ordered')
    )


class RegionType:
    """
    Options for region field in MetOfficeView api,

    .. note::
       We could have stored regions in database but this parameter will be
       rarely changed so putting these values as choice field makes good choice

    """
    UK = 'UK'
    England = 'England'
    Wales = 'Wales'
    Scotland = 'Scotland'
    Northern_Ireland = 'Northern_Ireland'
    England_and_Wales = 'England_and_Wales'
    England_N = 'England_N'
    England_S = 'England_S'
    Scotland_N = 'Scotland_N'
    Scotland_E = 'Scotland_E'
    Scotland_W = 'Scotland_W'
    England_E_and_NE = 'England_E_and_NE'
    England_NW_and_N_Wales = 'England_NW_and_N_Wales'
    Midlands = 'Midlands'
    East_Anglia = 'East_Anglia'
    England_SW_and_S_Wales = 'England_SW_and_S_Wales'
    England_SE_and_Central_S = 'England_SE_and_Central_S'

    choices = (
        (UK, 'UK'),
        (England, 'England'),
        (Wales, 'Wales'),
        (Scotland, 'Scotland'),
        (Northern_Ireland, 'Northern_Ireland'),
        (England_and_Wales, 'England And Wales'),
        (England_N, 'England N'),
        (England_S, 'England_S'),
        (Scotland_N, 'Scotland_N'),
        (Scotland_E, 'Scotland_E'),
        (Scotland_W, 'Scotland_W'),
        (England_E_and_NE, 'England_E_and_NE'),
        (England_NW_and_N_Wales, 'England_NW_and_N_Wales'),
        (Midlands, 'Midlands'),
        (East_Anglia, 'East_Anglia'),
        (England_SW_and_S_Wales, 'England_SW_and_S_Wales'),
        (England_SE_and_Central_S, 'England_SE_and_Central_S'),
    )


class ParameterType:
    """
    options for parameter field in MetOffice api

    """

    Tmax = "Tmax"
    Tmin = 'Tmin'
    Tmean = 'Tmean'
    Sunshine = 'Sunshine'
    Rainfall = 'Rainfall'
    Raindays1mm = 'Raindays1mm'
    AirFrost = 'AirFrost'

    choices = (
        (Tmax, 'Tmax'),
        (Tmin, 'Tmin'),
        (Tmean, 'Tmean'),
        (Sunshine, 'Sunshine'),
        (Rainfall, 'Rainfall'),
        (Raindays1mm, 'Raindays1mm'),
        (AirFrost, 'AirFrost'),
    )
