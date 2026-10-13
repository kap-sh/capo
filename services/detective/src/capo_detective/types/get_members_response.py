"""Generated from Smithy shape ``com.amazonaws.detective#GetMembersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.member_detail_list
    import capo_detective.types.unprocessed_account_list


class GetMembersResponse(TypedDict, closed=True):
    member_details: NotRequired[
        "capo_detective.types.member_detail_list.MemberDetailList"
    ]
    """<p>The member account details that Detective is returning in response to the request.</p>"""
    unprocessed_accounts: NotRequired[
        "capo_detective.types.unprocessed_account_list.UnprocessedAccountList"
    ]
    """<p>The requested member accounts for which Detective was unable to return member details.</p> <p>For each account, provides the reason why the request could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembersResponse) -> dict:
    out: dict = {}
    if "member_details" in value:
        import capo_detective.types.member_detail_list

        out["MemberDetails"] = capo_detective.types.member_detail_list.serialize_json(
            value["member_details"]
        )
    if "unprocessed_accounts" in value:
        import capo_detective.types.unprocessed_account_list

        out["UnprocessedAccounts"] = (
            capo_detective.types.unprocessed_account_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMembersResponse:
    out: GetMembersResponse = {}  # type: ignore[typeddict-item]
    if data.get("MemberDetails") is not None:
        import capo_detective.types.member_detail_list

        out["member_details"] = (
            capo_detective.types.member_detail_list.deserialize_json(
                data["MemberDetails"]
            )
        )
    if data.get("UnprocessedAccounts") is not None:
        import capo_detective.types.unprocessed_account_list

        out["unprocessed_accounts"] = (
            capo_detective.types.unprocessed_account_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out


def redact_sensitive(value: GetMembersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member_details" in value:
        import capo_detective.types.member_detail_list

        out["member_details"] = (
            capo_detective.types.member_detail_list.redact_sensitive(
                value["member_details"]
            )
        )
    return out
