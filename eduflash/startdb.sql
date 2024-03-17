DROP DATABASE IF EXISTS eduflash;

CREATE DATABASE eduflash;
CREATE USER 'edu_dev'@'localhost' IDENTIFIED BY 'edu_pass';
GRANT ALL ON eduflash.* TO 'edu_dev'@'localhost';
FLUSH PRIVILEGES;
USE eduflash;

/*DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`(
    `id` VARCHAR(60) NOT NULL,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `email` VARCHAR(50) NOT NULL,
    `password` VARCHAR(50) NOT NULL,
    `first_name` VARCHAR(50) NOT NULL,
    `last_name` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `resources`;
CREATE TABLE `resources`(
    `id` VARCHAR(60) NOT NULL,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL,
    `name` VARCHAR(100),
    `user_id` VARCHAR(60),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

DROP TABLE IF EXISTS `flashcards`;
CREATE TABLE `users`(
    `id` VARCHAR(60) NOT NULL,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL,
    `question` VARCHAR(1000),
    `answer` VARCHAR(5000),
    `resource_id` VARCHAR(60),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`resource_id`) REFERENCES `resources`(`id`)
);
*/