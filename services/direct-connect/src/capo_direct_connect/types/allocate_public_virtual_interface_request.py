"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocatePublicVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.new_public_virtual_interface_allocation
    import capo_direct_connect.types.owner_account


class AllocatePublicVirtualInterfaceRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection on which the public virtual interface is provisioned.</p>"""
    owner_account: "capo_direct_connect.types.owner_account.OwnerAccount"
    """<p>The ID of the Amazon Web Services account that owns the public virtual interface.</p>"""
    new_public_virtual_interface_allocation: "capo_direct_connect.types.new_public_virtual_interface_allocation.NewPublicVirtualInterfaceAllocation"
    """<p>Information about the public virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocatePublicVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["ownerAccount"] = value["owner_account"]
    import capo_direct_connect.types.new_public_virtual_interface_allocation

    out["newPublicVirtualInterfaceAllocation"] = (
        capo_direct_connect.types.new_public_virtual_interface_allocation.serialize_aws_json_1_1(
            value["new_public_virtual_interface_allocation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocatePublicVirtualInterfaceRequest:
    out: AllocatePublicVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    else:
        out["owner_account"] = ""
    if data.get("newPublicVirtualInterfaceAllocation") is not None:
        import capo_direct_connect.types.new_public_virtual_interface_allocation

        out["new_public_virtual_interface_allocation"] = (
            capo_direct_connect.types.new_public_virtual_interface_allocation.deserialize_aws_json_1_1(
                data["newPublicVirtualInterfaceAllocation"]
            )
        )
    else:
        raise DeserializationError(
            "AllocatePublicVirtualInterfaceRequest.new_public_virtual_interface_allocation required"
        )
    return out
