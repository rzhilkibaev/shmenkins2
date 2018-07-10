create table if not exists shmenkins.artifact_group (
    id integer unsigned auto_increment primary key,
    name varchar(100) not null unique
);

create table if not exists shmenkins.scm_repo (
    id integer unsigned auto_increment primary key,
    url varchar(1000) character set utf8 not null,
    index (url)
);

create table if not exists shmenkins.scm_repo__artifact_group (
    scm_repo_id integer unsigned not null,
    artifact_group_id integer unsigned not null,
    primary key (scm_repo_id, artifact_group_id),
    index (scm_repo_id),
    index (artifact_group_id),
    foreign key (scm_repo_id) references shmenkins.scm_repo(id),
    foreign key (artifact_group_id) references shmenkins.artifact_group(id)
);
