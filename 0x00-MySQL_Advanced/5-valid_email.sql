-- Creates a trigger that resets the attribute valid_email only when
-- the email has been changed.
-- Nothing related to MySQL, but perfect for user email validation -
-- distribute the logic to the database itself!
DROP TRIGGER IF EXISTS reset_valid_email;
DELIMITER $$
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END $$
DELIMITER ;
