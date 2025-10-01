/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T6-mag-json.sql

--Student ID: 34269193
--Student Name: Robiatul Adawiyah Al-Qosh


/* Comments for your marker:

I had a problem with ordering the artwork_no. 
I thought it will ordered automatically since the initial table was ordered, but, it did not.
And regarding the brief did not mention about oredering requirement in artwork_no, so I left the result as it was.

*/


-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer


SET PAGESIZE 200

SELECT
    JSON_OBJECT ( '_id' VALUE artist_code, 'name' VALUE artist_gname
                || ' '
                || artist_fname, 
                'address' VALUE JSON_OBJECT ( 
                    'street' VALUE artist_street, 
                    'city'   VALUE artist_city, 
                    'region' VALUE p_name 
                    ), 
                'phone' VALUE artist_phone,
                'no_of_artworks' VALUE COUNT(artwork_no),
                'artworks' VALUE JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'no' VALUE artwork_no, 
                        'title' VALUE artwork_title, 
                        'minimum_price' VALUE artwork_minprice
                        )
                    ) FORMAT JSON )
    || ','
FROM
    artist
    NATURAL JOIN region
    NATURAL JOIN artwork
GROUP BY
    artist_code,
    artist_gname,
    artist_fname,
    artist_street,
    artist_city,
    p_name,
    artist_phone
ORDER BY
    artist_code;