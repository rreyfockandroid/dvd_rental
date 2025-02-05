select rental_date, return_date, 
extract(hour from rental_date) as rental_hour, extract(minute from rental_date) as rental_minute,
return_date-rental_date as diff_raw, 
extract(day from return_date-rental_date) as diff_day_BAD, 
return_date::date-rental_date::date as difference_in_days,
extract(epoch from (return_date::timestamp-rental_date::timestamp ))/3600 as difference_in_hours,
round(extract(epoch from (return_date::timestamp-rental_date::timestamp ))/3600, 0) as difference_in_hours
from rental 
limit 10;


     rental_date     |     return_date     | rental_hour | rental_minute |    diff_raw     | diff_day_bad | difference_in_days | difference_in_hours  | difference_in_hours 
---------------------+---------------------+-------------+---------------+-----------------+--------------+--------------------+----------------------+---------------------
 2005-05-24 22:54:33 | 2005-05-28 19:40:33 |          22 |            54 | 3 days 20:46:00 |            3 |                  4 |  92.7666666666666667 |                  93
 2005-05-24 23:03:39 | 2005-06-01 22:12:39 |          23 |             3 | 7 days 23:09:00 |            7 |                  8 | 191.1500000000000000 |                 191
 2005-05-24 23:04:41 | 2005-06-03 01:43:41 |          23 |             4 | 9 days 02:39:00 |            9 |                 10 | 218.6500000000000000 |                 219
 2005-05-24 23:05:21 | 2005-06-02 04:33:21 |          23 |             5 | 8 days 05:28:00 |            8 |                  9 | 197.4666666666666667 |                 197
 2005-05-24 23:08:07 | 2005-05-27 01:32:07 |          23 |             8 | 2 days 02:24:00 |            2 |                  3 |  50.4000000000000000 |                  50
 2005-05-24 23:11:53 | 2005-05-29 20:34:53 |          23 |            11 | 4 days 21:23:00 |            4 |                  5 | 117.3833333333333333 |                 117
 2005-05-24 23:31:46 | 2005-05-27 23:33:46 |          23 |            31 | 3 days 00:02:00 |            3 |                  3 |  72.0333333333333333 |                  72
 2005-05-25 00:00:40 | 2005-05-28 00:22:40 |           0 |             0 | 3 days 00:22:00 |            3 |                  3 |  72.3666666666666667 |                  72
 2005-05-25 00:02:21 | 2005-05-31 22:44:21 |           0 |             2 | 6 days 22:42:00 |            6 |                  6 | 166.7000000000000000 |                 167
 2005-05-25 00:09:02 | 2005-06-02 20:56:02 |           0 |             9 | 8 days 20:47:00 |            8 |                  8 | 212.7833333333333333 |                 213
(10 rows)


select rental_date,
extract(hour from rental_date) as rental_hour, extract(minute from rental_date) as rental_minute
from rental 
limit 10;
     rental_date     | rental_hour | rental_minute 
---------------------+-------------+---------------
 2005-05-24 22:54:33 |          22 |            54
 2005-05-24 23:03:39 |          23 |             3
 2005-05-24 23:04:41 |          23 |             4
 2005-05-24 23:05:21 |          23 |             5
 2005-05-24 23:08:07 |          23 |             8
 2005-05-24 23:11:53 |          23 |            11
 2005-05-24 23:31:46 |          23 |            31
 2005-05-25 00:00:40 |           0 |             0
 2005-05-25 00:02:21 |           0 |             2
 2005-05-25 00:09:02 |           0 |             9
(10 rows)


SELECT
  AGE('2012-03-05', '2010-04-01'),
  DATE_PART('year', AGE('2012-03-05', '2010-04-01')) AS years,
  DATE_PART('month', AGE('2012-03-05', '2010-04-01')) AS months,
  DATE_PART('day', AGE('2012-03-05', '2010-04-01')) AS days;
  
            age          | years | months | days 
-----------------------+-------+--------+------
 1 year 11 mons 4 days |     1 |     11 |    4
(1 row)

