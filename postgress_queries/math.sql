select sum(return_date::date-rental_date::date), count(*),
sum(return_date::date-rental_date::date)::numeric/count(*)::numeric as man_avg,
avg(return_date::date-rental_date::date) as avg
from rental;
  sum  | count |      man_avg       |        avg         
-------+-------+--------------------+--------------------
 79705 | 16044 | 4.9679007728745949 | 5.0252190908517748
(1 row)

