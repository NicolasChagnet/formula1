   select circuits.name as circuit_name,
          circuits.circuitid as circuit_id,
          circuits.location as circuit_city,
          circuits.country as circuit_country,
          drivers.forename as driver_forename,
          drivers.surname as driver_surname,
          (drivers.forename || " " || drivers.surname) as driver_fullname,
          results.grid,
          results.position,
          races.date as race_date
     from results
     join drivers on results.driverid = drivers.driverid
     join circuits on races.circuitid = circuits.circuitid
     join races on results.raceid = races.raceid
    where drivers.driverid = :id
      and races.year = :year_chosen
 order by race_date desc
;