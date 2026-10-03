"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_authorization_type
    import capo_eventbridge.types.connection_description
    import capo_eventbridge.types.connection_name
    import capo_eventbridge.types.connectivity_resource_parameters
    import capo_eventbridge.types.create_connection_auth_request_parameters
    import capo_eventbridge.types.kms_key_identifier


class CreateConnectionRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.connection_name.ConnectionName"
    """<p>The name for the connection to create.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.connection_description.ConnectionDescription"
    ]
    """<p>A description for the connection to create.</p>"""
    authorization_type: "capo_eventbridge.types.connection_authorization_type.ConnectionAuthorizationType"
    """<p>The type of authorization to use for the connection.</p> <note> <p>OAUTH tokens are refreshed when a 401 or 407 response is returned.</p> </note>"""
    auth_parameters: "capo_eventbridge.types.create_connection_auth_request_parameters.CreateConnectionAuthRequestParameters"
    """<p>The authorization parameters to use to authorize with the endpoint. </p> <p>You must include only authorization parameters for the <code>AuthorizationType</code> you specify.</p>"""
    invocation_connectivity_parameters: NotRequired[
        "capo_eventbridge.types.connectivity_resource_parameters.ConnectivityResourceParameters"
    ]
    """<p>For connections to private APIs, the parameters to use for invoking the API.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html">Connecting to private APIs</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    kms_key_identifier: NotRequired[
        "capo_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this connection. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt the connection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html">Identify and view keys</a> in the <i>Key Management Service Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_eventbridge.types.connection_authorization_type

    out["AuthorizationType"] = (
        capo_eventbridge.types.connection_authorization_type.serialize_aws_json_1_1(
            value["authorization_type"]
        )
    )
    import capo_eventbridge.types.create_connection_auth_request_parameters

    out["AuthParameters"] = (
        capo_eventbridge.types.create_connection_auth_request_parameters.serialize_aws_json_1_1(
            value["auth_parameters"]
        )
    )
    if "invocation_connectivity_parameters" in value:
        import capo_eventbridge.types.connectivity_resource_parameters

        out["InvocationConnectivityParameters"] = (
            capo_eventbridge.types.connectivity_resource_parameters.serialize_aws_json_1_1(
                value["invocation_connectivity_parameters"]
            )
        )
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
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
        import capo_eventbridge.types.connection_authorization_type

        out["authorization_type"] = (
            capo_eventbridge.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionRequest.authorization_type required"
        )
    if data.get("AuthParameters") is not None:
        import capo_eventbridge.types.create_connection_auth_request_parameters

        out["auth_parameters"] = (
            capo_eventbridge.types.create_connection_auth_request_parameters.deserialize_aws_json_1_1(
                data["AuthParameters"]
            )
        )
    else:
        raise DeserializationError("CreateConnectionRequest.auth_parameters required")
    if data.get("InvocationConnectivityParameters") is not None:
        import capo_eventbridge.types.connectivity_resource_parameters

        out["invocation_connectivity_parameters"] = (
            capo_eventbridge.types.connectivity_resource_parameters.deserialize_aws_json_1_1(
                data["InvocationConnectivityParameters"]
            )
        )
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
