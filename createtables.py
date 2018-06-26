# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:45:42 2018

@author: Mfundo Bright Shabalala
"""

import sys
import MySQLdb


CONN = MySQLdb.connect(host="localhost", user="root", passwd="password", db="prml")
CURSOR = CONN.cursor()

try:
    CURSOR.execute("""
    DROP TABLE IF EXISTS OHLCV, Stocks, Exchange, Vendor, Holidays
                    """)
    print("Affected: %d " %CURSOR.rowcount)

except MySQLdb.Error, err:
    print("Error occured: %s " %err.args[0])
    print(err)

try:
    CURSOR.execute("""
    CREATE TABLE Exchange(ExchangeId SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                          Abbreviation VARCHAR(64) NOT NULL,
                          City VARCHAR(225) NULL,
                          Country VARCHAR(225) NULL,
                          Currency VARCHAR(64) NULL,
                          CreatedBy VARCHAR(64) NOT NULL,
                          Created TIMESTAMP NOT NULL DEFAULT NOW(),
                          LastUpdated TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW()
                          );

    CREATE TABLE Vendor(VendorId SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        VendorName VARCHAR(225) NOT NULL,
                        WebsiteURL VARCHAR(225) NULL,
                        SupportEmail VARCHAR(225) NULL,
                        CreatedBy VARCHAR(64) NOT NULL,
                        Created TIMESTAMP NOT NULL DEFAULT NOW(),
                        LastUpdated TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW()
                        );

    CREATE TABLE Stocks(StockId SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        Ticker CHAR(18) UNIQUE NOT NULL,
                        StockName VARCHAR(64) NULL,
                        CurrentMarket_cap BIGINT NULL,
                        CreatedBy VARCHAR(64) NOT NULL,
                        Created TIMESTAMP NOT NULL DEFAULT NOW(),
                        LastUpdated TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW()
                        );

    CREATE TABLE OHLCV(PriceId SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       Ticker CHAR(18) UNIQUE NOT NULL,
                       TradeDate DATETIME NOT NULL,
                       Open DECIMAL(18,4) NULL,
                       High DECIMAL(18,4) NULL,
                       Low DECIMAL(18,4) NULL,
                       Close DECIMAL(18,4) NULL,
                       Volume BIGINT NULL,
                       ExDividend DECIMAL(18,4) NULL,
                       SplitRatio DECIMAL(18,4) NULL,
                       AdjOpen DECIMAL(18,4) NULL,
                       AdjHigh DECIMAL(18,4) NULL,
                       AdjLow DECIMAL(18,4) NULL,
                       AdjClose DECIMAL(18,4) NULL,
                       AdjVolume BIGINT NULL,
                       MonthlyReturns DECIMAL(18,4) NULL,
                       MonthlyAdjReturns DECIMAL(18,4) NULL,
                       YearlyReturns DECIMAL(18,4) NULL,
                       YearlyAdjeturns DECIMAL(18,4) NULL,
                       Holiday_id SMALLINT NULL,
                       CreatedBy VARCHAR(64) NOT NULL,
                       Created TIMESTAMP NOT NULL DEFAULT NOW(),
                       LastUpdated TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
                       FOREIGN KEY(Ticker) REFERENCES Stocks(Ticker)
                       );

    CREATE TABLE Holidays(HolidayId SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                          HolidayDate DATETIME NOT NULL,
                          HolidayName VARCHAR(225) NULL,
                          CreatedBy VARCHAR(64) NOT NULL,
                          Created TIMESTAMP NOT NULL DEFAULT NOW(),
                          LastUpdated TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW()
                          )
                   """)

except MySQLdb.Error, err2:
    print("Error in creating stocks table")
    print(err2)
    sys.exit(1)
CURSOR.close()
CONN.close()

if __name__ == '__main__':
    pass
