"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.amazon_elasticsearch_parameters
    import capo_quicksight.types.amazon_open_search_parameters
    import capo_quicksight.types.athena_parameters
    import capo_quicksight.types.aurora_parameters
    import capo_quicksight.types.aurora_postgre_sql_parameters
    import capo_quicksight.types.aws_iot_analytics_parameters
    import capo_quicksight.types.big_query_parameters
    import capo_quicksight.types.confluence_parameters
    import capo_quicksight.types.custom_connection_parameters
    import capo_quicksight.types.databricks_parameters
    import capo_quicksight.types.exasol_parameters
    import capo_quicksight.types.fmkb_parameters
    import capo_quicksight.types.google_drive_parameters
    import capo_quicksight.types.impala_parameters
    import capo_quicksight.types.jira_parameters
    import capo_quicksight.types.maria_db_parameters
    import capo_quicksight.types.my_sql_parameters
    import capo_quicksight.types.one_drive_parameters
    import capo_quicksight.types.oracle_parameters
    import capo_quicksight.types.postgre_sql_parameters
    import capo_quicksight.types.presto_parameters
    import capo_quicksight.types.q_business_parameters
    import capo_quicksight.types.rds_parameters
    import capo_quicksight.types.redshift_parameters
    import capo_quicksight.types.s3_knowledge_base_parameters
    import capo_quicksight.types.s3_parameters
    import capo_quicksight.types.s3_tables_parameters
    import capo_quicksight.types.service_now_parameters
    import capo_quicksight.types.share_point_parameters
    import capo_quicksight.types.snowflake_parameters
    import capo_quicksight.types.spark_parameters
    import capo_quicksight.types.sql_server_parameters
    import capo_quicksight.types.starburst_parameters
    import capo_quicksight.types.teradata_parameters
    import capo_quicksight.types.trino_parameters
    import capo_quicksight.types.twitter_parameters
    import capo_quicksight.types.web_crawler_parameters


class _DataSourceParameters_AmazonElasticsearchParameters(TypedDict, closed=True):
    AmazonElasticsearchParameters: "capo_quicksight.types.amazon_elasticsearch_parameters.AmazonElasticsearchParameters"


class _DataSourceParameters_AthenaParameters(TypedDict, closed=True):
    AthenaParameters: "capo_quicksight.types.athena_parameters.AthenaParameters"


class _DataSourceParameters_AuroraParameters(TypedDict, closed=True):
    AuroraParameters: "capo_quicksight.types.aurora_parameters.AuroraParameters"


class _DataSourceParameters_AuroraPostgreSqlParameters(TypedDict, closed=True):
    AuroraPostgreSqlParameters: (
        "capo_quicksight.types.aurora_postgre_sql_parameters.AuroraPostgreSqlParameters"
    )


class _DataSourceParameters_AwsIotAnalyticsParameters(TypedDict, closed=True):
    AwsIotAnalyticsParameters: (
        "capo_quicksight.types.aws_iot_analytics_parameters.AwsIotAnalyticsParameters"
    )


class _DataSourceParameters_JiraParameters(TypedDict, closed=True):
    JiraParameters: "capo_quicksight.types.jira_parameters.JiraParameters"


class _DataSourceParameters_MariaDbParameters(TypedDict, closed=True):
    MariaDbParameters: "capo_quicksight.types.maria_db_parameters.MariaDbParameters"


class _DataSourceParameters_MySqlParameters(TypedDict, closed=True):
    MySqlParameters: "capo_quicksight.types.my_sql_parameters.MySqlParameters"


class _DataSourceParameters_OracleParameters(TypedDict, closed=True):
    OracleParameters: "capo_quicksight.types.oracle_parameters.OracleParameters"


class _DataSourceParameters_PostgreSqlParameters(TypedDict, closed=True):
    PostgreSqlParameters: (
        "capo_quicksight.types.postgre_sql_parameters.PostgreSqlParameters"
    )


class _DataSourceParameters_PrestoParameters(TypedDict, closed=True):
    PrestoParameters: "capo_quicksight.types.presto_parameters.PrestoParameters"


class _DataSourceParameters_RdsParameters(TypedDict, closed=True):
    RdsParameters: "capo_quicksight.types.rds_parameters.RdsParameters"


class _DataSourceParameters_RedshiftParameters(TypedDict, closed=True):
    RedshiftParameters: "capo_quicksight.types.redshift_parameters.RedshiftParameters"


