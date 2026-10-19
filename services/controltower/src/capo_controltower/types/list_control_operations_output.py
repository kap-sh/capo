"""Generated from Smithy shape ``com.amazonaws.controltower#ListControlOperationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.control_operations
    import capo_controltower.types.list_control_operations_next_token


class ListControlOperationsOutput(TypedDict, closed=True):
    control_operations: "capo_controltower.types.control_operations.ControlOperations"
    """<p>Returns a list of output from control operations. </p>"""
    next_token: NotRequired[
        "capo_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
    ]
    """<p>A pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlOperationsOutput) -> dict:
    out: dict = {}
    import capo_controltower.types.control_operations

    out["controlOperations"] = (
        capo_controltower.types.control_operations.serialize_json(
            value["control_operations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlOperationsOutput:
    out: ListControlOperationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("controlOperations") is not None:
        import capo_controltower.types.control_operations

        out["control_operations"] = (
            capo_controltower.types.control_operations.deserialize_json(
                data["controlOperations"]
            )
        )
    else:
        out["control_operations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
