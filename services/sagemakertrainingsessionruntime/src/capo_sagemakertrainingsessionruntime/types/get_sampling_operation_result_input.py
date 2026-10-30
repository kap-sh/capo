"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#GetSamplingOperationResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.operation_id
    import capo_sagemakertrainingsessionruntime.types.training_session_name


class GetSamplingOperationResultInput(TypedDict, closed=True):
    training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName"
    """<p>The name of the training session that owns the sample operation.</p>"""
    operation_id: "capo_sagemakertrainingsessionruntime.types.operation_id.OperationId"
    """<p>The unique identifier of the sample operation to retrieve, returned by <code>ExecuteSamplingOperation</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingOperationResultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSamplingOperationResultInput:
    out: GetSamplingOperationResultInput = {}  # type: ignore[typeddict-item]
    return out
