"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.kafka_sasl_mechanism
    import capo_database_migration_service.types.kafka_security_protocol
    import capo_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm
    import capo_database_migration_service.types.message_format_value
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string


class KafkaSettings(TypedDict, closed=True):
    broker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance. Specify each broker location in the form <code> <i>broker-hostname-or-ip</i>:<i>port</i> </code>. For example, <code>"ec2-12-345-678-901.compute-1.amazonaws.com:2345"</code>. For more information and examples of specifying a list of broker locations, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html">Using Apache Kafka as a target for Database Migration Service</a> in the <i>Database Migration Service User Guide</i>. </p>"""
    topic: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The topic to which you migrate the data. If you don't specify a topic, DMS specifies <code>"kafka-default-topic"</code> as the migration topic.</p>"""
    message_format: NotRequired[
        "capo_database_migration_service.types.message_format_value.MessageFormatValue"
    ]
    """<p>The output format for the records created on the endpoint. The message format is <code>JSON</code> (default) or <code>JSON_UNFORMATTED</code> (a single line with no tab).</p>"""
    include_transaction_details: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for <code>transaction_id</code>, previous <code>transaction_id</code>, and <code>transaction_record_id</code> (the record offset within a transaction). The default is <code>false</code>.</p>"""
    include_partition_value: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Shows the partition value within the Kafka message output unless the partition type is <code>schema-table-type</code>. The default is <code>false</code>.</p>"""
    partition_include_schema_table: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Prefixes schema and table names to partition values, when the partition type is <code>primary-key-type</code>. Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is <code>false</code>.</p>"""
    include_table_alter_operations: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Includes any data definition language (DDL) operations that change the table in the control data, such as <code>rename-table</code>, <code>drop-table</code>, <code>add-column</code>, <code>drop-column</code>, and <code>rename-column</code>. The default is <code>false</code>.</p>"""
    include_control_details: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output. The default is <code>false</code>.</p>"""
    message_max_bytes: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum size in bytes for records created on the endpoint The default is 1,000,000.</p>"""
    include_null_and_empty: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Include NULL and empty columns for records migrated to the endpoint. The default is <code>false</code>.</p>"""
    security_protocol: NotRequired[
        "capo_database_migration_service.types.kafka_security_protocol.KafkaSecurityProtocol"
    ]
    """<p>Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS). Options include <code>ssl-encryption</code>, <code>ssl-authentication</code>, and <code>sasl-ssl</code>. <code>sasl-ssl</code> requires <code>SaslUsername</code> and <code>SaslPassword</code>.</p>"""
    ssl_client_certificate_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.</p>"""
    ssl_client_key_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.</p>"""
    ssl_client_key_password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p> The password for the client private key used to securely connect to a Kafka target endpoint.</p>"""
    ssl_ca_certificate_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that DMS uses to securely connect to your Kafka target endpoint.</p>"""
    sasl_username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The secure user name you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.</p>"""
    sasl_password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>The secure password you created when you first set up your MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.</p>"""
    no_hex_prefix: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this optional parameter to <code>true</code> to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the <code>NoHexPrefix</code> endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.</p>"""
    sasl_mechanism: NotRequired[
        "capo_database_migration_service.types.kafka_sasl_mechanism.KafkaSaslMechanism"
    ]
    """<p>For SASL/SSL authentication, DMS supports the <code>SCRAM-SHA-512</code> mechanism by default. DMS versions 3.5.0 and later also support the <code>PLAIN</code> mechanism. To use the <code>PLAIN</code> mechanism, set this parameter to <code>PLAIN.</code> </p>"""
    ssl_endpoint_identification_algorithm: NotRequired[
        "capo_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm.KafkaSslEndpointIdentificationAlgorithm"
    ]
    """<p>Sets hostname verification for the certificate. This setting is supported in DMS version 3.5.1 and later. </p>"""
    use_large_integer_value: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies using the large integer value with Kafka.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KafkaSettings) -> dict:
    out: dict = {}
    if "broker" in value:
        out["Broker"] = value["broker"]
    if "topic" in value:
        out["Topic"] = value["topic"]
    if "message_format" in value:
        import capo_database_migration_service.types.message_format_value

        out["MessageFormat"] = (
            capo_database_migration_service.types.message_format_value.serialize_aws_json_1_1(
                value["message_format"]
            )
        )
    if "include_transaction_details" in value:
        out["IncludeTransactionDetails"] = value["include_transaction_details"]
    if "include_partition_value" in value:
        out["IncludePartitionValue"] = value["include_partition_value"]
    if "partition_include_schema_table" in value:
        out["PartitionIncludeSchemaTable"] = value["partition_include_schema_table"]
    if "include_table_alter_operations" in value:
        out["IncludeTableAlterOperations"] = value["include_table_alter_operations"]
    if "include_control_details" in value:
        out["IncludeControlDetails"] = value["include_control_details"]
    if "message_max_bytes" in value:
        out["MessageMaxBytes"] = value["message_max_bytes"]
    if "include_null_and_empty" in value:
        out["IncludeNullAndEmpty"] = value["include_null_and_empty"]
    if "security_protocol" in value:
        import capo_database_migration_service.types.kafka_security_protocol

        out["SecurityProtocol"] = (
            capo_database_migration_service.types.kafka_security_protocol.serialize_aws_json_1_1(
                value["security_protocol"]
            )
        )
    if "ssl_client_certificate_arn" in value:
        out["SslClientCertificateArn"] = value["ssl_client_certificate_arn"]
    if "ssl_client_key_arn" in value:
        out["SslClientKeyArn"] = value["ssl_client_key_arn"]
    if "ssl_client_key_password" in value:
        out["SslClientKeyPassword"] = value["ssl_client_key_password"]
    if "ssl_ca_certificate_arn" in value:
        out["SslCaCertificateArn"] = value["ssl_ca_certificate_arn"]
    if "sasl_username" in value:
        out["SaslUsername"] = value["sasl_username"]
    if "sasl_password" in value:
        out["SaslPassword"] = value["sasl_password"]
    if "no_hex_prefix" in value:
        out["NoHexPrefix"] = value["no_hex_prefix"]
    if "sasl_mechanism" in value:
        import capo_database_migration_service.types.kafka_sasl_mechanism

        out["SaslMechanism"] = (
            capo_database_migration_service.types.kafka_sasl_mechanism.serialize_aws_json_1_1(
                value["sasl_mechanism"]
            )
        )
    if "ssl_endpoint_identification_algorithm" in value:
        import capo_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm

        out["SslEndpointIdentificationAlgorithm"] = (
            capo_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm.serialize_aws_json_1_1(
                value["ssl_endpoint_identification_algorithm"]
            )
        )
    if "use_large_integer_value" in value:
        out["UseLargeIntegerValue"] = value["use_large_integer_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KafkaSettings:
    out: KafkaSettings = {}  # type: ignore[typeddict-item]
    if data.get("Broker") is not None:
        out["broker"] = data["Broker"]
    if data.get("Topic") is not None:
        out["topic"] = data["Topic"]
    if data.get("MessageFormat") is not None:
        import capo_database_migration_service.types.message_format_value

        out["message_format"] = (
            capo_database_migration_service.types.message_format_value.deserialize_aws_json_1_1(
                data["MessageFormat"]
            )
        )
    if data.get("IncludeTransactionDetails") is not None:
        out["include_transaction_details"] = data["IncludeTransactionDetails"]
    if data.get("IncludePartitionValue") is not None:
        out["include_partition_value"] = data["IncludePartitionValue"]
    if data.get("PartitionIncludeSchemaTable") is not None:
        out["partition_include_schema_table"] = data["PartitionIncludeSchemaTable"]
    if data.get("IncludeTableAlterOperations") is not None:
        out["include_table_alter_operations"] = data["IncludeTableAlterOperations"]
    if data.get("IncludeControlDetails") is not None:
        out["include_control_details"] = data["IncludeControlDetails"]
    if data.get("MessageMaxBytes") is not None:
        out["message_max_bytes"] = data["MessageMaxBytes"]
    if data.get("IncludeNullAndEmpty") is not None:
        out["include_null_and_empty"] = data["IncludeNullAndEmpty"]
    if data.get("SecurityProtocol") is not None:
        import capo_database_migration_service.types.kafka_security_protocol

        out["security_protocol"] = (
            capo_database_migration_service.types.kafka_security_protocol.deserialize_aws_json_1_1(
                data["SecurityProtocol"]
            )
        )
    if data.get("SslClientCertificateArn") is not None:
        out["ssl_client_certificate_arn"] = data["SslClientCertificateArn"]
    if data.get("SslClientKeyArn") is not None:
        out["ssl_client_key_arn"] = data["SslClientKeyArn"]
    if data.get("SslClientKeyPassword") is not None:
        out["ssl_client_key_password"] = data["SslClientKeyPassword"]
    if data.get("SslCaCertificateArn") is not None:
        out["ssl_ca_certificate_arn"] = data["SslCaCertificateArn"]
    if data.get("SaslUsername") is not None:
        out["sasl_username"] = data["SaslUsername"]
    if data.get("SaslPassword") is not None:
        out["sasl_password"] = data["SaslPassword"]
    if data.get("NoHexPrefix") is not None:
        out["no_hex_prefix"] = data["NoHexPrefix"]
    if data.get("SaslMechanism") is not None:
        import capo_database_migration_service.types.kafka_sasl_mechanism

        out["sasl_mechanism"] = (
            capo_database_migration_service.types.kafka_sasl_mechanism.deserialize_aws_json_1_1(
                data["SaslMechanism"]
            )
        )
    if data.get("SslEndpointIdentificationAlgorithm") is not None:
        import capo_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm

        out["ssl_endpoint_identification_algorithm"] = (
            capo_database_migration_service.types.kafka_ssl_endpoint_identification_algorithm.deserialize_aws_json_1_1(
                data["SslEndpointIdentificationAlgorithm"]
            )
        )
    if data.get("UseLargeIntegerValue") is not None:
        out["use_large_integer_value"] = data["UseLargeIntegerValue"]
    return out
