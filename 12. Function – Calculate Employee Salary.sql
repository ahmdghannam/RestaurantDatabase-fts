USE Restaurants;
GO

CREATE FUNCTION fn_CalculateEmployeeSalary(@EmployeeId VARCHAR(10))
RETURNS INT
AS
BEGIN
    DECLARE @OrderCount INT;
    DECLARE @Rank INT;
    DECLARE @Salary INT;

    -- Get number of orders by employee
    SELECT @OrderCount = COUNT(*)
    FROM [ORDER]
    WHERE EMPLOYEE_ID = @EmployeeId;

    -- Determine rank based on position
    SELECT @Rank = CASE POSITION
                    WHEN 'VIPOrdersWaiter' THEN 5
                    WHEN 'StandardWaiter' THEN 4
                    WHEN 'AssistantWaiter' THEN 3
                    ELSE 1
                   END
    FROM EMPLOYEE
    WHERE EMPLOYEE_ID = @EmployeeId;

    -- Calculate salary
    SET @Salary = ISNULL(@OrderCount,0) * ISNULL(@Rank,1);

    RETURN @Salary;
END;
GO