class _DataSourceParameters_S3Parameters(TypedDict, closed=True):
    S3Parameters: "capo_quicksight.types.s3_parameters.S3Parameters"


class _DataSourceParameters_S3TablesParameters(TypedDict, closed=True):
    S3TablesParameters: "capo_quicksight.types.s3_tables_parameters.S3TablesParameters"


class _DataSourceParameters_S3KnowledgeBaseParameters(TypedDict, closed=True):
    S3KnowledgeBaseParameters: (
        "capo_quicksight.types.s3_knowledge_base_parameters.S3KnowledgeBaseParameters"
    )


class _DataSourceParameters_ServiceNowParameters(TypedDict, closed=True):
    ServiceNowParameters: (
        "capo_quicksight.types.service_now_parameters.ServiceNowParameters"
    )


class _DataSourceParameters_SnowflakeParameters(TypedDict, closed=True):
    SnowflakeParameters: (
        "capo_quicksight.types.snowflake_parameters.SnowflakeParameters"
    )


class _DataSourceParameters_SparkParameters(TypedDict, closed=True):
    SparkParameters: "capo_quicksight.types.spark_parameters.SparkParameters"


class _DataSourceParameters_SqlServerParameters(TypedDict, closed=True):
    SqlServerParameters: (
        "capo_quicksight.types.sql_server_parameters.SqlServerParameters"
    )


class _DataSourceParameters_TeradataParameters(TypedDict, closed=True):
    TeradataParameters: "capo_quicksight.types.teradata_parameters.TeradataParameters"


class _DataSourceParameters_TwitterParameters(TypedDict, closed=True):
    TwitterParameters: "capo_quicksight.types.twitter_parameters.TwitterParameters"


class _DataSourceParameters_AmazonOpenSearchParameters(TypedDict, closed=True):
    AmazonOpenSearchParameters: (
        "capo_quicksight.types.amazon_open_search_parameters.AmazonOpenSearchParameters"
    )


class _DataSourceParameters_ExasolParameters(TypedDict, closed=True):
    ExasolParameters: "capo_quicksight.types.exasol_parameters.ExasolParameters"


class _DataSourceParameters_DatabricksParameters(TypedDict, closed=True):
    DatabricksParameters: (
        "capo_quicksight.types.databricks_parameters.DatabricksParameters"
    )


class _DataSourceParameters_StarburstParameters(TypedDict, closed=True):
    StarburstParameters: (
        "capo_quicksight.types.starburst_parameters.StarburstParameters"
    )


class _DataSourceParameters_TrinoParameters(TypedDict, closed=True):
    TrinoParameters: "capo_quicksight.types.trino_parameters.TrinoParameters"


class _DataSourceParameters_BigQueryParameters(TypedDict, closed=True):
    BigQueryParameters: "capo_quicksight.types.big_query_parameters.BigQueryParameters"


class _DataSourceParameters_ImpalaParameters(TypedDict, closed=True):
    ImpalaParameters: "capo_quicksight.types.impala_parameters.ImpalaParameters"


class _DataSourceParameters_CustomConnectionParameters(TypedDict, closed=True):
    CustomConnectionParameters: (
        "capo_quicksight.types.custom_connection_parameters.CustomConnectionParameters"
    )


class _DataSourceParameters_WebCrawlerParameters(TypedDict, closed=True):
    WebCrawlerParameters: (
        "capo_quicksight.types.web_crawler_parameters.WebCrawlerParameters"
    )


class _DataSourceParameters_ConfluenceParameters(TypedDict, closed=True):
    ConfluenceParameters: (
        "capo_quicksight.types.confluence_parameters.ConfluenceParameters"
    )


class _DataSourceParameters_QBusinessParameters(TypedDict, closed=True):
    QBusinessParameters: (
        "capo_quicksight.types.q_business_parameters.QBusinessParameters"
    )


class _DataSourceParameters_SharePointParameters(TypedDict, closed=True):
    SharePointParameters: (
        "capo_quicksight.types.share_point_parameters.SharePointParameters"
    )


class _DataSourceParameters_GoogleDriveParameters(TypedDict, closed=True):
    GoogleDriveParameters: (
        "capo_quicksight.types.google_drive_parameters.GoogleDriveParameters"
    )


