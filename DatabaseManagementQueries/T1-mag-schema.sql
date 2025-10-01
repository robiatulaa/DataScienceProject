--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T1-mag-schema.sql

--Student ID: 34269193
--Student Name: Robiatul Adawiyah Al-Qosh


/* Comments for your marker:

I already ensure to not put drop table in this schema.

*/

-- Task 1 Add Create table statements for the Missing TABLES below
-- Ensure all column comments, and constraints (other than FK's)
-- are included. FK constraints are to be added at the end of this script

-- AW_DISPLAY

CREATE TABLE aw_display (
    aw_display_id           NUMBER (6) NOT NULL,
    artist_code             NUMBER (4) NOT NULL,
    artwork_no              NUMBER (4) NOT NULL,
    aw_display_start_date   DATE NOT NULL,
    aw_display_end_date     DATE,
    gallery_id              NUMBER (3) NOT NULL
);

COMMENT ON COLUMN aw_display.aw_display_id IS
    'Identifier for aw_display';

COMMENT ON COLUMN aw_display.artist_code IS
    'Identifier for artist';

COMMENT ON COLUMN aw_display.artwork_no IS
    'Identifier for artwork within this artist';

COMMENT ON COLUMN aw_display.aw_display_start_date IS
    'Date this artwork display in the gallery began';

COMMENT ON COLUMN aw_display.aw_display_end_date IS
    'Date this artwork display in the gallery ends';

COMMENT ON COLUMN aw_display.gallery_id IS
    'Identifier for Gallery';

ALTER TABLE aw_display ADD CONSTRAINT aw_display_pk PRIMARY KEY (aw_display_id);

ALTER TABLE aw_display ADD CONSTRAINT aw_display_uq UNIQUE (artist_code, 
                                                            artwork_no, 
                                                            aw_display_start_date);


-- AW_STATUS

CREATE TABLE aw_status (
    aws_id                  NUMBER (6) NOT NULL,
    artist_code             NUMBER (4) NOT NULL,
    artwork_no              NUMBER (4) NOT NULL,
    aws_date_time           DATE NOT NULL,
    aws_status              CHAR (1) NOT NULL,
    gallery_id              NUMBER (3)
);

COMMENT ON COLUMN aw_status.aws_id IS
    'Identifier for aw_status';

COMMENT ON COLUMN aw_status.artist_code IS
    'Identifier for artist';

COMMENT ON COLUMN aw_status.artwork_no IS
    'Identifier for artwork within this artist';

COMMENT ON COLUMN aw_status.aws_date_time IS
    'Date and time of status change took place';

COMMENT ON COLUMN aw_status.aws_status IS
    'Artwork status
    W = in MAG storage at the MAG central warehouse
    T = in transit (being shipped to/from a gallery)
    G = located at a gallery on display
    S = sold, or
    R = returned to the artist';

COMMENT ON COLUMN aw_status.gallery_id IS
    'Identifier for Gallery';

ALTER TABLE aw_status ADD CONSTRAINT aw_status_pk PRIMARY KEY (aws_id);

ALTER TABLE aw_status ADD CONSTRAINT aw_status_uq UNIQUE (  artist_code, 
                                                            artwork_no, 
                                                            aws_date_time);

ALTER TABLE aw_status 
    ADD CONSTRAINT "aws_status" 
        CHECK (aws_status IN ('W','T', 'G', 'S', 'R'));


-- SALE

CREATE TABLE sale (
    sale_id                 NUMBER (5) NOT NULL,
    sale_date               DATE NOT NULL,
    sale_price              NUMBER (9,2) NOT NULL,
    customer_id             NUMBER (5) NOT NULL,
    aw_display_id           NUMBER (7) NOT NULL
);

COMMENT ON COLUMN sale.sale_id IS
    'Identifier for sale';

COMMENT ON COLUMN sale.sale_date IS
    'Date sale was closed';

COMMENT ON COLUMN sale.sale_price IS
    'Price customer paid for artwork';

COMMENT ON COLUMN sale.customer_id IS
    'Identifier for customer';

COMMENT ON COLUMN sale.aw_display_id IS
    'Identifier for aw_display';

ALTER TABLE sale ADD CONSTRAINT sale_pk PRIMARY KEY (sale_id);


-- Add all missing FK Constraints below here

ALTER TABLE aw_display 
    ADD CONSTRAINT artwork_aw_display FOREIGN KEY ( artist_code,
                                                    artwork_no)
        REFERENCES artwork (artist_code,
                            artwork_no);

ALTER TABLE aw_display 
    ADD CONSTRAINT gallery_aw_display FOREIGN KEY (gallery_id)
        REFERENCES gallery (gallery_id);

ALTER TABLE aw_status
    ADD CONSTRAINT artwork_aw_status FOREIGN KEY (  artist_code,
                                                    artwork_no)
        REFERENCES artwork (artist_code,
                            artwork_no);

ALTER TABLE aw_status 
    ADD CONSTRAINT gallery_aw_status FOREIGN KEY (gallery_id)
        REFERENCES gallery (gallery_id);

ALTER TABLE sale 
    ADD CONSTRAINT customer_sale FOREIGN KEY (customer_id)
        REFERENCES customer (customer_id);

ALTER TABLE sale 
    ADD CONSTRAINT aw_display_sale FOREIGN KEY (aw_display_id)
        REFERENCES aw_display (aw_display_id);


COMMIT;