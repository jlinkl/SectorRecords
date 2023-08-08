# SectorRecords

An exercise in practising flask and SQL databases.

The goal of this full stack app is to show each record for the fastest time of every lost sector from every season of Destiny 2.

The times used for this app will be taken from https://www.speedrun.com/destiny_2_lost_sectors
(i have decided to do this manually, as I currently can't think of an efficient way to do this without having to make potentially hundreds of calls to the api, due to how both the runs are stored, and how calls from the api itself works).

There will be functionality to allow a user to check the fastest times for every season, for every lost sector, and to see which players have the most world records.

The data will be stored in an SQL databse, containing the name of the runner, a link to watch the run, the time of the run, the date of when the run was completed, and what lost sector was run.

psql -d sector_records -f db/sector_records.sql