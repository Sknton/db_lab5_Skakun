-- loop.sql
DO $$
DECLARE
  counter INT := 6;
BEGIN
  WHILE counter <= 8 LOOP
    INSERT INTO artist (pseudonym, artist_id)
    VALUES ('Artist ' || counter, counter);
    counter := counter + 1;
  END LOOP;
END $$;
