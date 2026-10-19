"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.amazon_uuid
    import capo_workspaces.types.authentication_type
    import capo_workspaces.types.network_access_configuration
    import capo_workspaces.types.session_connection_state
    import capo_workspaces.types.session_instance_id
    import capo_workspaces.types.timestamp
    import capo_workspaces.types.workspaces_pool_id
    import capo_workspaces.types.workspaces_pool_user_id


class WorkspacesPoolSession(TypedDict, closed=True):
    authentication_type: NotRequired[
        "capo_workspaces.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication method. The user is authenticated using a WorkSpaces Pools URL (API) or SAML 2.0 federation (SAML).</p>"""
    connection_state: NotRequired[
        "capo_workspaces.types.session_connection_state.SessionConnectionState"
    ]
    """<p>Specifies whether a user is connected to the pool session.</p>"""
    session_id: "capo_workspaces.types.amazon_uuid.AmazonUuid"
    """<p>The identifier of the session.</p>"""
    instance_id: NotRequired[
        "capo_workspaces.types.session_instance_id.SessionInstanceId"
    ]
    """<p>The identifier for the instance hosting the session.</p>"""
    pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""
    expiration_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time that the pool session ended.</p>"""
    network_access_configuration: NotRequired[
        "capo_workspaces.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    """<p>Describes the network details of the pool.</p>"""
    start_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The time that the pool sission started.</p>"""
    user_id: "capo_workspaces.types.workspaces_pool_user_id.WorkspacesPoolUserId"
    """<p>The identifier of the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolSession) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import capo_workspaces.types.authentication_type

        out["AuthenticationType"] = (
            capo_workspaces.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "connection_state" in value:
        import capo_workspaces.types.session_connection_state

        out["ConnectionState"] = (
            capo_workspaces.types.session_connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    out["SessionId"] = value["session_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    out["PoolId"] = value["pool_id"]
    if "expiration_time" in value:
        import capo_workspaces.types.timestamp

        out["ExpirationTime"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["expiration_time"]
        )
    if "network_access_configuration" in value:
        import capo_workspaces.types.network_access_configuration

        out["NetworkAccessConfiguration"] = (
            capo_workspaces.types.network_access_configuration.serialize_aws_json_1_1(
                value["network_access_configuration"]
            )
        )
    if "start_time" in value:
        import capo_workspaces.types.timestamp

        out["StartTime"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesPoolSession:
    out: WorkspacesPoolSession = {}  # type: ignore[typeddict-item]
    if data.get("AuthenticationType") is not None:
        import capo_workspaces.types.authentication_type

        out["authentication_type"] = (
            capo_workspaces.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("ConnectionState") is not None:
        import capo_workspaces.types.session_connection_state

        out["connection_state"] = (
            capo_workspaces.types.session_connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    if data.get("ExpirationTime") is not None:
        import capo_workspaces.types.timestamp

        out["expiration_time"] = (
            capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    if data.get("NetworkAccessConfiguration") is not None:
        import capo_workspaces.types.network_access_configuration

        out["network_access_configuration"] = (
            capo_workspaces.types.network_access_configuration.deserialize_aws_json_1_1(
                data["NetworkAccessConfiguration"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_workspaces.types.timestamp

        out["start_time"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    return out
