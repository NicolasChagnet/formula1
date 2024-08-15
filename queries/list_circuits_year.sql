   select distinct circuits.name,
          circuits.circuitid as circuit_id,
          races.date as race_date,
          circuits.location as circuit_city,
          circuits.country as circuit_country
     from circuits
     join races on circuits.circuitid = races.circuitid
    where races.year = :year_chosen
 order by races.date
;