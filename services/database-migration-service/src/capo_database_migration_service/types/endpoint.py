"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.dms_ssl_mode_value
    import capo_database_migration_service.types.dms_transfer_settings
    import capo_database_migration_service.types.doc_db_settings
    import capo_database_migration_service.types.dynamo_db_settings
    import capo_database_migration_service.types.elasticsearch_settings
    import capo_database_migration_service.types.gcp_my_sql_settings
    import capo_database_migration_service.types.ibm_db2_settings
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.kafka_settings
    import capo_database_migration_service.types.kinesis_settings
    import capo_database_migration_service.types.lakehouse_settings
    import capo_database_migration_service.types.microsoft_sql_server_settings
    import capo_database_migration_service.types.mongo_db_settings
    import capo_database_migration_service.types.my_sql_settings
    import capo_database_migration_service.types.neptune_settings
    import capo_database_migration_service.types.oracle_settings
    import capo_database_migration_service.types.postgre_sql_settings
    import capo_database_migration_service.types.redis_settings
    import capo_database_migration_service.types.redshift_settings
    import capo_database_migration_service.types.replication_endpoint_type_value
    import capo_database_migration_service.types.s3_settings
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.sybase_settings
    import capo_database_migration_service.types.timestream_settings


class Endpoint(TypedDict, closed=True):
    endpoint_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.</p>"""
    endpoint_type: NotRequired[
        "capo_database_migration_service.types.replication_endpoint_type_value.ReplicationEndpointTypeValue"
    ]
    """<p>The type of endpoint. Valid values are <code>source</code> and <code>target</code>.</p>"""
    engine_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The database engine name. Valid values, depending on the EndpointType, include <code>"mysql"</code>, <code>"oracle"</code>, <code>"postgres"</code>, <code>"mariadb"</code>, <code>"aurora"</code>, <code>"aurora-postgresql"</code>, <code>"redshift"</code>, <code>"redshift-serverless"</code>, <code>"s3"</code>, <code>"db2"</code>, <code>"db2-zos"</code>, <code>"azuredb"</code>, <code>"sybase"</code>, <code>"dynamodb"</code>, <code>"mongodb"</code>, <code>"kinesis"</code>, <code>"kafka"</code>, <code>"elasticsearch"</code>, <code>"documentdb"</code>, <code>"sqlserver"</code>, <code>"neptune"</code>, and <code>"babelfish"</code>.</p>"""
    engine_display_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The expanded name for the engine name. For example, if the <code>EngineName</code> parameter is "aurora", this value would be "Amazon Aurora MySQL".</p>"""
    username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The user name used to connect to the endpoint.</p>"""
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the server at the endpoint.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value used to access the endpoint.</p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the database at the endpoint.</p>"""
    extra_connection_attributes: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Additional connection attributes used to connect to the endpoint.</p>"""
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The status of the endpoint.</p>"""
    kms_key_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An KMS key identifier that is used to encrypt the connection parameters for the endpoint.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""
    endpoint_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>"""
    certificate_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) used for SSL connection to the endpoint.</p>"""
    ssl_mode: NotRequired[
        "capo_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the endpoint. The default value is <code>none</code>.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the <code>iam:PassRole</code> action.</p>"""
    external_table_definition: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The external table definition.</p>"""
    external_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account. </p>"""
    is_read_only: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the endpoint is read-only. When set to <code>true</code>, this endpoint is managed by DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only endpoints through their associated zero-ETL integration.</p>"""
    dynamo_db_settings: NotRequired[
        "capo_database_migration_service.types.dynamo_db_settings.DynamoDbSettings"
    ]
    """<p>The settings for the DynamoDB target endpoint. For more information, see the <code>DynamoDBSettings</code> structure.</p>"""
    s3_settings: NotRequired[
        "capo_database_migration_service.types.s3_settings.S3Settings"
    ]
    """<p>The settings for the S3 target endpoint. For more information, see the <code>S3Settings</code> structure.</p>"""
    dms_transfer_settings: NotRequired[
        "capo_database_migration_service.types.dms_transfer_settings.DmsTransferSettings"
    ]
    """<p>The settings for the DMS Transfer type source. For more information, see the DmsTransferSettings structure. </p>"""
    mongo_db_settings: NotRequired[
        "capo_database_migration_service.types.mongo_db_settings.MongoDbSettings"
    ]
    """<p>The settings for the MongoDB source endpoint. For more information, see the <code>MongoDbSettings</code> structure.</p>"""
    kinesis_settings: NotRequired[
        "capo_database_migration_service.types.kinesis_settings.KinesisSettings"
    ]
    """<p>The settings for the Amazon Kinesis target endpoint. For more information, see the <code>KinesisSettings</code> structure.</p>"""
    kafka_settings: NotRequired[
        "capo_database_migration_service.types.kafka_settings.KafkaSettings"
    ]
    """<p>The settings for the Apache Kafka target endpoint. For more information, see the <code>KafkaSettings</code> structure.</p>"""
    elasticsearch_settings: NotRequired[
        "capo_database_migration_service.types.elasticsearch_settings.ElasticsearchSettings"
    ]
    """<p>The settings for the OpenSearch source endpoint. For more information, see the <code>ElasticsearchSettings</code> structure.</p>"""
    neptune_settings: NotRequired[
        "capo_database_migration_service.types.neptune_settings.NeptuneSettings"
    ]
    """<p>The settings for the Amazon Neptune target endpoint. For more information, see the <code>NeptuneSettings</code> structure.</p>"""
    redshift_settings: NotRequired[
        "capo_database_migration_service.types.redshift_settings.RedshiftSettings"
    ]
    """<p>Settings for the Amazon Redshift endpoint.</p>"""
    postgre_sql_settings: NotRequired[
        "capo_database_migration_service.types.postgre_sql_settings.PostgreSQLSettings"
    ]
    """<p>The settings for the PostgreSQL source and target endpoint. For more information, see the <code>PostgreSQLSettings</code> structure.</p>"""
    my_sql_settings: NotRequired[
        "capo_database_migration_service.types.my_sql_settings.MySQLSettings"
    ]
    """<p>The settings for the MySQL source and target endpoint. For more information, see the <code>MySQLSettings</code> structure.</p>"""
    oracle_settings: NotRequired[
        "capo_database_migration_service.types.oracle_settings.OracleSettings"
    ]
    """<p>The settings for the Oracle source and target endpoint. For more information, see the <code>OracleSettings</code> structure.</p>"""
    sybase_settings: NotRequired[
        "capo_database_migration_service.types.sybase_settings.SybaseSettings"
    ]
    """<p>The settings for the SAP ASE source and target endpoint. For more information, see the <code>SybaseSettings</code> structure.</p>"""
    microsoft_sql_server_settings: NotRequired[
        "capo_database_migration_service.types.microsoft_sql_server_settings.MicrosoftSQLServerSettings"
    ]
    """<p>The settings for the Microsoft SQL Server source and target endpoint. For more information, see the <code>MicrosoftSQLServerSettings</code> structure.</p>"""
    ibm_db2_settings: NotRequired[
        "capo_database_migration_service.types.ibm_db2_settings.IBMDb2Settings"
    ]
    """<p>The settings for the IBM Db2 LUW source endpoint. For more information, see the <code>IBMDb2Settings</code> structure. </p>"""
    doc_db_settings: NotRequired[
        "capo_database_migration_service.types.doc_db_settings.DocDbSettings"
    ]
    redis_settings: NotRequired[
        "capo_database_migration_service.types.redis_settings.RedisSettings"
    ]
    """<p>The settings for the Redis target endpoint. For more information, see the <code>RedisSettings</code> structure.</p>"""
    gcp_my_sql_settings: NotRequired[
        "capo_database_migration_service.types.gcp_my_sql_settings.GcpMySQLSettings"
    ]
    """<p>Settings in JSON format for the source GCP MySQL endpoint.</p>"""
    timestream_settings: NotRequired[
        "capo_database_migration_service.types.timestream_settings.TimestreamSettings"
    ]
    """<p>The settings for the Amazon Timestream target endpoint. For more information, see the <code>TimestreamSettings</code> structure.</p>"""
    lakehouse_settings: NotRequired[
        "capo_database_migration_service.types.lakehouse_settings.LakehouseSettings"
    ]
    """<p>Settings in JSON format for the target Lakehouse endpoint. This parameter applies to endpoints that are automatically created by DMS for a Lakehouse data warehouse as part of a zero-ETL integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "endpoint_identifier" in value:
        out["EndpointIdentifier"] = value["endpoint_identifier"]
    if "endpoint_type" in value:
        import capo_database_migration_service.types.replication_endpoint_type_value

        out["EndpointType"] = (
            capo_database_migration_service.types.replication_endpoint_type_value.serialize_aws_json_1_1(
                value["endpoint_type"]
            )
        )
    if "engine_name" in value:
        out["EngineName"] = value["engine_name"]
    if "engine_display_name" in value:
        out["EngineDisplayName"] = value["engine_display_name"]
    if "username" in value:
        out["Username"] = value["username"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "extra_connection_attributes" in value:
        out["ExtraConnectionAttributes"] = value["extra_connection_attributes"]
    if "status" in value:
        out["Status"] = value["status"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "ssl_mode" in value:
        import capo_database_migration_service.types.dms_ssl_mode_value

        out["SslMode"] = (
            capo_database_migration_service.types.dms_ssl_mode_value.serialize_aws_json_1_1(
                value["ssl_mode"]
            )
        )
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "external_table_definition" in value:
        out["ExternalTableDefinition"] = value["external_table_definition"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "is_read_only" in value:
        out["IsReadOnly"] = value["is_read_only"]
    if "dynamo_db_settings" in value:
        import capo_database_migration_service.types.dynamo_db_settings

        out["DynamoDbSettings"] = (
            capo_database_migration_service.types.dynamo_db_settings.serialize_aws_json_1_1(
                value["dynamo_db_settings"]
            )
        )
    if "s3_settings" in value:
        import capo_database_migration_service.types.s3_settings

        out["S3Settings"] = (
            capo_database_migration_service.types.s3_settings.serialize_aws_json_1_1(
                value["s3_settings"]
            )
        )
    if "dms_transfer_settings" in value:
        import capo_database_migration_service.types.dms_transfer_settings

        out["DmsTransferSettings"] = (
            capo_database_migration_service.types.dms_transfer_settings.serialize_aws_json_1_1(
                value["dms_transfer_settings"]
            )
        )
    if "mongo_db_settings" in value:
        import capo_database_migration_service.types.mongo_db_settings

        out["MongoDbSettings"] = (
            capo_database_migration_service.types.mongo_db_settings.serialize_aws_json_1_1(
                value["mongo_db_settings"]
            )
        )
    if "kinesis_settings" in value:
        import capo_database_migration_service.types.kinesis_settings

        out["KinesisSettings"] = (
            capo_database_migration_service.types.kinesis_settings.serialize_aws_json_1_1(
                value["kinesis_settings"]
            )
        )
    if "kafka_settings" in value:
        import capo_database_migration_service.types.kafka_settings

        out["KafkaSettings"] = (
            capo_database_migration_service.types.kafka_settings.serialize_aws_json_1_1(
                value["kafka_settings"]
            )
        )
    if "elasticsearch_settings" in value:
        import capo_database_migration_service.types.elasticsearch_settings

        out["ElasticsearchSettings"] = (
            capo_database_migration_service.types.elasticsearch_settings.serialize_aws_json_1_1(
                value["elasticsearch_settings"]
            )
        )
    if "neptune_settings" in value:
        import capo_database_migration_service.types.neptune_settings

        out["NeptuneSettings"] = (
            capo_database_migration_service.types.neptune_settings.serialize_aws_json_1_1(
                value["neptune_settings"]
            )
        )
    if "redshift_settings" in value:
        import capo_database_migration_service.types.redshift_settings

        out["RedshiftSettings"] = (
            capo_database_migration_service.types.redshift_settings.serialize_aws_json_1_1(
                value["redshift_settings"]
            )
        )
    if "postgre_sql_settings" in value:
        import capo_database_migration_service.types.postgre_sql_settings

        out["PostgreSQLSettings"] = (
            capo_database_migration_service.types.postgre_sql_settings.serialize_aws_json_1_1(
                value["postgre_sql_settings"]
            )
        )
    if "my_sql_settings" in value:
        import capo_database_migration_service.types.my_sql_settings

        out["MySQLSettings"] = (
            capo_database_migration_service.types.my_sql_settings.serialize_aws_json_1_1(
                value["my_sql_settings"]
            )
        )
    if "oracle_settings" in value:
        import capo_database_migration_service.types.oracle_settings

        out["OracleSettings"] = (
            capo_database_migration_service.types.oracle_settings.serialize_aws_json_1_1(
                value["oracle_settings"]
            )
        )
    if "sybase_settings" in value:
        import capo_database_migration_service.types.sybase_settings

        out["SybaseSettings"] = (
            capo_database_migration_service.types.sybase_settings.serialize_aws_json_1_1(
                value["sybase_settings"]
            )
        )
    if "microsoft_sql_server_settings" in value:
        import capo_database_migration_service.types.microsoft_sql_server_settings

        out["MicrosoftSQLServerSettings"] = (
            capo_database_migration_service.types.microsoft_sql_server_settings.serialize_aws_json_1_1(
                value["microsoft_sql_server_settings"]
            )
        )
    if "ibm_db2_settings" in value:
        import capo_database_migration_service.types.ibm_db2_settings

        out["IBMDb2Settings"] = (
            capo_database_migration_service.types.ibm_db2_settings.serialize_aws_json_1_1(
                value["ibm_db2_settings"]
            )
        )
    if "doc_db_settings" in value:
        import capo_database_migration_service.types.doc_db_settings

        out["DocDbSettings"] = (
            capo_database_migration_service.types.doc_db_settings.serialize_aws_json_1_1(
                value["doc_db_settings"]
            )
        )
    if "redis_settings" in value:
        import capo_database_migration_service.types.redis_settings

        out["RedisSettings"] = (
            capo_database_migration_service.types.redis_settings.serialize_aws_json_1_1(
                value["redis_settings"]
            )
        )
    if "gcp_my_sql_settings" in value:
        import capo_database_migration_service.types.gcp_my_sql_settings

        out["GcpMySQLSettings"] = (
            capo_database_migration_service.types.gcp_my_sql_settings.serialize_aws_json_1_1(
                value["gcp_my_sql_settings"]
            )
        )
    if "timestream_settings" in value:
        import capo_database_migration_service.types.timestream_settings

        out["TimestreamSettings"] = (
            capo_database_migration_service.types.timestream_settings.serialize_aws_json_1_1(
                value["timestream_settings"]
            )
        )
    if "lakehouse_settings" in value:
        import capo_database_migration_service.types.lakehouse_settings

        out["LakehouseSettings"] = (
            capo_database_migration_service.types.lakehouse_settings.serialize_aws_json_1_1(
                value["lakehouse_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("EndpointIdentifier") is not None:
        out["endpoint_identifier"] = data["EndpointIdentifier"]
    if data.get("EndpointType") is not None:
        import capo_database_migration_service.types.replication_endpoint_type_value

        out["endpoint_type"] = (
            capo_database_migration_service.types.replication_endpoint_type_value.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if data.get("EngineName") is not None:
        out["engine_name"] = data["EngineName"]
    if data.get("EngineDisplayName") is not None:
        out["engine_display_name"] = data["EngineDisplayName"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("ExtraConnectionAttributes") is not None:
        out["extra_connection_attributes"] = data["ExtraConnectionAttributes"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("SslMode") is not None:
        import capo_database_migration_service.types.dms_ssl_mode_value

        out["ssl_mode"] = (
            capo_database_migration_service.types.dms_ssl_mode_value.deserialize_aws_json_1_1(
                data["SslMode"]
            )
        )
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if data.get("ExternalTableDefinition") is not None:
        out["external_table_definition"] = data["ExternalTableDefinition"]
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("IsReadOnly") is not None:
        out["is_read_only"] = data["IsReadOnly"]
    if data.get("DynamoDbSettings") is not None:
        import capo_database_migration_service.types.dynamo_db_settings

        out["dynamo_db_settings"] = (
            capo_database_migration_service.types.dynamo_db_settings.deserialize_aws_json_1_1(
                data["DynamoDbSettings"]
            )
        )
    if data.get("S3Settings") is not None:
        import capo_database_migration_service.types.s3_settings

        out["s3_settings"] = (
            capo_database_migration_service.types.s3_settings.deserialize_aws_json_1_1(
                data["S3Settings"]
            )
        )
    if data.get("DmsTransferSettings") is not None:
        import capo_database_migration_service.types.dms_transfer_settings

        out["dms_transfer_settings"] = (
            capo_database_migration_service.types.dms_transfer_settings.deserialize_aws_json_1_1(
                data["DmsTransferSettings"]
            )
        )
    if data.get("MongoDbSettings") is not None:
        import capo_database_migration_service.types.mongo_db_settings

        out["mongo_db_settings"] = (
            capo_database_migration_service.types.mongo_db_settings.deserialize_aws_json_1_1(
                data["MongoDbSettings"]
            )
        )
    if data.get("KinesisSettings") is not None:
        import capo_database_migration_service.types.kinesis_settings

        out["kinesis_settings"] = (
            capo_database_migration_service.types.kinesis_settings.deserialize_aws_json_1_1(
                data["KinesisSettings"]
            )
        )
    if data.get("KafkaSettings") is not None:
        import capo_database_migration_service.types.kafka_settings

        out["kafka_settings"] = (
            capo_database_migration_service.types.kafka_settings.deserialize_aws_json_1_1(
                data["KafkaSettings"]
            )
        )
    if data.get("ElasticsearchSettings") is not None:
        import capo_database_migration_service.types.elasticsearch_settings

        out["elasticsearch_settings"] = (
            capo_database_migration_service.types.elasticsearch_settings.deserialize_aws_json_1_1(
                data["ElasticsearchSettings"]
            )
        )
    if data.get("NeptuneSettings") is not None:
        import capo_database_migration_service.types.neptune_settings

        out["neptune_settings"] = (
            capo_database_migration_service.types.neptune_settings.deserialize_aws_json_1_1(
                data["NeptuneSettings"]
            )
        )
    if data.get("RedshiftSettings") is not None:
        import capo_database_migration_service.types.redshift_settings

        out["redshift_settings"] = (
            capo_database_migration_service.types.redshift_settings.deserialize_aws_json_1_1(
                data["RedshiftSettings"]
            )
        )
    if data.get("PostgreSQLSettings") is not None:
        import capo_database_migration_service.types.postgre_sql_settings

        out["postgre_sql_settings"] = (
            capo_database_migration_service.types.postgre_sql_settings.deserialize_aws_json_1_1(
                data["PostgreSQLSettings"]
            )
        )
    if data.get("MySQLSettings") is not None:
        import capo_database_migration_service.types.my_sql_settings

        out["my_sql_settings"] = (
            capo_database_migration_service.types.my_sql_settings.deserialize_aws_json_1_1(
                data["MySQLSettings"]
            )
        )
    if data.get("OracleSettings") is not None:
        import capo_database_migration_service.types.oracle_settings

        out["oracle_settings"] = (
            capo_database_migration_service.types.oracle_settings.deserialize_aws_json_1_1(
                data["OracleSettings"]
            )
        )
    if data.get("SybaseSettings") is not None:
        import capo_database_migration_service.types.sybase_settings

        out["sybase_settings"] = (
            capo_database_migration_service.types.sybase_settings.deserialize_aws_json_1_1(
                data["SybaseSettings"]
            )
        )
    if data.get("MicrosoftSQLServerSettings") is not None:
        import capo_database_migration_service.types.microsoft_sql_server_settings

        out["microsoft_sql_server_settings"] = (
            capo_database_migration_service.types.microsoft_sql_server_settings.deserialize_aws_json_1_1(
                data["MicrosoftSQLServerSettings"]
            )
        )
    if data.get("IBMDb2Settings") is not None:
        import capo_database_migration_service.types.ibm_db2_settings

        out["ibm_db2_settings"] = (
            capo_database_migration_service.types.ibm_db2_settings.deserialize_aws_json_1_1(
                data["IBMDb2Settings"]
            )
        )
    if data.get("DocDbSettings") is not None:
        import capo_database_migration_service.types.doc_db_settings

        out["doc_db_settings"] = (
            capo_database_migration_service.types.doc_db_settings.deserialize_aws_json_1_1(
                data["DocDbSettings"]
            )
        )
    if data.get("RedisSettings") is not None:
        import capo_database_migration_service.types.redis_settings

        out["redis_settings"] = (
            capo_database_migration_service.types.redis_settings.deserialize_aws_json_1_1(
                data["RedisSettings"]
            )
        )
    if data.get("GcpMySQLSettings") is not None:
        import capo_database_migration_service.types.gcp_my_sql_settings

        out["gcp_my_sql_settings"] = (
            capo_database_migration_service.types.gcp_my_sql_settings.deserialize_aws_json_1_1(
                data["GcpMySQLSettings"]
            )
        )
    if data.get("TimestreamSettings") is not None:
        import capo_database_migration_service.types.timestream_settings

        out["timestream_settings"] = (
            capo_database_migration_service.types.timestream_settings.deserialize_aws_json_1_1(
                data["TimestreamSettings"]
            )
        )
    if data.get("LakehouseSettings") is not None:
        import capo_database_migration_service.types.lakehouse_settings

        out["lakehouse_settings"] = (
            capo_database_migration_service.types.lakehouse_settings.deserialize_aws_json_1_1(
                data["LakehouseSettings"]
            )
        )
    return out
