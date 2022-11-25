-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: vicjosh.mysql.pythonanywhere-services.com    Database: vicjosh$default
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add banco',7,'add_banco'),(26,'Can change banco',7,'change_banco'),(27,'Can delete banco',7,'delete_banco'),(28,'Can view banco',7,'view_banco'),(29,'Can add civil',8,'add_civil'),(30,'Can change civil',8,'change_civil'),(31,'Can delete civil',8,'delete_civil'),(32,'Can view civil',8,'view_civil'),(33,'Can add contrato',9,'add_contrato'),(34,'Can change contrato',9,'change_contrato'),(35,'Can delete contrato',9,'delete_contrato'),(36,'Can view contrato',9,'view_contrato'),(37,'Can add costo',10,'add_costo'),(38,'Can change costo',10,'change_costo'),(39,'Can delete costo',10,'delete_costo'),(40,'Can view costo',10,'view_costo'),(41,'Can add datos bancarios',11,'add_datosbancarios'),(42,'Can change datos bancarios',11,'change_datosbancarios'),(43,'Can delete datos bancarios',11,'delete_datosbancarios'),(44,'Can view datos bancarios',11,'view_datosbancarios'),(45,'Can add datos isr',12,'add_datosisr'),(46,'Can change datos isr',12,'change_datosisr'),(47,'Can delete datos isr',12,'delete_datosisr'),(48,'Can view datos isr',12,'view_datosisr'),(49,'Can add distrito',13,'add_distrito'),(50,'Can change distrito',13,'change_distrito'),(51,'Can delete distrito',13,'delete_distrito'),(52,'Can view distrito',13,'view_distrito'),(53,'Can add empleados_ batch',14,'add_empleados_batch'),(54,'Can change empleados_ batch',14,'change_empleados_batch'),(55,'Can delete empleados_ batch',14,'delete_empleados_batch'),(56,'Can view empleados_ batch',14,'view_empleados_batch'),(57,'Can add empresa',15,'add_empresa'),(58,'Can change empresa',15,'change_empresa'),(59,'Can delete empresa',15,'delete_empresa'),(60,'Can view empresa',15,'view_empresa'),(61,'Can add nivel',16,'add_nivel'),(62,'Can change nivel',16,'change_nivel'),(63,'Can delete nivel',16,'delete_nivel'),(64,'Can view nivel',16,'view_nivel'),(65,'Can add perfil',17,'add_perfil'),(66,'Can change perfil',17,'change_perfil'),(67,'Can delete perfil',17,'delete_perfil'),(68,'Can view perfil',17,'view_perfil'),(69,'Can add proyecto',18,'add_proyecto'),(70,'Can change proyecto',18,'change_proyecto'),(71,'Can delete proyecto',18,'delete_proyecto'),(72,'Can view proyecto',18,'view_proyecto'),(73,'Can add puesto',19,'add_puesto'),(74,'Can change puesto',19,'change_puesto'),(75,'Can delete puesto',19,'delete_puesto'),(76,'Can view puesto',19,'view_puesto'),(77,'Can add registro patronal',20,'add_registropatronal'),(78,'Can change registro patronal',20,'change_registropatronal'),(79,'Can delete registro patronal',20,'delete_registropatronal'),(80,'Can view registro patronal',20,'view_registropatronal'),(81,'Can add ropa',21,'add_ropa'),(82,'Can change ropa',21,'change_ropa'),(83,'Can delete ropa',21,'delete_ropa'),(84,'Can view ropa',21,'view_ropa'),(85,'Can add sangre',22,'add_sangre'),(86,'Can change sangre',22,'change_sangre'),(87,'Can delete sangre',22,'delete_sangre'),(88,'Can view sangre',22,'view_sangre'),(89,'Can add sexo',23,'add_sexo'),(90,'Can change sexo',23,'change_sexo'),(91,'Can delete sexo',23,'delete_sexo'),(92,'Can view sexo',23,'view_sexo'),(93,'Can add status',24,'add_status'),(94,'Can change status',24,'change_status'),(95,'Can delete status',24,'delete_status'),(96,'Can view status',24,'view_status'),(97,'Can add status_ batch',25,'add_status_batch'),(98,'Can change status_ batch',25,'change_status_batch'),(99,'Can delete status_ batch',25,'delete_status_batch'),(100,'Can view status_ batch',25,'view_status_batch'),(101,'Can add sub proyecto',26,'add_subproyecto'),(102,'Can change sub proyecto',26,'change_subproyecto'),(103,'Can delete sub proyecto',26,'delete_subproyecto'),(104,'Can view sub proyecto',26,'view_subproyecto'),(105,'Can add tabla vacaciones',27,'add_tablavacaciones'),(106,'Can change tabla vacaciones',27,'change_tablavacaciones'),(107,'Can delete tabla vacaciones',27,'delete_tablavacaciones'),(108,'Can view tabla vacaciones',27,'view_tablavacaciones'),(109,'Can add tallas',28,'add_tallas'),(110,'Can change tallas',28,'change_tallas'),(111,'Can delete tallas',28,'delete_tallas'),(112,'Can view tallas',28,'view_tallas'),(113,'Can add vacaciones',29,'add_vacaciones'),(114,'Can change vacaciones',29,'change_vacaciones'),(115,'Can delete vacaciones',29,'delete_vacaciones'),(116,'Can view vacaciones',29,'view_vacaciones'),(117,'Can add user datos',30,'add_userdatos'),(118,'Can change user datos',30,'change_userdatos'),(119,'Can delete user datos',30,'delete_userdatos'),(120,'Can view user datos',30,'view_userdatos'),(121,'Can add uniformes',31,'add_uniformes'),(122,'Can change uniformes',31,'change_uniformes'),(123,'Can delete uniformes',31,'delete_uniformes'),(124,'Can view uniformes',31,'view_uniformes'),(125,'Can add uniforme',32,'add_uniforme'),(126,'Can change uniforme',32,'change_uniforme'),(127,'Can delete uniforme',32,'delete_uniforme'),(128,'Can view uniforme',32,'view_uniforme'),(129,'Can add historical vacaciones',33,'add_historicalvacaciones'),(130,'Can change historical vacaciones',33,'change_historicalvacaciones'),(131,'Can delete historical vacaciones',33,'delete_historicalvacaciones'),(132,'Can view historical vacaciones',33,'view_historicalvacaciones'),(133,'Can add historical uniformes',34,'add_historicaluniformes'),(134,'Can change historical uniformes',34,'change_historicaluniformes'),(135,'Can delete historical uniformes',34,'delete_historicaluniformes'),(136,'Can view historical uniformes',34,'view_historicaluniformes'),(137,'Can add historical economicos',35,'add_historicaleconomicos'),(138,'Can change historical economicos',35,'change_historicaleconomicos'),(139,'Can delete historical economicos',35,'delete_historicaleconomicos'),(140,'Can view historical economicos',35,'view_historicaleconomicos'),(141,'Can add historical costo',36,'add_historicalcosto'),(142,'Can change historical costo',36,'change_historicalcosto'),(143,'Can delete historical costo',36,'delete_historicalcosto'),(144,'Can view historical costo',36,'view_historicalcosto'),(145,'Can add historical bonos',37,'add_historicalbonos'),(146,'Can change historical bonos',37,'change_historicalbonos'),(147,'Can delete historical bonos',37,'delete_historicalbonos'),(148,'Can view historical bonos',37,'view_historicalbonos'),(149,'Can add economicos',38,'add_economicos'),(150,'Can change economicos',38,'change_economicos'),(151,'Can delete economicos',38,'delete_economicos'),(152,'Can view economicos',38,'view_economicos'),(153,'Can add catorcenas',39,'add_catorcenas'),(154,'Can change catorcenas',39,'change_catorcenas'),(155,'Can delete catorcenas',39,'delete_catorcenas'),(156,'Can view catorcenas',39,'view_catorcenas'),(157,'Can add bonos',40,'add_bonos'),(158,'Can change bonos',40,'change_bonos'),(159,'Can delete bonos',40,'delete_bonos'),(160,'Can view bonos',40,'view_bonos');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$btvhXAd88JmyBNLwOtbGei$GvO5PIyQvKL7L4eC122P1wxwQPrItzzpi5/tCNu3NMI=','2022-09-13 02:16:12.720362',1,'vicjosh','','','victorjosh02@hotmail.com',1,1,'2022-08-17 18:43:25.392000'),(2,'pbkdf2_sha256$320000$FbuUWUcLH7fmvyZWWnKMs2$WtRl6v250J2K1T4087M+2x5A0iud51cJJoww5xf0Nr4=','2022-09-13 02:29:57.856651',0,'Fidel_Matriz','','','',0,1,'2022-08-17 18:53:29.677000'),(3,'pbkdf2_sha256$320000$EZhNZ0Ltxhp14Bk8ib1BxZ$5WrLA5Ejp56qSqiWlwIclbmd6WLJOQ7Gtn+/8/kN+mE=',NULL,0,'Jesus_Matriz','','','',0,1,'2022-08-17 18:53:56.278000'),(4,'pbkdf2_sha256$320000$yxAkM5gqTEfvLNygYGoHDy$HiNYyp42eo2ARe+1AMePyeiAeC/6m+lq//6hLTRIa0U=','2022-09-11 21:45:13.530000',0,'Usuario_Distrito','','','',0,1,'2022-08-17 18:54:13.251000'),(5,'pbkdf2_sha256$320000$EPPoGsq9IMIMSijA2AFc4z$b4MGiefLQLSKwuslWs4Tt6zhrgo/Pp4cBpoG/zY00+w=','2022-08-18 22:54:33.598000',0,'Usuario_Distrito2','','','',0,1,'2022-08-17 18:54:31.940000'),(6,'pbkdf2_sha256$320000$DmVogSkw00xRqEXvl3pJPj$IOgBPGBfa9BAxrG+imF8PUQfLFXobVgmevpCAygf9Pw=','2022-09-13 23:24:12.325704',1,'ulises_huesca','','','ulises_huesc@hotmail.com',1,1,'2022-09-08 23:38:30.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=203 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-09-13 02:17:05.184869','1','Matriz',1,'[{\"added\": {}}]',13,1),(2,'2022-09-13 02:18:10.364586','2','Altamira',1,'[{\"added\": {}}]',13,1),(3,'2022-09-13 02:18:34.070664','3','Planta Veracruz',1,'[{\"added\": {}}]',13,1),(4,'2022-09-13 02:18:40.865518','4','Poza Rica',1,'[{\"added\": {}}]',13,1),(5,'2022-09-13 02:18:50.283593','5','Villahermosa',1,'[{\"added\": {}}]',13,1),(6,'2022-09-13 02:18:56.866019','6','Veracruz',1,'[{\"added\": {}}]',13,1),(7,'2022-09-13 02:19:22.240860','1','vicjosh, distrito: Matriz ',1,'[{\"added\": {}}]',30,1),(8,'2022-09-13 02:19:32.031464','2','ulises_huesca, distrito: Matriz ',1,'[{\"added\": {}}]',30,1),(9,'2022-09-13 02:19:43.268879','3','Fidel_Matriz, distrito: Matriz ',1,'[{\"added\": {}}]',30,1),(10,'2022-09-13 02:19:48.517925','4','Jesus_Matriz, distrito: Matriz ',1,'[{\"added\": {}}]',30,1),(11,'2022-09-13 02:20:18.464680','5','Usuario_Distrito, distrito: Altamira ',1,'[{\"added\": {}}]',30,1),(12,'2022-09-13 02:20:25.230954','6','Usuario_Distrito2, distrito: Planta Veracruz ',1,'[{\"added\": {}}]',30,1),(13,'2022-09-13 16:46:23.115520','1','Femenino',1,'[{\"added\": {}}]',23,6),(14,'2022-09-13 16:46:43.387685','2','Masculino',1,'[{\"added\": {}}]',23,6),(15,'2022-09-13 18:04:24.698260','1','Santander',1,'[{\"added\": {}}]',7,1),(16,'2022-09-13 18:04:29.353630','2','BBVA',1,'[{\"added\": {}}]',7,1),(17,'2022-09-13 18:04:34.067019','3','HSBC',1,'[{\"added\": {}}]',7,1),(18,'2022-09-13 18:04:41.703859','4','Banorte',1,'[{\"added\": {}}]',7,1),(19,'2022-09-13 18:04:46.915056','5','Banamex',1,'[{\"added\": {}}]',7,1),(20,'2022-09-13 18:04:51.602805','6','Scotiabank',1,'[{\"added\": {}}]',7,1),(21,'2022-09-13 18:05:07.025271','1','Soltero',1,'[{\"added\": {}}]',8,1),(22,'2022-09-13 18:05:11.853278','2','Casado',1,'[{\"added\": {}}]',8,1),(23,'2022-09-13 18:05:24.043464','1','Planta',1,'[{\"added\": {}}]',9,1),(24,'2022-09-13 18:05:28.943197','2','Eventual',1,'[{\"added\": {}}]',9,1),(25,'2022-09-13 18:06:02.717048','1','VORDCAB',1,'[{\"added\": {}}]',15,1),(26,'2022-09-13 18:06:10.530696','2','VORDTEC',1,'[{\"added\": {}}]',15,1),(27,'2022-09-13 18:06:27.938183','1','1',1,'[{\"added\": {}}]',16,1),(28,'2022-09-13 18:06:31.672697','2','2',1,'[{\"added\": {}}]',16,1),(29,'2022-09-13 18:06:35.287193','3','3',1,'[{\"added\": {}}]',16,1),(30,'2022-09-13 18:06:41.769883','4','4',1,'[{\"added\": {}}]',16,1),(31,'2022-09-13 18:06:45.705703','5','5',1,'[{\"added\": {}}]',16,1),(32,'2022-09-13 18:06:49.639095','6','6',1,'[{\"added\": {}}]',16,1),(33,'2022-09-13 18:07:25.083531','1','Registro',3,'',20,1),(34,'2022-09-13 18:07:42.217284','1','A+',1,'[{\"added\": {}}]',22,1),(35,'2022-09-13 18:07:46.407334','2','A-',1,'[{\"added\": {}}]',22,1),(36,'2022-09-13 18:07:50.863812','3','B+',1,'[{\"added\": {}}]',22,1),(37,'2022-09-13 18:07:57.162113','4','B-',1,'[{\"added\": {}}]',22,1),(38,'2022-09-13 18:08:09.138874','5','AB+',1,'[{\"added\": {}}]',22,1),(39,'2022-09-13 18:08:13.982180','6','AB-',1,'[{\"added\": {}}]',22,1),(40,'2022-09-13 18:08:19.450876','7','O+',1,'[{\"added\": {}}]',22,1),(41,'2022-09-13 18:08:23.418989','8','O-',1,'[{\"added\": {}}]',22,1),(42,'2022-09-13 18:10:30.155160','1','Años: 1, dias de vacaciones: 8',1,'[{\"added\": {}}]',27,1),(43,'2022-09-13 18:10:34.945467','2','Años: 2, dias de vacaciones: 10',1,'[{\"added\": {}}]',27,1),(44,'2022-09-13 18:10:43.105330','3','Años: 3, dias de vacaciones: 12',1,'[{\"added\": {}}]',27,1),(45,'2022-09-13 18:10:48.943121','4','Años: 4, dias de vacaciones: 14',1,'[{\"added\": {}}]',27,1),(46,'2022-09-13 18:10:55.158883','5','Años: 5, dias de vacaciones: 16',1,'[{\"added\": {}}]',27,1),(47,'2022-09-13 18:11:02.462056','6','Años: 10, dias de vacaciones: 18',1,'[{\"added\": {}}]',27,1),(48,'2022-09-13 18:11:08.459547','7','Años: 15, dias de vacaciones: 20',1,'[{\"added\": {}}]',27,1),(49,'2022-09-13 18:11:16.376738','8','Años: 20, dias de vacaciones: 22',1,'[{\"added\": {}}]',27,1),(50,'2022-09-13 18:11:25.047860','9','Años: 25, dias de vacaciones: 24',1,'[{\"added\": {}}]',27,1),(51,'2022-09-13 18:16:26.358766','1','Sub. Administrativa',1,'[{\"added\": {}}]',18,1),(52,'2022-09-13 18:16:43.712933','2','Sub. Finanzas y ventas',1,'[{\"added\": {}}]',18,1),(53,'2022-09-13 18:17:12.658800','3','Sub. Operaciones',1,'[{\"added\": {}}]',18,1),(54,'2022-09-13 18:17:37.865683','4','Sub. Ingeniería',1,'[{\"added\": {}}]',18,1),(55,'2022-09-13 18:17:54.645381','5','Dirección General',1,'[{\"added\": {}}]',18,1),(56,'2022-09-13 18:18:08.482946','6','Fijos',1,'[{\"added\": {}}]',18,1),(57,'2022-09-13 18:18:14.917856','7','SPP',1,'[{\"added\": {}}]',18,1),(58,'2022-09-13 18:18:59.931287','1','Contabilidad',1,'[{\"added\": {}}]',26,1),(59,'2022-09-13 18:19:46.271400','2','RH',1,'[{\"added\": {}}]',26,1),(60,'2022-09-13 18:19:51.605071','3','Compras',1,'[{\"added\": {}}]',26,1),(61,'2022-09-13 18:19:57.442456','4','Activos',1,'[{\"added\": {}}]',26,1),(62,'2022-09-13 18:20:04.511457','5','Sistemas',1,'[{\"added\": {}}]',26,1),(63,'2022-09-13 18:20:23.681430','6','Evaluación proveedores',1,'[{\"added\": {}}]',26,1),(64,'2022-09-13 18:20:31.539241','7','Subdirector',1,'[{\"added\": {}}]',26,1),(65,'2022-09-13 18:20:59.117668','8','Jurídico',1,'[{\"added\": {}}]',26,1),(66,'2022-09-13 18:21:13.797082','9','Tesorería',1,'[{\"added\": {}}]',26,1),(67,'2022-09-13 18:21:21.169241','10','Ventas',1,'[{\"added\": {}}]',26,1),(68,'2022-09-13 18:22:01.498624','11','Contratos y licitaciones',1,'[{\"added\": {}}]',26,1),(69,'2022-09-13 18:22:22.801040','12','Sub. Finanzas y ventas',1,'[{\"added\": {}}]',26,1),(70,'2022-09-13 18:22:33.950895','13','Sub. Operaciones',1,'[{\"added\": {}}]',26,1),(71,'2022-09-13 18:22:53.965872','14','SUBIDT',1,'[{\"added\": {}}]',26,1),(72,'2022-09-13 18:23:22.650412','15','Indirecto IDT',1,'[{\"added\": {}}]',26,1),(73,'2022-09-13 18:23:44.398715','16','Telemetría',1,'[{\"added\": {}}]',26,1),(74,'2022-09-13 18:24:00.282700','17','ESTAFF DG',1,'[{\"added\": {}}]',26,1),(75,'2022-09-13 18:24:27.009117','18','Controles técnicos',1,'[{\"added\": {}}]',26,1),(76,'2022-09-13 18:24:34.618522','19','SEOV',1,'[{\"added\": {}}]',26,1),(77,'2022-09-13 18:24:41.992896','20','Seguridad',1,'[{\"added\": {}}]',26,1),(78,'2022-09-13 18:24:56.074550','21','Publicidad redes',1,'[{\"added\": {}}]',26,1),(79,'2022-09-13 18:25:09.564874','22','DG Motos',1,'[{\"added\": {}}]',26,1),(80,'2022-09-13 18:27:14.391399','23','Gastos  Mtto Oficina',1,'[{\"added\": {}}]',26,1),(81,'2022-09-13 18:27:38.293990','24','Luz, teléfono y agua',1,'[{\"added\": {}}]',26,1),(82,'2022-09-13 18:27:48.414505','25','Intendencia',1,'[{\"added\": {}}]',26,1),(83,'2022-09-13 18:28:00.903320','26','RP',1,'[{\"added\": {}}]',26,1),(84,'2022-09-13 18:28:14.007469','27','Seguridad privada',1,'[{\"added\": {}}]',26,1),(85,'2022-09-13 18:28:30.412485','28','Sub. Administrativa',1,'[{\"added\": {}}]',26,1),(86,'2022-09-13 18:29:53.741882','29','Sub. Ingeniería',1,'[{\"added\": {}}]',26,1),(87,'2022-09-13 18:30:03.789249','30','Dirección general',1,'[{\"added\": {}}]',26,1),(88,'2022-09-13 18:38:53.918588','30','Dirección general',3,'',26,1),(89,'2022-09-13 18:38:53.958110','29','Sub. Ingeniería',3,'',26,1),(90,'2022-09-13 18:38:53.975552','28','Sub. Administrativa',3,'',26,1),(91,'2022-09-13 18:38:53.989864','27','Seguridad privada',3,'',26,1),(92,'2022-09-13 18:38:54.018514','26','RP',3,'',26,1),(93,'2022-09-13 18:38:54.026328','25','Intendencia',3,'',26,1),(94,'2022-09-13 18:38:54.044767','24','Luz, teléfono y agua',3,'',26,1),(95,'2022-09-13 18:38:54.056122','23','Gastos  Mtto Oficina',3,'',26,1),(96,'2022-09-13 18:38:54.068781','22','DG Motos',3,'',26,1),(97,'2022-09-13 18:38:54.101008','21','Publicidad redes',3,'',26,1),(98,'2022-09-13 18:38:54.115015','20','Seguridad',3,'',26,1),(99,'2022-09-13 18:38:54.152546','19','SEOV',3,'',26,1),(100,'2022-09-13 18:38:54.186305','18','Controles técnicos',3,'',26,1),(101,'2022-09-13 18:38:54.212953','17','ESTAFF DG',3,'',26,1),(102,'2022-09-13 18:38:54.240952','16','Telemetría',3,'',26,1),(103,'2022-09-13 18:38:54.257008','15','Indirecto IDT',3,'',26,1),(104,'2022-09-13 18:38:54.276222','14','SUBIDT',3,'',26,1),(105,'2022-09-13 18:38:54.314710','13','Sub. Operaciones',3,'',26,1),(106,'2022-09-13 18:38:54.325077','12','Sub. Finanzas y ventas',3,'',26,1),(107,'2022-09-13 18:38:54.341844','11','Contratos y licitaciones',3,'',26,1),(108,'2022-09-13 18:38:54.357011','10','Ventas',3,'',26,1),(109,'2022-09-13 18:38:54.376929','9','Tesorería',3,'',26,1),(110,'2022-09-13 18:38:54.402489','8','Jurídico',3,'',26,1),(111,'2022-09-13 18:38:54.426525','7','Subdirector',3,'',26,1),(112,'2022-09-13 18:38:54.442094','6','Evaluación proveedores',3,'',26,1),(113,'2022-09-13 18:38:54.459433','5','Sistemas',3,'',26,1),(114,'2022-09-13 18:38:54.488266','4','Activos',3,'',26,1),(115,'2022-09-13 18:38:54.505793','3','Compras',3,'',26,1),(116,'2022-09-13 18:38:54.525778','2','RH',3,'',26,1),(117,'2022-09-13 18:38:54.561778','1','Contabilidad',3,'',26,1),(118,'2022-09-13 18:53:05.144821','31','Contabilidad',1,'[{\"added\": {}}]',26,1),(119,'2022-09-13 18:53:12.886407','32','RH',1,'[{\"added\": {}}]',26,1),(120,'2022-09-13 18:53:22.794019','33','Compras',1,'[{\"added\": {}}]',26,1),(121,'2022-09-13 18:53:29.718342','34','Activos',1,'[{\"added\": {}}]',26,1),(122,'2022-09-13 18:53:36.594423','35','Sistemas',1,'[{\"added\": {}}]',26,1),(123,'2022-09-13 18:53:43.424846','36','Evaluación proveedores',1,'[{\"added\": {}}]',26,1),(124,'2022-09-13 18:53:56.534421','37','Subdirector',1,'[{\"added\": {}}]',26,1),(125,'2022-09-13 18:54:05.995815','38','Jurídico',1,'[{\"added\": {}}]',26,1),(126,'2022-09-13 18:54:16.565569','39','Tesorería',1,'[{\"added\": {}}]',26,1),(127,'2022-09-13 18:54:30.211482','40','Ventas',1,'[{\"added\": {}}]',26,1),(128,'2022-09-13 18:54:38.233568','41','Contratos y licitaciones',1,'[{\"added\": {}}]',26,1),(129,'2022-09-13 18:54:50.010710','42','Sub. Finanzas y ventas',1,'[{\"added\": {}}]',26,1),(130,'2022-09-13 18:55:05.882351','43','Sub. Operaciones',1,'[{\"added\": {}}]',26,1),(131,'2022-09-13 18:56:25.684535','44','SUBIDT',1,'[{\"added\": {}}]',26,1),(132,'2022-09-13 18:56:36.605966','45','Indirecto IDT',1,'[{\"added\": {}}]',26,1),(133,'2022-09-13 18:56:43.238312','46','Telemetría',1,'[{\"added\": {}}]',26,1),(134,'2022-09-13 18:56:52.244688','47','ESTAFF DG',1,'[{\"added\": {}}]',26,1),(135,'2022-09-13 18:57:03.254044','48','Controles técnicos',1,'[{\"added\": {}}]',26,1),(136,'2022-09-13 18:57:39.537594','49','SEOV',1,'[{\"added\": {}}]',26,1),(137,'2022-09-13 18:57:56.789605','50','Seguridad',1,'[{\"added\": {}}]',26,1),(138,'2022-09-13 18:58:16.406829','51','Publicidad redes',1,'[{\"added\": {}}]',26,1),(139,'2022-09-13 18:58:24.187976','52','DG Motos',1,'[{\"added\": {}}]',26,1),(140,'2022-09-13 18:58:33.924104','53','Gastos  Mtto Oficina',1,'[{\"added\": {}}]',26,1),(141,'2022-09-13 18:58:42.059512','54','Luz, teléfono y agua',1,'[{\"added\": {}}]',26,1),(142,'2022-09-13 18:58:55.040722','55','Intendencia',1,'[{\"added\": {}}]',26,1),(143,'2022-09-13 18:59:01.664848','56','RP',1,'[{\"added\": {}}]',26,1),(144,'2022-09-13 18:59:09.469544','57','Seguridad privada',1,'[{\"added\": {}}]',26,1),(145,'2022-09-13 18:59:25.563318','58','Sub. Administrativa',1,'[{\"added\": {}}]',26,1),(146,'2022-09-13 18:59:35.814423','59','Sub. Finanzas y ventas',1,'[{\"added\": {}}]',26,1),(147,'2022-09-13 19:00:08.302045','60','Sub. Operaciones',1,'[{\"added\": {}}]',26,1),(148,'2022-09-13 19:00:18.342880','61','Sub. Ingeniería',1,'[{\"added\": {}}]',26,1),(149,'2022-09-13 19:00:27.473886','62','Dirección general',1,'[{\"added\": {}}]',26,1),(150,'2022-09-13 19:08:46.523874','1','XCH',1,'[{\"added\": {}}]',28,1),(151,'2022-09-13 19:09:00.699468','2','CH',1,'[{\"added\": {}}]',28,1),(152,'2022-09-13 19:09:09.303908','3','M',1,'[{\"added\": {}}]',28,1),(153,'2022-09-13 19:09:16.961011','4','G',1,'[{\"added\": {}}]',28,1),(154,'2022-09-13 19:09:25.717653','5','XG',1,'[{\"added\": {}}]',28,1),(155,'2022-09-13 19:12:22.330001','6','XCH',1,'[{\"added\": {}}]',28,1),(156,'2022-09-13 19:12:32.888106','7','CH',1,'[{\"added\": {}}]',28,1),(157,'2022-09-13 19:12:43.781820','8','G',1,'[{\"added\": {}}]',28,1),(158,'2022-09-13 19:13:44.300407','9','XG',1,'[{\"added\": {}}]',28,1),(159,'2022-09-13 19:13:54.818345','10','CH',1,'[{\"added\": {}}]',28,1),(160,'2022-09-13 19:14:25.510141','10','CH',3,'',28,1),(161,'2022-09-13 19:15:02.808996','11','XCH',1,'[{\"added\": {}}]',28,1),(162,'2022-09-13 19:15:12.580884','12','CH',1,'[{\"added\": {}}]',28,1),(163,'2022-09-13 19:15:21.673288','13','M',1,'[{\"added\": {}}]',28,1),(164,'2022-09-13 19:15:28.913938','14','G',1,'[{\"added\": {}}]',28,1),(165,'2022-09-13 19:15:35.800912','15','XG',1,'[{\"added\": {}}]',28,1),(166,'2022-09-13 19:15:52.547018','16','XCH',1,'[{\"added\": {}}]',28,1),(167,'2022-09-13 19:15:59.986443','17','CH',1,'[{\"added\": {}}]',28,1),(168,'2022-09-13 19:16:07.378821','18','M',1,'[{\"added\": {}}]',28,1),(169,'2022-09-13 19:16:14.237987','19','G',1,'[{\"added\": {}}]',28,1),(170,'2022-09-13 19:16:21.057780','20','XG',1,'[{\"added\": {}}]',28,1),(171,'2022-09-13 19:16:29.381010','21','CH',1,'[{\"added\": {}}]',28,1),(172,'2022-09-13 19:17:08.233899','21','XCH',2,'[{\"changed\": {\"fields\": [\"Talla\"]}}]',28,1),(173,'2022-09-13 19:17:59.977969','22','XCH',1,'[{\"added\": {}}]',28,1),(174,'2022-09-13 19:18:09.390206','23','CH',1,'[{\"added\": {}}]',28,1),(175,'2022-09-13 19:18:17.540413','24','M',1,'[{\"added\": {}}]',28,1),(176,'2022-09-13 19:18:29.802196','25','G',1,'[{\"added\": {}}]',28,1),(177,'2022-09-13 19:18:41.217396','26','XG',1,'[{\"added\": {}}]',28,1),(178,'2022-09-13 19:20:16.158425','22','CH',2,'[{\"changed\": {\"fields\": [\"Ropa\", \"Talla\"]}}]',28,1),(179,'2022-09-13 19:27:30.746889','23','Tallas object (23)',2,'[{\"changed\": {\"fields\": [\"Ropa\"]}}]',28,1),(180,'2022-09-13 19:27:45.393272','23','Tallas object (23)',2,'[{\"changed\": {\"fields\": [\"Talla\"]}}]',28,1),(181,'2022-09-13 19:27:57.381250','24','Tallas object (24)',2,'[{\"changed\": {\"fields\": [\"Ropa\", \"Talla\"]}}]',28,1),(182,'2022-09-13 19:28:07.623931','25','Tallas object (25)',2,'[{\"changed\": {\"fields\": [\"Ropa\", \"Talla\"]}}]',28,1),(183,'2022-09-13 19:28:35.853836','26','Tallas object (26)',2,'[{\"changed\": {\"fields\": [\"Talla\"]}}]',28,1),(184,'2022-09-13 19:28:49.006486','26','Tallas object (26)',2,'[{\"changed\": {\"fields\": [\"Talla\"]}}]',28,1),(185,'2022-09-13 19:29:21.562132','27','Tallas object (27)',1,'[{\"added\": {}}]',28,1),(186,'2022-09-13 19:30:09.642822','28','Tallas object (28)',1,'[{\"added\": {}}]',28,1),(187,'2022-09-13 19:30:15.043195','29','Tallas object (29)',1,'[{\"added\": {}}]',28,1),(188,'2022-09-13 19:30:21.128823','30','Tallas object (30)',1,'[{\"added\": {}}]',28,1),(189,'2022-09-13 19:30:56.682556','31','Tallas object (31)',1,'[{\"added\": {}}]',28,1),(190,'2022-09-13 19:31:16.368022','32','Tallas object (32)',1,'[{\"added\": {}}]',28,1),(191,'2022-09-13 19:31:25.190457','33','Tallas object (33)',1,'[{\"added\": {}}]',28,1),(192,'2022-09-13 19:31:31.431847','34','Tallas object (34)',1,'[{\"added\": {}}]',28,1),(193,'2022-09-13 19:31:37.293256','35','Tallas object (35)',1,'[{\"added\": {}}]',28,1),(194,'2022-09-13 19:31:46.090419','36','Tallas object (36)',1,'[{\"added\": {}}]',28,1),(195,'2022-09-13 19:31:52.718503','37','Tallas object (37)',1,'[{\"added\": {}}]',28,1),(196,'2022-09-13 19:31:57.431536','38','Tallas object (38)',1,'[{\"added\": {}}]',28,1),(197,'2022-09-13 19:32:02.692587','39','Tallas object (39)',1,'[{\"added\": {}}]',28,1),(198,'2022-09-13 19:32:08.361108','40','Tallas object (40)',1,'[{\"added\": {}}]',28,1),(199,'2022-09-13 19:32:14.222680','41','Tallas object (41)',1,'[{\"added\": {}}]',28,1),(200,'2022-09-13 19:32:18.471880','42','Tallas object (42)',1,'[{\"added\": {}}]',28,1),(201,'2022-09-13 19:32:23.610932','43','Tallas object (43)',1,'[{\"added\": {}}]',28,1),(202,'2022-09-13 19:32:30.081852','44','Tallas object (44)',1,'[{\"added\": {}}]',28,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'proyecto','banco'),(40,'proyecto','bonos'),(39,'proyecto','catorcenas'),(8,'proyecto','civil'),(9,'proyecto','contrato'),(10,'proyecto','costo'),(11,'proyecto','datosbancarios'),(12,'proyecto','datosisr'),(13,'proyecto','distrito'),(38,'proyecto','economicos'),(14,'proyecto','empleados_batch'),(15,'proyecto','empresa'),(37,'proyecto','historicalbonos'),(36,'proyecto','historicalcosto'),(35,'proyecto','historicaleconomicos'),(34,'proyecto','historicaluniformes'),(33,'proyecto','historicalvacaciones'),(16,'proyecto','nivel'),(17,'proyecto','perfil'),(18,'proyecto','proyecto'),(19,'proyecto','puesto'),(20,'proyecto','registropatronal'),(21,'proyecto','ropa'),(22,'proyecto','sangre'),(23,'proyecto','sexo'),(24,'proyecto','status'),(25,'proyecto','status_batch'),(26,'proyecto','subproyecto'),(27,'proyecto','tablavacaciones'),(28,'proyecto','tallas'),(32,'proyecto','uniforme'),(31,'proyecto','uniformes'),(30,'proyecto','userdatos'),(29,'proyecto','vacaciones'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-09-13 00:25:19.858951'),(2,'auth','0001_initial','2022-09-13 00:34:14.011428'),(3,'admin','0001_initial','2022-09-13 00:36:15.775323'),(4,'admin','0002_logentry_remove_auto_add','2022-09-13 00:36:15.811598'),(5,'admin','0003_logentry_add_action_flag_choices','2022-09-13 00:36:15.836908'),(6,'contenttypes','0002_remove_content_type_name','2022-09-13 00:36:16.137696'),(7,'auth','0002_alter_permission_name_max_length','2022-09-13 00:36:16.320344'),(8,'auth','0003_alter_user_email_max_length','2022-09-13 00:36:16.531143'),(9,'auth','0004_alter_user_username_opts','2022-09-13 00:36:16.557400'),(10,'auth','0005_alter_user_last_login_null','2022-09-13 00:36:16.730324'),(11,'auth','0006_require_contenttypes_0002','2022-09-13 00:36:16.780976'),(12,'auth','0007_alter_validators_add_error_messages','2022-09-13 00:36:16.797809'),(13,'auth','0008_alter_user_username_max_length','2022-09-13 00:36:17.000432'),(14,'auth','0009_alter_user_last_name_max_length','2022-09-13 00:36:17.219451'),(15,'auth','0010_alter_group_name_max_length','2022-09-13 00:36:17.333806'),(16,'auth','0011_update_proxy_permissions','2022-09-13 00:36:17.364715'),(17,'auth','0012_alter_user_first_name_max_length','2022-09-13 00:36:17.530586'),(18,'proyecto','0001_initial','2022-09-13 01:54:09.776208'),(19,'sessions','0001_initial','2022-09-13 01:54:48.648680'),(20,'proyecto','0002_subproyecto_proyecto','2022-09-13 18:50:32.062936'),(21,'proyecto','0003_tallas_ropa','2022-09-13 19:08:02.854415');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1j28etsmcdlyjob00zbdculfyzshr22q','.eJxVjDsOwjAQBe_iGln2Bv8o6XMGa9de4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVFWHH63QjTg9sO8h3bbZZpbusykdwVedAuxznz83q4fwcVe_3WhXWiHIJ2mskUtIq0U2rgoIxK5D0mOLODYiFxLgN5DGQsQCg6WALx_gD7Lzgz:1oYFGG:4UlysyN_cbtrFf9ODhFpHg3PkeZE3YrdPfPwwo5l2Zs','2022-09-27 23:24:12.342643'),('bo0k8rswqrivkotf5fuf9eb3gplcq297','.eJxVjDsOwjAQBe_iGln2xr-lpOcM1vqHA8iW4qRC3B0ipYD2zcx7MU_bWv028uLnxM4M2Ol3CxQfue0g3andOo-9rcsc-K7wgw5-7Sk_L4f7d1Bp1G89SUBCTcJKEXQgKgBFIzphMSrjQKWgjKVJZ5e1A6mFERZkQgIqU2bvD7vlNuA:1oXvgT:hlm4VQ-ltvlEE5-D6MULgEOWnIXS1cSkv5A3NlGaJoQ','2022-09-27 02:29:57.865781'),('k0zyyq6fcp98f01av8vettexomyoneq4','.eJxVjEEOwiAQRe_C2hAGChaX7nsGwjCDVA0kpV0Z765NutDtf-_9lwhxW0vYOi9hJnERIE6_G8b04LoDusd6azK1ui4zyl2RB-1yasTP6-H-HZTYy7fWaACVAsA8sBtzYut8PhsD2tgIWQM7o2FIXpFyNDirCAhN1kxIfhTvD8spN4c:1oXvTA:Vl9inzlxMqUnsqAkD4N9HxnwgCURVWBq4qwasTzWe80','2022-09-27 02:16:12.744127');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_banco`
--

DROP TABLE IF EXISTS `proyecto_banco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_banco` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `banco` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_banco`
--

