USE Restaurants;
GO

CREATE PROCEDURE sp_AddNewOrder
    @ReservationId VARCHAR(10),
    @EmployeeId VARCHAR(10),
    @OrderDate DATE,
    @TotalAmount DECIMAL(10,2)
AS
BEGIN
    -- Check if reservation exists
    IF NOT EXISTS (SELECT 1 FROM RESERVATION WHERE RESERVATION_ID = @ReservationId)
    BEGIN
        RAISERROR('Reservation does not exist.', 16, 1);
        RETURN;
    END

    -- Check if employee exists
    IF NOT EXISTS (SELECT 1 FROM EMPLOYEE WHERE EMPLOYEE_ID = @EmployeeId)
    BEGIN
        RAISERROR('Employee does not exist.', 16, 1);
        RETURN;
    END

    -- Insert new order
    INSERT INTO [ORDER] (ORDER_ID, EMPLOYEE_ID, RESERVATION_ID, ORDER_DATE, TOTAL_AMOUNT)
    VALUES (NEWID(), @EmployeeId, @ReservationId, @OrderDate, @TotalAmount);

    SELECT 'Order added successfully.' AS Message;
END;
GO
