"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterfaces``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.pagination_token
    import capo_direct_connect.types.virtual_interface_list


class VirtualInterfaces(TypedDict, closed=True):
    virtual_interfaces: NotRequired[
        "capo_direct_connect.types.virtual_interface_list.VirtualInterfaceList"
    ]
    """<p>The virtual interfaces</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterfaces) -> dict:
    out: dict = {}
    if "virtual_interfaces" in value:
        import capo_direct_connect.types.virtual_interface_list

        out["virtualInterfaces"] = (
            capo_direct_connect.types.virtual_interface_list.serialize_aws_json_1_1(
                value["virtual_interfaces"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VirtualInterfaces:
    out: VirtualInterfaces = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaces") is not None:
        import capo_direct_connect.types.virtual_interface_list

        out["virtual_interfaces"] = (
            capo_direct_connect.types.virtual_interface_list.deserialize_aws_json_1_1(
                data["virtualInterfaces"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VirtualInterfaces) -> dict:
    out: dict = {}
    if "virtual_interfaces" in value:
        import capo_direct_connect.types.virtual_interface_list

        out["virtualInterfaces"] = (
            capo_direct_connect.types.virtual_interface_list.serialize_cbor(
                value["virtual_interfaces"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> VirtualInterfaces:
    out: VirtualInterfaces = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaces") is not None:
        import capo_direct_connect.types.virtual_interface_list

        out["virtual_interfaces"] = (
            capo_direct_connect.types.virtual_interface_list.deserialize_cbor(
                data["virtualInterfaces"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
