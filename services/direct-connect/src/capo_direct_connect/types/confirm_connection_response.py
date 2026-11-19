"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_state


class ConfirmConnectionResponse(TypedDict, closed=True):
    connection_state: NotRequired[
        "capo_direct_connect.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection. The following are the possible values:</p> <ul> <li> <p> <code>ordering</code>: The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.</p> </li> <li> <p> <code>requested</code>: The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.</p> </li> <li> <p> <code>pending</code>: The connection has been approved and is being initialized.</p> </li> <li> <p> <code>available</code>: The network link is up and the connection is ready for use.</p> </li> <li> <p> <code>down</code>: The network link is down.</p> </li> <li> <p> <code>deleting</code>: The connection is being deleted.</p> </li> <li> <p> <code>deleted</code>: The connection has been deleted.</p> </li> <li> <p> <code>rejected</code>: A hosted connection in the <code>ordering</code> state enters the <code>rejected</code> state if it is deleted by the customer.</p> </li> <li> <p> <code>unknown</code>: The state of the connection is not available.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmConnectionResponse) -> dict:
    out: dict = {}
    if "connection_state" in value:
        import capo_direct_connect.types.connection_state

        out["connectionState"] = (
            capo_direct_connect.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmConnectionResponse:
    out: ConfirmConnectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectionState") is not None:
        import capo_direct_connect.types.connection_state

        out["connection_state"] = (
            capo_direct_connect.types.connection_state.deserialize_aws_json_1_1(
                data["connectionState"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfirmConnectionResponse) -> dict:
    out: dict = {}
    if "connection_state" in value:
        import capo_direct_connect.types.connection_state

        out["connectionState"] = (
            capo_direct_connect.types.connection_state.serialize_cbor(
                value["connection_state"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ConfirmConnectionResponse:
    out: ConfirmConnectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectionState") is not None:
        import capo_direct_connect.types.connection_state

        out["connection_state"] = (
            capo_direct_connect.types.connection_state.deserialize_cbor(
                data["connectionState"]
            )
        )
    return out
