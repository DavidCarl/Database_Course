# Task-10

### Made by David Carl & Tjalfe Møller
### www.dcarl.me

## Setup

First download the `sql_scripts.zip` we uploaded. This contains all the necessary SQL scripts. Import these to your desired database. 

Just a tiny warning. This can take a long time, so you better be patient!

There is also a SQL dump of our working database, it can be found [here](https://github.com/DavidCarl/Database_Course/blob/master/Task-10/dump.sql)

This include our whole database so take this as a part of Excersise 1 and 2.


## Excersise 1

### Description

Copenhagen has a strategy for improving the living conditions in socially exposed areas (udsatte områder). It a policy which both addresses the social aspects for the people living there, and the physical conditions.

This exercises addresses the physical conditions, through the following two questions:

* How many parks are located in exposed areas?
* How many trees are located in exposed areas?

### Answer

Our answer to the first question, 'How many parks are located in exposed areas?'

SQLQuery:

```
with parkregister_extended as (select *, ST_Area(wkb_geometry) as area from parkregister)

select byomraade,
       delomraade,
       count(parkregister_extended.areal_id)  as "parks"
from udsatte_byomraader,
     parkregister_extended
where ST_Within(parkregister_extended.wkb_geometry, udsatte_byomraader.wkb_geometry)
group by udsatte_byomraader.id;
```

Result:

```
Valby/Sydhavnen,Sydhavnen,9
Valby/Sydhavnen,Ved Folehaven,1
Amager/Sundby,Urbanplanen mv.,1
Nørrebro,Ved Bispeengbuen,3
Nordvest/Ryparken,Ryparken,7
Nordvest/Ryparken,Nordvest,11
Tingbjerg/Husum,Tingbjerg/Husum,5
Nørrebro,Ved Jagtvej,2
Valby/Sydhavnen,Ved Kulbanevej,1
Valby/Sydhavnen,Ved Valby Langgade,1
Nørrebro,Ydre Nørrebro,1
Nørrebro,Indre Nørrebro,2
```

Our answer to the second question, 'How many trees are located in exposed areas?'

SQLQuery:

```
select byomraade,
       delomraade,
       count(gadetraer.id)  as "trees"
from udsatte_byomraader, gadetraer
where st_within(gadetraer.wkb_geometry, udsatte_byomraader.wkb_geometry)
group by udsatte_byomraader.id;
```

Result:

```
Nørrebro,Ved Jagtvej,74
Nørrebro,Indre Nørrebro,176
Valby/Sydhavnen,Sydhavnen,1340
Valby/Sydhavnen,Ved Kulbanevej,142
Valby/Sydhavnen,Ved Valby Langgade,54
Tingbjerg/Husum,Tingbjerg/Husum,600
Valby/Sydhavnen,Ved Folehaven,145
Nordvest/Ryparken,Nordvest,721
Nørrebro,Ved Bispeengbuen,260
Nørrebro,Ydre Nørrebro,247
Nordvest/Ryparken,Ved Bispebjerg Parkallé,65
Nordvest/Ryparken,Ved Bispebjerg Parkallé,6
Amager/Sundby,Urbanplanen mv.,318
Amager/Sundby,Ved Gyldenrisvej,31
Nørrebro,Ved Jagtvej,62
Nordvest/Ryparken,Ryparken,570
Amager/Sundby,Ved Frankrigsgade,55
```

## Excersise 2

### Description

Copenhagen prides itself for its lively bike culture. There are a number of different data on bike and bike services. But in particular, bikes do not mix well with trucks. 

* How many bike racks are places along routes for heavy traffic?

Again, to help navigate the danish table names:
* bike rack (cykelstativ)
* heavy traffic (tungvogn)

### Answer

SQLQuery:

```
with heavy_roads as (select ST_GeomFromText(ST_ASTEXT(ST_Buffer(ST_GeomFromText(ST_AsText(wkb_geometry), 0), 0.00025)), 4326) as area, id, vej from tungvognsnet)
select
       count(*) as "no_racks",
       sum(cykelstativ.antal_pladser) as "no_spaces"
from heavy_roads, cykelstativ
where st_within(cykelstativ.wkb_geometry, heavy_roads.area);
```

Result:

```
642,9141
```
