CREATE OR REPLACE PACKAGE USER_PACKAGE AS
  TYPE T_USER IS RECORD (
    LOGIN VARCHAR2(30 CHAR),
    PASSWORD VARCHAR2(30 CHAR),
    NAME VARCHAR2(30 CHAR),
    EMAIL VARCHAR2(30 CHAR)
    );

  TYPE T_USER_TABLE IS TABLE OF T_USER;

  FUNCTION LOG_IN(LOG_NAME IN SUPERUSER.LOGIN%TYPE, PASS IN SUPERUSER.PASSWORD%TYPE)
    RETURN NUMBER;

  PROCEDURE REGISTRATION(LOG_IN IN SUPERUSER.LOGIN%TYPE, PASS IN SUPERUSER.PASSWORD%TYPE,
                         NEW_NAME IN SUPERUSER.NAME%TYPE,
                         NEW_EMAIL IN SUPERUSER.EMAIL%TYPE);
END;

CREATE OR REPLACE PACKAGE BODY USER_PACKAGE AS
  FUNCTION LOG_IN(LOG_NAME IN SUPERUSER.LOGIN%TYPE, PASS IN SUPERUSER.PASSWORD%TYPE)
    RETURN NUMBER AS
    rec NUMBER(1);
  BEGIN
    SELECT count(*)
           INTO rec
    FROM SUPERUSER
    WHERE SUPERUSER.LOGIN = LOG_NAME
      AND SUPERUSER.PASSWORD = PASS;

    RETURN (rec);
  END;

  PROCEDURE REGISTRATION(LOG_IN IN SUPERUSER.LOGIN%TYPE, PASS IN SUPERUSER.PASSWORD%TYPE,
                         NEW_NAME IN SUPERUSER.NAME%TYPE,
                         NEW_EMAIL IN SUPERUSER.EMAIL%TYPE) AS
  BEGIN
    INSERT INTO SUPERUSER (LOGIN, PASSWORD, NAME, EMAIL) VALUES (LOG_IN, PASS, NEW_NAME, NEW_EMAIL);

    commit;
  END;

END USER_PACKAGE;
/

select USER_PACKAGE.LOG_IN('Gray', '5116951169') from dual;
CALL USER_PACKAGE.REGISTRATION('Sirko', 'fghjk', 'Serhii', 'sirko2097@outlook.com');