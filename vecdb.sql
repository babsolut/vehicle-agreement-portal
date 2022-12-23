-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2022 at 03:13 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vecdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `vectbl`
--

CREATE TABLE `vectbl` (
  `vecid` int(12) NOT NULL,
  `vecname` varchar(40) NOT NULL,
  `vecmode` varchar(40) NOT NULL,
  `regno` varchar(40) NOT NULL,
  `chasis` varchar(40) NOT NULL,
  `engno` varchar(40) NOT NULL,
  `color` varchar(40) NOT NULL,
  `vendorname` varchar(40) NOT NULL,
  `vendoraddr` varchar(200) NOT NULL,
  `buyername` varchar(40) NOT NULL,
  `buyeraddr` varchar(200) NOT NULL,
  `place` varchar(40) NOT NULL,
  `price` int(100) NOT NULL,
  `price_inwords` varchar(150) NOT NULL,
  `regdate` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vectbl`
--

INSERT INTO `vectbl` (`vecid`, `vecname`, `vecmode`, `regno`, `chasis`, `engno`, `color`, `vendorname`, `vendoraddr`, `buyername`, `buyeraddr`, `place`, `price`, `price_inwords`, `regdate`) VALUES
(1, 'Toyota ', 'Sienna', 'AKJ 234PK', 'frr55', '3e3e32w2', 'gold', 'Taye Alaba', 'ibadn', 'Idowu Taiwo', 'lagos', 'Ibadan', 200000, '', '02/06/2022'),
(2, 'Toyota ', 'Corrolla', 'AKJ 234PK', 'frr55', '3e3e32w2', 'gold', 'Segun John', 'ibadn', 'Kemi Alaba', 'lagos', 'Ibadan', 200000, '', '02/06/2022'),
(3, 'Toyota ', 'camry', 'ABJ 876 QA', 'frr55', 'hhh7u6y77', 'white', 'Ajakaye Thomas', 'Eko', 'Femi Olawale', 'Ikene', 'Ibadan', 40000000, '', '02/06/2022'),
(4, 'Nissan', 'Exterra', 'BDJ 120LK', 'fr4456y6', 'u8u87y6t', 'black', 'Queen Becks', 'lagos Island', 'Peter Buer', 'Ondo', 'Ibadan', 890, '', '02/06/2022'),
(5, 'Volkwagon', 'Passat', 'TYE 876 GD', 'jhg5434r', 'y767654', 'green', 'Ola Baba', 'ijyhtgr', 'Olu Babamo', 'juhyt', 'Ibadab', 500000, '', '02/06/2022'),
(6, 'Volks Wagon', 'Golf 3', 'GGE876TR', 'nhg554r4', 'kkiuh76y', 'blue', 'Babjide Sanwoolu', 'Lagos government', 'Seun Kuti', 'Kalakuta Republic, Lagos', 'Lagos', 3501202, 'Three million Five Hundred and Twelve THOUSAND', '05/06/2022'),
(7, 'Nissan', 'Almeira', 'BDJ 666 HGD', 'BHg5t4re4', 'kjh77665', 'red', 'Shade Adu', '2, lawson str, Idi Aro, Ibadan', 'Chief Babalade', 'osun state', 'Ibadan', 750000, 'Seven Hundred and Fifty Thousand ', '13/03/2022'),
(8, 'NIssan', 'pathfinder', 'abj120pj', 'sw223456', '87654t56', 'gold', 'alaba Alli', 'alaba, lagos', 'Akanni Omoro', 'ijegun, Lagos', 'Ibadan', 12000000, 'twelve million', '11/12/2022'),
(9, 'ALMERA', 'PINTO', 'UYTGR65', 'U7655', 'Y6665543', 'BLACK', 'SEUN KUTI', 'AAMIEDA AVENUE, LAGOS', 'JIDE KOSOKO', 'IBADAN OLUYOLE', 'LAGOS', 1800000, 'EIGHTEEN MILLION', '11/12/2022'),
(10, 'VOLKS WAGON', 'PASSAT', 'U7865', '76YTG', 'TTRE34', 'RED', 'TUNBOSUN ADEGOKE', '12, ADEGOKE NEW GARAGE, IBA', 'BISI ALAWIYE', 'ALAYIWE CLOSE, IBADAN', 'IBADAN', 560000, 'FIVE HUNDRED AND SIXTY THOUSAND', '11/12/2022');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `vectbl`
--
ALTER TABLE `vectbl`
  ADD PRIMARY KEY (`vecid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
