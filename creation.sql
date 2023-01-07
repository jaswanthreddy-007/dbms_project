create database test1;
use test1;

create table flight(
flight_number int primary key,
sourcec varchar(20),
destination varchar (20),
arrival_time time,
departure_time time,
FOREIGN KEY (airlineid) REFERENCES airline(airlineid));

create table passenger(
passport_number varchar(20) primary key,
Name_  varchar (20),
age int,
phoneno varchar (10),
FOREIGN KEY (tickid) REFERENCES ticket(tickid));

create table ticket(
ticket_num int primary key,
price int,
seat_num int,
FOREIGN KEY (passport_number) REFERENCES passenger(passport_number),
FOREIGN KEY (flight_number) REFERENCES flight(flight_number)
);

create table employee(
phone_num varchar(20) ,
name_ varchar(20),
emp_id varchar(10) primary key
);

create table airline(
airline_name varchar(20) primary key,
airline_id varchar(10)
);