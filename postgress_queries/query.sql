-- userzy z najwieksza liczba operacji/wypozyczen
select customer_id, count(*) c 
from rental
group by customer_id 
order by c desc;

-- na ile czasu wyporzyczaja srednio globalnie
select
sum(return_date::date-rental_date::date)::numeric/count(*)::numeric as days
from rental;

-- na ile czasu wyporzyczaja srednio poszczegolni
select customer_id,
sum(return_date::date-rental_date::date)::numeric/count(*)::numeric as days
from rental
group by customer_id
order by days desc;

-- wypozyczyli a jeszcze nie oddali
select *
from rental r left join payment p on r.rental_id=p.rental_id
where p.rental_id is null;

-- ile wypozyczyl, ile oddal, ile lacznie juz zaplacil, na ile dni srednio wypozycza
select (c.first_name || ' ' || c.last_name) as name , sum(p.amount) as pay, 
count(r.customer_id)-count(p.customer_id) as still_rentaled, count(p.customer_id) as returned,
round(sum(return_date::date-rental_date::date)::numeric/count(*)::numeric, 0) as avg_rental_days
from rental r left join payment p on r.rental_id=p.rental_id
inner join customer c on c.customer_id=r.customer_id 
group by name
order by pay desc
;


-- 10 filmow ktore najwiecej zarobily
select sum(p.amount) as amount, count(p.payment_id), (f.title || ' - ' || f.film_id) as title from payment p 
inner join rental r on p.rental_id = r.rental_id
inner join inventory i on i.inventory_id =r.inventory_id 
inner join film f on i.film_id = f.film_id
group by f.film_id order by amount desc limit 10;

-- jaki user najwiecej kasy zostawil
-- lzejsze
select c.customer_id, c.first_name, c.last_name  from customer c where c.customer_id = 
(select p.customer_id from payment p group by p.customer_id order by sum(p.amount) desc limit 1);
-- ciezsze
select p.customer_id, c.first_name,  c.last_name   from customer c inner join payment p on p.customer_id = c.customer_id  
group by p.customer_id, c.first_name, c.last_name order by sum(p.amount) desc limit 1;