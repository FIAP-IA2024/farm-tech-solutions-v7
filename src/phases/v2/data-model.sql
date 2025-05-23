-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'Sensor'
-- 
-- ---

DROP TABLE IF EXISTS `Sensor`;
		
CREATE TABLE `Sensor` (
  `sensor_id` INT NOT NULL AUTO_INCREMENT DEFAULT NULL,
  `sensor_type` VARCHAR(50) NOT NULL DEFAULT 'NULL',
  PRIMARY KEY (`sensor_id`)
);

-- ---
-- Table 'Sensor_Reading'
-- 
-- ---

DROP TABLE IF EXISTS `Sensor_Reading`;
		
CREATE TABLE `Sensor_Reading` (
  `reading_id` INT NOT NULL AUTO_INCREMENT DEFAULT NULL,
  `sensor_id` INT NOT NULL DEFAULT NULL,
  `crop_id` INT NOT NULL DEFAULT NULL,
  `location_id` INT NOT NULL DEFAULT NULL,
  `timestamp` DATETIME NOT NULL DEFAULT 'NULL',
  `moisture_value` DOUBLE NULL DEFAULT NULL,
  `ph_value` DOUBLE NULL DEFAULT NULL,
  `phosphorus_value` DOUBLE NULL DEFAULT NULL,
  `potassium_value` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`reading_id`)
);

-- ---
-- Table 'Application'
-- 
-- ---

DROP TABLE IF EXISTS `Application`;
		
CREATE TABLE `Application` (
  `application_id` INT NOT NULL AUTO_INCREMENT DEFAULT NULL,
  `crop_id` INT NOT NULL DEFAULT NULL,
  `timestamp` TIMESTAMP NOT NULL DEFAULT 'NULL',
  `water_amount` DOUBLE NULL DEFAULT NULL,
  `phosphorus_amount` DOUBLE NULL DEFAULT NULL,
  `potassium_amount` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`application_id`)
);

-- ---
-- Table 'Crop'
-- 
-- ---

DROP TABLE IF EXISTS `Crop`;
		
CREATE TABLE `Crop` (
  `crop_id` INT NOT NULL AUTO_INCREMENT DEFAULT NULL,
  `crop_name` VARCHAR(100) NOT NULL DEFAULT 'NULL',
  `planting_date` DATETIME NOT NULL DEFAULT 'NULL',
  PRIMARY KEY (`crop_id`)
);

-- ---
-- Table 'Location'
-- 
-- ---

DROP TABLE IF EXISTS `Location`;
		
CREATE TABLE `Location` (
  `location_id` INT NOT NULL AUTO_INCREMENT DEFAULT NULL,
  `location_name` VARCHAR(100) NOT NULL DEFAULT 'NULL',
  `coordinates` VARCHAR(100) NOT NULL DEFAULT 'NULL',
  PRIMARY KEY (`location_id`)
);

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `Sensor_Reading` ADD FOREIGN KEY (sensor_id) REFERENCES `Sensor` (`sensor_id`);
ALTER TABLE `Sensor_Reading` ADD FOREIGN KEY (crop_id) REFERENCES `Crop` (`crop_id`);
ALTER TABLE `Sensor_Reading` ADD FOREIGN KEY (location_id) REFERENCES `Location` (`location_id`);
ALTER TABLE `Application` ADD FOREIGN KEY (crop_id) REFERENCES `Crop` (`crop_id`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `Sensor` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Sensor_Reading` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Application` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Crop` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Location` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `Sensor` (`sensor_id`,`sensor_type`) VALUES
-- ('','');
-- INSERT INTO `Sensor_Reading` (`reading_id`,`sensor_id`,`crop_id`,`location_id`,`timestamp`,`moisture_value`,`ph_value`,`phosphorus_value`,`potassium_value`) VALUES
-- ('','','','','','','','','');
-- INSERT INTO `Application` (`application_id`,`crop_id`,`timestamp`,`water_amount`,`phosphorus_amount`,`potassium_amount`) VALUES
-- ('','','','','','');
-- INSERT INTO `Crop` (`crop_id`,`crop_name`,`planting_date`) VALUES
-- ('','','');
-- INSERT INTO `Location` (`location_id`,`location_name`,`coordinates`) VALUES
-- ('','','');