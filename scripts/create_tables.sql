CREATE TABLE "circuits"(
  "circuitId" INT   ,
  "circuitRef" TEXT,
  "name" TEXT,
  "location" TEXT,
  "country" TEXT,
  "lat" INT,
  "lng" INT,
  "alt" INT,
  "url" TEXT
);
CREATE TABLE "constructor_results"(
  "constructorResultsId" INT,
  "raceId" INT,
  "constructorId" INT,
  "points" INT,
  "status" TEXT
);
CREATE TABLE "constructors"(
  "constructorId" INT,
  "constructorRef" TEXT,
  "name" TEXT,
  "nationality" TEXT,
  "url" TEXT
);
CREATE TABLE "constructor_standings"(
  "constructorStandingsId" INT,
  "raceId" INT,
  "constructorId" INT,
  "points" INT,
  "position" INT,
  "positionText" TEXT,
  "wins" INT
);
CREATE TABLE "drivers"(
  "driverId" INT,
  "driverRef" TEXT,
  "number" TEXT,
  "code" TEXT,
  "forename" TEXT,
  "surname" TEXT,
  "dob" DATE,
  "nationality" TEXT,
  "url" TEXT
);
CREATE TABLE "driver_standings"(
  "driverStandingsId" INT,
  "raceId" INT,
  "driverId" INT,
  "points" INT,
  "position" INT,
  "positionText" TEXT,
  "wins" INT
);
CREATE TABLE "lap_times"(
  "raceId" INT,
  "driverId" INT,
  "lap" INT,
  "position" INT,
  "time" TEXT,
  "milliseconds" INT
);
CREATE TABLE "pit_stops"(
  "raceId" INT,
  "driverId" INT,
  "stop" INT,
  "lap" INT,
  "time" TEXT,
  "duration" FLOAT,
  "milliseconds" INT
);
CREATE TABLE "qualifying"(
  "qualifyId" INT,
  "raceId" INT,
  "driverId" INT,
  "constructorId" INT,
  "number" INT,
  "position" INT,
  "q1" TEXT,
  "q2" TEXT,
  "q3" TEXT
);
CREATE TABLE "races"(
  "raceId" INT,
  "year" INT,
  "round" INT,
  "circuitId" INT,
  "name" TEXT,
  "date" DATE,
  "time" TEXT,
  "url" TEXT,
  "fp1_date" TEXT,
  "fp1_time" TEXT,
  "fp2_date" TEXT,
  "fp2_time" TEXT,
  "fp3_date" TEXT,
  "fp3_time" TEXT,
  "quali_date" TEXT,
  "quali_time" TEXT,
  "sprint_date" TEXT,
  "sprint_time" TEXT
);
CREATE TABLE "results"(
  "resultId" INT,
  "raceId" INT,
  "driverId" INT,
  "constructorId" INT,
  "number" INT,
  "grid" INT,
  "position" INT,
  "positionText" TEXT,
  "positionOrder" INT,
  "points" INT,
  "laps" INT,
  "time" TEXT,
  "milliseconds" INT,
  "fastestLap" INT,
  "rank" INT,
  "fastestLapTime" TEXT,
  "fastestLapSpeed" FLOAT,
  "statusId" INT
);
CREATE TABLE "seasons"(
  "year" INT,
  "url" TEXT
);
CREATE TABLE "sprint_results"(
  "resultId" INT,
  "raceId" INT,
  "driverId" INT,
  "constructorId" INT,
  "number" INT,
  "grid" INT,
  "position" INT,
  "positionText" TEXT,
  "positionOrder" INT,
  "points" INT,
  "laps" INT,
  "time" TEXT,
  "milliseconds" TEXT,
  "fastestLap" INT,
  "fastestLapTime" TEXT,
  "statusId" INT
);
CREATE TABLE "status"(
  "statusId" INT,
  "status" TEXT
);