class _DataSourceParameters_OneDriveParameters(TypedDict, closed=True):
    OneDriveParameters: "capo_quicksight.types.one_drive_parameters.OneDriveParameters"


class _DataSourceParameters_FMKBParameters(TypedDict, closed=True):
    FMKBParameters: "capo_quicksight.types.fmkb_parameters.FMKBParameters"


DataSourceParameters: TypeAlias = (
    _DataSourceParameters_AmazonElasticsearchParameters
    | _DataSourceParameters_AthenaParameters
    | _DataSourceParameters_AuroraParameters
    | _DataSourceParameters_AuroraPostgreSqlParameters
    | _DataSourceParameters_AwsIotAnalyticsParameters
    | _DataSourceParameters_JiraParameters
    | _DataSourceParameters_MariaDbParameters
    | _DataSourceParameters_MySqlParameters
    | _DataSourceParameters_OracleParameters
    | _DataSourceParameters_PostgreSqlParameters
    | _DataSourceParameters_PrestoParameters
    | _DataSourceParameters_RdsParameters
    | _DataSourceParameters_RedshiftParameters
    | _DataSourceParameters_S3Parameters
    | _DataSourceParameters_S3TablesParameters
    | _DataSourceParameters_S3KnowledgeBaseParameters
    | _DataSourceParameters_ServiceNowParameters
    | _DataSourceParameters_SnowflakeParameters
    | _DataSourceParameters_SparkParameters
    | _DataSourceParameters_SqlServerParameters
    | _DataSourceParameters_TeradataParameters
    | _DataSourceParameters_TwitterParameters
    | _DataSourceParameters_AmazonOpenSearchParameters
    | _DataSourceParameters_ExasolParameters
    | _DataSourceParameters_DatabricksParameters
    | _DataSourceParameters_StarburstParameters
    | _DataSourceParameters_TrinoParameters
    | _DataSourceParameters_BigQueryParameters
    | _DataSourceParameters_ImpalaParameters
    | _DataSourceParameters_CustomConnectionParameters
    | _DataSourceParameters_WebCrawlerParameters
    | _DataSourceParameters_ConfluenceParameters
    | _DataSourceParameters_QBusinessParameters
    | _DataSourceParameters_SharePointParameters
    | _DataSourceParameters_GoogleDriveParameters
    | _DataSourceParameters_OneDriveParameters
    | _DataSourceParameters_FMKBParameters
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceParameters) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DataSourceParameters: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AmazonElasticsearchParameters" in value:
        import capo_quicksight.types.amazon_elasticsearch_parameters

        return {
            "AmazonElasticsearchParameters": capo_quicksight.types.amazon_elasticsearch_parameters.serialize_json(
                value["AmazonElasticsearchParameters"]
            )
        }
    elif "AthenaParameters" in value:
        import capo_quicksight.types.athena_parameters

        return {
            "AthenaParameters": capo_quicksight.types.athena_parameters.serialize_json(
                value["AthenaParameters"]
            )
        }
    elif "AuroraParameters" in value:
        import capo_quicksight.types.aurora_parameters

        return {
            "AuroraParameters": capo_quicksight.types.aurora_parameters.serialize_json(
                value["AuroraParameters"]
            )
        }
    elif "AuroraPostgreSqlParameters" in value:
        import capo_quicksight.types.aurora_postgre_sql_parameters

        return {
            "AuroraPostgreSqlParameters": capo_quicksight.types.aurora_postgre_sql_parameters.serialize_json(
                value["AuroraPostgreSqlParameters"]
            )
        }
    elif "AwsIotAnalyticsParameters" in value:
        import capo_quicksight.types.aws_iot_analytics_parameters

        return {
            "AwsIotAnalyticsParameters": capo_quicksight.types.aws_iot_analytics_parameters.serialize_json(
                value["AwsIotAnalyticsParameters"]
            )
        }
    elif "JiraParameters" in value:
        import capo_quicksight.types.jira_parameters

        return {
            "JiraParameters": capo_quicksight.types.jira_parameters.serialize_json(
                value["JiraParameters"]
            )
        }
    elif "MariaDbParameters" in value:
        import capo_quicksight.types.maria_db_parameters

        return {
            "MariaDbParameters": capo_quicksight.types.maria_db_parameters.serialize_json(
                value["MariaDbParameters"]
            )
        }
    elif "MySqlParameters" in value:
        import capo_quicksight.types.my_sql_parameters

        return {
            "MySqlParameters": capo_quicksight.types.my_sql_parameters.serialize_json(
                value["MySqlParameters"]
            )
        }
    elif "OracleParameters" in value:
        import capo_quicksight.types.oracle_parameters

        return {
            "OracleParameters": capo_quicksight.types.oracle_parameters.serialize_json(
                value["OracleParameters"]
            )
        }
    elif "PostgreSqlParameters" in value:
        import capo_quicksight.types.postgre_sql_parameters

        return {
            "PostgreSqlParameters": capo_quicksight.types.postgre_sql_parameters.serialize_json(
                value["PostgreSqlParameters"]
            )
        }
    elif "PrestoParameters" in value:
        import capo_quicksight.types.presto_parameters

        return {
            "PrestoParameters": capo_quicksight.types.presto_parameters.serialize_json(
                value["PrestoParameters"]
            )
        }
    elif "RdsParameters" in value:
        import capo_quicksight.types.rds_parameters

        return {
            "RdsParameters": capo_quicksight.types.rds_parameters.serialize_json(
                value["RdsParameters"]
            )
        }
    elif "RedshiftParameters" in value:
        import capo_quicksight.types.redshift_parameters

        return {
            "RedshiftParameters": capo_quicksight.types.redshift_parameters.serialize_json(
                value["RedshiftParameters"]
            )
        }
    elif "S3Parameters" in value:
        import capo_quicksight.types.s3_parameters

        return {
            "S3Parameters": capo_quicksight.types.s3_parameters.serialize_json(
                value["S3Parameters"]
            )
        }
    elif "S3TablesParameters" in value:
        import capo_quicksight.types.s3_tables_parameters

        return {
            "S3TablesParameters": capo_quicksight.types.s3_tables_parameters.serialize_json(
                value["S3TablesParameters"]
            )
        }
    elif "S3KnowledgeBaseParameters" in value:
        import capo_quicksight.types.s3_knowledge_base_parameters

        return {
            "S3KnowledgeBaseParameters": capo_quicksight.types.s3_knowledge_base_parameters.serialize_json(
                value["S3KnowledgeBaseParameters"]
            )
        }
    elif "ServiceNowParameters" in value:
        import capo_quicksight.types.service_now_parameters

        return {
            "ServiceNowParameters": capo_quicksight.types.service_now_parameters.serialize_json(
                value["ServiceNowParameters"]
            )
        }
    elif "SnowflakeParameters" in value:
        import capo_quicksight.types.snowflake_parameters

        return {
            "SnowflakeParameters": capo_quicksight.types.snowflake_parameters.serialize_json(
                value["SnowflakeParameters"]
            )
        }
    elif "SparkParameters" in value:
        import capo_quicksight.types.spark_parameters

        return {
            "SparkParameters": capo_quicksight.types.spark_parameters.serialize_json(
                value["SparkParameters"]
            )
        }
    elif "SqlServerParameters" in value:
        import capo_quicksight.types.sql_server_parameters

        return {
            "SqlServerParameters": capo_quicksight.types.sql_server_parameters.serialize_json(
                value["SqlServerParameters"]
            )
        }
    elif "TeradataParameters" in value:
        import capo_quicksight.types.teradata_parameters

        return {
            "TeradataParameters": capo_quicksight.types.teradata_parameters.serialize_json(
                value["TeradataParameters"]
            )
        }
    elif "TwitterParameters" in value:
        import capo_quicksight.types.twitter_parameters

        return {
            "TwitterParameters": capo_quicksight.types.twitter_parameters.serialize_json(
                value["TwitterParameters"]
            )
        }
    elif "AmazonOpenSearchParameters" in value:
        import capo_quicksight.types.amazon_open_search_parameters

        return {
            "AmazonOpenSearchParameters": capo_quicksight.types.amazon_open_search_parameters.serialize_json(
                value["AmazonOpenSearchParameters"]
            )
        }
    elif "ExasolParameters" in value:
        import capo_quicksight.types.exasol_parameters

        return {
            "ExasolParameters": capo_quicksight.types.exasol_parameters.serialize_json(
                value["ExasolParameters"]
            )
        }
    elif "DatabricksParameters" in value:
        import capo_quicksight.types.databricks_parameters

        return {
            "DatabricksParameters": capo_quicksight.types.databricks_parameters.serialize_json(
                value["DatabricksParameters"]
            )
        }
    elif "StarburstParameters" in value:
        import capo_quicksight.types.starburst_parameters

        return {
            "StarburstParameters": capo_quicksight.types.starburst_parameters.serialize_json(
                value["StarburstParameters"]
            )
        }
    elif "TrinoParameters" in value:
        import capo_quicksight.types.trino_parameters

        return {
            "TrinoParameters": capo_quicksight.types.trino_parameters.serialize_json(
                value["TrinoParameters"]
            )
        }
    elif "BigQueryParameters" in value:
        import capo_quicksight.types.big_query_parameters

        return {
            "BigQueryParameters": capo_quicksight.types.big_query_parameters.serialize_json(
                value["BigQueryParameters"]
            )
        }
    elif "ImpalaParameters" in value:
        import capo_quicksight.types.impala_parameters

        return {
            "ImpalaParameters": capo_quicksight.types.impala_parameters.serialize_json(
                value["ImpalaParameters"]
            )
        }
    elif "CustomConnectionParameters" in value:
        import capo_quicksight.types.custom_connection_parameters

        return {
            "CustomConnectionParameters": capo_quicksight.types.custom_connection_parameters.serialize_json(
                value["CustomConnectionParameters"]
            )
        }
    elif "WebCrawlerParameters" in value:
        import capo_quicksight.types.web_crawler_parameters

        return {
            "WebCrawlerParameters": capo_quicksight.types.web_crawler_parameters.serialize_json(
                value["WebCrawlerParameters"]
            )
        }
    elif "ConfluenceParameters" in value:
        import capo_quicksight.types.confluence_parameters

        return {
            "ConfluenceParameters": capo_quicksight.types.confluence_parameters.serialize_json(
                value["ConfluenceParameters"]
            )
        }
    elif "QBusinessParameters" in value:
        import capo_quicksight.types.q_business_parameters

        return {
            "QBusinessParameters": capo_quicksight.types.q_business_parameters.serialize_json(
                value["QBusinessParameters"]
            )
        }
    elif "SharePointParameters" in value:
        import capo_quicksight.types.share_point_parameters

        return {
            "SharePointParameters": capo_quicksight.types.share_point_parameters.serialize_json(
                value["SharePointParameters"]
            )
        }
    elif "GoogleDriveParameters" in value:
        import capo_quicksight.types.google_drive_parameters

        return {
            "GoogleDriveParameters": capo_quicksight.types.google_drive_parameters.serialize_json(
                value["GoogleDriveParameters"]
            )
        }
    elif "OneDriveParameters" in value:
        import capo_quicksight.types.one_drive_parameters

        return {
            "OneDriveParameters": capo_quicksight.types.one_drive_parameters.serialize_json(
                value["OneDriveParameters"]
            )
        }
    elif "FMKBParameters" in value:
        import capo_quicksight.types.fmkb_parameters

        return {
            "FMKBParameters": capo_quicksight.types.fmkb_parameters.serialize_json(
                value["FMKBParameters"]
            )
        }
    else:
        raise SerializationError("DataSourceParameters: no variant present")


