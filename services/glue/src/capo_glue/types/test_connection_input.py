"""Generated from Smithy shape ``com.amazonaws.glue#TestConnectionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.authentication_configuration_input
    import capo_glue.types.connection_properties
    import capo_glue.types.connection_type


class TestConnectionInput(TypedDict, closed=True):
    connection_type: "capo_glue.types.connection_type.ConnectionType"
    """<p>The type of connection to test. This operation is only available for the <code>JDBC</code> or <code>SALESFORCE</code> connection types.</p>"""
    connection_properties: "capo_glue.types.connection_properties.ConnectionProperties"
    """<p>The key-value pairs that define parameters for the connection.</p> <p>JDBC connections use the following connection properties:</p> <ul> <li> <p>Required: All of (<code>HOST</code>, <code>PORT</code>, <code>JDBC_ENGINE</code>) or <code>JDBC_CONNECTION_URL</code>.</p> </li> <li> <p>Required: All of (<code>USERNAME</code>, <code>PASSWORD</code>) or <code>SECRET_ID</code>.</p> </li> <li> <p>Optional: <code>JDBC_ENFORCE_SSL</code>, <code>CUSTOM_JDBC_CERT</code>, <code>CUSTOM_JDBC_CERT_STRING</code>, <code>SKIP_CUSTOM_JDBC_CERT_VALIDATION</code>. These parameters are used to configure SSL with JDBC.</p> </li> </ul> <p>SALESFORCE connections require the <code>AuthenticationConfiguration</code> member to be configured.</p>"""
    authentication_configuration: NotRequired[
        "capo_glue.types.authentication_configuration_input.AuthenticationConfigurationInput"
    ]
    """<p>A structure containing the authentication configuration in the TestConnection request. Required for a connection to Salesforce using OAuth authentication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestConnectionInput) -> dict:
    out: dict = {}
    import capo_glue.types.connection_type

    out["ConnectionType"] = capo_glue.types.connection_type.serialize_aws_json_1_1(
        value["connection_type"]
    )
    import capo_glue.types.connection_properties

    out["ConnectionProperties"] = (
        capo_glue.types.connection_properties.serialize_aws_json_1_1(
            value["connection_properties"]
        )
    )
    if "authentication_configuration" in value:
        import capo_glue.types.authentication_configuration_input

        out["AuthenticationConfiguration"] = (
            capo_glue.types.authentication_configuration_input.serialize_aws_json_1_1(
                value["authentication_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestConnectionInput:
    out: TestConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionType") is not None:
        import capo_glue.types.connection_type

        out["connection_type"] = (
            capo_glue.types.connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    else:
        raise DeserializationError("TestConnectionInput.connection_type required")
    if data.get("ConnectionProperties") is not None:
        import capo_glue.types.connection_properties

        out["connection_properties"] = (
            capo_glue.types.connection_properties.deserialize_aws_json_1_1(
                data["ConnectionProperties"]
            )
        )
    else:
        raise DeserializationError("TestConnectionInput.connection_properties required")
    if data.get("AuthenticationConfiguration") is not None:
        import capo_glue.types.authentication_configuration_input

        out["authentication_configuration"] = (
            capo_glue.types.authentication_configuration_input.deserialize_aws_json_1_1(
                data["AuthenticationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: TestConnectionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_configuration" in value:
        import capo_glue.types.authentication_configuration_input

        out["authentication_configuration"] = (
            capo_glue.types.authentication_configuration_input.redact_sensitive(
                value["authentication_configuration"]
            )
        )
    return out
