"""Generated from Smithy shape ``com.amazonaws.glue#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.authentication_configuration
    import capo_glue.types.compute_environment_list
    import capo_glue.types.connection_properties
    import capo_glue.types.connection_schema_version
    import capo_glue.types.connection_status
    import capo_glue.types.connection_type
    import capo_glue.types.description_string
    import capo_glue.types.long_value_string
    import capo_glue.types.match_criteria
    import capo_glue.types.name_string
    import capo_glue.types.physical_connection_requirements
    import capo_glue.types.property_map
    import capo_glue.types.timestamp


class Connection(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the connection definition.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The description of the connection.</p>"""
    connection_type: NotRequired["capo_glue.types.connection_type.ConnectionType"]
    """<p>The type of the connection. Currently, SFTP is not supported.</p>"""
    match_criteria: NotRequired["capo_glue.types.match_criteria.MatchCriteria"]
    """<p>A list of criteria that can be used in selecting this connection.</p>"""
    connection_properties: NotRequired[
        "capo_glue.types.connection_properties.ConnectionProperties"
    ]
    """<p>These key-value pairs define parameters for the connection when using the version 1 Connection schema:</p> <ul> <li> <p> <code>HOST</code> - The host URI: either the fully qualified domain name (FQDN) or the IPv4 address of the database host.</p> </li> <li> <p> <code>PORT</code> - The port number, between 1024 and 65535, of the port on which the database host is listening for database connections.</p> </li> <li> <p> <code>USER_NAME</code> - The name under which to log in to the database. The value string for <code>USER_NAME</code> is "<code>USERNAME</code>".</p> </li> <li> <p> <code>PASSWORD</code> - A password, if one is used, for the user name.</p> </li> <li> <p> <code>ENCRYPTED_PASSWORD</code> - When you enable connection password protection by setting <code>ConnectionPasswordEncryption</code> in the Data Catalog encryption settings, this field stores the encrypted password.</p> </li> <li> <p> <code>JDBC_DRIVER_JAR_URI</code> - The Amazon Simple Storage Service (Amazon S3) path of the JAR file that contains the JDBC driver to use.</p> </li> <li> <p> <code>JDBC_DRIVER_CLASS_NAME</code> - The class name of the JDBC driver to use.</p> </li> <li> <p> <code>JDBC_ENGINE</code> - The name of the JDBC engine to use.</p> </li> <li> <p> <code>JDBC_ENGINE_VERSION</code> - The version of the JDBC engine to use.</p> </li> <li> <p> <code>CONFIG_FILES</code> - (Reserved for future use.)</p> </li> <li> <p> <code>INSTANCE_ID</code> - The instance ID to use.</p> </li> <li> <p> <code>JDBC_CONNECTION_URL</code> - The URL for connecting to a JDBC data source.</p> </li> <li> <p> <code>JDBC_ENFORCE_SSL</code> - A case-insensitive Boolean string (true, false) specifying whether Secure Sockets Layer (SSL) with hostname matching is enforced for the JDBC connection on the client. The default is false.</p> </li> <li> <p> <code>CUSTOM_JDBC_CERT</code> - An Amazon S3 location specifying the customer's root certificate. Glue uses this root certificate to validate the customer’s certificate when connecting to the customer database. Glue only handles X.509 certificates. The certificate provided must be DER-encoded and supplied in Base64 encoding PEM format.</p> </li> <li> <p> <code>SKIP_CUSTOM_JDBC_CERT_VALIDATION</code> - By default, this is <code>false</code>. Glue validates the Signature algorithm and Subject Public Key Algorithm for the customer certificate. The only permitted algorithms for the Signature algorithm are SHA256withRSA, SHA384withRSA or SHA512withRSA. For the Subject Public Key Algorithm, the key length must be at least 2048. You can set the value of this property to <code>true</code> to skip Glue’s validation of the customer certificate.</p> </li> <li> <p> <code>CUSTOM_JDBC_CERT_STRING</code> - A custom JDBC certificate string which is used for domain match or distinguished name match to prevent a man-in-the-middle attack. In Oracle database, this is used as the <code>SSL_SERVER_CERT_DN</code>; in Microsoft SQL Server, this is used as the <code>hostNameInCertificate</code>.</p> </li> <li> <p> <code>CONNECTION_URL</code> - The URL for connecting to a general (non-JDBC) data source.</p> </li> <li> <p> <code>SECRET_ID</code> - The secret ID used for the secret manager of credentials.</p> </li> <li> <p> <code>CONNECTOR_URL</code> - The connector URL for a MARKETPLACE or CUSTOM connection.</p> </li> <li> <p> <code>CONNECTOR_TYPE</code> - The connector type for a MARKETPLACE or CUSTOM connection.</p> </li> <li> <p> <code>CONNECTOR_CLASS_NAME</code> - The connector class name for a MARKETPLACE or CUSTOM connection.</p> </li> <li> <p> <code>KAFKA_BOOTSTRAP_SERVERS</code> - A comma-separated list of host and port pairs that are the addresses of the Apache Kafka brokers in a Kafka cluster to which a Kafka client will connect to and bootstrap itself.</p> </li> <li> <p> <code>KAFKA_SSL_ENABLED</code> - Whether to enable or disable SSL on an Apache Kafka connection. Default value is "true".</p> </li> <li> <p> <code>KAFKA_CUSTOM_CERT</code> - The Amazon S3 URL for the private CA cert file (.pem format). The default is an empty string.</p> </li> <li> <p> <code>KAFKA_SKIP_CUSTOM_CERT_VALIDATION</code> - Whether to skip the validation of the CA cert file or not. Glue validates for three algorithms: SHA256withRSA, SHA384withRSA and SHA512withRSA. Default value is "false".</p> </li> <li> <p> <code>KAFKA_CLIENT_KEYSTORE</code> - The Amazon S3 location of the client keystore file for Kafka client side authentication (Optional).</p> </li> <li> <p> <code>KAFKA_CLIENT_KEYSTORE_PASSWORD</code> - The password to access the provided keystore (Optional).</p> </li> <li> <p> <code>KAFKA_CLIENT_KEY_PASSWORD</code> - A keystore can consist of multiple keys, so this is the password to access the client key to be used with the Kafka server side key (Optional).</p> </li> <li> <p> <code>ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD</code> - The encrypted version of the Kafka client keystore password (if the user has the Glue encrypt passwords setting selected).</p> </li> <li> <p> <code>ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD</code> - The encrypted version of the Kafka client key password (if the user has the Glue encrypt passwords setting selected).</p> </li> <li> <p> <code>KAFKA_SASL_MECHANISM</code> - <code>"SCRAM-SHA-512"</code>, <code>"GSSAPI"</code>, <code>"AWS_MSK_IAM"</code>, or <code>"PLAIN"</code>. These are the supported <a href="https://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml">SASL Mechanisms</a>.</p> </li> <li> <p> <code>KAFKA_SASL_PLAIN_USERNAME</code> - A plaintext username used to authenticate with the "PLAIN" mechanism.</p> </li> <li> <p> <code>KAFKA_SASL_PLAIN_PASSWORD</code> - A plaintext password used to authenticate with the "PLAIN" mechanism.</p> </li> <li> <p> <code>ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD</code> - The encrypted version of the Kafka SASL PLAIN password (if the user has the Glue encrypt passwords setting selected).</p> </li> <li> <p> <code>KAFKA_SASL_SCRAM_USERNAME</code> - A plaintext username used to authenticate with the "SCRAM-SHA-512" mechanism.</p> </li> <li> <p> <code>KAFKA_SASL_SCRAM_PASSWORD</code> - A plaintext password used to authenticate with the "SCRAM-SHA-512" mechanism.</p> </li> <li> <p> <code>ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD</code> - The encrypted version of the Kafka SASL SCRAM password (if the user has the Glue encrypt passwords setting selected).</p> </li> <li> <p> <code>KAFKA_SASL_SCRAM_SECRETS_ARN</code> - The Amazon Resource Name of a secret in Amazon Web Services Secrets Manager.</p> </li> <li> <p> <code>KAFKA_SASL_GSSAPI_KEYTAB</code> - The S3 location of a Kerberos <code>keytab</code> file. A keytab stores long-term keys for one or more principals. For more information, see <a href="https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html">MIT Kerberos Documentation: Keytab</a>.</p> </li> <li> <p> <code>KAFKA_SASL_GSSAPI_KRB5_CONF</code> - The S3 location of a Kerberos <code>krb5.conf</code> file. A krb5.conf stores Kerberos configuration information, such as the location of the KDC server. For more information, see <a href="https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html">MIT Kerberos Documentation: krb5.conf</a>.</p> </li> <li> <p> <code>KAFKA_SASL_GSSAPI_SERVICE</code> - The Kerberos service name, as set with <code>sasl.kerberos.service.name</code> in your <a href="https://kafka.apache.org/documentation/#brokerconfigs_sasl.kerberos.service.name">Kafka Configuration</a>.</p> </li> <li> <p> <code>KAFKA_SASL_GSSAPI_PRINCIPAL</code> - The name of the Kerberos princial used by Glue. For more information, see <a href="https://kafka.apache.org/documentation/#security_sasl_kerberos_clientconfig">Kafka Documentation: Configuring Kafka Brokers</a>.</p> </li> <li> <p> <code>ROLE_ARN</code> - The role to be used for running queries.</p> </li> <li> <p> <code>REGION</code> - The Amazon Web Services Region where queries will be run.</p> </li> <li> <p> <code>WORKGROUP_NAME</code> - The name of an Amazon Redshift serverless workgroup or Amazon Athena workgroup in which queries will run.</p> </li> <li> <p> <code>CLUSTER_IDENTIFIER</code> - The cluster identifier of an Amazon Redshift cluster in which queries will run.</p> </li> <li> <p> <code>DATABASE</code> - The Amazon Redshift database that you are connecting to.</p> </li> </ul>"""
    spark_properties: NotRequired["capo_glue.types.property_map.PropertyMap"]
    """<p>Connection properties specific to the Spark compute environment.</p>"""
    athena_properties: NotRequired["capo_glue.types.property_map.PropertyMap"]
    """<p>Connection properties specific to the Athena compute environment.</p>"""
    python_properties: NotRequired["capo_glue.types.property_map.PropertyMap"]
    """<p>Connection properties specific to the Python compute environment.</p>"""
    physical_connection_requirements: NotRequired[
        "capo_glue.types.physical_connection_requirements.PhysicalConnectionRequirements"
    ]
    """<p>The physical connection requirements, such as virtual private cloud (VPC) and <code>SecurityGroup</code>, that are needed to make this connection successfully.</p>"""
    creation_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The timestamp of the time that this connection definition was created.</p>"""
    last_updated_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The timestamp of the last time the connection definition was updated.</p>"""
    last_updated_by: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The user, group, or role that last updated this connection definition.</p>"""
    status: NotRequired["capo_glue.types.connection_status.ConnectionStatus"]
    """<p>The status of the connection. Can be one of: <code>READY</code>, <code>IN_PROGRESS</code>, or <code>FAILED</code>.</p>"""
    status_reason: NotRequired["capo_glue.types.long_value_string.LongValueString"]
    """<p>The reason for the connection status.</p>"""
    last_connection_validation_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>A timestamp of the time this connection was last validated.</p>"""
    authentication_configuration: NotRequired[
        "capo_glue.types.authentication_configuration.AuthenticationConfiguration"
    ]
    """<p>The authentication properties of the connection.</p>"""
    connection_schema_version: NotRequired[
        "capo_glue.types.connection_schema_version.ConnectionSchemaVersion"
    ]
    """<p>The version of the connection schema for this connection. Version 2 supports properties for specific compute environments.</p>"""
    compatible_compute_environments: NotRequired[
        "capo_glue.types.compute_environment_list.ComputeEnvironmentList"
    ]
    """<p>A list of compute environments compatible with the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connection) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "connection_type" in value:
        import capo_glue.types.connection_type

        out["ConnectionType"] = capo_glue.types.connection_type.serialize_aws_json_1_1(
            value["connection_type"]
        )
    if "match_criteria" in value:
        import capo_glue.types.match_criteria

        out["MatchCriteria"] = capo_glue.types.match_criteria.serialize_aws_json_1_1(
            value["match_criteria"]
        )
    if "connection_properties" in value:
        import capo_glue.types.connection_properties

        out["ConnectionProperties"] = (
            capo_glue.types.connection_properties.serialize_aws_json_1_1(
                value["connection_properties"]
            )
        )
    if "spark_properties" in value:
        import capo_glue.types.property_map

        out["SparkProperties"] = capo_glue.types.property_map.serialize_aws_json_1_1(
            value["spark_properties"]
        )
    if "athena_properties" in value:
        import capo_glue.types.property_map

        out["AthenaProperties"] = capo_glue.types.property_map.serialize_aws_json_1_1(
            value["athena_properties"]
        )
    if "python_properties" in value:
        import capo_glue.types.property_map

        out["PythonProperties"] = capo_glue.types.property_map.serialize_aws_json_1_1(
            value["python_properties"]
        )
    if "physical_connection_requirements" in value:
        import capo_glue.types.physical_connection_requirements

        out["PhysicalConnectionRequirements"] = (
            capo_glue.types.physical_connection_requirements.serialize_aws_json_1_1(
                value["physical_connection_requirements"]
            )
        )
    if "creation_time" in value:
        import capo_glue.types.timestamp

        out["CreationTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_glue.types.timestamp

        out["LastUpdatedTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "last_updated_by" in value:
        out["LastUpdatedBy"] = value["last_updated_by"]
    if "status" in value:
        import capo_glue.types.connection_status

        out["Status"] = capo_glue.types.connection_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "last_connection_validation_time" in value:
        import capo_glue.types.timestamp

        out["LastConnectionValidationTime"] = (
            capo_glue.types.timestamp.serialize_aws_json_1_1(
                value["last_connection_validation_time"]
            )
        )
    if "authentication_configuration" in value:
        import capo_glue.types.authentication_configuration

        out["AuthenticationConfiguration"] = (
            capo_glue.types.authentication_configuration.serialize_aws_json_1_1(
                value["authentication_configuration"]
            )
        )
    if "connection_schema_version" in value:
        out["ConnectionSchemaVersion"] = value["connection_schema_version"]
    if "compatible_compute_environments" in value:
        import capo_glue.types.compute_environment_list

        out["CompatibleComputeEnvironments"] = (
            capo_glue.types.compute_environment_list.serialize_aws_json_1_1(
                value["compatible_compute_environments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConnectionType") is not None:
        import capo_glue.types.connection_type

        out["connection_type"] = (
            capo_glue.types.connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    if data.get("MatchCriteria") is not None:
        import capo_glue.types.match_criteria

        out["match_criteria"] = capo_glue.types.match_criteria.deserialize_aws_json_1_1(
            data["MatchCriteria"]
        )
    if data.get("ConnectionProperties") is not None:
        import capo_glue.types.connection_properties

        out["connection_properties"] = (
            capo_glue.types.connection_properties.deserialize_aws_json_1_1(
                data["ConnectionProperties"]
            )
        )
    if data.get("SparkProperties") is not None:
        import capo_glue.types.property_map

        out["spark_properties"] = capo_glue.types.property_map.deserialize_aws_json_1_1(
            data["SparkProperties"]
        )
    if data.get("AthenaProperties") is not None:
        import capo_glue.types.property_map

        out["athena_properties"] = (
            capo_glue.types.property_map.deserialize_aws_json_1_1(
                data["AthenaProperties"]
            )
        )
    if data.get("PythonProperties") is not None:
        import capo_glue.types.property_map

        out["python_properties"] = (
            capo_glue.types.property_map.deserialize_aws_json_1_1(
                data["PythonProperties"]
            )
        )
    if data.get("PhysicalConnectionRequirements") is not None:
        import capo_glue.types.physical_connection_requirements

        out["physical_connection_requirements"] = (
            capo_glue.types.physical_connection_requirements.deserialize_aws_json_1_1(
                data["PhysicalConnectionRequirements"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_glue.types.timestamp

        out["creation_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_glue.types.timestamp

        out["last_updated_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdatedTime"]
        )
    if data.get("LastUpdatedBy") is not None:
        out["last_updated_by"] = data["LastUpdatedBy"]
    if data.get("Status") is not None:
        import capo_glue.types.connection_status

        out["status"] = capo_glue.types.connection_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("LastConnectionValidationTime") is not None:
        import capo_glue.types.timestamp

        out["last_connection_validation_time"] = (
            capo_glue.types.timestamp.deserialize_aws_json_1_1(
                data["LastConnectionValidationTime"]
            )
        )
    if data.get("AuthenticationConfiguration") is not None:
        import capo_glue.types.authentication_configuration

        out["authentication_configuration"] = (
            capo_glue.types.authentication_configuration.deserialize_aws_json_1_1(
                data["AuthenticationConfiguration"]
            )
        )
    if data.get("ConnectionSchemaVersion") is not None:
        out["connection_schema_version"] = data["ConnectionSchemaVersion"]
    if data.get("CompatibleComputeEnvironments") is not None:
        import capo_glue.types.compute_environment_list

        out["compatible_compute_environments"] = (
            capo_glue.types.compute_environment_list.deserialize_aws_json_1_1(
                data["CompatibleComputeEnvironments"]
            )
        )
    return out
