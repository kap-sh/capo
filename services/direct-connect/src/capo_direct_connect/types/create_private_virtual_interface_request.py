"""Generated from Smithy shape ``com.amazonaws.directconnect#CreatePrivateVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.new_private_virtual_interface


class CreatePrivateVirtualInterfaceRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    new_private_virtual_interface: "capo_direct_connect.types.new_private_virtual_interface.NewPrivateVirtualInterface"
    """<p>Information about the private virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePrivateVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    import capo_direct_connect.types.new_private_virtual_interface

    out["newPrivateVirtualInterface"] = (
        capo_direct_connect.types.new_private_virtual_interface.serialize_aws_json_1_1(
            value["new_private_virtual_interface"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePrivateVirtualInterfaceRequest:
    out: CreatePrivateVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("newPrivateVirtualInterface") is not None:
        import capo_direct_connect.types.new_private_virtual_interface

        out["new_private_virtual_interface"] = (
            capo_direct_connect.types.new_private_virtual_interface.deserialize_aws_json_1_1(
                data["newPrivateVirtualInterface"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePrivateVirtualInterfaceRequest.new_private_virtual_interface required"
        )
    return out
