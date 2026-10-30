"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#GetTrainingOperationResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.operation_id
    import capo_sagemakertrainingsessionruntime.types.training_session_name


class GetTrainingOperationResultInput(TypedDict, closed=True):
    training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName"
    """<p>The name of the training session that owns the operation.</p>"""
    operation_id: "capo_sagemakertrainingsessionruntime.types.operation_id.OperationId"
    """<p>The unique identifier of the operation to retrieve, returned by <code>ExecuteTrainingOperation</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainingOperationResultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTrainingOperationResultInput:
    out: GetTrainingOperationResultInput = {}  # type: ignore[typeddict-item]
    return out
