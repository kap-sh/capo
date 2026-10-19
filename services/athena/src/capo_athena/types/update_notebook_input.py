"""Generated from Smithy shape ``com.amazonaws.athena#UpdateNotebookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.client_request_token
    import capo_athena.types.notebook_id
    import capo_athena.types.notebook_type
    import capo_athena.types.payload
    import capo_athena.types.session_id


class UpdateNotebookInput(TypedDict, closed=True):
    notebook_id: "capo_athena.types.notebook_id.NotebookId"
    """<p>The ID of the notebook to update.</p>"""
    payload: "capo_athena.types.payload.Payload"
    """<p>The updated content for the notebook.</p>"""
    type: "capo_athena.types.notebook_type.NotebookType"
    """<p>The notebook content type. Currently, the only valid type is <code>IPYNB</code>.</p>"""
    session_id: NotRequired["capo_athena.types.session_id.SessionId"]
    """<p>The active notebook session ID. Required if the notebook has an active session.</p>"""
    client_request_token: NotRequired[
        "capo_athena.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the notebook is idempotent (executes only once).</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for you. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotebookInput) -> dict:
    out: dict = {}
    out["NotebookId"] = value["notebook_id"]
    out["Payload"] = value["payload"]
    import capo_athena.types.notebook_type

    out["Type"] = capo_athena.types.notebook_type.serialize_aws_json_1_1(value["type"])
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotebookInput:
    out: UpdateNotebookInput = {}  # type: ignore[typeddict-item]
    if data.get("NotebookId") is not None:
        out["notebook_id"] = data["NotebookId"]
    else:
        out["notebook_id"] = ""
    if data.get("Payload") is not None:
        out["payload"] = data["Payload"]
    else:
        out["payload"] = ""
    if data.get("Type") is not None:
        import capo_athena.types.notebook_type

        out["type"] = capo_athena.types.notebook_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_athena.types.notebook_type.NotebookType", "")
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
