"""Generated from Smithy shape ``com.amazonaws.braket#CancelQuantumTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.cancellation_status
    import capo_braket.types.quantum_task_arn


class CancelQuantumTaskResponse(TypedDict, closed=True):
    quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task.</p>"""
    cancellation_status: "capo_braket.types.cancellation_status.CancellationStatus"
    """<p>The status of the quantum task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelQuantumTaskResponse) -> dict:
    out: dict = {}
    out["quantumTaskArn"] = value["quantum_task_arn"]
    out["cancellationStatus"] = value["cancellation_status"]
    return out


def deserialize_json(data: dict) -> CancelQuantumTaskResponse:
    out: CancelQuantumTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("quantumTaskArn") is not None:
        out["quantum_task_arn"] = data["quantumTaskArn"]
    else:
        out["quantum_task_arn"] = ""
    if data.get("cancellationStatus") is not None:
        out["cancellation_status"] = data["cancellationStatus"]
    else:
        out["cancellation_status"] = ""
    return out
