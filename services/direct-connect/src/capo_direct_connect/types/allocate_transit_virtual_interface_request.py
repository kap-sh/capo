"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocateTransitVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.new_transit_virtual_interface_allocation
    import capo_direct_connect.types.owner_account


class AllocateTransitVirtualInterfaceRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection on which the transit virtual interface is provisioned.</p>"""
    owner_account: "capo_direct_connect.types.owner_account.OwnerAccount"
    """<p>The ID of the Amazon Web Services account that owns the transit virtual interface.</p>"""
    new_transit_virtual_interface_allocation: "capo_direct_connect.types.new_transit_virtual_interface_allocation.NewTransitVirtualInterfaceAllocation"
    """<p>Information about the transit virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocateTransitVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["ownerAccount"] = value["owner_account"]
    import capo_direct_connect.types.new_transit_virtual_interface_allocation

    out["newTransitVirtualInterfaceAllocation"] = (
        capo_direct_connect.types.new_transit_virtual_interface_allocation.serialize_aws_json_1_1(
            value["new_transit_virtual_interface_allocation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocateTransitVirtualInterfaceRequest:
    out: AllocateTransitVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    else:
        out["owner_account"] = ""
    if data.get("newTransitVirtualInterfaceAllocation") is not None:
        import capo_direct_connect.types.new_transit_virtual_interface_allocation

        out["new_transit_virtual_interface_allocation"] = (
            capo_direct_connect.types.new_transit_virtual_interface_allocation.deserialize_aws_json_1_1(
                data["newTransitVirtualInterfaceAllocation"]
            )
        )
    else:
        raise DeserializationError(
            "AllocateTransitVirtualInterfaceRequest.new_transit_virtual_interface_allocation required"
        )
    return out
