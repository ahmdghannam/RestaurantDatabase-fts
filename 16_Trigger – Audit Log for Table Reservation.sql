CREATE TABLE AuditLog (
    AuditID INT IDENTITY PRIMARY KEY,
    RestaurantId VARCHAR(10),
    TableId VARCHAR(10),
    ReservationDate DATE,
    ChangeDate DATETIME DEFAULT GETDATE()
);
GO

CREATE TRIGGER trg_LogTableReservation
ON RESERVATION
AFTER INSERT
AS
BEGIN
    INSERT INTO AuditLog (RestaurantId, TableId, ReservationDate)
    SELECT
        i.RESTAURANT_ID,
        i.TABLE_ID,
        i.RESERVATION_DATE
    FROM inserted i;
END;
GO
