"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyEndpointMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

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
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.sybase_settings
    import capo_database_migration_service.types.timestream_settings


class ModifyEndpointMessage(TypedDict, closed=True):
    endpoint_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>"""
    endpoint_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.</p>"""
    endpoint_type: NotRequired[
        "capo_database_migration_service.types.replication_endpoint_type_value.ReplicationEndpointTypeValue"
    ]
    """<p>The type of endpoint. Valid values are <code>source</code> and <code>target</code>.</p>"""
    engine_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The database engine name. Valid values, depending on the EndpointType, include <code>"mysql"</code>, <code>"oracle"</code>, <code>"postgres"</code>, <code>"mariadb"</code>, <code>"aurora"</code>, <code>"aurora-postgresql"</code>, <code>"redshift"</code>, <code>"s3"</code>, <code>"db2"</code>, <code>"db2-zos"</code>, <code>"azuredb"</code>, <code>"sybase"</code>, <code>"dynamodb"</code>, <code>"mongodb"</code>, <code>"kinesis"</code>, <code>"kafka"</code>, <code>"elasticsearch"</code>, <code>"documentdb"</code>, <code>"sqlserver"</code>, <code>"neptune"</code>, and <code>"babelfish"</code>.</p>"""
    username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The user name to be used to login to the endpoint database.</p>"""
    password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>The password to be used to login to the endpoint database.</p>"""
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the server where the endpoint database resides.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port used by the endpoint database.</p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the endpoint database. For a MySQL source or target endpoint, do not specify DatabaseName.</p>"""
    extra_connection_attributes: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Additional attributes associated with the connection. To reset this parameter, pass the empty string ("") as an argument.</p>"""
    certificate_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>"""
    ssl_mode: NotRequired[
        "capo_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the endpoint. The default value is <code>none</code>.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> The Amazon Resource Name (ARN) for the IAM role you want to use to modify the endpoint. The role must allow the <code>iam:PassRole</code> action.</p>"""
    external_table_definition: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The external table definition.</p>"""
    dynamo_db_settings: NotRequired[
        "capo_database_migration_service.types.dynamo_db_settings.DynamoDbSettings"
    ]
    """<p>Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping">Using Object Mapping to Migrate Data to DynamoDB</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    s3_settings: NotRequired[
        "capo_database_migration_service.types.s3_settings.S3Settings"
    ]
    """<p>Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring">Extra Connection Attributes When Using Amazon S3 as a Target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    dms_transfer_settings: NotRequired[
        "capo_database_migration_service.types.dms_transfer_settings.DmsTransferSettings"
    ]
    """<p>The settings in JSON format for the DMS transfer type of source endpoint. </p> <p>Attributes include the following:</p> <ul> <li> <p>serviceAccessRoleArn - The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the <code>iam:PassRole</code> action.</p> </li> <li> <p>BucketName - The name of the S3 bucket to use.</p> </li> </ul> <p>Shorthand syntax for these settings is as follows: <code>ServiceAccessRoleArn=string ,BucketName=string</code> </p> <p>JSON syntax for these settings is as follows: <code>{ "ServiceAccessRoleArn": "string", "BucketName": "string"} </code> </p>"""
    mongo_db_settings: NotRequired[
        "capo_database_migration_service.types.mongo_db_settings.MongoDbSettings"
    ]
    """<p>Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the configuration properties section in <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration">Endpoint configuration settings when using MongoDB as a source for Database Migration Service</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    kinesis_settings: NotRequired[
        "capo_database_migration_service.types.kinesis_settings.KinesisSettings"
    ]
    """<p>Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping">Using object mapping to migrate data to a Kinesis data stream</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    kafka_settings: NotRequired[
        "capo_database_migration_service.types.kafka_settings.KafkaSettings"
    ]
    """<p>Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping">Using object mapping to migrate data to a Kafka topic</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    elasticsearch_settings: NotRequired[
        "capo_database_migration_service.types.elasticsearch_settings.ElasticsearchSettings"
    ]
    """<p>Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration">Extra Connection Attributes When Using OpenSearch as a Target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    neptune_settings: NotRequired[
        "capo_database_migration_service.types.neptune_settings.NeptuneSettings"
    ]
    """<p>Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings">Specifying graph-mapping rules using Gremlin and R2RML for Amazon Neptune as a target</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    redshift_settings: NotRequired[
        "capo_database_migration_service.types.redshift_settings.RedshiftSettings"
    ]
    postgre_sql_settings: NotRequired[
        "capo_database_migration_service.types.postgre_sql_settings.PostgreSQLSettings"
    ]
    """<p>Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib">Extra connection attributes when using PostgreSQL as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib"> Extra connection attributes when using PostgreSQL as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    my_sql_settings: NotRequired[
        "capo_database_migration_service.types.my_sql_settings.MySQLSettings"
    ]
    """<p>Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib">Extra connection attributes when using MySQL as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib">Extra connection attributes when using a MySQL-compatible database as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    oracle_settings: NotRequired[
        "capo_database_migration_service.types.oracle_settings.OracleSettings"
    ]
    """<p>Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib">Extra connection attributes when using Oracle as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib"> Extra connection attributes when using Oracle as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    sybase_settings: NotRequired[
        "capo_database_migration_service.types.sybase_settings.SybaseSettings"
    ]
    """<p>Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib">Extra connection attributes when using SAP ASE as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib">Extra connection attributes when using SAP ASE as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    microsoft_sql_server_settings: NotRequired[
        "capo_database_migration_service.types.microsoft_sql_server_settings.MicrosoftSQLServerSettings"
    ]
    """<p>Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib">Extra connection attributes when using SQL Server as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib"> Extra connection attributes when using SQL Server as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    ibm_db2_settings: NotRequired[
        "capo_database_migration_service.types.ibm_db2_settings.IBMDb2Settings"
    ]
    """<p>Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib">Extra connection attributes when using Db2 LUW as a source for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>"""
    doc_db_settings: NotRequired[
        "capo_database_migration_service.types.doc_db_settings.DocDbSettings"
    ]
    """<p>Settings in JSON format for the source DocumentDB endpoint. For more information about the available settings, see the configuration properties section in <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html"> Using DocumentDB as a Target for Database Migration Service </a> in the <i>Database Migration Service User Guide.</i> </p>"""
    redis_settings: NotRequired[
        "capo_database_migration_service.types.redis_settings.RedisSettings"
    ]
    """<p>Settings in JSON format for the Redis target endpoint.</p>"""
    exact_settings: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this attribute is Y, the current call to <code>ModifyEndpoint</code> replaces all existing endpoint settings with the exact settings that you specify in this call. If this attribute is N, the current call to <code>ModifyEndpoint</code> does two things: </p> <ul> <li> <p>It replaces any endpoint settings that already exist with new values, for settings with the same names.</p> </li> <li> <p>It creates new endpoint settings that you specify in the call, for settings with different names. </p> </li> </ul> <p>For example, if you call <code>create-endpoint ... --endpoint-settings '{"a":1}' ...</code>, the endpoint has the following endpoint settings: <code>'{"a":1}'</code>. If you then call <code>modify-endpoint ... --endpoint-settings '{"b":2}' ...</code> for the same endpoint, the endpoint has the following settings: <code>'{"a":1,"b":2}'</code>. </p> <p>However, suppose that you follow this with a call to <code>modify-endpoint ... --endpoint-settings '{"b":2}' --exact-settings ...</code> for that same endpoint again. Then the endpoint has the following settings: <code>'{"b":2}'</code>. All existing settings are replaced with the exact settings that you specify. </p>"""
    gcp_my_sql_settings: NotRequired[
        "capo_database_migration_service.types.gcp_my_sql_settings.GcpMySQLSettings"
    ]
    """<p>Settings in JSON format for the source GCP MySQL endpoint.</p>"""
    timestream_settings: NotRequired[
        "capo_database_migration_service.types.timestream_settings.TimestreamSettings"
    ]
    """<p>Settings in JSON format for the target Amazon Timestream endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyEndpointMessage) -> dict:
    out: dict = {}
    out["EndpointArn"] = value["endpoint_arn"]
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
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "extra_connection_attributes" in value:
        out["ExtraConnectionAttributes"] = value["extra_connection_attributes"]
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
    if "exact_settings" in value:
        out["ExactSettings"] = value["exact_settings"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyEndpointMessage:
    out: ModifyEndpointMessage = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        raise DeserializationError("ModifyEndpointMessage.endpoint_arn required")
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
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("ExtraConnectionAttributes") is not None:
        out["extra_connection_attributes"] = data["ExtraConnectionAttributes"]
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
    if data.get("ExactSettings") is not None:
        out["exact_settings"] = data["ExactSettings"]
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
    return out
