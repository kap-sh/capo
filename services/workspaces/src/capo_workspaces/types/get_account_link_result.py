"""Generated from Smithy shape ``com.amazonaws.workspaces#GetAccountLinkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.account_link


class GetAccountLinkResult(TypedDict, closed=True):
    account_link: NotRequired["capo_workspaces.types.account_link.AccountLink"]
    """<p>The account link of the account link to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountLinkResult) -> dict:
    out: dict = {}
    if "account_link" in value:
        import capo_workspaces.types.account_link

        out["AccountLink"] = capo_workspaces.types.account_link.serialize_aws_json_1_1(
            value["account_link"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountLinkResult:
    out: GetAccountLinkResult = {}  # type: ignore[typeddict-item]
    if data.get("AccountLink") is not None:
        import capo_workspaces.types.account_link

        out["account_link"] = (
            capo_workspaces.types.account_link.deserialize_aws_json_1_1(
                data["AccountLink"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAccountLinkResult) -> dict:
    out: dict = {}
    if "account_link" in value:
        import capo_workspaces.types.account_link

        out["AccountLink"] = capo_workspaces.types.account_link.serialize_cbor(
            value["account_link"]
        )
    return out


def deserialize_cbor(data: dict) -> GetAccountLinkResult:
    out: GetAccountLinkResult = {}  # type: ignore[typeddict-item]
    if data.get("AccountLink") is not None:
        import capo_workspaces.types.account_link

        out["account_link"] = capo_workspaces.types.account_link.deserialize_cbor(
            data["AccountLink"]
        )
    return out
