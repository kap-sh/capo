"""Generated from Smithy shape ``com.amazonaws.glue#RegisterConnectionTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.connection_properties_configuration
    import capo_glue.types.connector_authentication_configuration
    import capo_glue.types.description
    import capo_glue.types.integration_type
    import capo_glue.types.name_string
    import capo_glue.types.rest_configuration
    import capo_glue.types.tags_map


class RegisterConnectionTypeRequest(TypedDict, closed=True):
    connection_type: "capo_glue.types.name_string.NameString"
    """<p>The name of the connection type. Must be between 1 and 255 characters and must be prefixed with "REST-" to indicate it is a REST-based connector.</p>"""
    integration_type: "capo_glue.types.integration_type.IntegrationType"
    """<p>The integration type for the connection. Currently only "REST" protocol is supported.</p>"""
    description: NotRequired["capo_glue.types.description.Description"]
    """<p>A description of the connection type. Can be up to 2048 characters and provides details about the purpose and functionality of the connection type.</p>"""
    connection_properties: "capo_glue.types.connection_properties_configuration.ConnectionPropertiesConfiguration"
    """<p>Defines the base URL and additional request parameters needed during connection creation for this connection type.</p>"""
    connector_authentication_configuration: "capo_glue.types.connector_authentication_configuration.ConnectorAuthenticationConfiguration"
    """<p>Defines the supported authentication types and required properties for this connection type, including Basic, OAuth2, and Custom authentication methods.</p>"""
    rest_configuration: "capo_glue.types.rest_configuration.RestConfiguration"
    """<p>Defines the HTTP request and response configuration, validation endpoint, and entity configurations for REST API interactions.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The tags you assign to the connection type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterConnectionTypeRequest) -> dict:
    out: dict = {}
    out["ConnectionType"] = value["connection_type"]
    import capo_glue.types.integration_type

    out["IntegrationType"] = capo_glue.types.integration_type.serialize_aws_json_1_1(
        value["integration_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_glue.types.connection_properties_configuration

    out["ConnectionProperties"] = (
        capo_glue.types.connection_properties_configuration.serialize_aws_json_1_1(
            value["connection_properties"]
        )
    )
    import capo_glue.types.connector_authentication_configuration

    out["ConnectorAuthenticationConfiguration"] = (
        capo_glue.types.connector_authentication_configuration.serialize_aws_json_1_1(
            value["connector_authentication_configuration"]
        )
    )
    import capo_glue.types.rest_configuration

    out["RestConfiguration"] = (
        capo_glue.types.rest_configuration.serialize_aws_json_1_1(
            value["rest_configuration"]
        )
    )
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterConnectionTypeRequest:
    out: RegisterConnectionTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionType") is not None:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.connection_type required"
        )
    if data.get("IntegrationType") is not None:
        import capo_glue.types.integration_type

        out["integration_type"] = (
            capo_glue.types.integration_type.deserialize_aws_json_1_1(
                data["IntegrationType"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.integration_type required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConnectionProperties") is not None:
        import capo_glue.types.connection_properties_configuration

        out["connection_properties"] = (
            capo_glue.types.connection_properties_configuration.deserialize_aws_json_1_1(
                data["ConnectionProperties"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.connection_properties required"
        )
    if data.get("ConnectorAuthenticationConfiguration") is not None:
        import capo_glue.types.connector_authentication_configuration

        out["connector_authentication_configuration"] = (
            capo_glue.types.connector_authentication_configuration.deserialize_aws_json_1_1(
                data["ConnectorAuthenticationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.connector_authentication_configuration required"
        )
    if data.get("RestConfiguration") is not None:
        import capo_glue.types.rest_configuration

        out["rest_configuration"] = (
            capo_glue.types.rest_configuration.deserialize_aws_json_1_1(
                data["RestConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.rest_configuration required"
        )
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
