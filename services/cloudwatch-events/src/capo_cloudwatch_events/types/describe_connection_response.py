"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeConnectionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_arn
    import capo_cloudwatch_events.types.connection_auth_response_parameters
    import capo_cloudwatch_events.types.connection_authorization_type
    import capo_cloudwatch_events.types.connection_description
    import capo_cloudwatch_events.types.connection_name
    import capo_cloudwatch_events.types.connection_state
    import capo_cloudwatch_events.types.connection_state_reason
    import capo_cloudwatch_events.types.secrets_manager_secret_arn
    import capo_cloudwatch_events.types.timestamp


class DescribeConnectionResponse(TypedDict, closed=True):
    connection_arn: NotRequired[
        "capo_cloudwatch_events.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection retrieved.</p>"""
    name: NotRequired["capo_cloudwatch_events.types.connection_name.ConnectionName"]
    """<p>The name of the connection retrieved.</p>"""
    description: NotRequired[
        "capo_cloudwatch_events.types.connection_description.ConnectionDescription"
    ]
    """<p>The description for the connection retrieved.</p>"""
    connection_state: NotRequired[
        "capo_cloudwatch_events.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection retrieved.</p>"""
    state_reason: NotRequired[
        "capo_cloudwatch_events.types.connection_state_reason.ConnectionStateReason"
    ]
    """<p>The reason that the connection is in the current connection state.</p>"""
    authorization_type: NotRequired[
        "capo_cloudwatch_events.types.connection_authorization_type.ConnectionAuthorizationType"
    ]
    """<p>The type of authorization specified for the connection.</p>"""
    secret_arn: NotRequired[
        "capo_cloudwatch_events.types.secrets_manager_secret_arn.SecretsManagerSecretArn"
    ]
    """<p>The ARN of the secret created from the authorization parameters specified for the connection.</p>"""
    auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_auth_response_parameters.ConnectionAuthResponseParameters"
    ]
    """<p>The parameters to use for authorization for the connection.</p>"""
    creation_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last modified.</p>"""
    last_authorized_time: NotRequired[
        "capo_cloudwatch_events.types.timestamp.Timestamp"
    ]
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
    if "connection_state" in value:
        import capo_cloudwatch_events.types.connection_state

        out["ConnectionState"] = (
            capo_cloudwatch_events.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "authorization_type" in value:
        import capo_cloudwatch_events.types.connection_authorization_type

        out["AuthorizationType"] = (
            capo_cloudwatch_events.types.connection_authorization_type.serialize_aws_json_1_1(
                value["authorization_type"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "auth_parameters" in value:
        import capo_cloudwatch_events.types.connection_auth_response_parameters

        out["AuthParameters"] = (
            capo_cloudwatch_events.types.connection_auth_response_parameters.serialize_aws_json_1_1(
                value["auth_parameters"]
            )
        )
    if "creation_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["CreationTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["LastModifiedTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_authorized_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["LastAuthorizedTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
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
    if data.get("ConnectionState") is not None:
        import capo_cloudwatch_events.types.connection_state

        out["connection_state"] = (
            capo_cloudwatch_events.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("AuthorizationType") is not None:
        import capo_cloudwatch_events.types.connection_authorization_type

        out["authorization_type"] = (
            capo_cloudwatch_events.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("AuthParameters") is not None:
        import capo_cloudwatch_events.types.connection_auth_response_parameters

        out["auth_parameters"] = (
            capo_cloudwatch_events.types.connection_auth_response_parameters.deserialize_aws_json_1_1(
                data["AuthParameters"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_cloudwatch_events.types.timestamp

        out["creation_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_cloudwatch_events.types.timestamp

        out["last_modified_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LastAuthorizedTime") is not None:
        import capo_cloudwatch_events.types.timestamp

        out["last_authorized_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["LastAuthorizedTime"]
            )
        )
    return out


def redact_sensitive(value: DescribeConnectionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_parameters" in value:
        import capo_cloudwatch_events.types.connection_auth_response_parameters

        out["auth_parameters"] = (
            capo_cloudwatch_events.types.connection_auth_response_parameters.redact_sensitive(
                value["auth_parameters"]
            )
        )
    return out
