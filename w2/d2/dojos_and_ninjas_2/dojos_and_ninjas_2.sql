SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id
WHERE ninjas.id=(SELECT max(id) FROM ninjas);


