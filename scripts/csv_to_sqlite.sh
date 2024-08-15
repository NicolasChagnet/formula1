#!/bin/bash
# This script must be executed from the main folder!
locationDB="./data/final/formula1.db"
pathToData="./data/raw"
queryFile="./scripts/create_tables.sql"
# Erase previous database
[ -e ${locationDB} ] && rm ${locationDB}

# Create all tables
sqlite3 ${locationDB} < ${queryFile}
# Load all CSV files
for filename in ${pathToData}/*.csv; do
    base=$(basename -- "$filename" .csv)
    sqlite3 ${locationDB} ".mode csv" ".import --skip 1 ${filename} ${base}"
done