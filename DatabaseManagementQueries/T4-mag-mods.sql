/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T4-mag-mods.sql

--Student ID: 34269193
--Student Name: Robiatul Adawiyah Al-Qosh


/* Comments for your marker:

I assume that i might create a new table for this task, since i don't want to change previous schema

*/


/*4(a)*/

-- Creating table that will record the number of artworks which had by each artist
DROP TABLE total_artworks CASCADE CONSTRAINTS;
CREATE TABLE total_artworks (
    artist_code             NUMBER (4) NOT NULL,
    num_of_artworks         NUMBER (4)
);

COMMENT ON COLUMN total_artworks.artist_code IS
    'Identifier for artist';

COMMENT ON COLUMN total_artworks.num_of_artworks IS
    'Total number of artworks that artist submitted';

ALTER TABLE total_artworks ADD CONSTRAINT total_artworks_pk PRIMARY KEY (artist_code);

-- Assumed that this table had relation with artist table, then artist_code becoming FK
ALTER TABLE total_artworks 
    ADD CONSTRAINT artist_total_artworks FOREIGN KEY (artist_code)
        REFERENCES artist (artist_code);

-- Inserted artist_code and num_of_artworks (I count the artworks in artwork table minus the returned art in aw_status)
INSERT INTO total_artworks (artist_code, num_of_artworks)
SELECT a.artist_code, 
    COUNT(DISTINCT a.artwork_no) - COUNT(CASE WHEN b.aws_status = 'R' THEN 1 END) as num_of_artworks
FROM artwork a
JOIN aw_status b ON a.artist_code = b.artist_code
GROUP BY a.artist_code
ORDER BY a.artist_code;


/*4(b)*/

-- Creating table that will record the number of artworks which purchased by each customer per artist
DROP TABLE customer_purchase CASCADE CONSTRAINTS;
CREATE TABLE customer_purchase (
    customer_id             NUMBER (5) NOT NULL,
    artist_code             NUMBER (4) NOT NULL,
    num_of_purchases        NUMBER (4)
);

COMMENT ON COLUMN customer_purchase.customer_id IS
    'Identifier for customer';

COMMENT ON COLUMN customer_purchase.artist_code IS
    'Identifier for artist';

COMMENT ON COLUMN customer_purchase.num_of_purchases IS
    'Total number of artworks that customer purchased';

ALTER TABLE customer_purchase ADD CONSTRAINT customer_purchase_pk PRIMARY KEY ( customer_id,
                                                                                artist_code);

-- Assumed that this table had relation with customer and artist table, then customer_id and artist_code becoming FK
ALTER TABLE customer_purchase 
    ADD CONSTRAINT customer_customer_purchase FOREIGN KEY (customer_id)
        REFERENCES customer (customer_id);

ALTER TABLE customer_purchase 
    ADD CONSTRAINT artist_customer_purchase FOREIGN KEY (artist_code)
        REFERENCES artist (artist_code);

-- Inserted contents in this table from sale and aw_display values
INSERT INTO customer_purchase (customer_id, artist_code, num_of_purchases)
SELECT a.customer_id, b.artist_code, COUNT(a.aw_display_id) as num_of_purchases
FROM sale a
JOIN aw_display b ON a.aw_display_id = b.aw_display_id
GROUP BY a.customer_id, b.artist_code
ORDER BY a.customer_id, b.artist_code;


COMMIT;