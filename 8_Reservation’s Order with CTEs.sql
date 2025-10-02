USE Restaurants;
GO

WITH ReservationOrderCounts AS
(
    SELECT
        r.RESERVATION_ID,
        COUNT(o.ORDER_ID) AS OrderCount
    FROM RESERVATION r
    LEFT JOIN [ORDER] o ON r.RESERVATION_ID = o.RESERVATION_ID
    GROUP BY r.RESERVATION_ID
)
SELECT 
    r.RESERVATION_ID,
    r.OrderCount
FROM ReservationOrderCounts r
WHERE r.OrderCount >= 2;
GO