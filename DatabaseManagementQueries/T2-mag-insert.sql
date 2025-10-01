/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T2-mag-insert.sql

--Student ID: 34269193
--Student Name: Robiatul Adawiyah Al-Qosh

/* Comments for your marker:

In this part, I inputted 10 aw_display entries and 4 sale entries
In aw_status, I assumed that I have to enter all the artworks, if the artwork not in aw_display I decided to make the status 'W'
Since there are some artworks that displayed in defferent galleries, I made several status for those artworks
And, for your note. I might put the date one day before the display date for 'T' status (transit to gallery)

*/


--------------------------------------
--INSERT INTO aw_display
--------------------------------------

INSERT INTO aw_display VALUES (1, 3, 1, TO_DATE('2-Jul-2022', 'DD-MON-YYYY'), TO_DATE('10-Aug-2022', 'DD-MON-YYYY'), 1);
INSERT INTO aw_display VALUES (2, 5, 1, TO_DATE('16-Aug-2022', 'DD-MON-YYYY'), TO_DATE('1-Sep-2022', 'DD-MON-YYYY'), 5);
INSERT INTO aw_display VALUES (3, 1, 1, TO_DATE('17-Aug-2022', 'DD-MON-YYYY'), TO_DATE('28-Sep-2022', 'DD-MON-YYYY'), 5);
INSERT INTO aw_display VALUES (4, 3, 1, TO_DATE('18-Aug-2022', 'DD-MON-YYYY'), TO_DATE('28-Sep-2022', 'DD-MON-YYYY'), 5);
INSERT INTO aw_display VALUES (5, 10, 1, TO_DATE('11-Sep-2022', 'DD-MON-YYYY'), TO_DATE('5-Oct-2022', 'DD-MON-YYYY'), 4);
INSERT INTO aw_display VALUES (6, 4, 1, TO_DATE('12-Sep-2022', 'DD-MON-YYYY'), NULL, 4);
INSERT INTO aw_display VALUES (7, 8, 2, TO_DATE('26-Oct-2022', 'DD-MON-YYYY'), TO_DATE('2-Nov-2022', 'DD-MON-YYYY'), 3);
INSERT INTO aw_display VALUES (8, 1, 1, TO_DATE('27-Oct-2022', 'DD-MON-YYYY'), TO_DATE('1-Nov-2022', 'DD-MON-YYYY'), 3);
INSERT INTO aw_display VALUES (9, 3, 1, TO_DATE('28-Nov-2022', 'DD-MON-YYYY'), TO_DATE('28-Dec-2022', 'DD-MON-YYYY'), 2);
INSERT INTO aw_display VALUES (10, 7, 2, TO_DATE('29-Nov-2022', 'DD-MON-YYYY'), TO_DATE('16-Dec-2022', 'DD-MON-YYYY'), 2);
INSERT INTO aw_display VALUES (11, 5, 2, TO_DATE('30-Nov-2022', 'DD-MON-YYYY'), TO_DATE('28-Dec-2022', 'DD-MON-YYYY'), 3);


--------------------------------------
--INSERT INTO aw_status
--------------------------------------

