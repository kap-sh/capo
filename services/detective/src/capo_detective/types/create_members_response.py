"""Generated from Smithy shape ``com.amazonaws.detective#CreateMembersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.member_detail_list
    import capo_detective.types.unprocessed_account_list


class CreateMembersResponse(TypedDict, closed=True):
    members: NotRequired["capo_detective.types.member_detail_list.MemberDetailList"]
    """<p>The set of member account invitation or enablement requests that Detective was able to process. This includes accounts that are being verified, that failed verification, and that passed verification and are being sent an invitation or are being enabled.</p>"""
    unprocessed_accounts: NotRequired[
        "capo_detective.types.unprocessed_account_list.UnprocessedAccountList"
    ]
    """<p>The list of accounts for which Detective was unable to process the invitation or enablement request. For each account, the list provides the reason why the request could not be processed. The list includes accounts that are already member accounts in the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import capo_detective.types.member_detail_list

        out["Members"] = capo_detective.types.member_detail_list.serialize_json(
            value["members"]
        )
    if "unprocessed_accounts" in value:
        import capo_detective.types.unprocessed_account_list

        out["UnprocessedAccounts"] = (
            capo_detective.types.unprocessed_account_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMembersResponse:
    out: CreateMembersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Members") is not None:
        import capo_detective.types.member_detail_list

        out["members"] = capo_detective.types.member_detail_list.deserialize_json(
            data["Members"]
        )
    if data.get("UnprocessedAccounts") is not None:
        import capo_detective.types.unprocessed_account_list

        out["unprocessed_accounts"] = (
            capo_detective.types.unprocessed_account_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out


def redact_sensitive(value: CreateMembersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "members" in value:
        import capo_detective.types.member_detail_list

        out["members"] = capo_detective.types.member_detail_list.redact_sensitive(
            value["members"]
        )
    return out
