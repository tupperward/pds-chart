#!/bin/sh

set -e

helm install postgresql oci://registry-1.docker.io/bitnamicharts/postgresql \
  --set global.postgresql.auth.username=pds \
  --set global.postgresql.auth.password=pds \
  --set global.postgresql.auth.database=pds
