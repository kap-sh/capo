"""Generated from Smithy shape ``com.amazonaws.chime#ListUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.string
    import capo_chime.types.user_list


class ListUsersResponse(TypedDict, closed=True):
    users: NotRequired["capo_chime.types.user_list.UserList"]
    """<p>List of users and user details.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_chime.types.user_list

        out["Users"] = capo_chime.types.user_list.serialize_json(value["users"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_chime.types.user_list

        out["users"] = capo_chime.types.user_list.deserialize_json(data["Users"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_chime.types.user_list

        out["users"] = capo_chime.types.user_list.redact_sensitive(value["users"])
    return out
