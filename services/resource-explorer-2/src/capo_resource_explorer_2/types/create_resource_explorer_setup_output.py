"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CreateResourceExplorerSetupOutput``."""

from typing_extensions import TypedDict


class CreateResourceExplorerSetupOutput(TypedDict, closed=True):
    task_id: "str"
    """<p>The unique identifier for the setup task. Use this ID with <code>GetResourceExplorerSetup</code> to monitor the progress of the configuration operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceExplorerSetupOutput) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> CreateResourceExplorerSetupOutput:
    out: CreateResourceExplorerSetupOutput = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    return out
