"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.pagination_token
    import capo_finspace_data.types.user_list


class ListUsersResponse(TypedDict, closed=True):
    users: NotRequired["capo_finspace_data.types.user_list.UserList"]
    """<p>A list of all the users.</p>"""
    next_token: NotRequired["capo_finspace_data.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_finspace_data.types.user_list

        out["users"] = capo_finspace_data.types.user_list.serialize_json(value["users"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("users") is not None:
        import capo_finspace_data.types.user_list

        out["users"] = capo_finspace_data.types.user_list.deserialize_json(
            data["users"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_finspace_data.types.user_list

        out["users"] = capo_finspace_data.types.user_list.redact_sensitive(
            value["users"]
        )
    return out
