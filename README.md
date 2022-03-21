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
- Assuming both prod and dev requires same requiremnts.txt
- SECRET_KEY is not coming from environment variable, left as it is intentionally
- Static files are served withinn django itself not using any production grade service like S3
- Assuming you won't run dev and prod containers at same time so volume names
  are kept same intentionally


**Steps**

```shell
~$ docker-compose up -f docker-compose-dev.yml up

```
