"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.connection_name
    import capo_direct_connect.types.lag_id
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.provider_name
    import capo_direct_connect.types.request_billing_mode
    import capo_direct_connect.types.request_mac_sec
    import capo_direct_connect.types.tag_list


class CreateConnectionRequest(TypedDict, closed=True):
    location: "capo_direct_connect.types.location_code.LocationCode"
    """<p>The location of the connection.</p>"""
    bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth"
    """<p>The bandwidth of the connection.</p>"""
    connection_name: "capo_direct_connect.types.connection_name.ConnectionName"
    """<p>The name of the connection.</p>"""
    lag_id: NotRequired["capo_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the lag.</p>"""
    provider_name: NotRequired["capo_direct_connect.types.provider_name.ProviderName"]
    """<p>The name of the service provider associated with the requested connection.</p>"""
    request_mac_sec: NotRequired[
        "capo_direct_connect.types.request_mac_sec.RequestMACSec"
    ]
    """<p>Indicates whether you want the connection to support MAC Security (MACsec).</p> <p>MAC Security (MACsec) is unavailable on hosted connections. For information about MAC Security (MACsec) prerequisites, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACSec.html">MAC Security in Direct Connect</a> in the <i>Direct Connect User Guide</i>.</p>"""
    billing_mode: NotRequired[
        "capo_direct_connect.types.request_billing_mode.RequestBillingMode"
    ]
    """<p>The billing mode for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    out["location"] = value["location"]
    out["bandwidth"] = value["bandwidth"]
    out["connectionName"] = value["connection_name"]
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
    if "billing_mode" in value:
        import capo_direct_connect.types.request_billing_mode

        out["billingMode"] = (
            capo_direct_connect.types.request_billing_mode.serialize_aws_json_1_1(
                value["billing_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        raise DeserializationError("CreateConnectionRequest.location required")
    if data.get("bandwidth") is not None:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("CreateConnectionRequest.bandwidth required")
    if data.get("connectionName") is not None:
        out["connection_name"] = data["connectionName"]
    else:
        raise DeserializationError("CreateConnectionRequest.connection_name required")
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
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.request_billing_mode

        out["billing_mode"] = (
            capo_direct_connect.types.request_billing_mode.deserialize_aws_json_1_1(
                data["billingMode"]
            )
        )
    return out
