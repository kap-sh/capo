"""Generated from Smithy shape ``com.amazonaws.iot#GetThingConnectivityDataResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.boolean
    import capo_iot.types.client_id
    import capo_iot.types.connectivity_api_thing_name
    import capo_iot.types.disconnect_reason_value
    import capo_iot.types.keep_alive_duration
    import capo_iot.types.session_expiry
    import capo_iot.types.source_ip
    import capo_iot.types.source_port
    import capo_iot.types.target_ip
    import capo_iot.types.target_port
    import capo_iot.types.timestamp
    import capo_iot.types.vpc_endpoint_id


class GetThingConnectivityDataResponse(TypedDict, closed=True):
    thing_name: NotRequired[
        "capo_iot.types.connectivity_api_thing_name.ConnectivityApiThingName"
    ]
    """<p>The name of your IoT thing.</p>"""
    connected: NotRequired["capo_iot.types.boolean.Boolean"]
    """<p>A Boolean that indicates the connectivity status.</p>"""
    timestamp: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device connected or disconnected.</p>"""
    disconnect_reason: NotRequired[
        "capo_iot.types.disconnect_reason_value.DisconnectReasonValue"
    ]
    """<p>The reason that the client is disconnected.</p>"""
    source_ip: NotRequired["capo_iot.types.source_ip.SourceIp"]
    """<p>The IP address of the client that initiated the connection.</p>"""
    source_port: NotRequired["capo_iot.types.source_port.SourcePort"]
    """<p>The client's source port.</p>"""
    target_ip: NotRequired["capo_iot.types.target_ip.TargetIp"]
    """<p>The IP address of the Amazon Web Services IoT Core endpoint that the client connected to.</p>"""
    target_port: NotRequired["capo_iot.types.target_port.TargetPort"]
    """<p>The port number of the Amazon Web Services IoT Core endpoint that the client connected to.</p>"""
    vpc_endpoint_id: NotRequired["capo_iot.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the VPC endpoint. Present for clients connected to Amazon Web Services IoT Core via a VPC endpoint.</p>"""
    keep_alive_duration: NotRequired[
        "capo_iot.types.keep_alive_duration.KeepAliveDuration"
    ]
    """<p>The keep-alive interval in seconds that the client specified when establishing the connection.</p>"""
    clean_session: NotRequired["capo_iot.types.boolean.Boolean"]
    """<p>Indicates whether the client is using a clean session. Returns <code>true</code> for clean sessions.</p>"""
    session_expiry: NotRequired["capo_iot.types.session_expiry.SessionExpiry"]
    """<p>The session expiry interval in seconds for the MQTT client connection. This value indicates how long the session will remain active after the client disconnects.</p>"""
    client_id: NotRequired["capo_iot.types.client_id.ClientId"]
    """<p>The unique identifier of the MQTT client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingConnectivityDataResponse) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "connected" in value:
        out["connected"] = value["connected"]
    if "timestamp" in value:
        import capo_iot.types.timestamp

        out["timestamp"] = capo_iot.types.timestamp.serialize_json(value["timestamp"])
    if "disconnect_reason" in value:
        import capo_iot.types.disconnect_reason_value

        out["disconnectReason"] = capo_iot.types.disconnect_reason_value.serialize_json(
            value["disconnect_reason"]
        )
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "source_port" in value:
        out["sourcePort"] = value["source_port"]
    if "target_ip" in value:
        out["targetIp"] = value["target_ip"]
    if "target_port" in value:
        out["targetPort"] = value["target_port"]
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "keep_alive_duration" in value:
        out["keepAliveDuration"] = value["keep_alive_duration"]
    if "clean_session" in value:
        out["cleanSession"] = value["clean_session"]
    if "session_expiry" in value:
        out["sessionExpiry"] = value["session_expiry"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> GetThingConnectivityDataResponse:
    out: GetThingConnectivityDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    if data.get("connected") is not None:
        out["connected"] = data["connected"]
    if data.get("timestamp") is not None:
        import capo_iot.types.timestamp

        out["timestamp"] = capo_iot.types.timestamp.deserialize_json(data["timestamp"])
    if data.get("disconnectReason") is not None:
        import capo_iot.types.disconnect_reason_value

        out["disconnect_reason"] = (
            capo_iot.types.disconnect_reason_value.deserialize_json(
                data["disconnectReason"]
            )
        )
    if data.get("sourceIp") is not None:
        out["source_ip"] = data["sourceIp"]
    if data.get("sourcePort") is not None:
        out["source_port"] = data["sourcePort"]
    if data.get("targetIp") is not None:
        out["target_ip"] = data["targetIp"]
    if data.get("targetPort") is not None:
        out["target_port"] = data["targetPort"]
    if data.get("vpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if data.get("keepAliveDuration") is not None:
        out["keep_alive_duration"] = data["keepAliveDuration"]
    if data.get("cleanSession") is not None:
        out["clean_session"] = data["cleanSession"]
    if data.get("sessionExpiry") is not None:
        out["session_expiry"] = data["sessionExpiry"]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    return out


def redact_sensitive(value: GetThingConnectivityDataResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "thing_name" in value:
        out["thing_name"] = "*** Sensitive Data Redacted ***"
    if "source_ip" in value:
        out["source_ip"] = "*** Sensitive Data Redacted ***"
    if "source_port" in value:
        out["source_port"] = "*** Sensitive Data Redacted ***"
    if "target_ip" in value:
        out["target_ip"] = "*** Sensitive Data Redacted ***"
    if "target_port" in value:
        out["target_port"] = "*** Sensitive Data Redacted ***"
    if "vpc_endpoint_id" in value:
        out["vpc_endpoint_id"] = "*** Sensitive Data Redacted ***"
    return out
