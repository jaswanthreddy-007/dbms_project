--1 show all passengers
--2 book ticket (trigger)
--3 veiw ticket
--4 flight related query


--1 show all passengers

select p.passport_number,p.name,p.flight_number,f.destination
from passenger p,flight f
where(p.flight_number = f.flight_number);



--3 veiw ticket

select p.passport_number,p.name,p.sex,p.flight_number,f.source,f.destination,f.arrival_time,f.departure_time,a.airline_name
from passenger p,flight f,airline a
where(p.flight_number=f.flight_number and f.airline_id = a.airline_id);


--2 trigger

create trigger exp_trig after insert on passenger
for each row
BEGIN
select p.passport_number,p.name,p.sex,p.flight_number,f.source,f.destination,f.arrival_time,f.departure_time,a.airline_name
from passenger p,flight f,airline a
where(p.flight_number=f.flight_number and f.airline_id = a.airline_id);
END