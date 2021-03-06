CREATE OR REPLACE PACKAGE BAND_PACKAGE AS
  TYPE T_BAND IS RECORD (
    NAME_OF_BAND VARCHAR2(30 CHAR),
    MUSIC_LABEL VARCHAR2(30 CHAR)
    );

  TYPE T_BAND_TABLE IS TABLE OF T_BAND;

  FUNCTION GET_BAND(NAME IN BAND.NAME_OF_BAND%TYPE)
    RETURN T_BAND_TABLE PIPELINED;
  FUNCTION GET_BANDS
    RETURN T_BAND_TABLE PIPELINED;
  PROCEDURE ADD_BAND(B_NAME IN BAND.NAME_OF_BAND%TYPE,
                     LABEL IN BAND.MUSIC_LABEL%TYPE);
END;


CREATE OR REPLACE PACKAGE BODY BAND_PACKAGE AS
  PROCEDURE ADD_BAND(B_NAME IN BAND.NAME_OF_BAND%TYPE,
                     LABEL IN BAND.MUSIC_LABEL%TYPE) as
  begin
    insert into BAND (NAME_OF_BAND, MUSIC_LABEL) VALUES (B_NAME, LABEL);
    commit ;
  end;

  FUNCTION GET_BAND(NAME IN BAND.NAME_OF_BAND%type)
    RETURN T_BAND_TABLE PIPELINED AS
    CURSOR MY_CUR IS
      SELECT *
      FROM BAND
      WHERE BAND.NAME_OF_BAND = NAME;
  BEGIN
    FOR CURR IN MY_CUR
      LOOP
        PIPE ROW (CURR);
      end loop;
  END;

  FUNCTION GET_BANDS
    RETURN T_BAND_TABLE PIPELINED AS
    CURSOR MY_CURSOR IS
      SELECT *
      FROM BAND;
  BEGIN
    FOR REC IN MY_CURSOR
      LOOP
        PIPE ROW (REC);
      END LOOP;
  END;
END;