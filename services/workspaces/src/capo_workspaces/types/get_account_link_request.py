"""Generated from Smithy shape ``com.amazonaws.workspaces#GetAccountLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.link_id


class GetAccountLinkRequest(TypedDict, closed=True):
    link_id: NotRequired["capo_workspaces.types.link_id.LinkId"]
    """<p>The identifier of the account to link.</p>"""
    linked_account_id: NotRequired["capo_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the account link</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountLinkRequest) -> dict:
    out: dict = {}
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "linked_account_id" in value:
        out["LinkedAccountId"] = value["linked_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountLinkRequest:
    out: GetAccountLinkRequest = {}  # type: ignore[typeddict-item]
    if data.get("LinkId") is not None:
        out["link_id"] = data["LinkId"]
    if data.get("LinkedAccountId") is not None:
        out["linked_account_id"] = data["LinkedAccountId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAccountLinkRequest) -> dict:
    out: dict = {}
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "linked_account_id" in value:
        out["LinkedAccountId"] = value["linked_account_id"]
    return out


def deserialize_cbor(data: dict) -> GetAccountLinkRequest:
    out: GetAccountLinkRequest = {}  # type: ignore[typeddict-item]
    if data.get("LinkId") is not None:
        out["link_id"] = data["LinkId"]
    if data.get("LinkedAccountId") is not None:
        out["linked_account_id"] = data["LinkedAccountId"]
    return out
