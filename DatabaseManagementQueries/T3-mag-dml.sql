/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T3-mag-dml.sql

--Student ID: 34269193
--Student Name: Robiatul Adawiyah Al-Qosh

/* Comments for your marker:

I assumed that I have to record the second transit status where the artwork arrived to the gallery form warehouse
14 days is included the assigned date, so display date is between 2-Jan-2023 and 15-Jan-2023
Since, in schema the start date of aw_display and date time in aw_status is unique, I particulary used dates for look up the value

*/


/*3(a)*/

DROP sequence aw_display_seq;
DROP sequence aw_status_seq;
DROP sequence sale_seq;

CREATE sequence aw_display_seq start with 100 increment by 10;
CREATE sequence aw_status_seq start with 100 increment by 10;
CREATE sequence sale_seq start with 100 increment by 10;


/*3(b)*/

-- Insert the artwork first
INSERT INTO artwork VALUES (
    1,
    (
        SELECT max(artwork_no) + 1
        FROM artwork
        WHERE artist_code = 1
    ),
    'Serpihan Kaca',
    25000,
    TO_DATE('30-Dec-2022', 'DD-MON-YYYY')
);

-- Then, insert the status to aw_status
INSERT INTO aw_status VALUES (
    aw_status_seq.nextval,
    1,
    (
        SELECT artwork_no
        FROM artwork
        WHERE upper(artwork_title) = upper('Serpihan Kaca')
        AND artist_code = 1
    ),
    TO_DATE('30-Dec-2022 11:00', 'DD-MON-YYYY HH24:MI'),
    'W',
    NULL
);


/*3(c)*/

-- Firstly, I recorded the status transit form the warehouse to the gallery
INSERT INTO aw_status VALUES (
    aw_status_seq.nextval,
    1,
    (
        SELECT artwork_no
        FROM artwork
        WHERE upper(artwork_title) = upper('Serpihan Kaca')
        AND artist_code = 1
    ),
    TO_DATE('1-Jan-2023 13:00', 'DD-MON-YYYY HH24:MI'),
    'T',
    (
        SELECT gallery_id
        FROM gallery
        WHERE gallery_phone = '0274556646'
    )
);

-- Secondly, I recorded the transit status that the artwork arrived to the gallery
INSERT INTO aw_status VALUES (
    aw_status_seq.nextval,
    1,
    (
        SELECT artwork_no
        FROM artwork
        WHERE upper(artwork_title) = upper('Serpihan Kaca')
        AND artist_code = 1
    ),
    TO_DATE('1-Jan-2023 15:30', 'DD-MON-YYYY HH24:MI'),
    'T',
    (
        SELECT gallery_id
        FROM gallery
        WHERE gallery_phone = '0274556646'
    )
);

-- Next, I inserted the artwork to the aw_display
INSERT INTO aw_display VALUES (
    aw_display_seq.nextval,
    1,
    (
        SELECT artwork_no
        FROM artwork
        WHERE upper(artwork_title) = upper('Serpihan Kaca')
        AND artist_code = 1
    ),
    TO_DATE('2-Jan-2023', 'DD-MON-YYYY'),
    TO_DATE('15-Jan-2023', 'DD-MON-YYYY'),
    (
        SELECT gallery_id
        FROM gallery
        WHERE gallery_phone = '0274556646'
    )
);

-- Then, I also recorded the status where the artwork being displayed in the gallery
INSERT INTO aw_status VALUES (
    aw_status_seq.nextval,
    1,
    (
        SELECT artwork_no
        FROM artwork
        WHERE upper(artwork_title) = upper('Serpihan Kaca')
        AND artist_code = 1
    ),
    TO_DATE('2-Jan-2023 10:00', 'DD-MON-YYYY HH24:MI'),
    'G',
    (
        SELECT gallery_id
        FROM gallery
        WHERE gallery_phone = '0274556646'
    )
);


/*3(d)*/

-- Insert the artwork sales activity into sale table
INSERT INTO sale VALUES (
    sale_seq.nextval,
    TO_DATE('4-Jan-2023', 'DD-MON-YYYY'),
    29499.99,
    (
        SELECT customer_id
        FROM customer
        WHERE customer_phone = '0815271315'
    ),
    (
        SELECT aw_display_id
        FROM aw_display
        WHERE aw_display_start_date = TO_DATE('2-Jan-2023', 'DD-MON-YYYY')
    )
);

-- Then, I recorded the status where the artwork sold
INSERT INTO aw_status VALUES (
    aw_status_seq.nextval,
    1,
    (
        SELECT artwork_no
        FROM artwork
        WHERE upper(artwork_title) = upper('Serpihan Kaca')
        AND artist_code = 1
    ),
    TO_DATE('4-Jan-2023 11:30', 'DD-MON-YYYY HH24:MI'),
    'S',
    (
        SELECT gallery_id
        FROM gallery
        WHERE gallery_phone = '0274556646'
    )
);

-- After that, i should update the end date of the artwork that already sold on aw_display
UPDATE aw_display
SET aw_display_end_date = TO_DATE('4-Jan-2023', 'DD-MON-YYYY')
WHERE aw_display_start_date = TO_DATE('2-Jan-2023', 'DD-MON-YYYY');


/*3(e)*/

-- Delete the transaction in sale table
DELETE FROM sale
WHERE customer_id = (
                    SELECT customer_id
                    FROM customer
                    WHERE customer_phone = '0815271315'
                    )
AND aw_display_id = (
                    SELECT aw_display_id
                    FROM aw_display
                    WHERE aw_display_start_date = TO_DATE('2-Jan-2023', 'DD-MON-YYYY')
                    );

-- Delete the sold status in aw_status table
DELETE FROM aw_status
WHERE aws_date_time = TO_DATE('4-Jan-2023 11:30', 'DD-MON-YYYY HH24:MI');

-- Update the aw_display end date for the artwork to the initial
UPDATE aw_display
SET aw_display_end_date = TO_DATE('15-Jan-2023', 'DD-MON-YYYY')
WHERE aw_display_start_date = TO_DATE('2-Jan-2023', 'DD-MON-YYYY');


COMMIT;