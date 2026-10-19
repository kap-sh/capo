"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteMatchingWorkflowOutput``."""

from typing_extensions import TypedDict


class DeleteMatchingWorkflowOutput(TypedDict, closed=True):
    message: "str"
    """<p>A successful operation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMatchingWorkflowOutput) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteMatchingWorkflowOutput:
    out: DeleteMatchingWorkflowOutput = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
