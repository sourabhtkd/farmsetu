class OrderingType:
    RANKED = 'ranked'
    YEAR_ORDERED = 'date'

    choices = (
        (RANKED, 'Ranked Ordered'),
        (YEAR_ORDERED, 'Year Ordered')
    )


class RegionType:
    """
    As per convention all constants should be uppercase but due to time limitation
    avoiding convention

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
    As per convention all constants should be uppercase but due to time limitation
    avoiding convention

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


class Month:
    JAN = 'jan'
