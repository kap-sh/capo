"""Generated from Smithy shape ``com.amazonaws.directconnect#CreatePublicVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.new_public_virtual_interface


class CreatePublicVirtualInterfaceRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    new_public_virtual_interface: "capo_direct_connect.types.new_public_virtual_interface.NewPublicVirtualInterface"
    """<p>Information about the public virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePublicVirtualInterfaceRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    import capo_direct_connect.types.new_public_virtual_interface

    out["newPublicVirtualInterface"] = (
        capo_direct_connect.types.new_public_virtual_interface.serialize_aws_json_1_1(
            value["new_public_virtual_interface"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePublicVirtualInterfaceRequest:
    out: CreatePublicVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("newPublicVirtualInterface") is not None:
        import capo_direct_connect.types.new_public_virtual_interface

        out["new_public_virtual_interface"] = (
            capo_direct_connect.types.new_public_virtual_interface.deserialize_aws_json_1_1(
                data["newPublicVirtualInterface"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePublicVirtualInterfaceRequest.new_public_virtual_interface required"
        )
    return out
