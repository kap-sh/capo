"""Generated from Smithy shape ``com.amazonaws.athena#GetNotebookMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.notebook_id


class GetNotebookMetadataInput(TypedDict, closed=True):
    notebook_id: "capo_athena.types.notebook_id.NotebookId"
    """<p>The ID of the notebook whose metadata is to be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNotebookMetadataInput) -> dict:
    out: dict = {}
    out["NotebookId"] = value["notebook_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNotebookMetadataInput:
    out: GetNotebookMetadataInput = {}  # type: ignore[typeddict-item]
    if data.get("NotebookId") is not None:
        out["notebook_id"] = data["NotebookId"]
    else:
        out["notebook_id"] = ""
    return out
