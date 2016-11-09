
DELIMITER $$

CREATE PROCEDURE `sadfmcoz_dwtest`.`GetExchangeRateData`()
BEGIN

	CREATE TEMPORARY TABLE IF NOT EXISTS tblTimestamp AS 
	(
		SELECT 
		`timestamp` AS `timestamp`
		FROM `sadfmcoz_dwtest`.`exchangeRates` AS `exchangeRate` 
		GROUP BY DATE_FORMAT( `timestamp` , '%m-%d-%Y %H:00' ) 
		ORDER BY `timestamp` DESC LIMIT 20
	);

	SELECT DATE_FORMAT( `timestamp` , '%m-%d-%Y %H:00' ) AS `timestamp` ,
	 (SELECT `rate` AS `rate` FROM `sadfmcoz_dwtest`.`exchangeRates` 
	 WHERE `timestamp` <= `exchangeRate`.`timestamp` 
	 AND `fromCurrencyCode` = 'ZAR' 
	 AND `toCurrencyCode` = 'USD' 
	 ORDER BY `timestamp` DESC LIMIT 1 ) AS `ZAR-USD` ,
	 (SELECT `rate` AS `rate` FROM `sadfmcoz_dwtest`.`exchangeRates` 
	 WHERE `timestamp` <= `exchangeRate`.`timestamp` 
	 AND `fromCurrencyCode` = 'ZAR' 
	 AND `toCurrencyCode` = 'EUR' 
	 ORDER BY `timestamp` DESC LIMIT 1 ) AS `ZAR-EUR` ,
	 (SELECT `rate` AS `rate` FROM `sadfmcoz_dwtest`.`exchangeRates` 
	 WHERE `timestamp` <= `exchangeRate`.`timestamp` 
	 AND `fromCurrencyCode` = 'ZAR' 
	 AND `toCurrencyCode` = 'GBP' 
	 ORDER BY `timestamp` DESC LIMIT 1 ) AS `ZAR-GBP` 
	 FROM tblTimestamp AS `exchangeRate` 
	 GROUP BY DATE_FORMAT( `timestamp` , '%m-%d-%Y %H:00' ) 
	 ORDER BY `timestamp` ASC;
	 
	 
	 DROP TABLE tblTimestamp;

END $$

DELIMITER ;