   select distinct drivers.driverid,
          drivers.forename as driver_forename,
          drivers.surname as driver_surname,
          (drivers.forename || " " || drivers.surname) as driver_fullname,
          drivers.url as driver_url,
          drivers.nationality as driver_country
     from drivers
     join results on drivers.driverid = results.driverid
     join races on results.raceid = races.raceid
    where races.year = :year_chosen