"""Generated from Smithy shape ``com.amazonaws.appstream#Session``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.authentication_type
    import capo_appstream.types.instance_drain_status
    import capo_appstream.types.network_access_configuration
    import capo_appstream.types.session_connection_state
    import capo_appstream.types.session_state
    import capo_appstream.types.string
    import capo_appstream.types.timestamp
    import capo_appstream.types.user_id


class Session(TypedDict, closed=True):
    id: NotRequired["capo_appstream.types.string.String"]
    """<p>The identifier of the streaming session.</p>"""
    user_id: NotRequired["capo_appstream.types.user_id.UserId"]
    """<p>The identifier of the user for whom the session was created.</p>"""
    stack_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack for the streaming session.</p>"""
    fleet_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the fleet for the streaming session.</p>"""
    state: NotRequired["capo_appstream.types.session_state.SessionState"]
    """<p>The current state of the streaming session.</p>"""
    connection_state: NotRequired[
        "capo_appstream.types.session_connection_state.SessionConnectionState"
    ]
    """<p>Specifies whether a user is connected to the streaming session.</p>"""
    start_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time when a streaming instance is dedicated for the user.</p>"""
    max_expiration_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time when the streaming session is set to expire. This time is based on the <code>MaxUserDurationinSeconds</code> value, which determines the maximum length of time that a streaming session can run. A streaming session might end earlier than the time specified in <code>SessionMaxExpirationTime</code>, when the <code>DisconnectTimeOutInSeconds</code> elapses or the user chooses to end his or her session. If the <code>DisconnectTimeOutInSeconds</code> elapses, or the user chooses to end his or her session, the streaming instance is terminated and the streaming session ends.</p>"""
    authentication_type: NotRequired[
        "capo_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication method. The user is authenticated using a streaming URL (<code>API</code>) or SAML 2.0 federation (<code>SAML</code>).</p>"""
    network_access_configuration: NotRequired[
        "capo_appstream.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    """<p>The network details for the streaming session.</p>"""
    instance_id: NotRequired["capo_appstream.types.string.String"]
    """<p>The identifier for the instance hosting the session.</p>"""
    instance_drain_status: NotRequired[
        "capo_appstream.types.instance_drain_status.InstanceDrainStatus"
    ]
    """<p>The drain status of the instance hosting the streaming session. This only applies to multi-session fleets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "state" in value:
        import capo_appstream.types.session_state

        out["State"] = capo_appstream.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "connection_state" in value:
        import capo_appstream.types.session_connection_state

        out["ConnectionState"] = (
            capo_appstream.types.session_connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "start_time" in value:
        import capo_appstream.types.timestamp

        out["StartTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "max_expiration_time" in value:
        import capo_appstream.types.timestamp

        out["MaxExpirationTime"] = (
            capo_appstream.types.timestamp.serialize_aws_json_1_1(
                value["max_expiration_time"]
            )
        )
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "network_access_configuration" in value:
        import capo_appstream.types.network_access_configuration

        out["NetworkAccessConfiguration"] = (
            capo_appstream.types.network_access_configuration.serialize_aws_json_1_1(
                value["network_access_configuration"]
            )
        )
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_drain_status" in value:
        import capo_appstream.types.instance_drain_status

        out["InstanceDrainStatus"] = (
            capo_appstream.types.instance_drain_status.serialize_aws_json_1_1(
                value["instance_drain_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("State") is not None:
        import capo_appstream.types.session_state

        out["state"] = capo_appstream.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("ConnectionState") is not None:
        import capo_appstream.types.session_connection_state

        out["connection_state"] = (
            capo_appstream.types.session_connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_appstream.types.timestamp

        out["start_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("MaxExpirationTime") is not None:
        import capo_appstream.types.timestamp

        out["max_expiration_time"] = (
            capo_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["MaxExpirationTime"]
            )
        )
    if data.get("AuthenticationType") is not None:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("NetworkAccessConfiguration") is not None:
        import capo_appstream.types.network_access_configuration

        out["network_access_configuration"] = (
            capo_appstream.types.network_access_configuration.deserialize_aws_json_1_1(
                data["NetworkAccessConfiguration"]
            )
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("InstanceDrainStatus") is not None:
        import capo_appstream.types.instance_drain_status

        out["instance_drain_status"] = (
            capo_appstream.types.instance_drain_status.deserialize_aws_json_1_1(
                data["InstanceDrainStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Session) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "state" in value:
        import capo_appstream.types.session_state

        out["State"] = capo_appstream.types.session_state.serialize_cbor(value["state"])
    if "connection_state" in value:
        import capo_appstream.types.session_connection_state

        out["ConnectionState"] = (
            capo_appstream.types.session_connection_state.serialize_cbor(
                value["connection_state"]
            )
        )
    if "start_time" in value:
        import capo_appstream.types.timestamp

        out["StartTime"] = capo_appstream.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "max_expiration_time" in value:
        import capo_appstream.types.timestamp

        out["MaxExpirationTime"] = capo_appstream.types.timestamp.serialize_cbor(
            value["max_expiration_time"]
        )
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_cbor(
                value["authentication_type"]
            )
        )
    if "network_access_configuration" in value:
        import capo_appstream.types.network_access_configuration

        out["NetworkAccessConfiguration"] = (
            capo_appstream.types.network_access_configuration.serialize_cbor(
                value["network_access_configuration"]
            )
        )
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_drain_status" in value:
        import capo_appstream.types.instance_drain_status

        out["InstanceDrainStatus"] = (
            capo_appstream.types.instance_drain_status.serialize_cbor(
                value["instance_drain_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("State") is not None:
        import capo_appstream.types.session_state

        out["state"] = capo_appstream.types.session_state.deserialize_cbor(
            data["State"]
        )
    if data.get("ConnectionState") is not None:
        import capo_appstream.types.session_connection_state

        out["connection_state"] = (
            capo_appstream.types.session_connection_state.deserialize_cbor(
                data["ConnectionState"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_appstream.types.timestamp

        out["start_time"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("MaxExpirationTime") is not None:
        import capo_appstream.types.timestamp

        out["max_expiration_time"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["MaxExpirationTime"]
        )
    if data.get("AuthenticationType") is not None:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_cbor(
                data["AuthenticationType"]
            )
        )
    if data.get("NetworkAccessConfiguration") is not None:
        import capo_appstream.types.network_access_configuration

        out["network_access_configuration"] = (
            capo_appstream.types.network_access_configuration.deserialize_cbor(
                data["NetworkAccessConfiguration"]
            )
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("InstanceDrainStatus") is not None:
        import capo_appstream.types.instance_drain_status

        out["instance_drain_status"] = (
            capo_appstream.types.instance_drain_status.deserialize_cbor(
                data["InstanceDrainStatus"]
            )
        )
    return out
