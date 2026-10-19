"""Generated from Smithy shape ``com.amazonaws.notifications#ListMemberAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.member_accounts
    import capo_notifications.types.next_token


class ListMemberAccountsResponse(TypedDict, closed=True):
    member_accounts: "capo_notifications.types.member_accounts.MemberAccounts"
    """<p>The list of member accounts that match the specified criteria.</p>"""
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>The token to use for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemberAccountsResponse) -> dict:
    out: dict = {}
    import capo_notifications.types.member_accounts

    out["memberAccounts"] = capo_notifications.types.member_accounts.serialize_json(
        value["member_accounts"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemberAccountsResponse:
    out: ListMemberAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("memberAccounts") is not None:
        import capo_notifications.types.member_accounts

        out["member_accounts"] = (
            capo_notifications.types.member_accounts.deserialize_json(
                data["memberAccounts"]
            )
        )
    else:
        out["member_accounts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
