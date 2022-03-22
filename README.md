# Farmsetu Assignment

## Tasks
- Call API https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series#yearOrdered
- Parse data
- Format data and return response


## Installation Process 

**Assumptions**
- Production server uses docker container for db not AWS RDS or
  some other service for database(which will be used in real project) so that you can try with production configuration also
- Production confs are intended to demonstrate logic of separation
  in dev and prod confs
- Assuming both prod and dev requires same requirements.txt
- SECRET_KEY is not coming from environment variable, left as it is intentionally
- Static files are served within django itself not using any production grade services like S3
- Assuming you won't run dev and prod containers at same time so volume names
  are kept same intentionally
- Database is not used but postgresql is configured to port 5433 assuming you have 
  postgresql installed in local system and running in default port 5432
- prod env and dev env are same except DEBUG flag

**Note**: Authentication and Authorization was not required as per task hence not implemented


**Steps**

```shell
## for dev docker-compose 
~$ docker-compose up -f docker-compose-dev.yml up
~$ docker-compose -f docker-compose-dev.yml exec web sh

## for prod docker-compose
~$ docker-compose up -f docker-compose-prod.yml up
~$ docker-compose -f docker-compose-prod.yml exec web sh

~$ python manage.py makemigrations
~$ python manage.py migrate
~$ python manage.py collectstatic --no-input

```
Running Test Cases

```shell
~$ docker-compose -f docker-compose-dev.yml exec web python manage.py test
~$ docker-compose -f docker-compose-prod.yml exec web python manage.py test
```

### API

1. Get Climate Data
   - **URL** = http://localhost:8000/
   - **Method** = POST
   - **Data** :-

##### Rank ordered

```json
{
    "order":"ranked",
    "region":"UK",
    "parameter":"Tmin"
}
```
##### Year Ordered

```json
{
    "order":"date",
    "region":"UK",
    "parameter":"Tmin"
}
```

**Field Level errors**

###### status code =400
```json
{
    "errors": {
        "order": [
            "This field may not be null."
        ],
        "region": [
            "This field may not be null."
        ],
        "parameter": [
            "This field may not be null."
        ]
    }
}
```

**Top level errors**
###### status_code = 400 
```json
{
    "errors": "Error while fetching data from climate api"
}


```

##### Rank Order Response example(truncated)

```json
{
  "order": "ranked",
  "region": "Wales",
  "parameter": "Tmin",
  "data": {
    "months": {
      "jan": [
        {
          "1916": 4.8
        },
        {
          "1921": 4.6
        }
      ],
      "feb": [
        {
          "1916": 4.8
        },
        {
          "1921": 4.6
        }
      ]
    },
    "seasons": {
            "win": [
                {
                    "2016": 3.67
                }
            ], 
            "spr": [
                {
                    "2016": 3.67
                }
            ]
     },
    "ann": [
            {
                "2017": 6.54
            }
    ]
  }
}
```

##### year order response example (truncated)

```json
{
  "order": "date",
  "region": "Wales",
  "parameter": "Tmin",
  "data": {
    "1884": {
      "months": {
        "jan": 3.6,
        "feb": 1.9,
        "mar": 2.2
      },
      "seasons": {
                "win": null,
                "spr": 3.28,
                "sum": 9.79,
                "aut": 6.12
            },
       "ann": 5.43
    }
    
  }
}

```
**Available parameter options**



| order                |   region                                             |   parameter                |
| ---------------------| ---------------------------------------------------- |----------------------------|
| RANKED = 'ranked'    | UK = 'UK'                                            | Tmax = "Tmax"              |
| YEAR_ORDERED = 'date'| England = 'England'                                  | Tmin = 'Tmin'              |
|                      | Wales = 'Wales'                                      | Tmean = 'Tmean'            |
|                      | Scotland = 'Scotland'                                | Sunshine = 'Sunshine'      |
|                      | Northern_Ireland = 'Northern_Ireland'                | Rainfall = 'Rainfall'      |
|                      | England_and_Wales = 'England_and_Wales'              | Raindays1mm = 'Raindays1mm'|
|                      | England_N = 'England_N'                              | AirFrost = 'AirFrost'      |
|                      | England_S = 'England_S'                              |
|                      | Scotland_N = 'Scotland_N'                            |
|                      | Scotland_E = 'Scotland_E'                            |
|                      | Scotland_W = 'Scotland_W'                            |
|                      | England_E_and_NE = 'England_E_and_NE'                |
|                      | England_NW_and_N_Wales = 'England_NW_and_N_Wales'    |
|                      | Midlands = 'Midlands'                                |
|                      | East_Anglia = 'East_Anglia'                          |
|                      | England_SW_and_S_Wales = 'England_SW_and_S_Wales'    |
|                      | England_SE_and_Central_S = 'England_SE_and_Central_S'|


