"""Generated from Smithy shape ``com.amazonaws.directconnect#ListVirtualInterfaceRoutesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.route_list
    import capo_direct_connect.types.virtual_interface_id


class ListVirtualInterfaceRoutesResponse(TypedDict, closed=True):
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    routes: NotRequired["capo_direct_connect.types.route_list.RouteList"]
    """<p>The routes for the virtual interface.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVirtualInterfaceRoutesResponse) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "routes" in value:
        import capo_direct_connect.types.route_list

        out["routes"] = capo_direct_connect.types.route_list.serialize_aws_json_1_1(
            value["routes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVirtualInterfaceRoutesResponse:
    out: ListVirtualInterfaceRoutesResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("routes") is not None:
        import capo_direct_connect.types.route_list

        out["routes"] = capo_direct_connect.types.route_list.deserialize_aws_json_1_1(
            data["routes"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVirtualInterfaceRoutesResponse) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "routes" in value:
        import capo_direct_connect.types.route_list

        out["routes"] = capo_direct_connect.types.route_list.serialize_cbor(
            value["routes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListVirtualInterfaceRoutesResponse:
    out: ListVirtualInterfaceRoutesResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("routes") is not None:
        import capo_direct_connect.types.route_list

        out["routes"] = capo_direct_connect.types.route_list.deserialize_cbor(
            data["routes"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
