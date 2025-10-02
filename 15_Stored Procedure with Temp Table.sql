USE Restaurants;
GO

CREATE PROCEDURE sp_FutureReservedTables
AS
BEGIN
    -- Create temp table
    CREATE TABLE #FutureTables (
        TABLE_ID VARCHAR(10),
        RESERVATION_DATE DATE
    );

    -- Insert future reservations
    INSERT INTO #FutureTables(TABLE_ID, RESERVATION_DATE)
    SELECT TABLE_ID, RESERVATION_DATE
    FROM RESERVATION
    WHERE RESERVATION_DATE > GETDATE();

    -- Join with restaurants
    SELECT
        ft.TABLE_ID,
        ft.RESERVATION_DATE,
        r.RESTAURANT_ID,
        r.NAME AS RESTAURANT_NAME,
        r.ADDRESS,
        r.PHONE_NUMBER
    FROM #FutureTables ft
    INNER JOIN [TABLE] t ON ft.TABLE_ID = t.TABLE_ID
    INNER JOIN RESTAURANT r ON t.RESTAURANT_ID = r.RESTAURANT_ID;

    -- Drop temp table
    DROP TABLE #FutureTables;
END;
GO
