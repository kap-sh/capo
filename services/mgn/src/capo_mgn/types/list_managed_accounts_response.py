"""Generated from Smithy shape ``com.amazonaws.mgn#ListManagedAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.managed_accounts
    import capo_mgn.types.pagination_token


class ListManagedAccountsResponse(TypedDict, closed=True):
    items: "capo_mgn.types.managed_accounts.ManagedAccounts"
    """<p>List managed accounts response items.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List managed accounts response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedAccountsResponse) -> dict:
    out: dict = {}
    import capo_mgn.types.managed_accounts

    out["items"] = capo_mgn.types.managed_accounts.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedAccountsResponse:
    out: ListManagedAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.managed_accounts

        out["items"] = capo_mgn.types.managed_accounts.deserialize_json(data["items"])
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
