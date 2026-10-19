"""Generated from Smithy shape ``com.amazonaws.braket#CancelQuantumTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.quantum_task_arn
    import capo_braket.types.string64


class CancelQuantumTaskRequest(TypedDict, closed=True):
    quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task to cancel.</p>"""
    client_token: "capo_braket.types.string64.String64"
    """<p>The client token associated with the cancellation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelQuantumTaskRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CancelQuantumTaskRequest:
    out: CancelQuantumTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
