"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateLagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.count
    import capo_direct_connect.types.lag_name
    import capo_direct_connect.types.location_code
    import capo_direct_connect.types.provider_name
    import capo_direct_connect.types.request_billing_mode
    import capo_direct_connect.types.request_mac_sec
    import capo_direct_connect.types.tag_list


class CreateLagRequest(TypedDict, closed=True):
    number_of_connections: "capo_direct_connect.types.count.Count"
    """<p>The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1Gbps or 10Gbps, or two when the port speed is 100Gbps or 400Gbps.</p>"""
    location: "capo_direct_connect.types.location_code.LocationCode"
    """<p>The location for the LAG.</p>"""
    connections_bandwidth: "capo_direct_connect.types.bandwidth.Bandwidth"
    """<p>The bandwidth of the individual physical dedicated connections bundled by the LAG. The possible values are 1Gbps,10Gbps, 100Gbps, and 400Gbps. </p>"""
    lag_name: "capo_direct_connect.types.lag_name.LagName"
    """<p>The name of the LAG.</p>"""
    connection_id: NotRequired["capo_direct_connect.types.connection_id.ConnectionId"]
    """<p>The ID of an existing dedicated connection to migrate to the LAG.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the LAG.</p>"""
    child_connection_tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the automtically created LAGs.</p>"""
    provider_name: NotRequired["capo_direct_connect.types.provider_name.ProviderName"]
    """<p>The name of the service provider associated with the LAG.</p>"""
    request_mac_sec: NotRequired[
        "capo_direct_connect.types.request_mac_sec.RequestMACSec"
    ]
    """<p>Indicates whether the connection will support MAC Security (MACsec).</p> <note> <p>All connections in the LAG must be capable of supporting MAC Security (MACsec). For information about MAC Security (MACsec) prerequisties, see <a href="https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites">MACsec prerequisties</a> in the <i>Direct Connect User Guide</i>.</p> </note>"""
    billing_mode: NotRequired[
        "capo_direct_connect.types.request_billing_mode.RequestBillingMode"
    ]
    """<p>The billing mode for the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLagRequest) -> dict:
    out: dict = {}
    out["numberOfConnections"] = value.get("number_of_connections", 0)
    out["location"] = value["location"]
    out["connectionsBandwidth"] = value["connections_bandwidth"]
    out["lagName"] = value["lag_name"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "child_connection_tags" in value:
        import capo_direct_connect.types.tag_list

        out["childConnectionTags"] = (
            capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
                value["child_connection_tags"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> CreateLagRequest:
    out: CreateLagRequest = {}  # type: ignore[typeddict-item]
    if data.get("numberOfConnections") is not None:
        out["number_of_connections"] = data["numberOfConnections"]
    else:
        out["number_of_connections"] = 0
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        raise DeserializationError("CreateLagRequest.location required")
    if data.get("connectionsBandwidth") is not None:
        out["connections_bandwidth"] = data["connectionsBandwidth"]
    else:
        raise DeserializationError("CreateLagRequest.connections_bandwidth required")
    if data.get("lagName") is not None:
        out["lag_name"] = data["lagName"]
    else:
        raise DeserializationError("CreateLagRequest.lag_name required")
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("childConnectionTags") is not None:
        import capo_direct_connect.types.tag_list

        out["child_connection_tags"] = (
            capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
                data["childConnectionTags"]
            )
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
