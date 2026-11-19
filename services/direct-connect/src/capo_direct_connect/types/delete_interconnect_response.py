"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteInterconnectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.interconnect_state


class DeleteInterconnectResponse(TypedDict, closed=True):
    interconnect_state: NotRequired[
        "capo_direct_connect.types.interconnect_state.InterconnectState"
    ]
    """<p>The state of the interconnect. The following are the possible values:</p> <ul> <li> <p> <code>requested</code>: The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.</p> </li> <li> <p> <code>pending</code>: The interconnect is approved, and is being initialized.</p> </li> <li> <p> <code>available</code>: The network link is up, and the interconnect is ready for use.</p> </li> <li> <p> <code>down</code>: The network link is down.</p> </li> <li> <p> <code>deleting</code>: The interconnect is being deleted.</p> </li> <li> <p> <code>deleted</code>: The interconnect is deleted.</p> </li> <li> <p> <code>unknown</code>: The state of the interconnect is not available.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInterconnectResponse) -> dict:
    out: dict = {}
    if "interconnect_state" in value:
        import capo_direct_connect.types.interconnect_state

        out["interconnectState"] = (
            capo_direct_connect.types.interconnect_state.serialize_aws_json_1_1(
                value["interconnect_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInterconnectResponse:
    out: DeleteInterconnectResponse = {}  # type: ignore[typeddict-item]
    if data.get("interconnectState") is not None:
        import capo_direct_connect.types.interconnect_state

        out["interconnect_state"] = (
            capo_direct_connect.types.interconnect_state.deserialize_aws_json_1_1(
                data["interconnectState"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteInterconnectResponse) -> dict:
    out: dict = {}
    if "interconnect_state" in value:
        import capo_direct_connect.types.interconnect_state

        out["interconnectState"] = (
            capo_direct_connect.types.interconnect_state.serialize_cbor(
                value["interconnect_state"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteInterconnectResponse:
    out: DeleteInterconnectResponse = {}  # type: ignore[typeddict-item]
    if data.get("interconnectState") is not None:
        import capo_direct_connect.types.interconnect_state

        out["interconnect_state"] = (
            capo_direct_connect.types.interconnect_state.deserialize_cbor(
                data["interconnectState"]
            )
        )
    return out
