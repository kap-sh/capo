"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenConfigurationNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.aggregate
    import capo_glue.types.amazon_redshift_source
    import capo_glue.types.amazon_redshift_target
    import capo_glue.types.apply_mapping
    import capo_glue.types.athena_connector_source
    import capo_glue.types.basic_catalog_target
    import capo_glue.types.catalog_delta_source
    import capo_glue.types.catalog_hudi_source
    import capo_glue.types.catalog_iceberg_source
    import capo_glue.types.catalog_kafka_source
    import capo_glue.types.catalog_kinesis_source
    import capo_glue.types.catalog_source
    import capo_glue.types.connector_data_source
    import capo_glue.types.connector_data_target
    import capo_glue.types.custom_code
    import capo_glue.types.direct_jdbc_source
    import capo_glue.types.direct_kafka_source
    import capo_glue.types.direct_kinesis_source
    import capo_glue.types.drop_duplicates
    import capo_glue.types.drop_fields
    import capo_glue.types.drop_null_fields
    import capo_glue.types.dynamic_transform
    import capo_glue.types.dynamo_db_catalog_source
    import capo_glue.types.dynamo_dbelt_connector_source
    import capo_glue.types.evaluate_data_quality
    import capo_glue.types.evaluate_data_quality_multi_frame
    import capo_glue.types.fill_missing_values
    import capo_glue.types.filter
    import capo_glue.types.governed_catalog_source
    import capo_glue.types.governed_catalog_target
    import capo_glue.types.jdbc_connector_source
    import capo_glue.types.jdbc_connector_target
    import capo_glue.types.join
    import capo_glue.types.merge
    import capo_glue.types.microsoft_sql_server_catalog_source
    import capo_glue.types.microsoft_sql_server_catalog_target
    import capo_glue.types.my_sql_catalog_source
    import capo_glue.types.my_sql_catalog_target
    import capo_glue.types.oracle_sql_catalog_source
    import capo_glue.types.oracle_sql_catalog_target
    import capo_glue.types.pii_detection
    import capo_glue.types.postgre_sql_catalog_source
    import capo_glue.types.postgre_sql_catalog_target
    import capo_glue.types.recipe
    import capo_glue.types.redshift_source
    import capo_glue.types.redshift_target
    import capo_glue.types.relational_catalog_source
    import capo_glue.types.rename_field
    import capo_glue.types.route
    import capo_glue.types.s3_catalog_delta_source
    import capo_glue.types.s3_catalog_hudi_source
    import capo_glue.types.s3_catalog_iceberg_source
    import capo_glue.types.s3_catalog_source
    import capo_glue.types.s3_catalog_target
    import capo_glue.types.s3_csv_source
    import capo_glue.types.s3_delta_catalog_target
    import capo_glue.types.s3_delta_direct_target
    import capo_glue.types.s3_delta_source
    import capo_glue.types.s3_direct_target
    import capo_glue.types.s3_excel_source
    import capo_glue.types.s3_glue_parquet_target
    import capo_glue.types.s3_hudi_catalog_target
    import capo_glue.types.s3_hudi_direct_target
    import capo_glue.types.s3_hudi_source
    import capo_glue.types.s3_hyper_direct_target
    import capo_glue.types.s3_iceberg_catalog_target
    import capo_glue.types.s3_iceberg_direct_target
    import capo_glue.types.s3_json_source
    import capo_glue.types.s3_parquet_source
    import capo_glue.types.select_fields
    import capo_glue.types.select_from_collection
    import capo_glue.types.snowflake_source
    import capo_glue.types.snowflake_target
    import capo_glue.types.spark_connector_source
    import capo_glue.types.spark_connector_target
    import capo_glue.types.spark_sql
    import capo_glue.types.spigot
    import capo_glue.types.split_fields
    import capo_glue.types.union


