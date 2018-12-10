CREATE OR REPLACE PACKAGE SONG_PACKAGE AS
  TYPE T_SONG IS RECORD (
  ID_SONG NUMBER,
  NAME_OF_SONG VARCHAR2(30 CHAR),
  DURATION BINARY_DOUBLE,
  BAND VARCHAR2(30 CHAR)
  );

  TYPE T_SONG_TABLE IS TABLE OF T_SONG;

  FUNCTION GET_SONG(S_ID IN SONG.ID%TYPE)
    RETURN T_SONG_TABLE PIPELINED;
  FUNCTION GET_SONGS
    RETURN T_SONG_TABLE PIPELINED;
END;

CREATE OR REPLACE PACKAGE BODY SONG_PACKAGE AS
  FUNCTION GET_SONG(S_ID IN SONG.ID%type)
    RETURN T_SONG_TABLE PIPELINED AS
    CURSOR MY_CUR IS
      SELECT *
      FROM SONG
      WHERE SONG.ID = S_ID;
    BEGIN
      FOR CURR IN MY_CUR
      LOOP
        PIPE ROW (CURR);
      end loop;
    END;

  FUNCTION GET_SONGS
    RETURN T_SONG_TABLE PIPELINED AS
    CURSOR MY_CURSOR IS
      SELECT *
      FROM SONG;
    BEGIN
      FOR REC IN MY_CURSOR
      LOOP
        PIPE ROW (REC);
      END LOOP;
    END;
END SONG_PACKAGE;
  /
select * from table (SONG_PACKAGE.GET_SONG(4));