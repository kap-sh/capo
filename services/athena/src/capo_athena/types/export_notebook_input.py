"""Generated from Smithy shape ``com.amazonaws.athena#ExportNotebookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.notebook_id


class ExportNotebookInput(TypedDict, closed=True):
    notebook_id: "capo_athena.types.notebook_id.NotebookId"
    """<p>The ID of the notebook to export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportNotebookInput) -> dict:
    out: dict = {}
    out["NotebookId"] = value["notebook_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportNotebookInput:
    out: ExportNotebookInput = {}  # type: ignore[typeddict-item]
    if data.get("NotebookId") is not None:
        out["notebook_id"] = data["NotebookId"]
    else:
        out["notebook_id"] = ""
    return out
