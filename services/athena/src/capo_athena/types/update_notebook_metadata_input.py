"""Generated from Smithy shape ``com.amazonaws.athena#UpdateNotebookMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.client_request_token
    import capo_athena.types.notebook_id
    import capo_athena.types.notebook_name


class UpdateNotebookMetadataInput(TypedDict, closed=True):
    notebook_id: "capo_athena.types.notebook_id.NotebookId"
    """<p>The ID of the notebook to update the metadata for.</p>"""
    client_request_token: NotRequired[
        "capo_athena.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""
    name: "capo_athena.types.notebook_name.NotebookName"
    """<p>The name to update the notebook to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotebookMetadataInput) -> dict:
    out: dict = {}
    out["NotebookId"] = value["notebook_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotebookMetadataInput:
    out: UpdateNotebookMetadataInput = {}  # type: ignore[typeddict-item]
    if data.get("NotebookId") is not None:
        out["notebook_id"] = data["NotebookId"]
    else:
        out["notebook_id"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
