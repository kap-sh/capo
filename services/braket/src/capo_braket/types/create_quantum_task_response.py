"""Generated from Smithy shape ``com.amazonaws.braket#CreateQuantumTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.quantum_task_arn


class CreateQuantumTaskResponse(TypedDict, closed=True):
    quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task created by the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuantumTaskResponse) -> dict:
    out: dict = {}
    out["quantumTaskArn"] = value["quantum_task_arn"]
    return out


def deserialize_json(data: dict) -> CreateQuantumTaskResponse:
    out: CreateQuantumTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("quantumTaskArn") is not None:
        out["quantum_task_arn"] = data["quantumTaskArn"]
    else:
        out["quantum_task_arn"] = ""
    return out
