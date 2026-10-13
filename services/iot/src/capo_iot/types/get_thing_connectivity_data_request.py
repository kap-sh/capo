"""Generated from Smithy shape ``com.amazonaws.iot#GetThingConnectivityDataRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.boolean
    import capo_iot.types.connectivity_api_thing_name


class GetThingConnectivityDataRequest(TypedDict, closed=True):
    thing_name: "capo_iot.types.connectivity_api_thing_name.ConnectivityApiThingName"
    """<p>The name of your IoT thing.</p>"""
    include_socket_information: NotRequired["capo_iot.types.boolean.Boolean"]
    """<p>Specifies if socket information (sourcePort, targetPort, sourceIp, targetIp, vpcEndpointId) should be included in the GetThingConnectivityData response. Set to <code>true</code> to include socket information. Set to <code>false</code> to omit socket information. By default, this is set to <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingConnectivityDataRequest) -> dict:
    out: dict = {}
    if "include_socket_information" in value:
        out["includeSocketInformation"] = value["include_socket_information"]
    return out


def deserialize_json(data: dict) -> GetThingConnectivityDataRequest:
    out: GetThingConnectivityDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("includeSocketInformation") is not None:
        out["include_socket_information"] = data["includeSocketInformation"]
    return out


def redact_sensitive(value: GetThingConnectivityDataRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "thing_name" in value:
        out["thing_name"] = "*** Sensitive Data Redacted ***"
    return out