LOCK TABLES `proyecto_banco` WRITE;
/*!40000 ALTER TABLE `proyecto_banco` DISABLE KEYS */;
INSERT INTO `proyecto_banco` VALUES (1,'Santander',1),(2,'BBVA',1),(3,'HSBC',1),(4,'Banorte',1),(5,'Banamex',1),(6,'Scotiabank',1);
/*!40000 ALTER TABLE `proyecto_banco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_bonos`
--

DROP TABLE IF EXISTS `proyecto_bonos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_bonos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `monto` decimal(14,2) DEFAULT NULL,
  `fecha_bono` date DEFAULT NULL,
  `mes_bono` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `costo_id` bigint(20) DEFAULT NULL,
  `datosbancarios_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_bonos_costo_id_077af0d8_fk_proyecto_costo_id` (`costo_id`),
  KEY `proyecto_bonos_datosbancarios_id_c90ae3ea_fk_proyecto_` (`datosbancarios_id`),
  CONSTRAINT `proyecto_bonos_costo_id_077af0d8_fk_proyecto_costo_id` FOREIGN KEY (`costo_id`) REFERENCES `proyecto_costo` (`id`),
  CONSTRAINT `proyecto_bonos_datosbancarios_id_c90ae3ea_fk_proyecto_` FOREIGN KEY (`datosbancarios_id`) REFERENCES `proyecto_datosbancarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_bonos`
--

LOCK TABLES `proyecto_bonos` WRITE;
/*!40000 ALTER TABLE `proyecto_bonos` DISABLE KEYS */;
INSERT INTO `proyecto_bonos` VALUES (1,0.00,NULL,NULL,'2022-09-13 22:47:17.354437','2022-09-13 22:47:17.354481',0,NULL,NULL);
/*!40000 ALTER TABLE `proyecto_bonos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_catorcenas`
--

DROP TABLE IF EXISTS `proyecto_catorcenas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_catorcenas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `catorcena` int(11) DEFAULT NULL,
  `fecha_inicial` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `proyecto_catorcenas_catorcena_fecha_inicial_78842e58_uniq` (`catorcena`,`fecha_inicial`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_catorcenas`
--

LOCK TABLES `proyecto_catorcenas` WRITE;
/*!40000 ALTER TABLE `proyecto_catorcenas` DISABLE KEYS */;
INSERT INTO `proyecto_catorcenas` VALUES (1,1,'2021-12-27','2022-01-09',1),(2,2,'2022-01-10','2022-01-23',1),(3,3,'2022-01-24','2022-02-06',1),(4,4,'2022-02-07','2022-02-20',1),(5,5,'2022-02-21','2022-03-06',1),(6,6,'2022-03-07','2022-03-20',1),(7,7,'2022-03-21','2022-04-03',1),(8,8,'2022-04-04','2022-04-17',1),(9,9,'2022-04-18','2022-05-01',1),(10,10,'2022-05-02','2022-05-15',1),(11,11,'2022-05-16','2022-05-29',1),(12,12,'2022-05-30','2022-06-12',1),(13,13,'2022-06-13','2022-06-26',1),(14,14,'2022-06-27','2022-07-10',1),(15,15,'2022-07-11','2022-07-24',1),(16,16,'2022-07-25','2022-08-07',1),(17,17,'2022-08-08','2022-08-21',1),(18,18,'2022-08-22','2022-09-04',1),(19,19,'2022-09-05','2022-09-18',1),(20,20,'2022-09-19','2022-10-02',1),(21,21,'2022-10-03','2022-10-16',1),(22,22,'2022-10-17','2022-10-30',1),(23,23,'2022-10-31','2022-11-13',1),(24,24,'2022-11-14','2022-11-27',1),(25,25,'2022-11-28','2022-12-11',1),(26,26,'2022-12-12','2022-12-25',1),(27,0,NULL,NULL,0);
/*!40000 ALTER TABLE `proyecto_catorcenas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_civil`
--

DROP TABLE IF EXISTS `proyecto_civil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_civil` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `estado_civil` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_civil`
--

LOCK TABLES `proyecto_civil` WRITE;
/*!40000 ALTER TABLE `proyecto_civil` DISABLE KEYS */;
INSERT INTO `proyecto_civil` VALUES (1,'Soltero',1),(2,'Casado',1);
/*!40000 ALTER TABLE `proyecto_civil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_contrato`
--

DROP TABLE IF EXISTS `proyecto_contrato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_contrato` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `contrato` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_contrato`
--

LOCK TABLES `proyecto_contrato` WRITE;
/*!40000 ALTER TABLE `proyecto_contrato` DISABLE KEYS */;
INSERT INTO `proyecto_contrato` VALUES (1,'Planta',1),(2,'Eventual',1);
/*!40000 ALTER TABLE `proyecto_contrato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_costo`
--

DROP TABLE IF EXISTS `proyecto_costo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_costo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `seccion` varchar(50) DEFAULT NULL,
  `amortizacion_infonavit` decimal(14,2) DEFAULT NULL,
  `fonacot` decimal(14,2) DEFAULT NULL,
  `neto_catorcenal_sin_deducciones` decimal(14,2) DEFAULT NULL,
  `complemento_salario_catorcenal` decimal(14,2) DEFAULT NULL,
  `sueldo_diario` decimal(14,2) DEFAULT NULL,
  `sdi` decimal(14,2) DEFAULT NULL,
  `apoyo_de_pasajes` decimal(14,2) DEFAULT NULL,
  `imms_obrero_patronal` decimal(14,2) DEFAULT NULL,
  `apoyo_vist_familiar` decimal(14,2) DEFAULT NULL,
  `estancia` decimal(14,2) DEFAULT NULL,
  `renta` decimal(14,2) DEFAULT NULL,
  `apoyo_estudios` decimal(14,2) DEFAULT NULL,
  `amv` decimal(14,2) DEFAULT NULL,
  `gasolina` decimal(14,2) DEFAULT NULL,
  `campamento` decimal(14,2) DEFAULT NULL,
  `total_deduccion` decimal(14,2) DEFAULT NULL,
  `neto_pagar` decimal(14,2) DEFAULT NULL,
  `sueldo_mensual_neto` decimal(14,2) DEFAULT NULL,
  `complemento_salario_mensual` decimal(14,2) DEFAULT NULL,
  `sueldo_mensual` decimal(14,2) DEFAULT NULL,
  `sueldo_mensual_sdi` decimal(14,2) DEFAULT NULL,
  `total_percepciones_mensual` decimal(14,2) DEFAULT NULL,
  `impuesto_estatal` decimal(14,2) DEFAULT NULL,
  `sar` decimal(14,2) DEFAULT NULL,
  `cesantia` decimal(14,2) DEFAULT NULL,
  `infonavit` decimal(14,2) DEFAULT NULL,
  `isr` decimal(14,2) DEFAULT NULL,
  `lim_inferior` decimal(14,2) DEFAULT NULL,
  `excedente` decimal(14,2) DEFAULT NULL,
  `tasa` decimal(14,2) DEFAULT NULL,
  `impuesto_marginal` decimal(14,2) DEFAULT NULL,
  `cuota_fija` decimal(14,2) DEFAULT NULL,
  `impuesto` decimal(14,2) DEFAULT NULL,
  `subsidio` decimal(14,2) DEFAULT NULL,
  `total_apoyosbonos_empleadocomp` decimal(14,2) DEFAULT NULL,
  `total_apoyosbonos_agregcomis` decimal(14,2) DEFAULT NULL,
  `comision_complemeto_salario_bonos` decimal(14,2) DEFAULT NULL,
  `total_costo_empresa` decimal(14,2) DEFAULT NULL,
  `ingreso_mensual_neto_empleado` decimal(14,2) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `puesto_id` bigint(20) DEFAULT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_costo_puesto_id_1eed41f9_fk_proyecto_puesto_id` (`puesto_id`),
  KEY `proyecto_costo_status_id_e6db7240_fk_proyecto_status_id` (`status_id`),
  CONSTRAINT `proyecto_costo_puesto_id_1eed41f9_fk_proyecto_puesto_id` FOREIGN KEY (`puesto_id`) REFERENCES `proyecto_puesto` (`id`),
  CONSTRAINT `proyecto_costo_status_id_e6db7240_fk_proyecto_status_id` FOREIGN KEY (`status_id`) REFERENCES `proyecto_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_costo`
--

LOCK TABLES `proyecto_costo` WRITE;
/*!40000 ALTER TABLE `proyecto_costo` DISABLE KEYS */;
INSERT INTO `proyecto_costo` VALUES (1,NULL,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,'2022-09-13','2022-09-13',0,NULL,NULL);
/*!40000 ALTER TABLE `proyecto_costo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_datosbancarios`
--

DROP TABLE IF EXISTS `proyecto_datosbancarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_datosbancarios` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `no_de_cuenta` varchar(50) DEFAULT NULL,
  `numero_de_tarjeta` varchar(50) DEFAULT NULL,
  `clabe_interbancaria` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  `banco_id` bigint(20) DEFAULT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_datosbancarios_status_id_e8dbebee_fk_proyecto_status_id` (`status_id`),
  KEY `proyecto_datosbancarios_banco_id_b9c051e5_fk_proyecto_banco_id` (`banco_id`),
  CONSTRAINT `proyecto_datosbancarios_banco_id_b9c051e5_fk_proyecto_banco_id` FOREIGN KEY (`banco_id`) REFERENCES `proyecto_banco` (`id`),
  CONSTRAINT `proyecto_datosbancarios_status_id_e8dbebee_fk_proyecto_status_id` FOREIGN KEY (`status_id`) REFERENCES `proyecto_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_datosbancarios`
--

LOCK TABLES `proyecto_datosbancarios` WRITE;
/*!40000 ALTER TABLE `proyecto_datosbancarios` DISABLE KEYS */;
INSERT INTO `proyecto_datosbancarios` VALUES (1,NULL,NULL,NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `proyecto_datosbancarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_datosisr`
--

DROP TABLE IF EXISTS `proyecto_datosisr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_datosisr` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `liminf` decimal(14,2) DEFAULT NULL,
  `limsup` decimal(14,2) DEFAULT NULL,
  `cuota` decimal(14,2) DEFAULT NULL,
  `excedente` decimal(14,4) DEFAULT NULL,
  `p_ingresos` decimal(14,2) DEFAULT NULL,
  `g_ingresos` decimal(14,2) DEFAULT NULL,
  `subsidio` decimal(14,2) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_datosisr`
--

LOCK TABLES `proyecto_datosisr` WRITE;
/*!40000 ALTER TABLE `proyecto_datosisr` DISABLE KEYS */;
INSERT INTO `proyecto_datosisr` VALUES (1,0.01,644.59,0.00,0.0192,0.01,1768.96,407.02,1),(2,644.59,5470.93,12.38,0.0640,1768.97,2653.38,406.83,1),(3,5470.93,9614.67,321.26,0.1088,2653.39,3472.84,406.62,1),(4,9614.67,11176.63,772.10,0.1600,3472.85,3537.87,392.77,1),(5,11176.63,13381.48,1022.01,0.1792,3537.88,4446.15,382.46,1),(6,13381.48,26988.51,1417.12,0.2136,4446.16,4717.18,354.23,1),(7,26988.51,42537.59,4323.58,0.2352,4717.19,5335.42,324.87,1),(8,42537.59,81211.26,7980.73,0.3000,5335.43,6224.67,294.63,1),(9,81211.26,108281.68,19582.83,0.3200,6224.68,7113.90,253.54,1),(10,108281.68,324845.02,28245.36,0.3400,7113.91,7382.33,217.61,1),(11,324845.02,324845.03,101876.90,0.3500,7382.34,7382.35,0.00,1);
/*!40000 ALTER TABLE `proyecto_datosisr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_distrito`
--

DROP TABLE IF EXISTS `proyecto_distrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_distrito` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `distrito` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_distrito`
--

LOCK TABLES `proyecto_distrito` WRITE;
/*!40000 ALTER TABLE `proyecto_distrito` DISABLE KEYS */;
INSERT INTO `proyecto_distrito` VALUES (1,'Matriz',1),(2,'Altamira',1),(3,'Planta Veracruz',1),(4,'Poza Rica',1),(5,'Villahermosa',1),(6,'Veracruz',1);
/*!40000 ALTER TABLE `proyecto_distrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_economicos`
--

DROP TABLE IF EXISTS `proyecto_economicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_economicos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `periodo` varchar(50) DEFAULT NULL,
  `dias_pendientes` int(11) DEFAULT NULL,
  `dias_disfrutados` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_economicos_status_id_7ec7ec4e_fk_proyecto_status_id` (`status_id`),
  CONSTRAINT `proyecto_economicos_status_id_7ec7ec4e_fk_proyecto_status_id` FOREIGN KEY (`status_id`) REFERENCES `proyecto_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_economicos`
--

LOCK TABLES `proyecto_economicos` WRITE;
/*!40000 ALTER TABLE `proyecto_economicos` DISABLE KEYS */;
INSERT INTO `proyecto_economicos` VALUES (1,NULL,0,0,'2022-09-13 22:52:54.981381','2022-09-13 22:52:54.981426',0,NULL);
/*!40000 ALTER TABLE `proyecto_economicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_empleados_batch`
--

DROP TABLE IF EXISTS `proyecto_empleados_batch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_empleados_batch` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(100) NOT NULL,
  `uploaded` date NOT NULL,
  `activated` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_empleados_batch`
--

LOCK TABLES `proyecto_empleados_batch` WRITE;
/*!40000 ALTER TABLE `proyecto_empleados_batch` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyecto_empleados_batch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_empresa`
--

DROP TABLE IF EXISTS `proyecto_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_empresa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `empresa` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  `logo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_empresa`
--

LOCK TABLES `proyecto_empresa` WRITE;
/*!40000 ALTER TABLE `proyecto_empresa` DISABLE KEYS */;
INSERT INTO `proyecto_empresa` VALUES (1,'VORDCAB',1,''),(2,'VORDTEC',1,'');
/*!40000 ALTER TABLE `proyecto_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_historicalbonos`
--

DROP TABLE IF EXISTS `proyecto_historicalbonos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_historicalbonos` (
  `id` bigint(20) NOT NULL,
  `monto` decimal(14,2) DEFAULT NULL,
  `fecha_bono` date DEFAULT NULL,
  `mes_bono` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `history_change_reason` longtext,
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_type` varchar(1) NOT NULL,
  `costo_id` bigint(20) DEFAULT NULL,
  `datosbancarios_id` bigint(20) DEFAULT NULL,
  `history_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `proyecto_historicalb_history_user_id_40a7a188_fk_auth_user` (`history_user_id`),
  KEY `proyecto_historicalbonos_id_b918039e` (`id`),
  KEY `proyecto_historicalbonos_history_date_fd8cc15e` (`history_date`),
  KEY `proyecto_historicalbonos_costo_id_fdba98a8` (`costo_id`),
  KEY `proyecto_historicalbonos_datosbancarios_id_969415e7` (`datosbancarios_id`),
  CONSTRAINT `proyecto_historicalb_history_user_id_40a7a188_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_historicalbonos`
--

LOCK TABLES `proyecto_historicalbonos` WRITE;
/*!40000 ALTER TABLE `proyecto_historicalbonos` DISABLE KEYS */;
INSERT INTO `proyecto_historicalbonos` VALUES (1,0.00,NULL,NULL,'2022-09-13 22:47:17.354437','2022-09-13 22:47:17.354481',0,NULL,1,'2022-09-13 22:47:17.362690','+',NULL,NULL,6);
/*!40000 ALTER TABLE `proyecto_historicalbonos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_historicalcosto`
--

DROP TABLE IF EXISTS `proyecto_historicalcosto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_historicalcosto` (
  `id` bigint(20) NOT NULL,
  `seccion` varchar(50) DEFAULT NULL,
  `amortizacion_infonavit` decimal(14,2) DEFAULT NULL,
  `fonacot` decimal(14,2) DEFAULT NULL,
  `neto_catorcenal_sin_deducciones` decimal(14,2) DEFAULT NULL,
  `complemento_salario_catorcenal` decimal(14,2) DEFAULT NULL,
  `sueldo_diario` decimal(14,2) DEFAULT NULL,
  `sdi` decimal(14,2) DEFAULT NULL,
  `apoyo_de_pasajes` decimal(14,2) DEFAULT NULL,
  `imms_obrero_patronal` decimal(14,2) DEFAULT NULL,
  `apoyo_vist_familiar` decimal(14,2) DEFAULT NULL,
  `estancia` decimal(14,2) DEFAULT NULL,
  `renta` decimal(14,2) DEFAULT NULL,
  `apoyo_estudios` decimal(14,2) DEFAULT NULL,
  `amv` decimal(14,2) DEFAULT NULL,
  `gasolina` decimal(14,2) DEFAULT NULL,
  `campamento` decimal(14,2) DEFAULT NULL,
  `total_deduccion` decimal(14,2) DEFAULT NULL,
  `neto_pagar` decimal(14,2) DEFAULT NULL,
  `sueldo_mensual_neto` decimal(14,2) DEFAULT NULL,
  `complemento_salario_mensual` decimal(14,2) DEFAULT NULL,
  `sueldo_mensual` decimal(14,2) DEFAULT NULL,
  `sueldo_mensual_sdi` decimal(14,2) DEFAULT NULL,
  `total_percepciones_mensual` decimal(14,2) DEFAULT NULL,
  `impuesto_estatal` decimal(14,2) DEFAULT NULL,
  `sar` decimal(14,2) DEFAULT NULL,
  `cesantia` decimal(14,2) DEFAULT NULL,
  `infonavit` decimal(14,2) DEFAULT NULL,
  `isr` decimal(14,2) DEFAULT NULL,
  `lim_inferior` decimal(14,2) DEFAULT NULL,
  `excedente` decimal(14,2) DEFAULT NULL,
  `tasa` decimal(14,2) DEFAULT NULL,
  `impuesto_marginal` decimal(14,2) DEFAULT NULL,
  `cuota_fija` decimal(14,2) DEFAULT NULL,
  `impuesto` decimal(14,2) DEFAULT NULL,
  `subsidio` decimal(14,2) DEFAULT NULL,
  `total_apoyosbonos_empleadocomp` decimal(14,2) DEFAULT NULL,
  `total_apoyosbonos_agregcomis` decimal(14,2) DEFAULT NULL,
  `comision_complemeto_salario_bonos` decimal(14,2) DEFAULT NULL,
  `total_costo_empresa` decimal(14,2) DEFAULT NULL,
  `ingreso_mensual_neto_empleado` decimal(14,2) DEFAULT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `history_change_reason` longtext,
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int(11) DEFAULT NULL,
  `puesto_id` bigint(20) DEFAULT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `proyecto_historicalc_history_user_id_c35735e9_fk_auth_user` (`history_user_id`),
  KEY `proyecto_historicalcosto_id_153d3b68` (`id`),
  KEY `proyecto_historicalcosto_history_date_1e0c0726` (`history_date`),
  KEY `proyecto_historicalcosto_puesto_id_bc559cbf` (`puesto_id`),
  KEY `proyecto_historicalcosto_status_id_2616be01` (`status_id`),
  CONSTRAINT `proyecto_historicalc_history_user_id_c35735e9_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_historicalcosto`
--

LOCK TABLES `proyecto_historicalcosto` WRITE;
/*!40000 ALTER TABLE `proyecto_historicalcosto` DISABLE KEYS */;
INSERT INTO `proyecto_historicalcosto` VALUES (1,NULL,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,'2022-09-13','2022-09-13',0,NULL,1,'2022-09-13 22:44:38.294445','+',6,NULL,NULL);
/*!40000 ALTER TABLE `proyecto_historicalcosto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_historicaleconomicos`
--

DROP TABLE IF EXISTS `proyecto_historicaleconomicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_historicaleconomicos` (
  `id` bigint(20) NOT NULL,
  `periodo` varchar(50) DEFAULT NULL,
  `dias_pendientes` int(11) DEFAULT NULL,
  `dias_disfrutados` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `history_change_reason` longtext,
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int(11) DEFAULT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `proyecto_historicale_history_user_id_7f8d704b_fk_auth_user` (`history_user_id`),
  KEY `proyecto_historicaleconomicos_id_6da54835` (`id`),
  KEY `proyecto_historicaleconomicos_history_date_dcb9c4b6` (`history_date`),
  KEY `proyecto_historicaleconomicos_status_id_976080a4` (`status_id`),
  CONSTRAINT `proyecto_historicale_history_user_id_7f8d704b_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_historicaleconomicos`
--

LOCK TABLES `proyecto_historicaleconomicos` WRITE;
/*!40000 ALTER TABLE `proyecto_historicaleconomicos` DISABLE KEYS */;
INSERT INTO `proyecto_historicaleconomicos` VALUES (1,NULL,0,0,'2022-09-13 22:52:54.981381','2022-09-13 22:52:54.981426',0,NULL,1,'2022-09-13 22:52:54.984556','+',6,NULL);
/*!40000 ALTER TABLE `proyecto_historicaleconomicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_historicaluniformes`
--

DROP TABLE IF EXISTS `proyecto_historicaluniformes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_historicaluniformes` (
  `id` bigint(20) NOT NULL,
  `fecha_pedido` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `history_change_reason` longtext,
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int(11) DEFAULT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `proyecto_historicalu_history_user_id_7745a3c8_fk_auth_user` (`history_user_id`),
  KEY `proyecto_historicaluniformes_id_7b0d7e58` (`id`),
  KEY `proyecto_historicaluniformes_history_date_af8e226c` (`history_date`),
  KEY `proyecto_historicaluniformes_status_id_b1d1ce2d` (`status_id`),
  CONSTRAINT `proyecto_historicalu_history_user_id_7745a3c8_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_historicaluniformes`
--

LOCK TABLES `proyecto_historicaluniformes` WRITE;
/*!40000 ALTER TABLE `proyecto_historicaluniformes` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyecto_historicaluniformes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_historicalvacaciones`
--

DROP TABLE IF EXISTS `proyecto_historicalvacaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_historicalvacaciones` (
  `id` bigint(20) NOT NULL,
  `periodo` varchar(50) DEFAULT NULL,
  `dias_de_vacaciones` int(11) DEFAULT NULL,
  `dias_disfrutados` int(11) DEFAULT NULL,
  `total_pendiente` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `history_change_reason` longtext,
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int(11) DEFAULT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `proyecto_historicalv_history_user_id_822586f9_fk_auth_user` (`history_user_id`),
  KEY `proyecto_historicalvacaciones_id_2221ff41` (`id`),
  KEY `proyecto_historicalvacaciones_history_date_fbc0e80a` (`history_date`),
  KEY `proyecto_historicalvacaciones_status_id_95ce23bb` (`status_id`),
  CONSTRAINT `proyecto_historicalv_history_user_id_822586f9_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_historicalvacaciones`
--

LOCK TABLES `proyecto_historicalvacaciones` WRITE;
/*!40000 ALTER TABLE `proyecto_historicalvacaciones` DISABLE KEYS */;
INSERT INTO `proyecto_historicalvacaciones` VALUES (1,NULL,0,0,0,'2022-09-13 22:50:15.434662','2022-09-13 22:50:15.434707',0,NULL,1,'2022-09-13 22:50:15.442429','+',6,NULL);
/*!40000 ALTER TABLE `proyecto_historicalvacaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_nivel`
--

DROP TABLE IF EXISTS `proyecto_nivel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_nivel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nivel` int(11) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_nivel`
--

LOCK TABLES `proyecto_nivel` WRITE;
/*!40000 ALTER TABLE `proyecto_nivel` DISABLE KEYS */;
INSERT INTO `proyecto_nivel` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1);
/*!40000 ALTER TABLE `proyecto_nivel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_perfil`
--

DROP TABLE IF EXISTS `proyecto_perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_perfil` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `foto` varchar(100) DEFAULT NULL,
  `numero_de_trabajador` int(11) DEFAULT NULL,
  `nombres` varchar(50) DEFAULT NULL,
  `apellidos` varchar(50) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `correo_electronico` varchar(50) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `complete_status` tinyint(1) NOT NULL,
  `distrito_id` bigint(20) DEFAULT NULL,
  `empresa_id` bigint(20) DEFAULT NULL,
  `proyecto_id` bigint(20) DEFAULT NULL,
  `subproyecto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_perfil_proyecto_id_8c3562b4_fk_proyecto_proyecto_id` (`proyecto_id`),
  KEY `proyecto_perfil_subproyecto_id_b4b07568_fk_proyecto_` (`subproyecto_id`),
  KEY `proyecto_perfil_distrito_id_e364166d_fk_proyecto_distrito_id` (`distrito_id`),
  KEY `proyecto_perfil_empresa_id_5b698011_fk_proyecto_empresa_id` (`empresa_id`),
  CONSTRAINT `proyecto_perfil_distrito_id_e364166d_fk_proyecto_distrito_id` FOREIGN KEY (`distrito_id`) REFERENCES `proyecto_distrito` (`id`),
  CONSTRAINT `proyecto_perfil_empresa_id_5b698011_fk_proyecto_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `proyecto_empresa` (`id`),
  CONSTRAINT `proyecto_perfil_proyecto_id_8c3562b4_fk_proyecto_proyecto_id` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto_proyecto` (`id`),
  CONSTRAINT `proyecto_perfil_subproyecto_id_b4b07568_fk_proyecto_` FOREIGN KEY (`subproyecto_id`) REFERENCES `proyecto_subproyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_perfil`
--

LOCK TABLES `proyecto_perfil` WRITE;
/*!40000 ALTER TABLE `proyecto_perfil` DISABLE KEYS */;
INSERT INTO `proyecto_perfil` VALUES (1,'',NULL,NULL,NULL,NULL,'',0,0,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `proyecto_perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_proyecto`
--

DROP TABLE IF EXISTS `proyecto_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_proyecto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `proyecto` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_proyecto`
--

LOCK TABLES `proyecto_proyecto` WRITE;
/*!40000 ALTER TABLE `proyecto_proyecto` DISABLE KEYS */;
INSERT INTO `proyecto_proyecto` VALUES (1,'Sub. Administrativa',1),(2,'Sub. Finanzas y ventas',1),(3,'Sub. Operaciones',1),(4,'Sub. Ingeniería',1),(5,'Dirección General',1),(6,'Fijos',1),(7,'SPP',1);
/*!40000 ALTER TABLE `proyecto_proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_puesto`
--

DROP TABLE IF EXISTS `proyecto_puesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_puesto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `puesto` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_puesto`
--

LOCK TABLES `proyecto_puesto` WRITE;
/*!40000 ALTER TABLE `proyecto_puesto` DISABLE KEYS */;
INSERT INTO `proyecto_puesto` VALUES (1,'Sistemas',1),(2,'Gerente de Zona',1),(3,'Administrador de AFI',1),(4,'Asistente Administrativo',1),(5,'Auxiliar de Adquisiciones',1),(6,'Auxiliar de AFI',1),(7,'Auxiliar de Almacen',1),(8,'Auxiliar de Tesorería',1),(9,'Coordinador Operativo',1),(10,'Estimaciones',1),(11,'Intendente',1),(12,'Jefe de Adquisiciones',1),(13,'Superintendente Operativo',1),(14,'Supervisor de Monitoreo',1),(15,'Supervisor de Telemetría',1),(16,'Asistente de Controles Técnicos',1),(17,'Técnico Operador de Tracto Camión',1),(18,'Inspector técnico de reparación',1),(19,'Analista de Precios Unitarios',1),(20,'Asistente de DG',1),(21,'Auxiliar Contable',1),(22,'Auxiliar de calidad',1),(23,'Auxiliar de HSE',1),(24,'Auxiliar en trámite de permisos PPTR',1),(25,'Ayudante Operativo',1),(26,'Cadista',1),(27,'Contador',1),(28,'Control de Calidad',1),(29,'Controles Tecnicos',1),(30,'Coordinador de Controles Técnicos',1),(31,'Coordinador de DG',1),(32,'Coordinador de HSE',1),(33,'Ingeniero de Diseño',1),(34,'Jefe de Almacén',1),(35,'Jefe de HSE',1),(36,'Jefe de Recursos Humanos',1),(37,'Jefe de redes y publicidad',1),(38,'Jefe de Tesorería',1),(39,'Paramedico',1),(40,'Psicólogo laboral',1),(41,'Superintendencia de Contratos y Licitaciones',1),(42,'Superintendente Administrativo',1),(43,'Superintendente de Sistemas de Gestión de Calidad',1),(44,'Superintendente Ingeniería',1),(45,'Supervisor Administrativo',1),(46,'Supervisor de Contratos y Licitaciones',1),(47,'Supervisor de Manufactura y Mantenimiento',1),(48,'Supervisor de Taller de Mantenimiento',1),(49,'Supervisor Operativo',1),(50,'Supervisor SCADA',1),(51,'Técnico Laboratorista',1),(52,'Tecnico de HSE',1),(53,'Técnico de Servicios Auxiliares',1),(54,'Técnico de Telemetria',1),(55,'Técnico Instrumentista',1),(56,'Técnico Operador de Bateria',1),(57,'Técnico Operador de producción',1),(58,'Técnico Armador',1),(59,'Técnico capturista operativo',1),(60,'Técnico de Registros',1),(61,'Técnico Electro-Mecánico',1),(62,'Técnico en Bombas de inserción',1),(63,'Técnico en varillas de succión',1),(64,'Técnico Operador de Grúa',1),(65,'Técnico operador de Llave Hidraulica',1),(66,'Técnico Operador de Tractor con chapoleadora',1),(67,'Técnico Operador Trifásico',1),(68,'Técnico Operativo',1),(69,'Técnico Pailero',1),(70,'Técnico Soldador',1),(71,'Técnico Tornero',1),(72,'Vigilante',1),(73,'Supervisor de Electromecánicos',1),(74,'Supervisor de Instalación',1),(75,'Superintendente de HSE',1),(76,'Supervisor de HSE',1),(77,'Auxiliar de Recursos Humanos',1);
/*!40000 ALTER TABLE `proyecto_puesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_registropatronal`
--

DROP TABLE IF EXISTS `proyecto_registropatronal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_registropatronal` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `patronal` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_registropatronal`
--

LOCK TABLES `proyecto_registropatronal` WRITE;
/*!40000 ALTER TABLE `proyecto_registropatronal` DISABLE KEYS */;
INSERT INTO `proyecto_registropatronal` VALUES (2,'F79 - 36050 - 10 - 1',1),(3,'F79 - 37560 - 10 - 8',1),(4,'E84 - 14716 - 10 - 7',1),(5,'E75 - 60308 - 10 - 7',1),(6,'F30 - 30661 - 10 - 9',1),(7,'F54 - 53150 - 10 - 6',1),(8,'E75 - 54603 - 10 - 9',1),(9,'F46 - 12343 - 10 - 8',1),(10,'F03 - 56255 - 10 - 2',1);
/*!40000 ALTER TABLE `proyecto_registropatronal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_ropa`
--

DROP TABLE IF EXISTS `proyecto_ropa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_ropa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ropa` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  `seleccionado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_ropa`
--

LOCK TABLES `proyecto_ropa` WRITE;
/*!40000 ALTER TABLE `proyecto_ropa` DISABLE KEYS */;
INSERT INTO `proyecto_ropa` VALUES (2,'Camisola',1,1),(3,'Pantalón',1,1),(4,'Camisa Blanca',1,0),(5,'Camisa Azul',1,0),(6,'Camisa Beige',1,0),(7,'Playera Polo',1,1),(8,'Overal',1,1),(9,'Botas',1,0);
/*!40000 ALTER TABLE `proyecto_ropa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_sangre`
--

DROP TABLE IF EXISTS `proyecto_sangre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_sangre` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sangre` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_sangre`
--

LOCK TABLES `proyecto_sangre` WRITE;
/*!40000 ALTER TABLE `proyecto_sangre` DISABLE KEYS */;
INSERT INTO `proyecto_sangre` VALUES (1,'A+',1),(2,'A-',1),(3,'B+',1),(4,'B-',1),(5,'AB+',1),(6,'AB-',1),(7,'O+',1),(8,'O-',1);
/*!40000 ALTER TABLE `proyecto_sangre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_sexo`
--

DROP TABLE IF EXISTS `proyecto_sexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_sexo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sexo` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_sexo`
--

LOCK TABLES `proyecto_sexo` WRITE;
/*!40000 ALTER TABLE `proyecto_sexo` DISABLE KEYS */;
INSERT INTO `proyecto_sexo` VALUES (1,'Femenino',0),(2,'Masculino',0);
/*!40000 ALTER TABLE `proyecto_sexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_status`
--

DROP TABLE IF EXISTS `proyecto_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_status` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nss` varchar(50) DEFAULT NULL,
  `curp` varchar(50) DEFAULT NULL,
  `rfc` varchar(50) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `profesion` varchar(50) DEFAULT NULL,
  `no_cedula` varchar(50) DEFAULT NULL,
  `ultimo_contrato_vence` date DEFAULT NULL,
  `domicilio` varchar(60) DEFAULT NULL,
  `fecha_planta_anterior` date DEFAULT NULL,
  `fecha_planta` date DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  `complete_costo` tinyint(1) NOT NULL,
  `complete_bancarios` tinyint(1) NOT NULL,
  `complete_vacaciones` tinyint(1) NOT NULL,
  `complete_uniformes` tinyint(1) NOT NULL,
  `complete_economicos` tinyint(1) NOT NULL,
  `estado_civil_id` bigint(20) DEFAULT NULL,
  `nivel_id` bigint(20) DEFAULT NULL,
  `perfil_id` bigint(20) DEFAULT NULL,
  `registro_patronal_id` bigint(20) DEFAULT NULL,
  `sexo_id` bigint(20) DEFAULT NULL,
  `tipo_de_contrato_id` bigint(20) DEFAULT NULL,
  `tipo_sangre_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_status_estado_civil_id_30ef4586_fk_proyecto_civil_id` (`estado_civil_id`),
  KEY `proyecto_status_nivel_id_5b4a0b7e_fk_proyecto_nivel_id` (`nivel_id`),
  KEY `proyecto_status_perfil_id_1e6bad6c_fk_proyecto_perfil_id` (`perfil_id`),
  KEY `proyecto_status_registro_patronal_id_6ef348a5_fk_proyecto_` (`registro_patronal_id`),
  KEY `proyecto_status_sexo_id_3b54327c_fk_proyecto_sexo_id` (`sexo_id`),
  KEY `proyecto_status_tipo_de_contrato_id_c0fc1684_fk_proyecto_` (`tipo_de_contrato_id`),
  KEY `proyecto_status_tipo_sangre_id_f0a88081_fk_proyecto_sangre_id` (`tipo_sangre_id`),
  CONSTRAINT `proyecto_status_estado_civil_id_30ef4586_fk_proyecto_civil_id` FOREIGN KEY (`estado_civil_id`) REFERENCES `proyecto_civil` (`id`),
  CONSTRAINT `proyecto_status_nivel_id_5b4a0b7e_fk_proyecto_nivel_id` FOREIGN KEY (`nivel_id`) REFERENCES `proyecto_nivel` (`id`),
  CONSTRAINT `proyecto_status_perfil_id_1e6bad6c_fk_proyecto_perfil_id` FOREIGN KEY (`perfil_id`) REFERENCES `proyecto_perfil` (`id`),
  CONSTRAINT `proyecto_status_registro_patronal_id_6ef348a5_fk_proyecto_` FOREIGN KEY (`registro_patronal_id`) REFERENCES `proyecto_registropatronal` (`id`),
  CONSTRAINT `proyecto_status_sexo_id_3b54327c_fk_proyecto_sexo_id` FOREIGN KEY (`sexo_id`) REFERENCES `proyecto_sexo` (`id`),
  CONSTRAINT `proyecto_status_tipo_de_contrato_id_c0fc1684_fk_proyecto_` FOREIGN KEY (`tipo_de_contrato_id`) REFERENCES `proyecto_contrato` (`id`),
  CONSTRAINT `proyecto_status_tipo_sangre_id_f0a88081_fk_proyecto_sangre_id` FOREIGN KEY (`tipo_sangre_id`) REFERENCES `proyecto_sangre` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_status`
--

LOCK TABLES `proyecto_status` WRITE;
/*!40000 ALTER TABLE `proyecto_status` DISABLE KEYS */;
INSERT INTO `proyecto_status` VALUES (1,NULL,NULL,NULL,'NR',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `proyecto_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_status_batch`
--

DROP TABLE IF EXISTS `proyecto_status_batch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_status_batch` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(100) NOT NULL,
  `uploaded` date NOT NULL,
  `activated` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_status_batch`
--

LOCK TABLES `proyecto_status_batch` WRITE;
/*!40000 ALTER TABLE `proyecto_status_batch` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyecto_status_batch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_subproyecto`
--

DROP TABLE IF EXISTS `proyecto_subproyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_subproyecto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subproyecto` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  `proyecto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_subproyecto_proyecto_id_042f8383_fk_proyecto_` (`proyecto_id`),
  CONSTRAINT `proyecto_subproyecto_proyecto_id_042f8383_fk_proyecto_` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto_proyecto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_subproyecto`
--

LOCK TABLES `proyecto_subproyecto` WRITE;
/*!40000 ALTER TABLE `proyecto_subproyecto` DISABLE KEYS */;
INSERT INTO `proyecto_subproyecto` VALUES (31,'Contabilidad',1,1),(32,'RH',1,1),(33,'Compras',1,1),(34,'Activos',1,1),(35,'Sistemas',1,1),(36,'Evaluación proveedores',1,1),(37,'Subdirector',1,1),(38,'Jurídico',1,2),(39,'Tesorería',1,2),(40,'Ventas',1,2),(41,'Contratos y licitaciones',1,2),(42,'Sub. Finanzas y ventas',1,2),(43,'Sub. Operaciones',1,3),(44,'SUBIDT',1,4),(45,'Indirecto IDT',1,4),(46,'Telemetría',1,4),(47,'ESTAFF DG',1,5),(48,'Controles técnicos',1,5),(49,'SEOV',1,5),(50,'Seguridad',1,5),(51,'Publicidad redes',1,5),(52,'DG Motos',1,5),(53,'Gastos  Mtto Oficina',1,6),(54,'Luz, teléfono y agua',1,6),(55,'Intendencia',1,6),(56,'RP',1,6),(57,'Seguridad privada',1,6),(58,'Sub. Administrativa',1,7),(59,'Sub. Finanzas y ventas',1,7),(60,'Sub. Operaciones',0,7),(61,'Sub. Ingeniería',1,7),(62,'Dirección general',1,7);
/*!40000 ALTER TABLE `proyecto_subproyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_tablavacaciones`
--

DROP TABLE IF EXISTS `proyecto_tablavacaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_tablavacaciones` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `years` int(11) DEFAULT NULL,
  `days` int(11) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_tablavacaciones`
--

LOCK TABLES `proyecto_tablavacaciones` WRITE;
/*!40000 ALTER TABLE `proyecto_tablavacaciones` DISABLE KEYS */;
INSERT INTO `proyecto_tablavacaciones` VALUES (1,1,8,1),(2,2,10,1),(3,3,12,1),(4,4,14,1),(5,5,16,1),(6,10,18,1),(7,15,20,1),(8,20,22,1),(9,25,24,1);
/*!40000 ALTER TABLE `proyecto_tablavacaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_tallas`
--

DROP TABLE IF EXISTS `proyecto_tallas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_tallas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `talla` varchar(50) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  `ropa_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_tallas_ropa_id_345fd002_fk_proyecto_ropa_id` (`ropa_id`),
  CONSTRAINT `proyecto_tallas_ropa_id_345fd002_fk_proyecto_ropa_id` FOREIGN KEY (`ropa_id`) REFERENCES `proyecto_ropa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_tallas`
--

LOCK TABLES `proyecto_tallas` WRITE;
/*!40000 ALTER TABLE `proyecto_tallas` DISABLE KEYS */;
INSERT INTO `proyecto_tallas` VALUES (1,'XCH',1,2),(2,'CH',1,2),(3,'M',1,2),(4,'G',1,2),(5,'XG',1,2),(6,'XCH',1,3),(7,'CH',1,3),(8,'G',1,3),(9,'XG',1,3),(11,'XCH',1,4),(12,'CH',1,4),(13,'M',1,4),(14,'G',1,4),(15,'XG',1,4),(16,'XCH',1,5),(17,'CH',1,5),(18,'M',1,5),(19,'G',1,5),(20,'XG',1,5),(21,'XCH',1,6),(22,'CH',1,6),(23,'M',1,6),(24,'G',1,6),(25,'XG',1,6),(26,'XCH',1,7),(27,'CH',1,7),(28,'M',1,7),(29,'G',1,7),(30,'XG',1,7),(31,'XCH',1,8),(32,'CH',1,8),(33,'M',1,8),(34,'G',1,8),(35,'XG',1,8),(36,'2',1,9),(37,'3',1,9),(38,'4',1,9),(39,'5',1,9),(40,'6',1,9),(41,'7',1,9),(42,'8',1,9),(43,'9',1,9),(44,'10',1,9);
/*!40000 ALTER TABLE `proyecto_tallas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_uniforme`
--

DROP TABLE IF EXISTS `proyecto_uniforme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_uniforme` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_entrega` date DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `complete` tinyint(1) NOT NULL,
  `orden_id` bigint(20) DEFAULT NULL,
  `ropa_id` bigint(20) DEFAULT NULL,
  `talla_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_uniforme_orden_id_26d5f980_fk_proyecto_uniformes_id` (`orden_id`),
  KEY `proyecto_uniforme_ropa_id_3db30d2d_fk_proyecto_ropa_id` (`ropa_id`),
  KEY `proyecto_uniforme_talla_id_37b92355_fk_proyecto_tallas_id` (`talla_id`),
  CONSTRAINT `proyecto_uniforme_orden_id_26d5f980_fk_proyecto_uniformes_id` FOREIGN KEY (`orden_id`) REFERENCES `proyecto_uniformes` (`id`),
  CONSTRAINT `proyecto_uniforme_ropa_id_3db30d2d_fk_proyecto_ropa_id` FOREIGN KEY (`ropa_id`) REFERENCES `proyecto_ropa` (`id`),
  CONSTRAINT `proyecto_uniforme_talla_id_37b92355_fk_proyecto_tallas_id` FOREIGN KEY (`talla_id`) REFERENCES `proyecto_tallas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_uniforme`
--

LOCK TABLES `proyecto_uniforme` WRITE;
/*!40000 ALTER TABLE `proyecto_uniforme` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyecto_uniforme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_uniformes`
--

DROP TABLE IF EXISTS `proyecto_uniformes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_uniformes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_pedido` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_uniformes_status_id_71cfe99b_fk_proyecto_status_id` (`status_id`),
  CONSTRAINT `proyecto_uniformes_status_id_71cfe99b_fk_proyecto_status_id` FOREIGN KEY (`status_id`) REFERENCES `proyecto_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_uniformes`
--

LOCK TABLES `proyecto_uniformes` WRITE;
/*!40000 ALTER TABLE `proyecto_uniformes` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyecto_uniformes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_userdatos`
--

DROP TABLE IF EXISTS `proyecto_userdatos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_userdatos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `distrito_id` bigint(20) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `proyecto_userdatos_distrito_id_72bf41c2_fk_proyecto_distrito_id` (`distrito_id`),
  CONSTRAINT `proyecto_userdatos_distrito_id_72bf41c2_fk_proyecto_distrito_id` FOREIGN KEY (`distrito_id`) REFERENCES `proyecto_distrito` (`id`),
  CONSTRAINT `proyecto_userdatos_user_id_004f4ed8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_userdatos`
--

LOCK TABLES `proyecto_userdatos` WRITE;
/*!40000 ALTER TABLE `proyecto_userdatos` DISABLE KEYS */;
INSERT INTO `proyecto_userdatos` VALUES (1,1,1),(2,1,6),(3,1,2),(4,1,3),(5,2,4),(6,3,5);
/*!40000 ALTER TABLE `proyecto_userdatos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto_vacaciones`
--

DROP TABLE IF EXISTS `proyecto_vacaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto_vacaciones` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `periodo` varchar(50) DEFAULT NULL,
  `dias_de_vacaciones` int(11) DEFAULT NULL,
  `dias_disfrutados` int(11) DEFAULT NULL,
  `total_pendiente` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `status_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_vacaciones_status_id_03f4667a_fk_proyecto_status_id` (`status_id`),
  CONSTRAINT `proyecto_vacaciones_status_id_03f4667a_fk_proyecto_status_id` FOREIGN KEY (`status_id`) REFERENCES `proyecto_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto_vacaciones`
--

LOCK TABLES `proyecto_vacaciones` WRITE;
/*!40000 ALTER TABLE `proyecto_vacaciones` DISABLE KEYS */;
INSERT INTO `proyecto_vacaciones` VALUES (1,NULL,0,0,0,'2022-09-13 22:50:15.434662','2022-09-13 22:50:15.434707',0,NULL);
/*!40000 ALTER TABLE `proyecto_vacaciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-18 17:56:35
