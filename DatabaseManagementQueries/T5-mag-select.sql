/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T5-mag-select.sql

--Student ID: 34269193
--Student Name: Robiatul Adawiyah Al-Qosh


/* Comments for your marker:

For 5a -->  I assumed that i have to fulfill both categories (not supplied phone number and not in 31, 34, or 36 region)
For 5c -->  I also assumed that 2 requirements (60 days after submit date and were never sent to galleries) have to be satisfied.
            Moreover, I recognized that I do not really understand about right align, I used RPAD function to represent that.

*/


/* (a) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT a.artist_code,
    TRIM (a.artist_gname || ' ' || a.artist_fname) as full_name,
    TRIM (a.artist_street || ', ' || a.artist_city || ', ' || r.p_name) as artist_address
FROM artist a
JOIN region r ON a.p_region_code = r.p_region_code
WHERE a.artist_phone IS NULL
    AND a.p_region_code NOT IN ('31', '34', '36')
ORDER BY a.artist_code ASC;


/* (b) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT j.artist_code, j.artwork_no, j.artwork_title, s.sale_date, '$'||to_char(s.sale_price, '999999999.99') as sale_price
FROM    (
        SELECT d.aw_display_id, d.artist_code, d.artwork_no, a.artwork_title, d.gallery_id
        FROM aw_display d
        JOIN artwork a ON d.artist_code = a.artist_code AND d.artwork_no = a.artwork_no
        ORDER BY d.aw_display_id
        ) j
JOIN sale s ON j.aw_display_id = s.aw_display_id
WHERE s.customer_id =   (
                        SELECT customer_id
                        FROM customer
                        WHERE LOWER(TRIM(customer_gname || ' ' || customer_fname)) = LOWER('Sri Susanti')
                        )
    AND j.gallery_id =  (
                        SElECT gallery_id
                        FROM gallery
                        WHERE gallery_phone = '0817407587'
                        )
ORDER BY s.sale_price DESC, j.artist_code, j.artwork_no ASC;


/* (c) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT j.artist_code, j.artist_fullname, j.artwork_no, j.artwork_title, 
    RPAD('$'||to_char(j.artwork_minprice, '999,999,999.99'), 16) as artist_minpayment,
    FLOOR(l.artwork_returndate - j.artwork_submitdate) as number_of_days
FROM    (
        SELECT a.artist_code, TRIM(a.artist_gname || ' ' || a.artist_fname) as artist_fullname,
            w.artwork_no, w.artwork_title, w.artwork_minprice, w.artwork_submitdate
        FROM artist a
        JOIN artwork w ON a.artist_code = w.artist_code
        ) j
JOIN    (
        SELECT s.artist_code, s.artwork_no, s.aws_date_time as artwork_returndate
        FROM aw_status s
        LEFT JOIN aw_display d ON s.artist_code = d.artist_code AND s.artwork_no = d.artwork_no
        WHERE d.artist_code IS NULL AND d.artwork_no IS NULL AND s.aws_status = 'R'
        ) l
    ON j.artist_code = l.artist_code AND j.artwork_no = l.artwork_no
WHERE FLOOR(l.artwork_returndate - j.artwork_submitdate) > 60
ORDER BY j.artist_code ASC, number_of_days DESC;


/* (d) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT z.artist_code, z.artist_fullname, z.artwork_title, z.gallery_name, 
    '$'||to_char(z.min_price, '999,999,999.99') as estimated_minprice,
    '$'||to_char(s.sale_price, '999,999,999.99') as sale_price,
    ROUND((s.sale_price - z.min_price)/s.sale_price*100, 1) || '%' as benefit_percent
FROM sale s
JOIN    (
        SELECT y.aw_display_id, x.artist_code, x.artist_fullname, x.artwork_title,
            y.gallery_name, x.artwork_minprice, y.commision,
            x.artwork_minprice*(100/(100 - y.commision)) as min_price
        FROM    (
                SELECT d.aw_display_id, d.artist_code, d.artwork_no, d.gallery_id,
                    g.gallery_name, (20 + g.gallery_sale_percent) as commision
                FROM aw_display d
                JOIN gallery g ON d.gallery_id = g.gallery_id
                ) y
        JOIN    (
                SELECT a.artist_code, TRIM(a.artist_gname || ' ' || a.artist_fname) as artist_fullname,
                    w.artwork_no, w.artwork_title, w.artwork_minprice
                FROM artist a
                JOIN artwork w ON a.artist_code = w.artist_code
                ) x
            ON y.artist_code = x.artist_code AND y.artwork_no = x.artwork_no
        ) z
    ON s.aw_display_id = z.aw_display_id
ORDER BY benefit_percent ASC;


/* (e) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT gallery_id, gallery_name, total_mag_commision,
    CASE
        WHEN percentage_of_revenue = MAX(percentage_of_revenue) OVER()
            THEN to_char(percentage_of_revenue, '990.00') || '% - Most profitable'
        WHEN percentage_of_revenue = MIN(percentage_of_revenue) OVER()
            THEN to_char(percentage_of_revenue, '990.00') || '% - Least profitable'
        ELSE to_char(percentage_of_revenue, '990.00') || '%'
    END AS percentage_of_revenue
FROM    (
        SELECT gallery_id, gallery_name,
            RPAD('$'||to_char(total_mag_commision, '999,999,990.00'), 16) as total_mag_commision,
            100 * total_mag_commision / SUM(total_mag_commision) OVER() as percentage_of_revenue
        FROM    (
                SELECT g.gallery_id, g.gallery_name,
                    COALESCE(SUM(j.mag_commision),0) as total_mag_commision
                FROM gallery g
                LEFT JOIN   (
                            SELECT d.gallery_id, (s.sale_price * 20/100) as mag_commision
                            FROM aw_display d
                            JOIN sale s ON d.aw_display_id = s.aw_display_id
                            ) j
                    ON g.gallery_id = j.gallery_id
                GROUP BY g.gallery_id, g.gallery_name
                )
        )
ORDER BY percentage_of_revenue DESC, gallery_id ASC;