   select coalesce(results.position,0) as position,
          coalesce(results.grid,0) as grid,
          drivers.forename as driver_forename,
          drivers.surname as driver_surname,
          (drivers.forename || " " || drivers.surname) as driver_fullname,
          circuits.location as circuit_city,
          circuits.country as circuit_country
     from results
     join races on results.raceid = races.raceid
     join drivers on results.driverid = drivers.driverid
     join circuits on races.circuitid = circuits.circuitid
    where races.year = :year_chosen
      and circuits.circuitid = :circuit_id
 order by results.position
;