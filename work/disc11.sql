CREATE TABLE pizzas AS
  SELECT "Artichoke" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"         , 11        , 22          UNION
  SELECT "Sliver"           , 11        , 20          UNION
  SELECT "Cheeseboard"      , 16        , 23          UNION
  SELECT "Emilia's"         , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;

CREATE TABLE opening AS
  SELECT name 
  FROM pizzas
  WHERE open < 13
  ORDER BY name DESC;

CREATE TABLE study AS
  SELECT a.name AS name,MAX(14-a.open, 0) AS duration
  FROM pizzas AS a
  ORDER BY duration DESC;

CREATE TABLE late AS
  SELECT name || " closes at " || close AS status
  FROM pizzas, meals
  WHERE meal = "snack" AND time <= close;

CREATE TABLE double AS
  SELECT a.meal as first, b.meal as second, name
  FROM meals as a, meals as b, pizzas as c
  WHERE b.time - a.time > 6 AND c.open <= a.time AND c.close >= b.time