"""Generated from Smithy shape ``com.amazonaws.controltower#GetBaselineOperationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.operation_identifier


class GetBaselineOperationInput(TypedDict, closed=True):
    operation_identifier: (
        "capo_controltower.types.operation_identifier.OperationIdentifier"
    )
    """<p>The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBaselineOperationInput) -> dict:
    out: dict = {}
    out["operationIdentifier"] = value["operation_identifier"]
    return out


def deserialize_json(data: dict) -> GetBaselineOperationInput:
    out: GetBaselineOperationInput = {}  # type: ignore[typeddict-item]
    if data.get("operationIdentifier") is not None:
        out["operation_identifier"] = data["operationIdentifier"]
    else:
        out["operation_identifier"] = ""
    return out
