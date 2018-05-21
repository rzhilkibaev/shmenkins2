create table if not exists shmenkins.artifact_group (
    id integer unsigned auto_increment primary key,
    name varchar(100) not null unique
);

create table if not exists shmenkins.scm_trigger (
    id integer unsigned auto_increment primary key,
    url varchar(1000) character set utf8 not null,
    index (url)
);

create table if not exists shmenkins.artifact_group__scm_trigger (
    artifact_group_id integer unsigned not null,
    scm_trigger_id integer unsigned not null,
    primary key (artifact_group_id, scm_trigger_id),
    index (artifact_group_id),
    index (scm_trigger_id),
    foreign key (artifact_group_id) references shmenkins.artifact_group(id),
    foreign key (scm_trigger_id) references shmenkins.scm_trigger(id)
);

drop table if exists shmenkins.artifact_group__scm_trigger;