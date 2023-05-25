-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: rv_rentals_schema
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `listings`
--

DROP TABLE IF EXISTS `listings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` text,
  `rate` int DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `availability` datetime DEFAULT NULL,
  `add_photos` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_listings_users_idx` (`user_id`),
  CONSTRAINT `fk_listings_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listings`
--

LOCK TABLES `listings` WRITE;
/*!40000 ALTER TABLE `listings` DISABLE KEYS */;
INSERT INTO `listings` VALUES (5,2,'Testing photos','testing photos',234,'minnesota','2023-05-19 00:00:00','[\"camper_layout-1.jpg\", \"camper_layout-2.jpg\"]','2023-05-19 13:56:14','2023-05-19 13:56:14'),(14,3,'Rileys second kitty camper','testing again',1234,'Minnesota','2023-05-27 00:00:00','[\"c91445b1695243baabe98e776e41fa96.jpg\"]','2023-05-22 10:45:45','2023-05-22 10:45:45'),(24,3,'Rileys Camper','Take a day off and enjoy yourself in this camper',50,'Minnesota','2023-05-22 00:00:00','[\"8c8f71bc9e0a45cca3c5a1faae4566fd.png\", \"1344a7e960c5445a861e59b477c49a38.png\", \"4751a57e7d9043499de85ff9acb7dffa.png\", \"19d63b8abe6d415b91aaec51404bef82.png\"]','2023-05-22 14:21:16','2023-05-22 14:21:16'),(25,1,'The Getaway Testing Edit-2','Spend a couple nights in this brand new camper without the montly payments!',180,'Minnesota','2023-05-27 00:00:00','[\"a6316ff28be645188c18f662a0a75022.webp\", \"4dc84173af074e36926c13bb6263ece0.jpg\", \"de37890701644f55a172db72394d4ea6.png\", \"1887c706ce484c7cb6ad2cf8a73cad7c.jpg\", \"86098e4e1e9c485db1958935646b66a9.jpg\"]','2023-05-22 17:04:56','2023-05-25 11:00:39'),(26,1,'Home Away From Home','Come enjoy a few nights stay where ever you would like to go! Will drop off wherever within 50 miles of pickup. ',150,'Rice, Minnesota','2023-05-24 00:00:00','[\"10e5beb528d84161a665981495daf4b5.png\"]','2023-05-24 08:38:02','2023-05-24 08:38:02');
/*!40000 ALTER TABLE `listings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-25 12:42:10
