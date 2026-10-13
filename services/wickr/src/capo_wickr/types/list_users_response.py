"""Generated from Smithy shape ``com.amazonaws.wickr#ListUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.users


class ListUsersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""
    users: NotRequired["capo_wickr.types.users.Users"]
    """<p>A list of user objects matching the specified filters and within the current page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "users" in value:
        import capo_wickr.types.users

        out["users"] = capo_wickr.types.users.serialize_json(value["users"])
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("users") is not None:
        import capo_wickr.types.users

        out["users"] = capo_wickr.types.users.deserialize_json(data["users"])
    return out


def redact_sensitive(value: ListUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_wickr.types.users

        out["users"] = capo_wickr.types.users.redact_sensitive(value["users"])
    return out
