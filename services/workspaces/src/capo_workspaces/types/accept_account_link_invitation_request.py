"""Generated from Smithy shape ``com.amazonaws.workspaces#AcceptAccountLinkInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.client_token
    import capo_workspaces.types.link_id


class AcceptAccountLinkInvitationRequest(TypedDict, closed=True):
    link_id: "capo_workspaces.types.link_id.LinkId"
    """<p>The identifier of the account link.</p>"""
    client_token: NotRequired["capo_workspaces.types.client_token.ClientToken"]
    """<p>A string of up to 64 ASCII characters that Amazon WorkSpaces uses to ensure idempotent creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptAccountLinkInvitationRequest) -> dict:
    out: dict = {}
    out["LinkId"] = value["link_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptAccountLinkInvitationRequest:
    out: AcceptAccountLinkInvitationRequest = {}  # type: ignore[typeddict-item]
    if data.get("LinkId") is not None:
        out["link_id"] = data["LinkId"]
    else:
        out["link_id"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