INSERT INTO aw_status VALUES (1, 1, 1, TO_DATE('2-Jun-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (2, 1, 1, TO_DATE('16-Aug-2022 12:00', 'DD-MON-YYYY HH24:MI'), 'T', 5);
INSERT INTO aw_status VALUES (3, 1, 1, TO_DATE('17-Aug-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'G', 5);
INSERT INTO aw_status VALUES (4, 1, 1, TO_DATE('28-Sep-2022 13:00', 'DD-MON-YYYY HH24:MI'), 'T', 5);
INSERT INTO aw_status VALUES (5, 1, 1, TO_DATE('25-Oct-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'T', 3);
INSERT INTO aw_status VALUES (6, 1, 1, TO_DATE('27-Oct-2022 15:00', 'DD-MON-YYYY HH24:MI'), 'G', 3);
INSERT INTO aw_status VALUES (7, 1, 1, TO_DATE('1-Nov-2022 17:00', 'DD-MON-YYYY HH24:MI'), 'S', 3);
INSERT INTO aw_status VALUES (8, 2, 1, TO_DATE('4-Jun-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (9, 3, 1, TO_DATE('5-Jun-2022 13:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (10, 3, 1, TO_DATE('1-Jul-2022 11:00', 'DD-MON-YYYY HH24:MI'), 'T', 1);
INSERT INTO aw_status VALUES (11, 3, 1, TO_DATE('2-Jul-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'G', 1);
INSERT INTO aw_status VALUES (12, 3, 1, TO_DATE('10-Aug-2022 12:00', 'DD-MON-YYYY HH24:MI'), 'T', 1);
INSERT INTO aw_status VALUES (13, 3, 1, TO_DATE('16-Aug-2022 13:00', 'DD-MON-YYYY HH24:MI'), 'T', 5);
INSERT INTO aw_status VALUES (14, 3, 1, TO_DATE('18-Aug-2022 12:00', 'DD-MON-YYYY HH24:MI'), 'G', 5);
INSERT INTO aw_status VALUES (15, 3, 1, TO_DATE('28-Sep-2022 17:00', 'DD-MON-YYYY HH24:MI'), 'T', 5);
INSERT INTO aw_status VALUES (16, 3, 1, TO_DATE('27-Nov-2022 17:30', 'DD-MON-YYYY HH24:MI'), 'T', 2);
INSERT INTO aw_status VALUES (17, 3, 1, TO_DATE('28-Nov-2022 09:00', 'DD-MON-YYYY HH24:MI'), 'G', 2);
INSERT INTO aw_status VALUES (18, 3, 1, TO_DATE('28-Dec-2022 15:00', 'DD-MON-YYYY HH24:MI'), 'R', NULL);
INSERT INTO aw_status VALUES (19, 4, 1, TO_DATE('6-Jun-2022 17:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (20, 4, 1, TO_DATE('10-Sep-2022 12:00', 'DD-MON-YYYY HH24:MI'), 'T', 4);
INSERT INTO aw_status VALUES (21, 4, 1, TO_DATE('12-Sep-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'G', 4);
INSERT INTO aw_status VALUES (22, 7, 1, TO_DATE('7-Jun-2022 16:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (23, 8, 1, TO_DATE('8-Jun-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (24, 5, 1, TO_DATE('15-Jul-2022 11:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (25, 5, 1, TO_DATE('14-Aug-2022 18:00', 'DD-MON-YYYY HH24:MI'), 'T', 5);
INSERT INTO aw_status VALUES (26, 5, 1, TO_DATE('15-Aug-2022 11:00', 'DD-MON-YYYY HH24:MI'), 'G', 5);
INSERT INTO aw_status VALUES (27, 5, 1, TO_DATE('1-Sep-2022 16:00', 'DD-MON-YYYY HH24:MI'), 'S', 5);
INSERT INTO aw_status VALUES (28, 9, 1, TO_DATE('14-Aug-2022 13:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (29, 10, 1, TO_DATE('1-Sep-2022 15:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (30, 10, 1, TO_DATE('10-Sep-2022 15:00', 'DD-MON-YYYY HH24:MI'), 'T', 4);
INSERT INTO aw_status VALUES (31, 10, 1, TO_DATE('11-Sep-2022 14:00', 'DD-MON-YYYY HH24:MI'), 'G', 4);
INSERT INTO aw_status VALUES (32, 10, 1, TO_DATE('5-Oct-2022 18:00', 'DD-MON-YYYY HH24:MI'), 'S', 4);
INSERT INTO aw_status VALUES (33, 1, 2, TO_DATE('18-Oct-2022 16:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (34, 7, 2, TO_DATE('19-Oct-2022 17:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (35, 7, 2, TO_DATE('27-Nov-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'T', 2);
INSERT INTO aw_status VALUES (36, 7, 2, TO_DATE('29-Nov-2022 09:00', 'DD-MON-YYYY HH24:MI'), 'G', 2);
INSERT INTO aw_status VALUES (37, 7, 2, TO_DATE('16-Dec-2022 17:00', 'DD-MON-YYYY HH24:MI'), 'S', 2);
INSERT INTO aw_status VALUES (38, 8, 2, TO_DATE('24-Oct-2022 14:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (39, 8, 2, TO_DATE('25-Oct-2022 18:00', 'DD-MON-YYYY HH24:MI'), 'T', 3);
INSERT INTO aw_status VALUES (40, 8, 2, TO_DATE('26-Oct-2022 11:00', 'DD-MON-YYYY HH24:MI'), 'G', 3);
INSERT INTO aw_status VALUES (41, 8, 2, TO_DATE('2-Nov-2022 11:00', 'DD-MON-YYYY HH24:MI'), 'S', 3);
INSERT INTO aw_status VALUES (42, 5, 2, TO_DATE('27-Oct-2022 16:00', 'DD-MON-YYYY HH24:MI'), 'W', NULL);
INSERT INTO aw_status VALUES (43, 5, 2, TO_DATE('29-Nov-2022 09:30', 'DD-MON-YYYY HH24:MI'), 'T', 3);
INSERT INTO aw_status VALUES (44, 5, 2, TO_DATE('30-Nov-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'G', 3);
INSERT INTO aw_status VALUES (45, 5, 2, TO_DATE('28-Dec-2022 16:00', 'DD-MON-YYYY HH24:MI'), 'S', 3);
INSERT INTO aw_status VALUES (46, 2, 1, TO_DATE('31-Dec-2022 10:00', 'DD-MON-YYYY HH24:MI'), 'R', NULL);
INSERT INTO aw_status VALUES (47, 7, 1, TO_DATE('31-Dec-2022 12:00', 'DD-MON-YYYY HH24:MI'), 'R', NULL);
INSERT INTO aw_status VALUES (48, 8, 1, TO_DATE('31-Dec-2022 14:00', 'DD-MON-YYYY HH24:MI'), 'R', NULL);
INSERT INTO aw_status VALUES (49, 9, 1, TO_DATE('31-Dec-2022 16:00', 'DD-MON-YYYY HH24:MI'), 'R', NULL);
INSERT INTO aw_status VALUES (50, 1, 2, TO_DATE('31-Dec-2022 18:00', 'DD-MON-YYYY HH24:MI'), 'R', NULL);


--------------------------------------
--INSERT INTO sale
--------------------------------------

INSERT INTO sale VALUES (1, TO_DATE('1-Sep-2022', 'DD-MON-YYYY'), 84748.21, 9, 2);
INSERT INTO sale VALUES (2, TO_DATE('5-Oct-2022', 'DD-MON-YYYY'), 54090.91, 1, 5);
INSERT INTO sale VALUES (3, TO_DATE('1-Nov-2022', 'DD-MON-YYYY'), 64379.32, 7, 8);
INSERT INTO sale VALUES (4, TO_DATE('2-Nov-2022', 'DD-MON-YYYY'), 64379.32, 7, 7);
INSERT INTO sale VALUES (5, TO_DATE('16-Dec-2022', 'DD-MON-YYYY'), 69550.79, 3, 10);
INSERT INTO sale VALUES (6, TO_DATE('28-Dec-2022', 'DD-MON-YYYY'), 81975.86, 7, 11);

COMMIT;