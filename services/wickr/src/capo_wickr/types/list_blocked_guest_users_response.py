"""Generated from Smithy shape ``com.amazonaws.wickr#ListBlockedGuestUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.blocked_guest_user_list
    import capo_wickr.types.generic_string


class ListBlockedGuestUsersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""
    blocklist: "capo_wickr.types.blocked_guest_user_list.BlockedGuestUserList"
    """<p>A list of blocked guest user objects within the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBlockedGuestUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_wickr.types.blocked_guest_user_list

    out["blocklist"] = capo_wickr.types.blocked_guest_user_list.serialize_json(
        value["blocklist"]
    )
    return out


def deserialize_json(data: dict) -> ListBlockedGuestUsersResponse:
    out: ListBlockedGuestUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("blocklist") is not None:
        import capo_wickr.types.blocked_guest_user_list

        out["blocklist"] = capo_wickr.types.blocked_guest_user_list.deserialize_json(
            data["blocklist"]
        )
    else:
        out["blocklist"] = []
    return out
