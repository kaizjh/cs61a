CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

CREATE TABLE by_parent_height AS
  SELECT a.child
  FROM parents as a, dogs as b
  WHERE a.parent = b.name
  ORDER BY b.height DESC;

CREATE TABLE size_of_dogs AS
  SELECT name, size
  FROM dogs, sizes
  WHERE height <= max AND height > min;

CREATE TABLE sentences AS
  SELECT "The two siblings, " || a.child || " and " || b.child || ", have the same size: " || c.size
  FROM parents as a, parents as b, size_of_dogs as c, size_of_dogs as d
  WHERE a.child <> b.child AND a.parent = b.parent AND a.child = c.name AND b.child = d.name AND c.size = d.size;

CREATE TABLE low_variance AS
  SELECT fur, MAX(height) - MIN(height) as height FROM dogs GROUP BY fur
  HAVING MAX(height) <= 1.3 * AVG(height) AND MIN(height) >= 0.7 * AVG(height);
