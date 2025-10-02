USE Restaurants;
GO

WITH MenuItemSales AS
(
    SELECT
        mi.RESTAURANT_ID,
        mi.ITEM_ID,
        mi.NAME AS ITEM_NAME,
        SUM(oi.QUANTITY) AS TotalSold
    FROM ORDER_ITEM oi
    INNER JOIN [ORDER] o ON oi.ORDER_ID = o.ORDER_ID
    INNER JOIN MenuItems mi ON oi.ITEM_ID = mi.ITEM_ID
    WHERE MONTH(o.ORDER_DATE) = 10 AND YEAR(o.ORDER_DATE) = 2025
    GROUP BY mi.RESTAURANT_ID, mi.ITEM_ID, mi.NAME
),
RankedMenuItems AS
(
    SELECT
        ms.RESTAURANT_ID,
        r.NAME AS RESTAURANT_NAME,
        ms.ITEM_ID,
        ms.ITEM_NAME,
        ms.TotalSold,
        ROW_NUMBER() OVER (PARTITION BY ms.RESTAURANT_ID ORDER BY ms.TotalSold DESC) AS RankNum
    FROM MenuItemSales ms
    INNER JOIN RESTAURANT r ON ms.RESTAURANT_ID = r.RESTAURANT_ID
)
SELECT
    RESTAURANT_ID,
    RESTAURANT_NAME,
    ITEM_ID,
    ITEM_NAME,
    TotalSold
FROM RankedMenuItems
WHERE RankNum = 1
ORDER BY RESTAURANT_NAME;
GO
