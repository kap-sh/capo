"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateWirelessGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.gateway_max_eirp
    import capo_iot_wireless.types.join_eui_filters
    import capo_iot_wireless.types.net_id_filters
    import capo_iot_wireless.types.wireless_gateway_id
    import capo_iot_wireless.types.wireless_gateway_name


class UpdateWirelessGatewayRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""
    name: NotRequired[
        "capo_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
    ]
    """<p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code>&lt;&gt;^#~$</code> </p> </note>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>A new description of the resource.</p>"""
    join_eui_filters: NotRequired[
        "capo_iot_wireless.types.join_eui_filters.JoinEuiFilters"
    ]
    net_id_filters: NotRequired["capo_iot_wireless.types.net_id_filters.NetIdFilters"]
    max_eirp: NotRequired["capo_iot_wireless.types.gateway_max_eirp.GatewayMaxEirp"]
    """<p>The MaxEIRP value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWirelessGatewayRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "join_eui_filters" in value:
        import capo_iot_wireless.types.join_eui_filters

        out["JoinEuiFilters"] = capo_iot_wireless.types.join_eui_filters.serialize_json(
            value["join_eui_filters"]
        )
    if "net_id_filters" in value:
        import capo_iot_wireless.types.net_id_filters

        out["NetIdFilters"] = capo_iot_wireless.types.net_id_filters.serialize_json(
            value["net_id_filters"]
        )
    if "max_eirp" in value:
        out["MaxEirp"] = (
            "NaN"
            if value["max_eirp"] != value["max_eirp"]
            else "Infinity"
            if value["max_eirp"] == float("inf")
            else "-Infinity"
            if value["max_eirp"] == float("-inf")
            else value["max_eirp"]
        )
    return out


def deserialize_json(data: dict) -> UpdateWirelessGatewayRequest:
    out: UpdateWirelessGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("JoinEuiFilters") is not None:
        import capo_iot_wireless.types.join_eui_filters

        out["join_eui_filters"] = (
            capo_iot_wireless.types.join_eui_filters.deserialize_json(
                data["JoinEuiFilters"]
            )
        )
    if data.get("NetIdFilters") is not None:
        import capo_iot_wireless.types.net_id_filters

        out["net_id_filters"] = capo_iot_wireless.types.net_id_filters.deserialize_json(
            data["NetIdFilters"]
        )
    if data.get("MaxEirp") is not None:
        out["max_eirp"] = float(data["MaxEirp"])
    return out
