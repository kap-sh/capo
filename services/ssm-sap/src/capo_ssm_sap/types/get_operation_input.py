"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetOperationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.operation_id


class GetOperationInput(TypedDict, closed=True):
    operation_id: "capo_ssm_sap.types.operation_id.OperationId"
    """<p>The ID of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOperationInput) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_json(data: dict) -> GetOperationInput:
    out: GetOperationInput = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    else:
        out["operation_id"] = ""
    return out
