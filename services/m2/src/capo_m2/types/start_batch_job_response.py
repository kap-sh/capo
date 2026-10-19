"""Generated from Smithy shape ``com.amazonaws.m2#StartBatchJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier


class StartBatchJobResponse(TypedDict, closed=True):
    execution_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of this execution of the batch job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBatchJobResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> StartBatchJobResponse:
    out: StartBatchJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    return out
