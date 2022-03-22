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


**Steps**

```shell
~$ docker-compose up -f docker-compose-dev.yml up
~$ docker-compose -f docker-compose-dev.yml exec web sh
~$ python manage.py makemigrations
~$ python manage.py migrate
~$ python manage.py collectstatic --no-input

```

### API

1. Get Climate Data
   - URL = http://localhost:8000/
   - Method = POST

Data

```json
{
    "order":"ranked",
    "region":"UK",
    "parameter":"Tmin"
}
```

Available parameter options

<div style="font-size:10px;">

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

</div>
