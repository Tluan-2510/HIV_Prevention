#!/bin/bash
psql -U hiv_user -d hiv_db -f /docker-entrypoint-initdb.d/init.sql
