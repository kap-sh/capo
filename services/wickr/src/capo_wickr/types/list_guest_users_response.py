"""Generated from Smithy shape ``com.amazonaws.wickr#ListGuestUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.guest_user_list


class ListGuestUsersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""
    guestlist: "capo_wickr.types.guest_user_list.GuestUserList"
    """<p>A list of guest user objects within the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGuestUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_wickr.types.guest_user_list

    out["guestlist"] = capo_wickr.types.guest_user_list.serialize_json(
        value["guestlist"]
    )
    return out


def deserialize_json(data: dict) -> ListGuestUsersResponse:
    out: ListGuestUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("guestlist") is not None:
        import capo_wickr.types.guest_user_list

        out["guestlist"] = capo_wickr.types.guest_user_list.deserialize_json(
            data["guestlist"]
        )
    else:
        out["guestlist"] = []
    return out