def deserialize_json(data: dict) -> DataSourceParameters:
    if data.get("AmazonElasticsearchParameters") is not None:
        import capo_quicksight.types.amazon_elasticsearch_parameters

        return {
            "AmazonElasticsearchParameters": capo_quicksight.types.amazon_elasticsearch_parameters.deserialize_json(
                data["AmazonElasticsearchParameters"]
            )
        }
    elif data.get("AthenaParameters") is not None:
        import capo_quicksight.types.athena_parameters

        return {
            "AthenaParameters": capo_quicksight.types.athena_parameters.deserialize_json(
                data["AthenaParameters"]
            )
        }
    elif data.get("AuroraParameters") is not None:
        import capo_quicksight.types.aurora_parameters

        return {
            "AuroraParameters": capo_quicksight.types.aurora_parameters.deserialize_json(
                data["AuroraParameters"]
            )
        }
    elif data.get("AuroraPostgreSqlParameters") is not None:
        import capo_quicksight.types.aurora_postgre_sql_parameters

        return {
            "AuroraPostgreSqlParameters": capo_quicksight.types.aurora_postgre_sql_parameters.deserialize_json(
                data["AuroraPostgreSqlParameters"]
            )
        }
    elif data.get("AwsIotAnalyticsParameters") is not None:
        import capo_quicksight.types.aws_iot_analytics_parameters

        return {
            "AwsIotAnalyticsParameters": capo_quicksight.types.aws_iot_analytics_parameters.deserialize_json(
                data["AwsIotAnalyticsParameters"]
            )
        }
    elif data.get("JiraParameters") is not None:
        import capo_quicksight.types.jira_parameters

        return {
            "JiraParameters": capo_quicksight.types.jira_parameters.deserialize_json(
                data["JiraParameters"]
            )
        }
    elif data.get("MariaDbParameters") is not None:
        import capo_quicksight.types.maria_db_parameters

        return {
            "MariaDbParameters": capo_quicksight.types.maria_db_parameters.deserialize_json(
                data["MariaDbParameters"]
            )
        }
    elif data.get("MySqlParameters") is not None:
        import capo_quicksight.types.my_sql_parameters

        return {
            "MySqlParameters": capo_quicksight.types.my_sql_parameters.deserialize_json(
                data["MySqlParameters"]
            )
        }
    elif data.get("OracleParameters") is not None:
        import capo_quicksight.types.oracle_parameters

        return {
            "OracleParameters": capo_quicksight.types.oracle_parameters.deserialize_json(
                data["OracleParameters"]
            )
        }
    elif data.get("PostgreSqlParameters") is not None:
        import capo_quicksight.types.postgre_sql_parameters

        return {
            "PostgreSqlParameters": capo_quicksight.types.postgre_sql_parameters.deserialize_json(
                data["PostgreSqlParameters"]
            )
        }
    elif data.get("PrestoParameters") is not None:
        import capo_quicksight.types.presto_parameters

        return {
            "PrestoParameters": capo_quicksight.types.presto_parameters.deserialize_json(
                data["PrestoParameters"]
            )
        }
    elif data.get("RdsParameters") is not None:
        import capo_quicksight.types.rds_parameters

        return {
            "RdsParameters": capo_quicksight.types.rds_parameters.deserialize_json(
                data["RdsParameters"]
            )
        }
    elif data.get("RedshiftParameters") is not None:
        import capo_quicksight.types.redshift_parameters

        return {
            "RedshiftParameters": capo_quicksight.types.redshift_parameters.deserialize_json(
                data["RedshiftParameters"]
            )
        }
    elif data.get("S3Parameters") is not None:
        import capo_quicksight.types.s3_parameters

        return {
            "S3Parameters": capo_quicksight.types.s3_parameters.deserialize_json(
                data["S3Parameters"]
            )
        }
    elif data.get("S3TablesParameters") is not None:
        import capo_quicksight.types.s3_tables_parameters

        return {
            "S3TablesParameters": capo_quicksight.types.s3_tables_parameters.deserialize_json(
                data["S3TablesParameters"]
            )
        }
    elif data.get("S3KnowledgeBaseParameters") is not None:
        import capo_quicksight.types.s3_knowledge_base_parameters

        return {
            "S3KnowledgeBaseParameters": capo_quicksight.types.s3_knowledge_base_parameters.deserialize_json(
                data["S3KnowledgeBaseParameters"]
            )
        }
    elif data.get("ServiceNowParameters") is not None:
        import capo_quicksight.types.service_now_parameters

        return {
            "ServiceNowParameters": capo_quicksight.types.service_now_parameters.deserialize_json(
                data["ServiceNowParameters"]
            )
        }
    elif data.get("SnowflakeParameters") is not None:
        import capo_quicksight.types.snowflake_parameters

        return {
            "SnowflakeParameters": capo_quicksight.types.snowflake_parameters.deserialize_json(
                data["SnowflakeParameters"]
            )
        }
    elif data.get("SparkParameters") is not None:
        import capo_quicksight.types.spark_parameters

        return {
            "SparkParameters": capo_quicksight.types.spark_parameters.deserialize_json(
                data["SparkParameters"]
            )
        }
    elif data.get("SqlServerParameters") is not None:
        import capo_quicksight.types.sql_server_parameters

        return {
            "SqlServerParameters": capo_quicksight.types.sql_server_parameters.deserialize_json(
                data["SqlServerParameters"]
            )
        }
    elif data.get("TeradataParameters") is not None:
        import capo_quicksight.types.teradata_parameters

        return {
            "TeradataParameters": capo_quicksight.types.teradata_parameters.deserialize_json(
                data["TeradataParameters"]
            )
        }
    elif data.get("TwitterParameters") is not None:
        import capo_quicksight.types.twitter_parameters

        return {
            "TwitterParameters": capo_quicksight.types.twitter_parameters.deserialize_json(
                data["TwitterParameters"]
            )
        }
    elif data.get("AmazonOpenSearchParameters") is not None:
        import capo_quicksight.types.amazon_open_search_parameters

        return {
            "AmazonOpenSearchParameters": capo_quicksight.types.amazon_open_search_parameters.deserialize_json(
                data["AmazonOpenSearchParameters"]
            )
        }
    elif data.get("ExasolParameters") is not None:
        import capo_quicksight.types.exasol_parameters

        return {
            "ExasolParameters": capo_quicksight.types.exasol_parameters.deserialize_json(
                data["ExasolParameters"]
            )
        }
    elif data.get("DatabricksParameters") is not None:
        import capo_quicksight.types.databricks_parameters

        return {
            "DatabricksParameters": capo_quicksight.types.databricks_parameters.deserialize_json(
                data["DatabricksParameters"]
            )
        }
    elif data.get("StarburstParameters") is not None:
        import capo_quicksight.types.starburst_parameters

        return {
            "StarburstParameters": capo_quicksight.types.starburst_parameters.deserialize_json(
                data["StarburstParameters"]
            )
        }
    elif data.get("TrinoParameters") is not None:
        import capo_quicksight.types.trino_parameters

        return {
            "TrinoParameters": capo_quicksight.types.trino_parameters.deserialize_json(
                data["TrinoParameters"]
            )
        }
    elif data.get("BigQueryParameters") is not None:
        import capo_quicksight.types.big_query_parameters

        return {
            "BigQueryParameters": capo_quicksight.types.big_query_parameters.deserialize_json(
                data["BigQueryParameters"]
            )
        }
    elif data.get("ImpalaParameters") is not None:
        import capo_quicksight.types.impala_parameters

        return {
            "ImpalaParameters": capo_quicksight.types.impala_parameters.deserialize_json(
                data["ImpalaParameters"]
            )
        }
    elif data.get("CustomConnectionParameters") is not None:
        import capo_quicksight.types.custom_connection_parameters

        return {
            "CustomConnectionParameters": capo_quicksight.types.custom_connection_parameters.deserialize_json(
                data["CustomConnectionParameters"]
            )
        }
    elif data.get("WebCrawlerParameters") is not None:
        import capo_quicksight.types.web_crawler_parameters

        return {
            "WebCrawlerParameters": capo_quicksight.types.web_crawler_parameters.deserialize_json(
                data["WebCrawlerParameters"]
            )
        }
    elif data.get("ConfluenceParameters") is not None:
        import capo_quicksight.types.confluence_parameters

        return {
            "ConfluenceParameters": capo_quicksight.types.confluence_parameters.deserialize_json(
                data["ConfluenceParameters"]
            )
        }
    elif data.get("QBusinessParameters") is not None:
        import capo_quicksight.types.q_business_parameters

        return {
            "QBusinessParameters": capo_quicksight.types.q_business_parameters.deserialize_json(
                data["QBusinessParameters"]
            )
        }
    elif data.get("SharePointParameters") is not None:
        import capo_quicksight.types.share_point_parameters

        return {
            "SharePointParameters": capo_quicksight.types.share_point_parameters.deserialize_json(
                data["SharePointParameters"]
            )
        }
    elif data.get("GoogleDriveParameters") is not None:
        import capo_quicksight.types.google_drive_parameters

        return {
            "GoogleDriveParameters": capo_quicksight.types.google_drive_parameters.deserialize_json(
                data["GoogleDriveParameters"]
            )
        }
    elif data.get("OneDriveParameters") is not None:
        import capo_quicksight.types.one_drive_parameters

        return {
            "OneDriveParameters": capo_quicksight.types.one_drive_parameters.deserialize_json(
                data["OneDriveParameters"]
            )
        }
    elif data.get("FMKBParameters") is not None:
        import capo_quicksight.types.fmkb_parameters

        return {
            "FMKBParameters": capo_quicksight.types.fmkb_parameters.deserialize_json(
                data["FMKBParameters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DataSourceParameters: no recognized variant key")
