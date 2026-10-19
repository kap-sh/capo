"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateAccountLinkInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.client_token


class CreateAccountLinkInvitationRequest(TypedDict, closed=True):
    target_account_id: "capo_workspaces.types.aws_account.AwsAccount"
    """<p>The identifier of the target account.</p>"""
    client_token: NotRequired["capo_workspaces.types.client_token.ClientToken"]
    """<p>A string of up to 64 ASCII characters that Amazon WorkSpaces uses to ensure idempotent creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountLinkInvitationRequest) -> dict:
    out: dict = {}
    out["TargetAccountId"] = value["target_account_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccountLinkInvitationRequest:
    out: CreateAccountLinkInvitationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TargetAccountId") is not None:
        out["target_account_id"] = data["TargetAccountId"]
    else:
        out["target_account_id"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
