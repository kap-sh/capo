"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateConnectionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_authorization_type
    import capo_cloudwatch_events.types.connection_description
    import capo_cloudwatch_events.types.connection_name
    import capo_cloudwatch_events.types.create_connection_auth_request_parameters


class CreateConnectionRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.connection_name.ConnectionName"
    """<p>The name for the connection to create.</p>"""
    description: NotRequired[
        "capo_cloudwatch_events.types.connection_description.ConnectionDescription"
    ]
    """<p>A description for the connection to create.</p>"""
    authorization_type: "capo_cloudwatch_events.types.connection_authorization_type.ConnectionAuthorizationType"
    """<p>The type of authorization to use for the connection.</p>"""
    auth_parameters: "capo_cloudwatch_events.types.create_connection_auth_request_parameters.CreateConnectionAuthRequestParameters"
    """<p>A <code>CreateConnectionAuthRequestParameters</code> object that contains the authorization parameters to use to authorize with the endpoint. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_cloudwatch_events.types.connection_authorization_type

    out["AuthorizationType"] = (
        capo_cloudwatch_events.types.connection_authorization_type.serialize_aws_json_1_1(
            value["authorization_type"]
        )
    )
    import capo_cloudwatch_events.types.create_connection_auth_request_parameters

    out["AuthParameters"] = (
        capo_cloudwatch_events.types.create_connection_auth_request_parameters.serialize_aws_json_1_1(
            value["auth_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateConnectionRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AuthorizationType") is not None:
        import capo_cloudwatch_events.types.connection_authorization_type

        out["authorization_type"] = (
            capo_cloudwatch_events.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionRequest.authorization_type required"
        )
    if data.get("AuthParameters") is not None:
        import capo_cloudwatch_events.types.create_connection_auth_request_parameters

        out["auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_auth_request_parameters.deserialize_aws_json_1_1(
                data["AuthParameters"]
            )
        )
    else:
        raise DeserializationError("CreateConnectionRequest.auth_parameters required")
    return out


def redact_sensitive(value: CreateConnectionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_auth_request_parameters

        out["auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_auth_request_parameters.redact_sensitive(
                value["auth_parameters"]
            )
        )
    return out
