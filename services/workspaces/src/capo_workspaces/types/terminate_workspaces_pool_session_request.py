"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspacesPoolSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.amazon_uuid


class TerminateWorkspacesPoolSessionRequest(TypedDict, closed=True):
    session_id: "capo_workspaces.types.amazon_uuid.AmazonUuid"
    """<p>The identifier of the pool session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspacesPoolSessionRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateWorkspacesPoolSessionRequest:
    out: TerminateWorkspacesPoolSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    return out
