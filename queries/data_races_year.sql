     with race_wins as (
             select drivers.driverref,
                    drivers.forename,
                    drivers.surname,
                    drivers.nationality,
                    (drivers.forename || " " || drivers.surname) as fullname,
                    races.name,
                    races.date,
                    results.position,
                    results.grid,
                    constructors.name as team_name
               from results
               join races on results.raceid = races.raceid
               join drivers on results.driverid = drivers.driverid
               join constructors on results.constructorid = constructors.constructorid
              where races.year = :year_chosen
          ),
          counting_wins as (
             select driverref,
                    forename,
                    surname,
                    fullname,
                    team_name,
                    sum(
                    case
                              when position = 1 then 1
                              else 0
                    end
                    ) as nb_race_wins,
                    sum(
                    case
                              when grid = 1 then 1
                              else 0
                    end
                    ) as nb_qual_wins
               from race_wins
           group by driverref
           order by nb_race_wins desc
          )
   select counting_wins.driverref as driver_ref,
          counting_wins.forename as driver_forename,
          counting_wins.surname as driver_surname,
          counting_wins.fullname as driver_fullname,
          coalesce(counting_wins.nb_race_wins, 0) as nb_race_wins,
          coalesce(counting_wins.nb_qual_wins, 0) as nb_qual_wins,
          counting_wins.team_name as team_name
     from counting_wins
    where (
          nb_race_wins > 0
       or nb_qual_wins > 0
          )
 order by counting_wins.nb_race_wins desc
    limit 10
;