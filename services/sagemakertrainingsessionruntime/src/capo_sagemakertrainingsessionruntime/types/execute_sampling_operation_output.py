"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ExecuteSamplingOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.operation_id


class ExecuteSamplingOperationOutput(TypedDict, closed=True):
    operation_id: "capo_sagemakertrainingsessionruntime.types.operation_id.OperationId"
    """<p>The unique identifier for the submitted sample operation. Use this identifier with <code>GetSamplingOperationResult</code> to retrieve the operation status and result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteSamplingOperationOutput) -> dict:
    out: dict = {}
    out["operationId"] = value["operation_id"]
    return out


def deserialize_json(data: dict) -> ExecuteSamplingOperationOutput:
    out: ExecuteSamplingOperationOutput = {}  # type: ignore[typeddict-item]
    if data.get("operationId") is not None:
        out["operation_id"] = data["operationId"]
    else:
        out["operation_id"] = ""
    return out
