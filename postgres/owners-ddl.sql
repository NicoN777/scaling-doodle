CREATE SEQUENCE IF NOT EXISTS seq_owner START 1;

CREATE TABLE IF NOT EXISTS owner (
    id bigint not null primary key default nextval('seq_owner'),
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    email varchar(100) not null,
    password varchar(100) not null,
    phone_no varchar(20),
    create_ts timestamp default statement_timestamp(),
    update_ts timestamp
    );