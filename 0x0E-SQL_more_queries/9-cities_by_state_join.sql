-- Lists cities in the database hbtn_0d_usa
-- Records are sorted in ascending order of cities.id
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
