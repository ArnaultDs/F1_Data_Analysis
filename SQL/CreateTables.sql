CREATE TABLE [dbo].[SAS_CIRCUITS](
    [CIRCUIT_ID] [nvarchar] (100), 
    [NAME] [nvarchar] (250) NULL, 
    [COUNTRY] [nvarchar] (250) NULL,
    [COORDINATES] [nvarchar] (30) NULL,
    [LAST_YEAR] [int] NULL,  
    [EXTRA_DATA] [nvarchar] (250) NULL,  

) ON [PRIMARY]
GO