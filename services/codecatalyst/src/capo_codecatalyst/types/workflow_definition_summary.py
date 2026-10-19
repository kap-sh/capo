"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowDefinitionSummary``."""

from typing_extensions import TypedDict


class WorkflowDefinitionSummary(TypedDict, closed=True):
    path: "str"
    """<p>The path to the workflow definition file stored in the source repository for the project, including the file name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowDefinitionSummary) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> WorkflowDefinitionSummary:
    out: WorkflowDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    return out
