CREATE TABLE IF NOT EXISTS topic_messages_1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message_key VARCHAR(255),
    message_value TEXT,
    `partition` INT,
    `offset` INT
);

CREATE TABLE IF NOT EXISTS topic_messages_2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message_key VARCHAR(255),
    message_value TEXT,
    `partition` INT,
    `offset` INT
);

CREATE TABLE IF NOT EXISTS topic_messages_3 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message_key VARCHAR(255),
    message_value TEXT,
    `partition` INT,
    `offset` INT
);
