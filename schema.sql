drop table if exists posts;
	create table posts(
		id integer primary key , 
		names text,
		content text not null
);