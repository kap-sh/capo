"""Generated from Smithy shape ``com.amazonaws.m2#CreateDataSetImportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier


class CreateDataSetImportTaskResponse(TypedDict, closed=True):
    task_id: "capo_m2.types.identifier.Identifier"
    """<p>The task identifier. This operation is asynchronous. Use this identifier with the <a>GetDataSetImportTask</a> operation to obtain the status of this task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSetImportTaskResponse) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> CreateDataSetImportTaskResponse:
    out: CreateDataSetImportTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    return out
