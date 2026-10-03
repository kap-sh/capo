"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_arn
    import capo_eventbridge.types.connection_auth_response_parameters
    import capo_eventbridge.types.connection_authorization_type
    import capo_eventbridge.types.connection_description
    import capo_eventbridge.types.connection_name
    import capo_eventbridge.types.connection_state
    import capo_eventbridge.types.connection_state_reason
    import capo_eventbridge.types.describe_connection_connectivity_parameters
    import capo_eventbridge.types.kms_key_identifier
    import capo_eventbridge.types.secrets_manager_secret_arn
    import capo_eventbridge.types.timestamp


class DescribeConnectionResponse(TypedDict, closed=True):
    connection_arn: NotRequired["capo_eventbridge.types.connection_arn.ConnectionArn"]
    """<p>The ARN of the connection retrieved.</p>"""
    name: NotRequired["capo_eventbridge.types.connection_name.ConnectionName"]
    """<p>The name of the connection retrieved.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.connection_description.ConnectionDescription"
    ]
    """<p>The description for the connection retrieved.</p>"""
    invocation_connectivity_parameters: NotRequired[
        "capo_eventbridge.types.describe_connection_connectivity_parameters.DescribeConnectionConnectivityParameters"
    ]
    """<p>For connections to private APIs The parameters EventBridge uses to invoke the resource endpoint.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html">Connecting to private APIs</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    connection_state: NotRequired[
        "capo_eventbridge.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection retrieved.</p>"""
    state_reason: NotRequired[
        "capo_eventbridge.types.connection_state_reason.ConnectionStateReason"
    ]
    """<p>The reason that the connection is in the current connection state.</p>"""
    authorization_type: NotRequired[
        "capo_eventbridge.types.connection_authorization_type.ConnectionAuthorizationType"
    ]
    """<p>The type of authorization specified for the connection.</p>"""
    secret_arn: NotRequired[
        "capo_eventbridge.types.secrets_manager_secret_arn.SecretsManagerSecretArn"
    ]
    """<p>The ARN of the secret created from the authorization parameters specified for the connection.</p>"""
    kms_key_identifier: NotRequired[
        "capo_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt the connection, if one has been specified.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-connections.html">Encrypting connections</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    auth_parameters: NotRequired[
        "capo_eventbridge.types.connection_auth_response_parameters.ConnectionAuthResponseParameters"
    ]
    """<p>The parameters to use for authorization for the connection.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last modified.</p>"""
    last_authorized_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last authorized.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionResponse) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "invocation_connectivity_parameters" in value:
        import capo_eventbridge.types.describe_connection_connectivity_parameters

        out["InvocationConnectivityParameters"] = (
            capo_eventbridge.types.describe_connection_connectivity_parameters.serialize_aws_json_1_1(
                value["invocation_connectivity_parameters"]
            )
        )
    if "connection_state" in value:
        import capo_eventbridge.types.connection_state

        out["ConnectionState"] = (
            capo_eventbridge.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "authorization_type" in value:
        import capo_eventbridge.types.connection_authorization_type

        out["AuthorizationType"] = (
            capo_eventbridge.types.connection_authorization_type.serialize_aws_json_1_1(
                value["authorization_type"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "auth_parameters" in value:
        import capo_eventbridge.types.connection_auth_response_parameters

        out["AuthParameters"] = (
            capo_eventbridge.types.connection_auth_response_parameters.serialize_aws_json_1_1(
                value["auth_parameters"]
            )
        )
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_authorized_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastAuthorizedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_authorized_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionResponse:
    out: DescribeConnectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("InvocationConnectivityParameters") is not None:
        import capo_eventbridge.types.describe_connection_connectivity_parameters

        out["invocation_connectivity_parameters"] = (
            capo_eventbridge.types.describe_connection_connectivity_parameters.deserialize_aws_json_1_1(
                data["InvocationConnectivityParameters"]
            )
        )
    if data.get("ConnectionState") is not None:
        import capo_eventbridge.types.connection_state

        out["connection_state"] = (
            capo_eventbridge.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("AuthorizationType") is not None:
        import capo_eventbridge.types.connection_authorization_type

        out["authorization_type"] = (
            capo_eventbridge.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if data.get("AuthParameters") is not None:
        import capo_eventbridge.types.connection_auth_response_parameters

        out["auth_parameters"] = (
            capo_eventbridge.types.connection_auth_response_parameters.deserialize_aws_json_1_1(
                data["AuthParameters"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_eventbridge.types.timestamp

        out["last_modified_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LastAuthorizedTime") is not None:
        import capo_eventbridge.types.timestamp

        out["last_authorized_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastAuthorizedTime"]
            )
        )
    return out
