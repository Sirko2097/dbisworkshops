UPDATE SONG SET MUSIC_LABEL = 'Shady records' WHERE (SELECT max(bands) from (select DISTINCT count(BAND ) as bands from SONG group by BAND));