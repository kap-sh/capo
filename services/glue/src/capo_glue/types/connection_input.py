"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.authentication_configuration_input
    import capo_glue.types.boolean
    import capo_glue.types.compute_environment_list
    import capo_glue.types.connection_properties
    import capo_glue.types.connection_type
    import capo_glue.types.description_string
    import capo_glue.types.match_criteria
    import capo_glue.types.name_string
    import capo_glue.types.physical_connection_requirements
    import capo_glue.types.property_map


class ConnectionInput(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the connection.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The description of the connection.</p>"""
    connection_type: "capo_glue.types.connection_type.ConnectionType"
    """<p>The type of the connection. Currently, these types are supported:</p> <ul> <li> <p> <code>JDBC</code> - Designates a connection to a database through Java Database Connectivity (JDBC).</p> <p> <code>JDBC</code> Connections use the following ConnectionParameters.</p> <ul> <li> <p>Required: All of (<code>HOST</code>, <code>PORT</code>, <code>JDBC_ENGINE</code>) or <code>JDBC_CONNECTION_URL</code>.</p> </li> <li> <p>Required: All of (<code>USERNAME</code>, <code>PASSWORD</code>) or <code>SECRET_ID</code>.</p> </li> <li> <p>Optional: <code>JDBC_ENFORCE_SSL</code>, <code>CUSTOM_JDBC_CERT</code>, <code>CUSTOM_JDBC_CERT_STRING</code>, <code>SKIP_CUSTOM_JDBC_CERT_VALIDATION</code>. These parameters are used to configure SSL with JDBC.</p> </li> </ul> </li> <li> <p> <code>KAFKA</code> - Designates a connection to an Apache Kafka streaming platform.</p> <p> <code>KAFKA</code> Connections use the following ConnectionParameters.</p> <ul> <li> <p>Required: <code>KAFKA_BOOTSTRAP_SERVERS</code>.</p> </li> <li> <p>Optional: <code>KAFKA_SSL_ENABLED</code>, <code>KAFKA_CUSTOM_CERT</code>, <code>KAFKA_SKIP_CUSTOM_CERT_VALIDATION</code>. These parameters are used to configure SSL with <code>KAFKA</code>.</p> </li> <li> <p>Optional: <code>KAFKA_CLIENT_KEYSTORE</code>, <code>KAFKA_CLIENT_KEYSTORE_PASSWORD</code>, <code>KAFKA_CLIENT_KEY_PASSWORD</code>, <code>ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD</code>, <code>ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD</code>. These parameters are used to configure TLS client configuration with SSL in <code>KAFKA</code>.</p> </li> <li> <p>Optional: <code>KAFKA_SASL_MECHANISM</code>. Can be specified as <code>SCRAM-SHA-512</code>, <code>GSSAPI</code>, or <code>AWS_MSK_IAM</code>.</p> </li> <li> <p>Optional: <code>KAFKA_SASL_SCRAM_USERNAME</code>, <code>KAFKA_SASL_SCRAM_PASSWORD</code>, <code>ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD</code>. These parameters are used to configure SASL/SCRAM-SHA-512 authentication with <code>KAFKA</code>.</p> </li> <li> <p>Optional: <code>KAFKA_SASL_GSSAPI_KEYTAB</code>, <code>KAFKA_SASL_GSSAPI_KRB5_CONF</code>, <code>KAFKA_SASL_GSSAPI_SERVICE</code>, <code>KAFKA_SASL_GSSAPI_PRINCIPAL</code>. These parameters are used to configure SASL/GSSAPI authentication with <code>KAFKA</code>.</p> </li> </ul> </li> <li> <p> <code>MONGODB</code> - Designates a connection to a MongoDB document database.</p> <p> <code>MONGODB</code> Connections use the following ConnectionParameters.</p> <ul> <li> <p>Required: <code>CONNECTION_URL</code>.</p> </li> <li> <p>Required: All of (<code>USERNAME</code>, <code>PASSWORD</code>) or <code>SECRET_ID</code>.</p> </li> </ul> </li> <li> <p> <code>VIEW_VALIDATION_REDSHIFT</code> - Designates a connection used for view validation by Amazon Redshift.</p> </li> <li> <p> <code>VIEW_VALIDATION_ATHENA</code> - Designates a connection used for view validation by Amazon Athena.</p> </li> <li> <p> <code>NETWORK</code> - Designates a network connection to a data source within an Amazon Virtual Private Cloud environment (Amazon VPC).</p> <p> <code>NETWORK</code> Connections do not require ConnectionParameters. Instead, provide a PhysicalConnectionRequirements.</p> </li> <li> <p> <code>MARKETPLACE</code> - Uses configuration settings contained in a connector purchased from Amazon Web Services Marketplace to read from and write to data stores that are not natively supported by Glue.</p> <p> <code>MARKETPLACE</code> Connections use the following ConnectionParameters.</p> <ul> <li> <p>Required: <code>CONNECTOR_TYPE</code>, <code>CONNECTOR_URL</code>, <code>CONNECTOR_CLASS_NAME</code>, <code>CONNECTION_URL</code>.</p> </li> <li> <p>Required for <code>JDBC</code> <code>CONNECTOR_TYPE</code> connections: All of (<code>USERNAME</code>, <code>PASSWORD</code>) or <code>SECRET_ID</code>.</p> </li> </ul> </li> <li> <p> <code>CUSTOM</code> - Uses configuration settings contained in a custom connector to read from and write to data stores that are not natively supported by Glue.</p> </li> </ul> <p>For more information on the connection parameters needed for a particular connector, see the documentation for the connector in <a href="https://docs.aws.amazon.com/glue/latest/dg/console-connections.html">Adding an Glue connection</a>in the Glue User Guide.</p> <p> <code>SFTP</code> is not supported.</p> <p>For more information about how optional ConnectionProperties are used to configure features in Glue, consult <a href="https://docs.aws.amazon.com/glue/latest/dg/connection-defining.html">Glue connection properties</a>.</p> <p>For more information about how optional ConnectionProperties are used to configure features in Glue Studio, consult <a href="https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html">Using connectors and connections</a>.</p>"""
    match_criteria: NotRequired["capo_glue.types.match_criteria.MatchCriteria"]
    """<p>A list of criteria that can be used in selecting this connection.</p>"""
    connection_properties: "capo_glue.types.connection_properties.ConnectionProperties"
    """<p>These key-value pairs define parameters for the connection.</p>"""
    spark_properties: NotRequired["capo_glue.types.property_map.PropertyMap"]
    """<p>Connection properties specific to the Spark compute environment.</p>"""
    athena_properties: NotRequired["capo_glue.types.property_map.PropertyMap"]
    """<p>Connection properties specific to the Athena compute environment.</p>"""
    python_properties: NotRequired["capo_glue.types.property_map.PropertyMap"]
    """<p>Connection properties specific to the Python compute environment.</p>"""
    physical_connection_requirements: NotRequired[
        "capo_glue.types.physical_connection_requirements.PhysicalConnectionRequirements"
    ]
    """<p>The physical connection requirements, such as virtual private cloud (VPC) and <code>SecurityGroup</code>, that are needed to successfully make this connection.</p>"""
    authentication_configuration: NotRequired[
        "capo_glue.types.authentication_configuration_input.AuthenticationConfigurationInput"
    ]
    """<p>The authentication properties of the connection.</p>"""
    validate_credentials: "capo_glue.types.boolean.Boolean"
    """<p>A flag to validate the credentials during create connection. Default is true. </p>"""
    validate_for_compute_environments: NotRequired[
        "capo_glue.types.compute_environment_list.ComputeEnvironmentList"
    ]
    """<p>The compute environments that the specified connection properties are validated against.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_glue.types.connection_type

    out["ConnectionType"] = capo_glue.types.connection_type.serialize_aws_json_1_1(
        value["connection_type"]
    )
    if "match_criteria" in value:
        import capo_glue.types.match_criteria

        out["MatchCriteria"] = capo_glue.types.match_criteria.serialize_aws_json_1_1(
            value["match_criteria"]
        )
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
    if "authentication_configuration" in value:
        import capo_glue.types.authentication_configuration_input

        out["AuthenticationConfiguration"] = (
            capo_glue.types.authentication_configuration_input.serialize_aws_json_1_1(
                value["authentication_configuration"]
            )
        )
    out["ValidateCredentials"] = value.get("validate_credentials", False)
    if "validate_for_compute_environments" in value:
        import capo_glue.types.compute_environment_list

        out["ValidateForComputeEnvironments"] = (
            capo_glue.types.compute_environment_list.serialize_aws_json_1_1(
                value["validate_for_compute_environments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionInput:
    out: ConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ConnectionInput.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConnectionType") is not None:
        import capo_glue.types.connection_type

        out["connection_type"] = (
            capo_glue.types.connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    else:
        raise DeserializationError("ConnectionInput.connection_type required")
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
    else:
        raise DeserializationError("ConnectionInput.connection_properties required")
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
    if data.get("AuthenticationConfiguration") is not None:
        import capo_glue.types.authentication_configuration_input

        out["authentication_configuration"] = (
            capo_glue.types.authentication_configuration_input.deserialize_aws_json_1_1(
                data["AuthenticationConfiguration"]
            )
        )
    if data.get("ValidateCredentials") is not None:
        out["validate_credentials"] = data["ValidateCredentials"]
    else:
        out["validate_credentials"] = False
    if data.get("ValidateForComputeEnvironments") is not None:
        import capo_glue.types.compute_environment_list

        out["validate_for_compute_environments"] = (
            capo_glue.types.compute_environment_list.deserialize_aws_json_1_1(
                data["ValidateForComputeEnvironments"]
            )
        )
    return out
