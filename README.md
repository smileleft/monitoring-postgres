# monitoring-postgres

## With pgmetrics

```
# how to install

wget https://github.com/rapidloop/pgmetrics/releases/download/v1.17.1/pgmetrics_1.17.1_linux_amd64.tar.gz
tar xvf pgmetrics_1.17.1_linux_amd64.tar.gz
cd pgmetrics_1.17.1_linux_amd64
./pgmetrics --help
```

## Query for Write Ahead Log related stat

```
SELECT wal_records, wal_fpi, wal_bytes FROM pg_stat_wal;
```
