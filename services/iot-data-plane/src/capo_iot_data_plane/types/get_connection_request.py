"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.client_id
    import capo_iot_data_plane.types.include_socket_information


class GetConnectionRequest(TypedDict, closed=True):
    client_id: "capo_iot_data_plane.types.client_id.ClientId"
    """<p>The unique identifier of the MQTT client to retrieve connection information. The client ID can't start with a dollar sign ($).</p> <p>MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.</p>"""
    include_socket_information: (
        "capo_iot_data_plane.types.include_socket_information.IncludeSocketInformation"
    )
    """<p>Specifies if socket information (sourcePort, targetPort, sourceIp, targetIp) should be included in the GetConnection response. Set to <code>TRUE</code> to include socket information. Set to <code>FALSE</code> to omit socket information. By default, this is set to <code>FALSE</code>. See the <a href="https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-client-disconnect">developer guide</a> for how to authorize this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectionRequest:
    out: GetConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
