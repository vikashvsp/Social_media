drop table if exists posts;
	create table posts(
		id integer primary key , 
		name text,
		content text not null
);