"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.direct_connect_gateway_name
    import capo_direct_connect.types.direct_connect_gateway_state
    import capo_direct_connect.types.long_asn
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.prefix_pool_allocated_count
    import capo_direct_connect.types.state_change_error
    import capo_direct_connect.types.tag_list


class DirectConnectGateway(TypedDict, closed=True):
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    direct_connect_gateway_name: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName"
    ]
    """<p>The name of the Direct Connect gateway.</p>"""
    amazon_side_asn: NotRequired["capo_direct_connect.types.long_asn.LongAsn"]
    """<p>The autonomous system number (AS) for the Amazon side of the connection.</p>"""
    owner_account: NotRequired["capo_direct_connect.types.owner_account.OwnerAccount"]
    """<p>The ID of the Amazon Web Services account that owns the Direct Connect gateway.</p>"""
    direct_connect_gateway_state: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_state.DirectConnectGatewayState"
    ]
    """<p>The state of the Direct Connect gateway. The following are the possible values:</p> <ul> <li> <p> <code>pending</code>: The initial state after calling <a>CreateDirectConnectGateway</a>.</p> </li> <li> <p> <code>available</code>: The Direct Connect gateway is ready for use.</p> </li> <li> <p> <code>deleting</code>: The initial state after calling <a>DeleteDirectConnectGateway</a>.</p> </li> <li> <p> <code>deleted</code>: The Direct Connect gateway is deleted and cannot pass traffic.</p> </li> </ul>"""
    state_change_error: NotRequired[
        "capo_direct_connect.types.state_change_error.StateChangeError"
    ]
    """<p>The error message if the state of an object failed to advance.</p>"""
    total_prefix_pool_allocations: NotRequired[
        "capo_direct_connect.types.prefix_pool_allocated_count.PrefixPoolAllocatedCount"
    ]
    """<p>The total number of inbound route prefixes allocated to the attachments on the Direct Connect gateway. The count combines the IPv4 and IPv6 address families.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>Information about a tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGateway) -> dict:
    out: dict = {}
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "direct_connect_gateway_name" in value:
        out["directConnectGatewayName"] = value["direct_connect_gateway_name"]
    if "amazon_side_asn" in value:
        out["amazonSideAsn"] = value["amazon_side_asn"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "direct_connect_gateway_state" in value:
        import capo_direct_connect.types.direct_connect_gateway_state

        out["directConnectGatewayState"] = (
            capo_direct_connect.types.direct_connect_gateway_state.serialize_aws_json_1_1(
                value["direct_connect_gateway_state"]
            )
        )
    if "state_change_error" in value:
        out["stateChangeError"] = value["state_change_error"]
    if "total_prefix_pool_allocations" in value:
        out["totalPrefixPoolAllocations"] = value["total_prefix_pool_allocations"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectConnectGateway:
    out: DirectConnectGateway = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("directConnectGatewayName") is not None:
        out["direct_connect_gateway_name"] = data["directConnectGatewayName"]
    if data.get("amazonSideAsn") is not None:
        out["amazon_side_asn"] = data["amazonSideAsn"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("directConnectGatewayState") is not None:
        import capo_direct_connect.types.direct_connect_gateway_state

        out["direct_connect_gateway_state"] = (
            capo_direct_connect.types.direct_connect_gateway_state.deserialize_aws_json_1_1(
                data["directConnectGatewayState"]
            )
        )
    if data.get("stateChangeError") is not None:
        out["state_change_error"] = data["stateChangeError"]
    if data.get("totalPrefixPoolAllocations") is not None:
        out["total_prefix_pool_allocations"] = data["totalPrefixPoolAllocations"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectConnectGateway) -> dict:
    out: dict = {}
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "direct_connect_gateway_name" in value:
        out["directConnectGatewayName"] = value["direct_connect_gateway_name"]
    if "amazon_side_asn" in value:
        out["amazonSideAsn"] = value["amazon_side_asn"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "direct_connect_gateway_state" in value:
        import capo_direct_connect.types.direct_connect_gateway_state

        out["directConnectGatewayState"] = (
            capo_direct_connect.types.direct_connect_gateway_state.serialize_cbor(
                value["direct_connect_gateway_state"]
            )
        )
    if "state_change_error" in value:
        out["stateChangeError"] = value["state_change_error"]
    if "total_prefix_pool_allocations" in value:
        out["totalPrefixPoolAllocations"] = value["total_prefix_pool_allocations"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> DirectConnectGateway:
    out: DirectConnectGateway = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayId") is not None:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if data.get("directConnectGatewayName") is not None:
        out["direct_connect_gateway_name"] = data["directConnectGatewayName"]
    if data.get("amazonSideAsn") is not None:
        out["amazon_side_asn"] = data["amazonSideAsn"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("directConnectGatewayState") is not None:
        import capo_direct_connect.types.direct_connect_gateway_state

        out["direct_connect_gateway_state"] = (
            capo_direct_connect.types.direct_connect_gateway_state.deserialize_cbor(
                data["directConnectGatewayState"]
            )
        )
    if data.get("stateChangeError") is not None:
        out["state_change_error"] = data["stateChangeError"]
    if data.get("totalPrefixPoolAllocations") is not None:
        out["total_prefix_pool_allocations"] = data["totalPrefixPoolAllocations"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_cbor(data["tags"])
    return out
