"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.clean_session
    import capo_iot_data_plane.types.client_id
    import capo_iot_data_plane.types.connected
    import capo_iot_data_plane.types.disconnect_reason
    import capo_iot_data_plane.types.keep_alive_duration
    import capo_iot_data_plane.types.session_expiry
    import capo_iot_data_plane.types.source_ip
    import capo_iot_data_plane.types.source_port
    import capo_iot_data_plane.types.target_ip
    import capo_iot_data_plane.types.target_port
    import capo_iot_data_plane.types.thing_name
    import capo_iot_data_plane.types.timestamp
    import capo_iot_data_plane.types.vpc_endpoint_id


class GetConnectionResponse(TypedDict, closed=True):
    connected: "capo_iot_data_plane.types.connected.Connected"
    """<p>The connection state of the client. Returns <code>true</code> if the client is currently connected, or <code>false</code> if the client is not connected.</p>"""
    thing_name: NotRequired["capo_iot_data_plane.types.thing_name.ThingName"]
    """<p>The name of the thing associated with the principal of the MQTT client, if applicable.</p>"""
    clean_session: "capo_iot_data_plane.types.clean_session.CleanSession"
    """<p>Indicates whether the client is using a clean session. Returns <code>true</code> for clean sessions or <code>false</code> for persistent sessions.</p>"""
    source_ip: NotRequired["capo_iot_data_plane.types.source_ip.SourceIp"]
    """<p>The IP address of the client that initiated the connection.</p>"""
    source_port: "capo_iot_data_plane.types.source_port.SourcePort"
    """<p>The client's source port.</p>"""
    target_ip: NotRequired["capo_iot_data_plane.types.target_ip.TargetIp"]
    """<p>The IP address of the Amazon Web Services IoT Core endpoint that the client connected to. For clients connected to VPC endpoints, this is the private IP address of the network interface the client is connected to.</p>"""
    target_port: "capo_iot_data_plane.types.target_port.TargetPort"
    """<p>The port number of the Amazon Web Services IoT Core endpoint that the client connected to.</p>"""
    keep_alive_duration: (
        "capo_iot_data_plane.types.keep_alive_duration.KeepAliveDuration"
    )
    """<p>The keep-alive interval in seconds that the client specified when establishing the connection.</p>"""
    connected_since: "capo_iot_data_plane.types.timestamp.Timestamp"
    """<p>Unix timestamp (in milliseconds) indicating when the client connected. Present only when connected is true.</p>"""
    disconnected_since: "capo_iot_data_plane.types.timestamp.Timestamp"
    """<p>Unix timestamp (in milliseconds) indicating when the client disconnected. Present only when connected is false. This information is available for 30 minutes after the client disconnects.</p>"""
    disconnect_reason: NotRequired[
        "capo_iot_data_plane.types.disconnect_reason.DisconnectReason"
    ]
    """<p>The reason for the last disconnection, if the client is currently disconnected. See the <a href="https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html#connect-disconnect">developer guide</a> for valid disconnect reasons.</p>"""
    session_expiry: "capo_iot_data_plane.types.session_expiry.SessionExpiry"
    """<p>The session expiry interval in seconds for the MQTT client connection. This is configured by the user. This value indicates how long the session will remain active after the client disconnects.</p>"""
    client_id: NotRequired["capo_iot_data_plane.types.client_id.ClientId"]
    """<p>The unique identifier of the MQTT client. This is the same client ID that was used when the client established the connection.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_iot_data_plane.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the VPC endpoint. Present for clients connected to IoT Core via a <a href="https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html">VPC endpoint</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionResponse) -> dict:
    out: dict = {}
    out["connected"] = value.get("connected", False)
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    out["cleanSession"] = value.get("clean_session", False)
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    out["sourcePort"] = value.get("source_port", 0)
    if "target_ip" in value:
        out["targetIp"] = value["target_ip"]
    out["targetPort"] = value.get("target_port", 0)
    out["keepAliveDuration"] = value.get("keep_alive_duration", 0)
    out["connectedSince"] = value.get("connected_since", 0)
    out["disconnectedSince"] = value.get("disconnected_since", 0)
    if "disconnect_reason" in value:
        out["disconnectReason"] = value["disconnect_reason"]
    out["sessionExpiry"] = value.get("session_expiry", 0)
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_json(data: dict) -> GetConnectionResponse:
    out: GetConnectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("connected") is not None:
        out["connected"] = data["connected"]
    else:
        out["connected"] = False
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    if data.get("cleanSession") is not None:
        out["clean_session"] = data["cleanSession"]
    else:
        out["clean_session"] = False
    if data.get("sourceIp") is not None:
        out["source_ip"] = data["sourceIp"]
    if data.get("sourcePort") is not None:
        out["source_port"] = data["sourcePort"]
    else:
        out["source_port"] = 0
    if data.get("targetIp") is not None:
        out["target_ip"] = data["targetIp"]
    if data.get("targetPort") is not None:
        out["target_port"] = data["targetPort"]
    else:
        out["target_port"] = 0
    if data.get("keepAliveDuration") is not None:
        out["keep_alive_duration"] = data["keepAliveDuration"]
    else:
        out["keep_alive_duration"] = 0
    if data.get("connectedSince") is not None:
        out["connected_since"] = data["connectedSince"]
    else:
        out["connected_since"] = 0
    if data.get("disconnectedSince") is not None:
        out["disconnected_since"] = data["disconnectedSince"]
    else:
        out["disconnected_since"] = 0
    if data.get("disconnectReason") is not None:
        out["disconnect_reason"] = data["disconnectReason"]
    if data.get("sessionExpiry") is not None:
        out["session_expiry"] = data["sessionExpiry"]
    else:
        out["session_expiry"] = 0
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("vpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    return out
