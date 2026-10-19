"""Generated from Smithy shape ``com.amazonaws.wickr#ListSecurityGroupUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.users


class ListSecurityGroupUsersResponse(TypedDict, closed=True):
    users: "capo_wickr.types.users.Users"
    """<p>A list of user objects belonging to the security group within the current page.</p>"""
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityGroupUsersResponse) -> dict:
    out: dict = {}
    import capo_wickr.types.users

    out["users"] = capo_wickr.types.users.serialize_json(value["users"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityGroupUsersResponse:
    out: ListSecurityGroupUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("users") is not None:
        import capo_wickr.types.users

        out["users"] = capo_wickr.types.users.deserialize_json(data["users"])
    else:
        out["users"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSecurityGroupUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_wickr.types.users

        out["users"] = capo_wickr.types.users.redact_sensitive(value["users"])
    return out
