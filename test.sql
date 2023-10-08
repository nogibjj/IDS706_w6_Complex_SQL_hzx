-- SELECT pc.Name AS CategoryName,
--     p.name AS ProductName
-- FROM [SalesLT].[ProductCategory] pc
-- INNER JOIN [SalesLT].[Product] p
--     ON pc.ProductCategoryId = p.ProductCategoryId;

-- INSERT INTO [SalesLT].[Product] (
--     [Name],
--     [ProductNumber],
--     [Color],
--     [ProductCategoryID],
--     [StandardCost],
--     [ListPrice],
--     [SellStartDate]
--  )
--  VALUES (
--     'myNewProduct',
--     123456789,
--     'NewColor',
--     1,
--     100,
--     100,
--     GETDATE()
--  );

-- SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName
-- FROM SalesLT.ProductCategory pc
-- JOIN SalesLT.Product p
-- ON pc.productcategoryid = p.productcategoryid;


-- find all the tables in the database
-- SELECT table_name = t.name
-- FROM sys.tables t
-- INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
-- ORDER BY t.name;

SELECT
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    soh.OrderDate AS PurchaseDate,
    SUM(sod.OrderQty * sod.UnitPrice) AS TotalPurchaseAmount
FROM
    SalesLT.Customer AS c
JOIN
    SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID
JOIN
    SalesLT.SalesOrderDetail AS sod ON soh.SalesOrderID = sod.SalesOrderID
GROUP BY
    c.CustomerID, c.FirstName, c.LastName, soh.OrderDate
ORDER BY
    TotalPurchaseAmount DESC;
