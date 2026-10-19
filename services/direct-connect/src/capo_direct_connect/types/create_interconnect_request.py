"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateInterconnectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.interconnect_name
    import capo_direct_connect.types.lag_id
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.provider_name
    import capo_direct_connect.types.request_mac_sec
    import capo_direct_connect.types.tag_list


class CreateInterconnectRequest(TypedDict, closed=True):
    interconnect_name: "capo_direct_connect.types.interconnect_name.InterconnectName"
    """<p>The name of the interconnect.</p>"""
    bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth"
    """<p>The port bandwidth, in Gbps. The possible values are 1, 10, and 100.</p>"""
    location: "capo_direct_connect.types.location_code.LocationCode"
    """<p>The location of the interconnect.</p>"""
    lag_id: NotRequired["capo_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the interconnect.</p>"""
    provider_name: NotRequired["capo_direct_connect.types.provider_name.ProviderName"]
    """<p>The name of the service provider associated with the interconnect.</p>"""
    request_mac_sec: NotRequired[
        "capo_direct_connect.types.request_mac_sec.RequestMACSec"
    ]
    """<p>Indicates whether you want the interconnect to support MAC Security (MACsec).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInterconnectRequest) -> dict:
    out: dict = {}
    out["interconnectName"] = value["interconnect_name"]
    out["bandwidth"] = value["bandwidth"]
    out["location"] = value["location"]
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "request_mac_sec" in value:
        out["requestMACSec"] = value["request_mac_sec"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInterconnectRequest:
    out: CreateInterconnectRequest = {}  # type: ignore[typeddict-item]
    if data.get("interconnectName") is not None:
        out["interconnect_name"] = data["interconnectName"]
    else:
        out["interconnect_name"] = ""
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        out["bandwidth"] = ""
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    if data.get("requestMACSec") is not None:
        out["request_mac_sec"] = data["requestMACSec"]
    return out
