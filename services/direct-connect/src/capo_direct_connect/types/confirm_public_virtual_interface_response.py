"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmPublicVirtualInterfaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.virtual_interface_state


class ConfirmPublicVirtualInterfaceResponse(TypedDict, closed=True):
    virtual_interface_state: NotRequired[
        "capo_direct_connect.types.virtual_interface_state.VirtualInterfaceState"
    ]
    """<p>The state of the virtual interface. The following are the possible values:</p> <ul> <li> <p> <code>confirming</code>: The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.</p> </li> <li> <p> <code>verifying</code>: This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.</p> </li> <li> <p> <code>pending</code>: A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.</p> </li> <li> <p> <code>available</code>: A virtual interface that is able to forward traffic.</p> </li> <li> <p> <code>down</code>: A virtual interface that is BGP down.</p> </li> <li> <p> <code>testing</code>: A virtual interface is in this state immediately after calling <a>StartBgpFailoverTest</a> and remains in this state during the duration of the test.</p> </li> <li> <p> <code>deleting</code>: A virtual interface is in this state immediately after calling <a>DeleteVirtualInterface</a> until it can no longer forward traffic.</p> </li> <li> <p> <code>deleted</code>: A virtual interface that cannot forward traffic.</p> </li> <li> <p> <code>rejected</code>: The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the <code>Confirming</code> state is deleted by the virtual interface owner, the virtual interface enters the <code>Rejected</code> state.</p> </li> <li> <p> <code>unknown</code>: The state of the virtual interface is not available.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmPublicVirtualInterfaceResponse) -> dict:
    out: dict = {}
    if "virtual_interface_state" in value:
        import capo_direct_connect.types.virtual_interface_state

        out["virtualInterfaceState"] = (
            capo_direct_connect.types.virtual_interface_state.serialize_aws_json_1_1(
                value["virtual_interface_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmPublicVirtualInterfaceResponse:
    out: ConfirmPublicVirtualInterfaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceState") is not None:
        import capo_direct_connect.types.virtual_interface_state

        out["virtual_interface_state"] = (
            capo_direct_connect.types.virtual_interface_state.deserialize_aws_json_1_1(
                data["virtualInterfaceState"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfirmPublicVirtualInterfaceResponse) -> dict:
    out: dict = {}
    if "virtual_interface_state" in value:
        import capo_direct_connect.types.virtual_interface_state

        out["virtualInterfaceState"] = (
            capo_direct_connect.types.virtual_interface_state.serialize_cbor(
                value["virtual_interface_state"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ConfirmPublicVirtualInterfaceResponse:
    out: ConfirmPublicVirtualInterfaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceState") is not None:
        import capo_direct_connect.types.virtual_interface_state

        out["virtual_interface_state"] = (
            capo_direct_connect.types.virtual_interface_state.deserialize_cbor(
                data["virtualInterfaceState"]
            )
        )
    return out
