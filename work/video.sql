create table ints as
    select "zero" as word , 0 as one, 0 as two, 0 as four, 0 as eight union
    select "one"          , 1       , 0        , 0        , 0         union
    select "two"          , 0       , 2        , 0        , 0         union
    select "three"        , 1       , 2        , 0        , 0         union
    select "four"         , 0       , 0        , 4        , 0         union
    select "five"         , 1       , 0        , 4        , 0         union
    select "six"          , 0       , 2        , 4        , 0         union
    select "seven"        , 1       , 2        , 4        , 0         union
    select "eight"        , 0       , 0        , 0        , 8         union
    select "nine"         , 1       , 0        , 0        , 8;





-- We get nothing for now, because we just create a empty table
CREATE TABLE primes (n UNIQUE, prime DEFAULT 1);


-- Add (insert) something into the table
INSERT INTO primes VALUES (2, 3), (3, 2);
/*SELECT * FROM primes;
2|3
3|2
*/
-- We insert into only n (column) here, and prime will get default number
INSERT INTO primes(n) VALUES (4), (5), (6);
/*SELECT * FROM primes;
2|3
3|2
4|1
5|1
6|1
*/
-- We can do more
INSERT INTO primes(n) SELECT n+6 FROM primes;
/*SELECT * FROM primes;
2|3
3|2
4|1
5|1
6|1
8|1
9|1
10|1
11|1
12|1
*/

-- Modify the data in the table
UPDATE primes SET prime=0 WHERE n>2 AND n%2=0;
UPDATE primes SET prime=0 WHERE n>2 AND n%3=0;
UPDATE primes SET prime=0 WHERE n>2 AND n%5=0;
/*SELECT * FROM primes;
2|3
3|0
4|0
5|0
6|0
8|0
9|0
10|0
11|1
12|0
*/

-- Finally we get a real prime table
DELETE FROM primes WHERE prime = 0;
/*SELECT * FROM primes;
2|3
11|1
*/

-- So, sometimes it's easier to build a table not just all in one go, but by manipulating the values after constructing it initially.
-- 阿忒修斯之船