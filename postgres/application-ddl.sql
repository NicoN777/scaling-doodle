CREATE SEQUENCE IF NOT EXISTS seq_application START 1;

CREATE TABLE IF NOT EXISTS application (
    id bigint not null primary key default nextval('seq_application'),
    name varchar(100) not null,
    password varchar(100) not null,
    create_ts timestamp default statement_timestamp(),
    update_ts timestamp
    );


CREATE SEQUENCE IF NOT EXISTS seq_owner_application_mapping START 1;
CREATE TABLE IF NOT EXISTS owner_application_mapping (
    id bigint not null default nextval('seq_owner_application_mapping'),
    owner_id bigint not null,
    application_id bigint not null,
    primary key (owner_id, application_id)
    );

ALTER TABLE owner_application_mapping ADD CONSTRAINT fk_owner_id_mapping FOREIGN KEY (owner_id) REFERENCES owner(id);
ALTER TABLE owner_application_mapping ADD CONSTRAINT fk_application_id_mapping FOREIGN KEY (application_id) REFERENCES application(id);