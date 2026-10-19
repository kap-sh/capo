"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#DeleteResourceExplorerSetupOutput``."""

from typing_extensions import TypedDict


class DeleteResourceExplorerSetupOutput(TypedDict, closed=True):
    task_id: "str"
    """<p>The unique identifier for the deletion task. Use this ID with <code>GetResourceExplorerSetup</code> to monitor the progress of the deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceExplorerSetupOutput) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> DeleteResourceExplorerSetupOutput:
    out: DeleteResourceExplorerSetupOutput = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    return out
