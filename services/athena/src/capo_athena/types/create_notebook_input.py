"""Generated from Smithy shape ``com.amazonaws.athena#CreateNotebookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.client_request_token
    import capo_athena.types.notebook_name
    import capo_athena.types.work_group_name


class CreateNotebookInput(TypedDict, closed=True):
    work_group: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The name of the Spark enabled workgroup in which the notebook will be created.</p>"""
    name: "capo_athena.types.notebook_name.NotebookName"
    """<p>The name of the <code>ipynb</code> file to be created in the Spark workgroup, without the <code>.ipynb</code> extension.</p>"""
    client_request_token: NotRequired[
        "capo_athena.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNotebookInput) -> dict:
    out: dict = {}
    out["WorkGroup"] = value["work_group"]
    out["Name"] = value["name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNotebookInput:
    out: CreateNotebookInput = {}  # type: ignore[typeddict-item]
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    else:
        out["work_group"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
