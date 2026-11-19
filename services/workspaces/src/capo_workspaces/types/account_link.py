"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.account_link_status_enum
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.link_id


class AccountLink(TypedDict, closed=True):
    account_link_id: NotRequired["capo_workspaces.types.link_id.LinkId"]
    """<p>The identifier of the account link.</p>"""
    account_link_status: NotRequired[
        "capo_workspaces.types.account_link_status_enum.AccountLinkStatusEnum"
    ]
    """<p>The status of the account link.</p>"""
    source_account_id: NotRequired["capo_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the source account.</p>"""
    target_account_id: NotRequired["capo_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the target account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountLink) -> dict:
    out: dict = {}
    if "account_link_id" in value:
        out["AccountLinkId"] = value["account_link_id"]
    if "account_link_status" in value:
        import capo_workspaces.types.account_link_status_enum

        out["AccountLinkStatus"] = (
            capo_workspaces.types.account_link_status_enum.serialize_aws_json_1_1(
                value["account_link_status"]
            )
        )
    if "source_account_id" in value:
        out["SourceAccountId"] = value["source_account_id"]
    if "target_account_id" in value:
        out["TargetAccountId"] = value["target_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountLink:
    out: AccountLink = {}  # type: ignore[typeddict-item]
    if data.get("AccountLinkId") is not None:
        out["account_link_id"] = data["AccountLinkId"]
    if data.get("AccountLinkStatus") is not None:
        import capo_workspaces.types.account_link_status_enum

        out["account_link_status"] = (
            capo_workspaces.types.account_link_status_enum.deserialize_aws_json_1_1(
                data["AccountLinkStatus"]
            )
        )
    if data.get("SourceAccountId") is not None:
        out["source_account_id"] = data["SourceAccountId"]
    if data.get("TargetAccountId") is not None:
        out["target_account_id"] = data["TargetAccountId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountLink) -> dict:
    out: dict = {}
    if "account_link_id" in value:
        out["AccountLinkId"] = value["account_link_id"]
    if "account_link_status" in value:
        import capo_workspaces.types.account_link_status_enum

        out["AccountLinkStatus"] = (
            capo_workspaces.types.account_link_status_enum.serialize_cbor(
                value["account_link_status"]
            )
        )
    if "source_account_id" in value:
        out["SourceAccountId"] = value["source_account_id"]
    if "target_account_id" in value:
        out["TargetAccountId"] = value["target_account_id"]
    return out


def deserialize_cbor(data: dict) -> AccountLink:
    out: AccountLink = {}  # type: ignore[typeddict-item]
    if data.get("AccountLinkId") is not None:
        out["account_link_id"] = data["AccountLinkId"]
    if data.get("AccountLinkStatus") is not None:
        import capo_workspaces.types.account_link_status_enum

        out["account_link_status"] = (
            capo_workspaces.types.account_link_status_enum.deserialize_cbor(
                data["AccountLinkStatus"]
            )
        )
    if data.get("SourceAccountId") is not None:
        out["source_account_id"] = data["SourceAccountId"]
    if data.get("TargetAccountId") is not None:
        out["target_account_id"] = data["TargetAccountId"]
    return out