class CodeGenConfigurationNode(TypedDict, closed=True):
    athena_connector_source: NotRequired[
        "capo_glue.types.athena_connector_source.AthenaConnectorSource"
    ]
    """<p>Specifies a connector to an Amazon Athena data source.</p>"""
    jdbc_connector_source: NotRequired[
        "capo_glue.types.jdbc_connector_source.JDBCConnectorSource"
    ]
    """<p>Specifies a connector to a JDBC data source.</p>"""
    spark_connector_source: NotRequired[
        "capo_glue.types.spark_connector_source.SparkConnectorSource"
    ]
    """<p>Specifies a connector to an Apache Spark data source.</p>"""
    catalog_source: NotRequired["capo_glue.types.catalog_source.CatalogSource"]
    """<p>Specifies a data store in the Glue Data Catalog.</p>"""
    redshift_source: NotRequired["capo_glue.types.redshift_source.RedshiftSource"]
    """<p>Specifies an Amazon Redshift data store.</p>"""
    s3_catalog_source: NotRequired["capo_glue.types.s3_catalog_source.S3CatalogSource"]
    """<p>Specifies an Amazon S3 data store in the Glue Data Catalog.</p>"""
    s3_csv_source: NotRequired["capo_glue.types.s3_csv_source.S3CsvSource"]
    """<p>Specifies a command-separated value (CSV) data store stored in Amazon S3.</p>"""
    s3_json_source: NotRequired["capo_glue.types.s3_json_source.S3JsonSource"]
    """<p>Specifies a JSON data store stored in Amazon S3.</p>"""
    s3_parquet_source: NotRequired["capo_glue.types.s3_parquet_source.S3ParquetSource"]
    """<p>Specifies an Apache Parquet data store stored in Amazon S3.</p>"""
    relational_catalog_source: NotRequired[
        "capo_glue.types.relational_catalog_source.RelationalCatalogSource"
    ]
    """<p>Specifies a relational catalog data store in the Glue Data Catalog.</p>"""
    dynamo_db_catalog_source: NotRequired[
        "capo_glue.types.dynamo_db_catalog_source.DynamoDBCatalogSource"
    ]
    """<p>Specifies a DynamoDBC Catalog data store in the Glue Data Catalog.</p>"""
    jdbc_connector_target: NotRequired[
        "capo_glue.types.jdbc_connector_target.JDBCConnectorTarget"
    ]
    """<p>Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.</p>"""
    spark_connector_target: NotRequired[
        "capo_glue.types.spark_connector_target.SparkConnectorTarget"
    ]
    """<p>Specifies a target that uses an Apache Spark connector.</p>"""
    catalog_target: NotRequired[
        "capo_glue.types.basic_catalog_target.BasicCatalogTarget"
    ]
    """<p>Specifies a target that uses a Glue Data Catalog table.</p>"""
    redshift_target: NotRequired["capo_glue.types.redshift_target.RedshiftTarget"]
    """<p>Specifies a target that uses Amazon Redshift.</p>"""
    s3_catalog_target: NotRequired["capo_glue.types.s3_catalog_target.S3CatalogTarget"]
    """<p>Specifies a data target that writes to Amazon S3 using the Glue Data Catalog.</p>"""
    s3_glue_parquet_target: NotRequired[
        "capo_glue.types.s3_glue_parquet_target.S3GlueParquetTarget"
    ]
    """<p>Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.</p>"""
    s3_direct_target: NotRequired["capo_glue.types.s3_direct_target.S3DirectTarget"]
    """<p>Specifies a data target that writes to Amazon S3.</p>"""
    apply_mapping: NotRequired["capo_glue.types.apply_mapping.ApplyMapping"]
    """<p>Specifies a transform that maps data property keys in the data source to data property keys in the data target. You can rename keys, modify the data types for keys, and choose which keys to drop from the dataset.</p>"""
    select_fields: NotRequired["capo_glue.types.select_fields.SelectFields"]
    """<p>Specifies a transform that chooses the data property keys that you want to keep.</p>"""
    drop_fields: NotRequired["capo_glue.types.drop_fields.DropFields"]
    """<p>Specifies a transform that chooses the data property keys that you want to drop.</p>"""
    rename_field: NotRequired["capo_glue.types.rename_field.RenameField"]
    """<p>Specifies a transform that renames a single data property key.</p>"""
    spigot: NotRequired["capo_glue.types.spigot.Spigot"]
    """<p>Specifies a transform that writes samples of the data to an Amazon S3 bucket.</p>"""
    join: NotRequired["capo_glue.types.join.Join"]
    """<p>Specifies a transform that joins two datasets into one dataset using a comparison phrase on the specified data property keys. You can use inner, outer, left, right, left semi, and left anti joins.</p>"""
    split_fields: NotRequired["capo_glue.types.split_fields.SplitFields"]
    """<p>Specifies a transform that splits data property keys into two <code>DynamicFrames</code>. The output is a collection of <code>DynamicFrames</code>: one with selected data property keys, and one with the remaining data property keys.</p>"""
    select_from_collection: NotRequired[
        "capo_glue.types.select_from_collection.SelectFromCollection"
    ]
    """<p>Specifies a transform that chooses one <code>DynamicFrame</code> from a collection of <code>DynamicFrames</code>. The output is the selected <code>DynamicFrame</code> </p>"""
    fill_missing_values: NotRequired[
        "capo_glue.types.fill_missing_values.FillMissingValues"
    ]
    """<p>Specifies a transform that locates records in the dataset that have missing values and adds a new field with a value determined by imputation. The input data set is used to train the machine learning model that determines what the missing value should be.</p>"""
    filter: NotRequired["capo_glue.types.filter.Filter"]
    """<p>Specifies a transform that splits a dataset into two, based on a filter condition.</p>"""
    custom_code: NotRequired["capo_glue.types.custom_code.CustomCode"]
    """<p>Specifies a transform that uses custom code you provide to perform the data transformation. The output is a collection of DynamicFrames.</p>"""
    spark_sql: NotRequired["capo_glue.types.spark_sql.SparkSQL"]
    """<p>Specifies a transform where you enter a SQL query using Spark SQL syntax to transform the data. The output is a single <code>DynamicFrame</code>.</p>"""
    direct_kinesis_source: NotRequired[
        "capo_glue.types.direct_kinesis_source.DirectKinesisSource"
    ]
    """<p>Specifies a direct Amazon Kinesis data source.</p>"""
    direct_kafka_source: NotRequired[
        "capo_glue.types.direct_kafka_source.DirectKafkaSource"
    ]
    """<p>Specifies an Apache Kafka data store.</p>"""
    catalog_kinesis_source: NotRequired[
        "capo_glue.types.catalog_kinesis_source.CatalogKinesisSource"
    ]
    """<p>Specifies a Kinesis data source in the Glue Data Catalog.</p>"""
    catalog_kafka_source: NotRequired[
        "capo_glue.types.catalog_kafka_source.CatalogKafkaSource"
    ]
    """<p>Specifies an Apache Kafka data store in the Data Catalog.</p>"""
    drop_null_fields: NotRequired["capo_glue.types.drop_null_fields.DropNullFields"]
    """<p>Specifies a transform that removes columns from the dataset if all values in the column are 'null'. By default, Glue Studio will recognize null objects, but some values such as empty strings, strings that are "null", -1 integers or other placeholders such as zeros, are not automatically recognized as nulls.</p>"""
    merge: NotRequired["capo_glue.types.merge.Merge"]
    """<p>Specifies a transform that merges a <code>DynamicFrame</code> with a staging <code>DynamicFrame</code> based on the specified primary keys to identify records. Duplicate records (records with the same primary keys) are not de-duplicated. </p>"""
    union: NotRequired["capo_glue.types.union.Union"]
    """<p>Specifies a transform that combines the rows from two or more datasets into a single result.</p>"""
    pii_detection: NotRequired["capo_glue.types.pii_detection.PIIDetection"]
    """<p>Specifies a transform that identifies, removes or masks PII data.</p>"""
    aggregate: NotRequired["capo_glue.types.aggregate.Aggregate"]
    """<p>Specifies a transform that groups rows by chosen fields and computes the aggregated value by specified function.</p>"""
    drop_duplicates: NotRequired["capo_glue.types.drop_duplicates.DropDuplicates"]
    """<p>Specifies a transform that removes rows of repeating data from a data set.</p>"""
    governed_catalog_target: NotRequired[
        "capo_glue.types.governed_catalog_target.GovernedCatalogTarget"
    ]
    """<p>Specifies a data target that writes to a goverened catalog.</p>"""
    governed_catalog_source: NotRequired[
        "capo_glue.types.governed_catalog_source.GovernedCatalogSource"
    ]
    """<p>Specifies a data source in a goverened Data Catalog.</p>"""
    microsoft_sql_server_catalog_source: NotRequired[
        "capo_glue.types.microsoft_sql_server_catalog_source.MicrosoftSQLServerCatalogSource"
    ]
    """<p>Specifies a Microsoft SQL server data source in the Glue Data Catalog.</p>"""
    my_sql_catalog_source: NotRequired[
        "capo_glue.types.my_sql_catalog_source.MySQLCatalogSource"
    ]
    """<p>Specifies a MySQL data source in the Glue Data Catalog.</p>"""
    oracle_sql_catalog_source: NotRequired[
        "capo_glue.types.oracle_sql_catalog_source.OracleSQLCatalogSource"
    ]
    """<p>Specifies an Oracle data source in the Glue Data Catalog.</p>"""
    postgre_sql_catalog_source: NotRequired[
        "capo_glue.types.postgre_sql_catalog_source.PostgreSQLCatalogSource"
    ]
    """<p>Specifies a PostgresSQL data source in the Glue Data Catalog.</p>"""
    microsoft_sql_server_catalog_target: NotRequired[
        "capo_glue.types.microsoft_sql_server_catalog_target.MicrosoftSQLServerCatalogTarget"
    ]
    """<p>Specifies a target that uses Microsoft SQL.</p>"""
    my_sql_catalog_target: NotRequired[
        "capo_glue.types.my_sql_catalog_target.MySQLCatalogTarget"
    ]
    """<p>Specifies a target that uses MySQL.</p>"""
    oracle_sql_catalog_target: NotRequired[
        "capo_glue.types.oracle_sql_catalog_target.OracleSQLCatalogTarget"
    ]
    """<p>Specifies a target that uses Oracle SQL.</p>"""
    postgre_sql_catalog_target: NotRequired[
        "capo_glue.types.postgre_sql_catalog_target.PostgreSQLCatalogTarget"
    ]
    """<p>Specifies a target that uses Postgres SQL.</p>"""
    route: NotRequired["capo_glue.types.route.Route"]
    """<p>Specifies a route node that directs data to different output paths based on defined filtering conditions.</p>"""
    dynamic_transform: NotRequired["capo_glue.types.dynamic_transform.DynamicTransform"]
    """<p>Specifies a custom visual transform created by a user.</p>"""
    evaluate_data_quality: NotRequired[
        "capo_glue.types.evaluate_data_quality.EvaluateDataQuality"
    ]
    """<p>Specifies your data quality evaluation criteria.</p>"""
    s3_catalog_hudi_source: NotRequired[
        "capo_glue.types.s3_catalog_hudi_source.S3CatalogHudiSource"
    ]
    """<p>Specifies a Hudi data source that is registered in the Glue Data Catalog. The data source must be stored in Amazon S3.</p>"""
    catalog_hudi_source: NotRequired[
        "capo_glue.types.catalog_hudi_source.CatalogHudiSource"
    ]
    """<p>Specifies a Hudi data source that is registered in the Glue Data Catalog.</p>"""
    s3_hudi_source: NotRequired["capo_glue.types.s3_hudi_source.S3HudiSource"]
    """<p>Specifies a Hudi data source stored in Amazon S3.</p>"""
    s3_hudi_catalog_target: NotRequired[
        "capo_glue.types.s3_hudi_catalog_target.S3HudiCatalogTarget"
    ]
    """<p>Specifies a target that writes to a Hudi data source in the Glue Data Catalog.</p>"""
    s3_hudi_direct_target: NotRequired[
        "capo_glue.types.s3_hudi_direct_target.S3HudiDirectTarget"
    ]
    """<p>Specifies a target that writes to a Hudi data source in Amazon S3.</p>"""
    direct_jdbc_source: NotRequired[
        "capo_glue.types.direct_jdbc_source.DirectJDBCSource"
    ]
    s3_catalog_delta_source: NotRequired[
        "capo_glue.types.s3_catalog_delta_source.S3CatalogDeltaSource"
    ]
    """<p>Specifies a Delta Lake data source that is registered in the Glue Data Catalog. The data source must be stored in Amazon S3.</p>"""
    catalog_delta_source: NotRequired[
        "capo_glue.types.catalog_delta_source.CatalogDeltaSource"
    ]
    """<p>Specifies a Delta Lake data source that is registered in the Glue Data Catalog.</p>"""
    s3_delta_source: NotRequired["capo_glue.types.s3_delta_source.S3DeltaSource"]
    """<p>Specifies a Delta Lake data source stored in Amazon S3.</p>"""
    s3_delta_catalog_target: NotRequired[
        "capo_glue.types.s3_delta_catalog_target.S3DeltaCatalogTarget"
    ]
    """<p>Specifies a target that writes to a Delta Lake data source in the Glue Data Catalog.</p>"""
    s3_delta_direct_target: NotRequired[
        "capo_glue.types.s3_delta_direct_target.S3DeltaDirectTarget"
    ]
    """<p>Specifies a target that writes to a Delta Lake data source in Amazon S3.</p>"""
    amazon_redshift_source: NotRequired[
        "capo_glue.types.amazon_redshift_source.AmazonRedshiftSource"
    ]
    """<p>Specifies a target that writes to a data source in Amazon Redshift.</p>"""
    amazon_redshift_target: NotRequired[
        "capo_glue.types.amazon_redshift_target.AmazonRedshiftTarget"
    ]
    """<p>Specifies a target that writes to a data target in Amazon Redshift.</p>"""
    evaluate_data_quality_multi_frame: NotRequired[
        "capo_glue.types.evaluate_data_quality_multi_frame.EvaluateDataQualityMultiFrame"
    ]
    """<p>Specifies your data quality evaluation criteria. Allows multiple input data and returns a collection of Dynamic Frames.</p>"""
    recipe: NotRequired["capo_glue.types.recipe.Recipe"]
    """<p>Specifies a Glue DataBrew recipe node.</p>"""
    snowflake_source: NotRequired["capo_glue.types.snowflake_source.SnowflakeSource"]
    """<p>Specifies a Snowflake data source.</p>"""
    snowflake_target: NotRequired["capo_glue.types.snowflake_target.SnowflakeTarget"]
    """<p>Specifies a target that writes to a Snowflake data source.</p>"""
    connector_data_source: NotRequired[
        "capo_glue.types.connector_data_source.ConnectorDataSource"
    ]
    """<p>Specifies a source generated with standard connection options.</p>"""
    connector_data_target: NotRequired[
        "capo_glue.types.connector_data_target.ConnectorDataTarget"
    ]
    """<p>Specifies a target generated with standard connection options.</p>"""
    s3_catalog_iceberg_source: NotRequired[
        "capo_glue.types.s3_catalog_iceberg_source.S3CatalogIcebergSource"
    ]
    """<p>Specifies an Apache Iceberg data source that is registered in the Glue Data Catalog. The Iceberg data source must be stored in Amazon S3.</p>"""
    catalog_iceberg_source: NotRequired[
        "capo_glue.types.catalog_iceberg_source.CatalogIcebergSource"
    ]
    """<p>Specifies an Apache Iceberg data source that is registered in the Glue Data Catalog.</p>"""
    s3_iceberg_catalog_target: NotRequired[
        "capo_glue.types.s3_iceberg_catalog_target.S3IcebergCatalogTarget"
    ]
    """<p>Specifies an Apache Iceberg catalog target that writes data to Amazon S3 and registers the table in the Glue Data Catalog.</p>"""
    s3_iceberg_direct_target: NotRequired[
        "capo_glue.types.s3_iceberg_direct_target.S3IcebergDirectTarget"
    ]
    """<p>Defines configuration parameters for writing data to Amazon S3 as an Apache Iceberg table.</p>"""
    s3_excel_source: NotRequired["capo_glue.types.s3_excel_source.S3ExcelSource"]
    """<p>Defines configuration parameters for reading Excel files from Amazon S3.</p>"""
    s3_hyper_direct_target: NotRequired[
        "capo_glue.types.s3_hyper_direct_target.S3HyperDirectTarget"
    ]
    """<p>Defines configuration parameters for writing data to Amazon S3 using HyperDirect optimization.</p>"""
    dynamo_dbelt_connector_source: NotRequired[
        "capo_glue.types.dynamo_dbelt_connector_source.DynamoDBELTConnectorSource"
    ]
    """<p>Specifies a DynamoDB ELT connector source for extracting data from DynamoDB tables.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeGenConfigurationNode) -> dict:
    out: dict = {}
    if "athena_connector_source" in value:
        import capo_glue.types.athena_connector_source

        out["AthenaConnectorSource"] = (
            capo_glue.types.athena_connector_source.serialize_aws_json_1_1(
                value["athena_connector_source"]
            )
        )
    if "jdbc_connector_source" in value:
        import capo_glue.types.jdbc_connector_source

        out["JDBCConnectorSource"] = (
            capo_glue.types.jdbc_connector_source.serialize_aws_json_1_1(
                value["jdbc_connector_source"]
            )
        )
    if "spark_connector_source" in value:
        import capo_glue.types.spark_connector_source

        out["SparkConnectorSource"] = (
            capo_glue.types.spark_connector_source.serialize_aws_json_1_1(
                value["spark_connector_source"]
            )
        )
    if "catalog_source" in value:
        import capo_glue.types.catalog_source

        out["CatalogSource"] = capo_glue.types.catalog_source.serialize_aws_json_1_1(
            value["catalog_source"]
        )
    if "redshift_source" in value:
        import capo_glue.types.redshift_source

        out["RedshiftSource"] = capo_glue.types.redshift_source.serialize_aws_json_1_1(
            value["redshift_source"]
        )
    if "s3_catalog_source" in value:
        import capo_glue.types.s3_catalog_source

        out["S3CatalogSource"] = (
            capo_glue.types.s3_catalog_source.serialize_aws_json_1_1(
                value["s3_catalog_source"]
            )
        )
    if "s3_csv_source" in value:
        import capo_glue.types.s3_csv_source

        out["S3CsvSource"] = capo_glue.types.s3_csv_source.serialize_aws_json_1_1(
            value["s3_csv_source"]
        )
    if "s3_json_source" in value:
        import capo_glue.types.s3_json_source

        out["S3JsonSource"] = capo_glue.types.s3_json_source.serialize_aws_json_1_1(
            value["s3_json_source"]
        )
    if "s3_parquet_source" in value:
        import capo_glue.types.s3_parquet_source

        out["S3ParquetSource"] = (
            capo_glue.types.s3_parquet_source.serialize_aws_json_1_1(
                value["s3_parquet_source"]
            )
        )
    if "relational_catalog_source" in value:
        import capo_glue.types.relational_catalog_source

        out["RelationalCatalogSource"] = (
            capo_glue.types.relational_catalog_source.serialize_aws_json_1_1(
                value["relational_catalog_source"]
            )
        )
    if "dynamo_db_catalog_source" in value:
        import capo_glue.types.dynamo_db_catalog_source

        out["DynamoDBCatalogSource"] = (
            capo_glue.types.dynamo_db_catalog_source.serialize_aws_json_1_1(
                value["dynamo_db_catalog_source"]
            )
        )
    if "jdbc_connector_target" in value:
        import capo_glue.types.jdbc_connector_target

        out["JDBCConnectorTarget"] = (
            capo_glue.types.jdbc_connector_target.serialize_aws_json_1_1(
                value["jdbc_connector_target"]
            )
        )
    if "spark_connector_target" in value:
        import capo_glue.types.spark_connector_target

        out["SparkConnectorTarget"] = (
            capo_glue.types.spark_connector_target.serialize_aws_json_1_1(
                value["spark_connector_target"]
            )
        )
    if "catalog_target" in value:
        import capo_glue.types.basic_catalog_target

        out["CatalogTarget"] = (
            capo_glue.types.basic_catalog_target.serialize_aws_json_1_1(
                value["catalog_target"]
            )
        )
    if "redshift_target" in value:
        import capo_glue.types.redshift_target

        out["RedshiftTarget"] = capo_glue.types.redshift_target.serialize_aws_json_1_1(
            value["redshift_target"]
        )
    if "s3_catalog_target" in value:
        import capo_glue.types.s3_catalog_target

        out["S3CatalogTarget"] = (
            capo_glue.types.s3_catalog_target.serialize_aws_json_1_1(
                value["s3_catalog_target"]
            )
        )
    if "s3_glue_parquet_target" in value:
        import capo_glue.types.s3_glue_parquet_target

        out["S3GlueParquetTarget"] = (
            capo_glue.types.s3_glue_parquet_target.serialize_aws_json_1_1(
                value["s3_glue_parquet_target"]
            )
        )
    if "s3_direct_target" in value:
        import capo_glue.types.s3_direct_target

        out["S3DirectTarget"] = capo_glue.types.s3_direct_target.serialize_aws_json_1_1(
            value["s3_direct_target"]
        )
    if "apply_mapping" in value:
        import capo_glue.types.apply_mapping

        out["ApplyMapping"] = capo_glue.types.apply_mapping.serialize_aws_json_1_1(
            value["apply_mapping"]
        )
    if "select_fields" in value:
        import capo_glue.types.select_fields

        out["SelectFields"] = capo_glue.types.select_fields.serialize_aws_json_1_1(
            value["select_fields"]
        )
    if "drop_fields" in value:
        import capo_glue.types.drop_fields

        out["DropFields"] = capo_glue.types.drop_fields.serialize_aws_json_1_1(
            value["drop_fields"]
        )
    if "rename_field" in value:
        import capo_glue.types.rename_field

        out["RenameField"] = capo_glue.types.rename_field.serialize_aws_json_1_1(
            value["rename_field"]
        )
    if "spigot" in value:
        import capo_glue.types.spigot

        out["Spigot"] = capo_glue.types.spigot.serialize_aws_json_1_1(value["spigot"])
    if "join" in value:
        import capo_glue.types.join

        out["Join"] = capo_glue.types.join.serialize_aws_json_1_1(value["join"])
    if "split_fields" in value:
        import capo_glue.types.split_fields

        out["SplitFields"] = capo_glue.types.split_fields.serialize_aws_json_1_1(
            value["split_fields"]
        )
    if "select_from_collection" in value:
        import capo_glue.types.select_from_collection

        out["SelectFromCollection"] = (
            capo_glue.types.select_from_collection.serialize_aws_json_1_1(
                value["select_from_collection"]
            )
        )
    if "fill_missing_values" in value:
        import capo_glue.types.fill_missing_values

        out["FillMissingValues"] = (
            capo_glue.types.fill_missing_values.serialize_aws_json_1_1(
                value["fill_missing_values"]
            )
        )
    if "filter" in value:
        import capo_glue.types.filter

        out["Filter"] = capo_glue.types.filter.serialize_aws_json_1_1(value["filter"])
    if "custom_code" in value:
        import capo_glue.types.custom_code

        out["CustomCode"] = capo_glue.types.custom_code.serialize_aws_json_1_1(
            value["custom_code"]
        )
    if "spark_sql" in value:
        import capo_glue.types.spark_sql

        out["SparkSQL"] = capo_glue.types.spark_sql.serialize_aws_json_1_1(
            value["spark_sql"]
        )
    if "direct_kinesis_source" in value:
        import capo_glue.types.direct_kinesis_source

        out["DirectKinesisSource"] = (
            capo_glue.types.direct_kinesis_source.serialize_aws_json_1_1(
                value["direct_kinesis_source"]
            )
        )
    if "direct_kafka_source" in value:
        import capo_glue.types.direct_kafka_source

        out["DirectKafkaSource"] = (
            capo_glue.types.direct_kafka_source.serialize_aws_json_1_1(
                value["direct_kafka_source"]
            )
        )
    if "catalog_kinesis_source" in value:
        import capo_glue.types.catalog_kinesis_source

        out["CatalogKinesisSource"] = (
            capo_glue.types.catalog_kinesis_source.serialize_aws_json_1_1(
                value["catalog_kinesis_source"]
            )
        )
    if "catalog_kafka_source" in value:
        import capo_glue.types.catalog_kafka_source

        out["CatalogKafkaSource"] = (
            capo_glue.types.catalog_kafka_source.serialize_aws_json_1_1(
                value["catalog_kafka_source"]
            )
        )
    if "drop_null_fields" in value:
        import capo_glue.types.drop_null_fields

        out["DropNullFields"] = capo_glue.types.drop_null_fields.serialize_aws_json_1_1(
            value["drop_null_fields"]
        )
    if "merge" in value:
        import capo_glue.types.merge

        out["Merge"] = capo_glue.types.merge.serialize_aws_json_1_1(value["merge"])
    if "union" in value:
        import capo_glue.types.union

        out["Union"] = capo_glue.types.union.serialize_aws_json_1_1(value["union"])
    if "pii_detection" in value:
        import capo_glue.types.pii_detection

        out["PIIDetection"] = capo_glue.types.pii_detection.serialize_aws_json_1_1(
            value["pii_detection"]
        )
    if "aggregate" in value:
        import capo_glue.types.aggregate

        out["Aggregate"] = capo_glue.types.aggregate.serialize_aws_json_1_1(
            value["aggregate"]
        )
    if "drop_duplicates" in value:
        import capo_glue.types.drop_duplicates

        out["DropDuplicates"] = capo_glue.types.drop_duplicates.serialize_aws_json_1_1(
            value["drop_duplicates"]
        )
    if "governed_catalog_target" in value:
        import capo_glue.types.governed_catalog_target

        out["GovernedCatalogTarget"] = (
            capo_glue.types.governed_catalog_target.serialize_aws_json_1_1(
                value["governed_catalog_target"]
            )
        )
    if "governed_catalog_source" in value:
        import capo_glue.types.governed_catalog_source

        out["GovernedCatalogSource"] = (
            capo_glue.types.governed_catalog_source.serialize_aws_json_1_1(
                value["governed_catalog_source"]
            )
        )
    if "microsoft_sql_server_catalog_source" in value:
        import capo_glue.types.microsoft_sql_server_catalog_source

        out["MicrosoftSQLServerCatalogSource"] = (
            capo_glue.types.microsoft_sql_server_catalog_source.serialize_aws_json_1_1(
                value["microsoft_sql_server_catalog_source"]
            )
        )
    if "my_sql_catalog_source" in value:
        import capo_glue.types.my_sql_catalog_source

        out["MySQLCatalogSource"] = (
            capo_glue.types.my_sql_catalog_source.serialize_aws_json_1_1(
                value["my_sql_catalog_source"]
            )
        )
    if "oracle_sql_catalog_source" in value:
        import capo_glue.types.oracle_sql_catalog_source

        out["OracleSQLCatalogSource"] = (
            capo_glue.types.oracle_sql_catalog_source.serialize_aws_json_1_1(
                value["oracle_sql_catalog_source"]
            )
        )
    if "postgre_sql_catalog_source" in value:
        import capo_glue.types.postgre_sql_catalog_source

        out["PostgreSQLCatalogSource"] = (
            capo_glue.types.postgre_sql_catalog_source.serialize_aws_json_1_1(
                value["postgre_sql_catalog_source"]
            )
        )
    if "microsoft_sql_server_catalog_target" in value:
        import capo_glue.types.microsoft_sql_server_catalog_target

        out["MicrosoftSQLServerCatalogTarget"] = (
            capo_glue.types.microsoft_sql_server_catalog_target.serialize_aws_json_1_1(
                value["microsoft_sql_server_catalog_target"]
            )
        )
    if "my_sql_catalog_target" in value:
        import capo_glue.types.my_sql_catalog_target

        out["MySQLCatalogTarget"] = (
            capo_glue.types.my_sql_catalog_target.serialize_aws_json_1_1(
                value["my_sql_catalog_target"]
            )
        )
    if "oracle_sql_catalog_target" in value:
        import capo_glue.types.oracle_sql_catalog_target

        out["OracleSQLCatalogTarget"] = (
            capo_glue.types.oracle_sql_catalog_target.serialize_aws_json_1_1(
                value["oracle_sql_catalog_target"]
            )
        )
    if "postgre_sql_catalog_target" in value:
        import capo_glue.types.postgre_sql_catalog_target

        out["PostgreSQLCatalogTarget"] = (
            capo_glue.types.postgre_sql_catalog_target.serialize_aws_json_1_1(
                value["postgre_sql_catalog_target"]
            )
        )
    if "route" in value:
        import capo_glue.types.route

        out["Route"] = capo_glue.types.route.serialize_aws_json_1_1(value["route"])
    if "dynamic_transform" in value:
        import capo_glue.types.dynamic_transform

        out["DynamicTransform"] = (
            capo_glue.types.dynamic_transform.serialize_aws_json_1_1(
                value["dynamic_transform"]
            )
        )
    if "evaluate_data_quality" in value:
        import capo_glue.types.evaluate_data_quality

        out["EvaluateDataQuality"] = (
            capo_glue.types.evaluate_data_quality.serialize_aws_json_1_1(
                value["evaluate_data_quality"]
            )
        )
    if "s3_catalog_hudi_source" in value:
        import capo_glue.types.s3_catalog_hudi_source

        out["S3CatalogHudiSource"] = (
            capo_glue.types.s3_catalog_hudi_source.serialize_aws_json_1_1(
                value["s3_catalog_hudi_source"]
            )
        )
    if "catalog_hudi_source" in value:
        import capo_glue.types.catalog_hudi_source

        out["CatalogHudiSource"] = (
            capo_glue.types.catalog_hudi_source.serialize_aws_json_1_1(
                value["catalog_hudi_source"]
            )
        )
    if "s3_hudi_source" in value:
        import capo_glue.types.s3_hudi_source

        out["S3HudiSource"] = capo_glue.types.s3_hudi_source.serialize_aws_json_1_1(
            value["s3_hudi_source"]
        )
    if "s3_hudi_catalog_target" in value:
        import capo_glue.types.s3_hudi_catalog_target

        out["S3HudiCatalogTarget"] = (
            capo_glue.types.s3_hudi_catalog_target.serialize_aws_json_1_1(
                value["s3_hudi_catalog_target"]
            )
        )
    if "s3_hudi_direct_target" in value:
        import capo_glue.types.s3_hudi_direct_target

        out["S3HudiDirectTarget"] = (
            capo_glue.types.s3_hudi_direct_target.serialize_aws_json_1_1(
                value["s3_hudi_direct_target"]
            )
        )
    if "direct_jdbc_source" in value:
        import capo_glue.types.direct_jdbc_source

        out["DirectJDBCSource"] = (
            capo_glue.types.direct_jdbc_source.serialize_aws_json_1_1(
                value["direct_jdbc_source"]
            )
        )
    if "s3_catalog_delta_source" in value:
        import capo_glue.types.s3_catalog_delta_source

        out["S3CatalogDeltaSource"] = (
            capo_glue.types.s3_catalog_delta_source.serialize_aws_json_1_1(
                value["s3_catalog_delta_source"]
            )
        )
    if "catalog_delta_source" in value:
        import capo_glue.types.catalog_delta_source

        out["CatalogDeltaSource"] = (
            capo_glue.types.catalog_delta_source.serialize_aws_json_1_1(
                value["catalog_delta_source"]
            )
        )
    if "s3_delta_source" in value:
        import capo_glue.types.s3_delta_source

        out["S3DeltaSource"] = capo_glue.types.s3_delta_source.serialize_aws_json_1_1(
            value["s3_delta_source"]
        )
    if "s3_delta_catalog_target" in value:
        import capo_glue.types.s3_delta_catalog_target

        out["S3DeltaCatalogTarget"] = (
            capo_glue.types.s3_delta_catalog_target.serialize_aws_json_1_1(
                value["s3_delta_catalog_target"]
            )
        )
    if "s3_delta_direct_target" in value:
        import capo_glue.types.s3_delta_direct_target

        out["S3DeltaDirectTarget"] = (
            capo_glue.types.s3_delta_direct_target.serialize_aws_json_1_1(
                value["s3_delta_direct_target"]
            )
        )
    if "amazon_redshift_source" in value:
        import capo_glue.types.amazon_redshift_source

        out["AmazonRedshiftSource"] = (
            capo_glue.types.amazon_redshift_source.serialize_aws_json_1_1(
                value["amazon_redshift_source"]
            )
        )
    if "amazon_redshift_target" in value:
        import capo_glue.types.amazon_redshift_target

        out["AmazonRedshiftTarget"] = (
            capo_glue.types.amazon_redshift_target.serialize_aws_json_1_1(
                value["amazon_redshift_target"]
            )
        )
    if "evaluate_data_quality_multi_frame" in value:
        import capo_glue.types.evaluate_data_quality_multi_frame

        out["EvaluateDataQualityMultiFrame"] = (
            capo_glue.types.evaluate_data_quality_multi_frame.serialize_aws_json_1_1(
                value["evaluate_data_quality_multi_frame"]
            )
        )
    if "recipe" in value:
        import capo_glue.types.recipe

        out["Recipe"] = capo_glue.types.recipe.serialize_aws_json_1_1(value["recipe"])
    if "snowflake_source" in value:
        import capo_glue.types.snowflake_source

        out["SnowflakeSource"] = (
            capo_glue.types.snowflake_source.serialize_aws_json_1_1(
                value["snowflake_source"]
            )
        )
    if "snowflake_target" in value:
        import capo_glue.types.snowflake_target

        out["SnowflakeTarget"] = (
            capo_glue.types.snowflake_target.serialize_aws_json_1_1(
                value["snowflake_target"]
            )
        )
    if "connector_data_source" in value:
        import capo_glue.types.connector_data_source

        out["ConnectorDataSource"] = (
            capo_glue.types.connector_data_source.serialize_aws_json_1_1(
                value["connector_data_source"]
            )
        )
    if "connector_data_target" in value:
        import capo_glue.types.connector_data_target

        out["ConnectorDataTarget"] = (
            capo_glue.types.connector_data_target.serialize_aws_json_1_1(
                value["connector_data_target"]
            )
        )
    if "s3_catalog_iceberg_source" in value:
        import capo_glue.types.s3_catalog_iceberg_source

        out["S3CatalogIcebergSource"] = (
            capo_glue.types.s3_catalog_iceberg_source.serialize_aws_json_1_1(
                value["s3_catalog_iceberg_source"]
            )
        )
    if "catalog_iceberg_source" in value:
        import capo_glue.types.catalog_iceberg_source

        out["CatalogIcebergSource"] = (
            capo_glue.types.catalog_iceberg_source.serialize_aws_json_1_1(
                value["catalog_iceberg_source"]
            )
        )
    if "s3_iceberg_catalog_target" in value:
        import capo_glue.types.s3_iceberg_catalog_target

        out["S3IcebergCatalogTarget"] = (
            capo_glue.types.s3_iceberg_catalog_target.serialize_aws_json_1_1(
                value["s3_iceberg_catalog_target"]
            )
        )
    if "s3_iceberg_direct_target" in value:
        import capo_glue.types.s3_iceberg_direct_target

        out["S3IcebergDirectTarget"] = (
            capo_glue.types.s3_iceberg_direct_target.serialize_aws_json_1_1(
                value["s3_iceberg_direct_target"]
            )
        )
    if "s3_excel_source" in value:
        import capo_glue.types.s3_excel_source

        out["S3ExcelSource"] = capo_glue.types.s3_excel_source.serialize_aws_json_1_1(
            value["s3_excel_source"]
        )
    if "s3_hyper_direct_target" in value:
        import capo_glue.types.s3_hyper_direct_target

        out["S3HyperDirectTarget"] = (
            capo_glue.types.s3_hyper_direct_target.serialize_aws_json_1_1(
                value["s3_hyper_direct_target"]
            )
        )
    if "dynamo_dbelt_connector_source" in value:
        import capo_glue.types.dynamo_dbelt_connector_source

        out["DynamoDBELTConnectorSource"] = (
            capo_glue.types.dynamo_dbelt_connector_source.serialize_aws_json_1_1(
                value["dynamo_dbelt_connector_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenConfigurationNode:
    out: CodeGenConfigurationNode = {}  # type: ignore[typeddict-item]
    if data.get("AthenaConnectorSource") is not None:
        import capo_glue.types.athena_connector_source

        out["athena_connector_source"] = (
            capo_glue.types.athena_connector_source.deserialize_aws_json_1_1(
                data["AthenaConnectorSource"]
            )
        )
    if data.get("JDBCConnectorSource") is not None:
        import capo_glue.types.jdbc_connector_source

        out["jdbc_connector_source"] = (
            capo_glue.types.jdbc_connector_source.deserialize_aws_json_1_1(
                data["JDBCConnectorSource"]
            )
        )
    if data.get("SparkConnectorSource") is not None:
        import capo_glue.types.spark_connector_source

        out["spark_connector_source"] = (
            capo_glue.types.spark_connector_source.deserialize_aws_json_1_1(
                data["SparkConnectorSource"]
            )
        )
    if data.get("CatalogSource") is not None:
        import capo_glue.types.catalog_source

        out["catalog_source"] = capo_glue.types.catalog_source.deserialize_aws_json_1_1(
            data["CatalogSource"]
        )
    if data.get("RedshiftSource") is not None:
        import capo_glue.types.redshift_source

        out["redshift_source"] = (
            capo_glue.types.redshift_source.deserialize_aws_json_1_1(
                data["RedshiftSource"]
            )
        )
    if data.get("S3CatalogSource") is not None:
        import capo_glue.types.s3_catalog_source

        out["s3_catalog_source"] = (
            capo_glue.types.s3_catalog_source.deserialize_aws_json_1_1(
                data["S3CatalogSource"]
            )
        )
    if data.get("S3CsvSource") is not None:
        import capo_glue.types.s3_csv_source

        out["s3_csv_source"] = capo_glue.types.s3_csv_source.deserialize_aws_json_1_1(
            data["S3CsvSource"]
        )
    if data.get("S3JsonSource") is not None:
        import capo_glue.types.s3_json_source

        out["s3_json_source"] = capo_glue.types.s3_json_source.deserialize_aws_json_1_1(
            data["S3JsonSource"]
        )
    if data.get("S3ParquetSource") is not None:
        import capo_glue.types.s3_parquet_source

        out["s3_parquet_source"] = (
            capo_glue.types.s3_parquet_source.deserialize_aws_json_1_1(
                data["S3ParquetSource"]
            )
        )
    if data.get("RelationalCatalogSource") is not None:
        import capo_glue.types.relational_catalog_source

        out["relational_catalog_source"] = (
            capo_glue.types.relational_catalog_source.deserialize_aws_json_1_1(
                data["RelationalCatalogSource"]
            )
        )
    if data.get("DynamoDBCatalogSource") is not None:
        import capo_glue.types.dynamo_db_catalog_source

        out["dynamo_db_catalog_source"] = (
            capo_glue.types.dynamo_db_catalog_source.deserialize_aws_json_1_1(
                data["DynamoDBCatalogSource"]
            )
        )
    if data.get("JDBCConnectorTarget") is not None:
        import capo_glue.types.jdbc_connector_target

        out["jdbc_connector_target"] = (
            capo_glue.types.jdbc_connector_target.deserialize_aws_json_1_1(
                data["JDBCConnectorTarget"]
            )
        )
    if data.get("SparkConnectorTarget") is not None:
        import capo_glue.types.spark_connector_target

        out["spark_connector_target"] = (
            capo_glue.types.spark_connector_target.deserialize_aws_json_1_1(
                data["SparkConnectorTarget"]
            )
        )
    if data.get("CatalogTarget") is not None:
        import capo_glue.types.basic_catalog_target

        out["catalog_target"] = (
            capo_glue.types.basic_catalog_target.deserialize_aws_json_1_1(
                data["CatalogTarget"]
            )
        )
    if data.get("RedshiftTarget") is not None:
        import capo_glue.types.redshift_target

        out["redshift_target"] = (
            capo_glue.types.redshift_target.deserialize_aws_json_1_1(
                data["RedshiftTarget"]
            )
        )
    if data.get("S3CatalogTarget") is not None:
        import capo_glue.types.s3_catalog_target

        out["s3_catalog_target"] = (
            capo_glue.types.s3_catalog_target.deserialize_aws_json_1_1(
                data["S3CatalogTarget"]
            )
        )
    if data.get("S3GlueParquetTarget") is not None:
        import capo_glue.types.s3_glue_parquet_target

        out["s3_glue_parquet_target"] = (
            capo_glue.types.s3_glue_parquet_target.deserialize_aws_json_1_1(
                data["S3GlueParquetTarget"]
            )
        )
    if data.get("S3DirectTarget") is not None:
        import capo_glue.types.s3_direct_target

        out["s3_direct_target"] = (
            capo_glue.types.s3_direct_target.deserialize_aws_json_1_1(
                data["S3DirectTarget"]
            )
        )
    if data.get("ApplyMapping") is not None:
        import capo_glue.types.apply_mapping

        out["apply_mapping"] = capo_glue.types.apply_mapping.deserialize_aws_json_1_1(
            data["ApplyMapping"]
        )
    if data.get("SelectFields") is not None:
        import capo_glue.types.select_fields

        out["select_fields"] = capo_glue.types.select_fields.deserialize_aws_json_1_1(
            data["SelectFields"]
        )
    if data.get("DropFields") is not None:
        import capo_glue.types.drop_fields

        out["drop_fields"] = capo_glue.types.drop_fields.deserialize_aws_json_1_1(
            data["DropFields"]
        )
    if data.get("RenameField") is not None:
        import capo_glue.types.rename_field

        out["rename_field"] = capo_glue.types.rename_field.deserialize_aws_json_1_1(
            data["RenameField"]
        )
    if data.get("Spigot") is not None:
        import capo_glue.types.spigot

        out["spigot"] = capo_glue.types.spigot.deserialize_aws_json_1_1(data["Spigot"])
    if data.get("Join") is not None:
        import capo_glue.types.join

        out["join"] = capo_glue.types.join.deserialize_aws_json_1_1(data["Join"])
    if data.get("SplitFields") is not None:
        import capo_glue.types.split_fields

        out["split_fields"] = capo_glue.types.split_fields.deserialize_aws_json_1_1(
            data["SplitFields"]
        )
    if data.get("SelectFromCollection") is not None:
        import capo_glue.types.select_from_collection

        out["select_from_collection"] = (
            capo_glue.types.select_from_collection.deserialize_aws_json_1_1(
                data["SelectFromCollection"]
            )
        )
    if data.get("FillMissingValues") is not None:
        import capo_glue.types.fill_missing_values

        out["fill_missing_values"] = (
            capo_glue.types.fill_missing_values.deserialize_aws_json_1_1(
                data["FillMissingValues"]
            )
        )
    if data.get("Filter") is not None:
        import capo_glue.types.filter

        out["filter"] = capo_glue.types.filter.deserialize_aws_json_1_1(data["Filter"])
    if data.get("CustomCode") is not None:
        import capo_glue.types.custom_code

        out["custom_code"] = capo_glue.types.custom_code.deserialize_aws_json_1_1(
            data["CustomCode"]
        )
    if data.get("SparkSQL") is not None:
        import capo_glue.types.spark_sql

        out["spark_sql"] = capo_glue.types.spark_sql.deserialize_aws_json_1_1(
            data["SparkSQL"]
        )
    if data.get("DirectKinesisSource") is not None:
        import capo_glue.types.direct_kinesis_source

        out["direct_kinesis_source"] = (
            capo_glue.types.direct_kinesis_source.deserialize_aws_json_1_1(
                data["DirectKinesisSource"]
            )
        )
    if data.get("DirectKafkaSource") is not None:
        import capo_glue.types.direct_kafka_source

        out["direct_kafka_source"] = (
            capo_glue.types.direct_kafka_source.deserialize_aws_json_1_1(
                data["DirectKafkaSource"]
            )
        )
    if data.get("CatalogKinesisSource") is not None:
        import capo_glue.types.catalog_kinesis_source

        out["catalog_kinesis_source"] = (
            capo_glue.types.catalog_kinesis_source.deserialize_aws_json_1_1(
                data["CatalogKinesisSource"]
            )
        )
    if data.get("CatalogKafkaSource") is not None:
        import capo_glue.types.catalog_kafka_source

        out["catalog_kafka_source"] = (
            capo_glue.types.catalog_kafka_source.deserialize_aws_json_1_1(
                data["CatalogKafkaSource"]
            )
        )
    if data.get("DropNullFields") is not None:
        import capo_glue.types.drop_null_fields

        out["drop_null_fields"] = (
            capo_glue.types.drop_null_fields.deserialize_aws_json_1_1(
                data["DropNullFields"]
            )
        )
    if data.get("Merge") is not None:
        import capo_glue.types.merge

        out["merge"] = capo_glue.types.merge.deserialize_aws_json_1_1(data["Merge"])
    if data.get("Union") is not None:
        import capo_glue.types.union

        out["union"] = capo_glue.types.union.deserialize_aws_json_1_1(data["Union"])
    if data.get("PIIDetection") is not None:
        import capo_glue.types.pii_detection

        out["pii_detection"] = capo_glue.types.pii_detection.deserialize_aws_json_1_1(
            data["PIIDetection"]
        )
    if data.get("Aggregate") is not None:
        import capo_glue.types.aggregate

        out["aggregate"] = capo_glue.types.aggregate.deserialize_aws_json_1_1(
            data["Aggregate"]
        )
    if data.get("DropDuplicates") is not None:
        import capo_glue.types.drop_duplicates

        out["drop_duplicates"] = (
            capo_glue.types.drop_duplicates.deserialize_aws_json_1_1(
                data["DropDuplicates"]
            )
        )
    if data.get("GovernedCatalogTarget") is not None:
        import capo_glue.types.governed_catalog_target

        out["governed_catalog_target"] = (
            capo_glue.types.governed_catalog_target.deserialize_aws_json_1_1(
                data["GovernedCatalogTarget"]
            )
        )
    if data.get("GovernedCatalogSource") is not None:
        import capo_glue.types.governed_catalog_source

        out["governed_catalog_source"] = (
            capo_glue.types.governed_catalog_source.deserialize_aws_json_1_1(
                data["GovernedCatalogSource"]
            )
        )
    if data.get("MicrosoftSQLServerCatalogSource") is not None:
        import capo_glue.types.microsoft_sql_server_catalog_source

        out["microsoft_sql_server_catalog_source"] = (
            capo_glue.types.microsoft_sql_server_catalog_source.deserialize_aws_json_1_1(
                data["MicrosoftSQLServerCatalogSource"]
            )
        )
    if data.get("MySQLCatalogSource") is not None:
        import capo_glue.types.my_sql_catalog_source

        out["my_sql_catalog_source"] = (
            capo_glue.types.my_sql_catalog_source.deserialize_aws_json_1_1(
                data["MySQLCatalogSource"]
            )
        )
    if data.get("OracleSQLCatalogSource") is not None:
        import capo_glue.types.oracle_sql_catalog_source

        out["oracle_sql_catalog_source"] = (
            capo_glue.types.oracle_sql_catalog_source.deserialize_aws_json_1_1(
                data["OracleSQLCatalogSource"]
            )
        )
    if data.get("PostgreSQLCatalogSource") is not None:
        import capo_glue.types.postgre_sql_catalog_source

        out["postgre_sql_catalog_source"] = (
            capo_glue.types.postgre_sql_catalog_source.deserialize_aws_json_1_1(
                data["PostgreSQLCatalogSource"]
            )
        )
    if data.get("MicrosoftSQLServerCatalogTarget") is not None:
        import capo_glue.types.microsoft_sql_server_catalog_target

        out["microsoft_sql_server_catalog_target"] = (
            capo_glue.types.microsoft_sql_server_catalog_target.deserialize_aws_json_1_1(
                data["MicrosoftSQLServerCatalogTarget"]
            )
        )
    if data.get("MySQLCatalogTarget") is not None:
        import capo_glue.types.my_sql_catalog_target

        out["my_sql_catalog_target"] = (
            capo_glue.types.my_sql_catalog_target.deserialize_aws_json_1_1(
                data["MySQLCatalogTarget"]
            )
        )
    if data.get("OracleSQLCatalogTarget") is not None:
        import capo_glue.types.oracle_sql_catalog_target

        out["oracle_sql_catalog_target"] = (
            capo_glue.types.oracle_sql_catalog_target.deserialize_aws_json_1_1(
                data["OracleSQLCatalogTarget"]
            )
        )
    if data.get("PostgreSQLCatalogTarget") is not None:
        import capo_glue.types.postgre_sql_catalog_target

        out["postgre_sql_catalog_target"] = (
            capo_glue.types.postgre_sql_catalog_target.deserialize_aws_json_1_1(
                data["PostgreSQLCatalogTarget"]
            )
        )
    if data.get("Route") is not None:
        import capo_glue.types.route

        out["route"] = capo_glue.types.route.deserialize_aws_json_1_1(data["Route"])
    if data.get("DynamicTransform") is not None:
        import capo_glue.types.dynamic_transform

        out["dynamic_transform"] = (
            capo_glue.types.dynamic_transform.deserialize_aws_json_1_1(
                data["DynamicTransform"]
            )
        )
    if data.get("EvaluateDataQuality") is not None:
        import capo_glue.types.evaluate_data_quality

        out["evaluate_data_quality"] = (
            capo_glue.types.evaluate_data_quality.deserialize_aws_json_1_1(
                data["EvaluateDataQuality"]
            )
        )
    if data.get("S3CatalogHudiSource") is not None:
        import capo_glue.types.s3_catalog_hudi_source

        out["s3_catalog_hudi_source"] = (
            capo_glue.types.s3_catalog_hudi_source.deserialize_aws_json_1_1(
                data["S3CatalogHudiSource"]
            )
        )
    if data.get("CatalogHudiSource") is not None:
        import capo_glue.types.catalog_hudi_source

        out["catalog_hudi_source"] = (
            capo_glue.types.catalog_hudi_source.deserialize_aws_json_1_1(
                data["CatalogHudiSource"]
            )
        )
    if data.get("S3HudiSource") is not None:
        import capo_glue.types.s3_hudi_source

        out["s3_hudi_source"] = capo_glue.types.s3_hudi_source.deserialize_aws_json_1_1(
            data["S3HudiSource"]
        )
    if data.get("S3HudiCatalogTarget") is not None:
        import capo_glue.types.s3_hudi_catalog_target

        out["s3_hudi_catalog_target"] = (
            capo_glue.types.s3_hudi_catalog_target.deserialize_aws_json_1_1(
                data["S3HudiCatalogTarget"]
            )
        )
    if data.get("S3HudiDirectTarget") is not None:
        import capo_glue.types.s3_hudi_direct_target

        out["s3_hudi_direct_target"] = (
            capo_glue.types.s3_hudi_direct_target.deserialize_aws_json_1_1(
                data["S3HudiDirectTarget"]
            )
        )
    if data.get("DirectJDBCSource") is not None:
        import capo_glue.types.direct_jdbc_source

        out["direct_jdbc_source"] = (
            capo_glue.types.direct_jdbc_source.deserialize_aws_json_1_1(
                data["DirectJDBCSource"]
            )
        )
    if data.get("S3CatalogDeltaSource") is not None:
        import capo_glue.types.s3_catalog_delta_source

        out["s3_catalog_delta_source"] = (
            capo_glue.types.s3_catalog_delta_source.deserialize_aws_json_1_1(
                data["S3CatalogDeltaSource"]
            )
        )
    if data.get("CatalogDeltaSource") is not None:
        import capo_glue.types.catalog_delta_source

        out["catalog_delta_source"] = (
            capo_glue.types.catalog_delta_source.deserialize_aws_json_1_1(
                data["CatalogDeltaSource"]
            )
        )
    if data.get("S3DeltaSource") is not None:
        import capo_glue.types.s3_delta_source

        out["s3_delta_source"] = (
            capo_glue.types.s3_delta_source.deserialize_aws_json_1_1(
                data["S3DeltaSource"]
            )
        )
    if data.get("S3DeltaCatalogTarget") is not None:
        import capo_glue.types.s3_delta_catalog_target

        out["s3_delta_catalog_target"] = (
            capo_glue.types.s3_delta_catalog_target.deserialize_aws_json_1_1(
                data["S3DeltaCatalogTarget"]
            )
        )
    if data.get("S3DeltaDirectTarget") is not None:
        import capo_glue.types.s3_delta_direct_target

        out["s3_delta_direct_target"] = (
            capo_glue.types.s3_delta_direct_target.deserialize_aws_json_1_1(
                data["S3DeltaDirectTarget"]
            )
        )
    if data.get("AmazonRedshiftSource") is not None:
        import capo_glue.types.amazon_redshift_source

        out["amazon_redshift_source"] = (
            capo_glue.types.amazon_redshift_source.deserialize_aws_json_1_1(
                data["AmazonRedshiftSource"]
            )
        )
    if data.get("AmazonRedshiftTarget") is not None:
        import capo_glue.types.amazon_redshift_target

        out["amazon_redshift_target"] = (
            capo_glue.types.amazon_redshift_target.deserialize_aws_json_1_1(
                data["AmazonRedshiftTarget"]
            )
        )
    if data.get("EvaluateDataQualityMultiFrame") is not None:
        import capo_glue.types.evaluate_data_quality_multi_frame

        out["evaluate_data_quality_multi_frame"] = (
            capo_glue.types.evaluate_data_quality_multi_frame.deserialize_aws_json_1_1(
                data["EvaluateDataQualityMultiFrame"]
            )
        )
    if data.get("Recipe") is not None:
        import capo_glue.types.recipe

        out["recipe"] = capo_glue.types.recipe.deserialize_aws_json_1_1(data["Recipe"])
    if data.get("SnowflakeSource") is not None:
        import capo_glue.types.snowflake_source

        out["snowflake_source"] = (
            capo_glue.types.snowflake_source.deserialize_aws_json_1_1(
                data["SnowflakeSource"]
            )
        )
    if data.get("SnowflakeTarget") is not None:
        import capo_glue.types.snowflake_target

        out["snowflake_target"] = (
            capo_glue.types.snowflake_target.deserialize_aws_json_1_1(
                data["SnowflakeTarget"]
            )
        )
    if data.get("ConnectorDataSource") is not None:
        import capo_glue.types.connector_data_source

        out["connector_data_source"] = (
            capo_glue.types.connector_data_source.deserialize_aws_json_1_1(
                data["ConnectorDataSource"]
            )
        )
    if data.get("ConnectorDataTarget") is not None:
        import capo_glue.types.connector_data_target

        out["connector_data_target"] = (
            capo_glue.types.connector_data_target.deserialize_aws_json_1_1(
                data["ConnectorDataTarget"]
            )
        )
    if data.get("S3CatalogIcebergSource") is not None:
        import capo_glue.types.s3_catalog_iceberg_source

        out["s3_catalog_iceberg_source"] = (
            capo_glue.types.s3_catalog_iceberg_source.deserialize_aws_json_1_1(
                data["S3CatalogIcebergSource"]
            )
        )
    if data.get("CatalogIcebergSource") is not None:
        import capo_glue.types.catalog_iceberg_source

        out["catalog_iceberg_source"] = (
            capo_glue.types.catalog_iceberg_source.deserialize_aws_json_1_1(
                data["CatalogIcebergSource"]
            )
        )
    if data.get("S3IcebergCatalogTarget") is not None:
        import capo_glue.types.s3_iceberg_catalog_target

        out["s3_iceberg_catalog_target"] = (
            capo_glue.types.s3_iceberg_catalog_target.deserialize_aws_json_1_1(
                data["S3IcebergCatalogTarget"]
            )
        )
    if data.get("S3IcebergDirectTarget") is not None:
        import capo_glue.types.s3_iceberg_direct_target

        out["s3_iceberg_direct_target"] = (
            capo_glue.types.s3_iceberg_direct_target.deserialize_aws_json_1_1(
                data["S3IcebergDirectTarget"]
            )
        )
    if data.get("S3ExcelSource") is not None:
        import capo_glue.types.s3_excel_source

        out["s3_excel_source"] = (
            capo_glue.types.s3_excel_source.deserialize_aws_json_1_1(
                data["S3ExcelSource"]
            )
        )
    if data.get("S3HyperDirectTarget") is not None:
        import capo_glue.types.s3_hyper_direct_target

        out["s3_hyper_direct_target"] = (
            capo_glue.types.s3_hyper_direct_target.deserialize_aws_json_1_1(
                data["S3HyperDirectTarget"]
            )
        )
    if data.get("DynamoDBELTConnectorSource") is not None:
        import capo_glue.types.dynamo_dbelt_connector_source

        out["dynamo_dbelt_connector_source"] = (
            capo_glue.types.dynamo_dbelt_connector_source.deserialize_aws_json_1_1(
                data["DynamoDBELTConnectorSource"]
            )
        )
    return out
