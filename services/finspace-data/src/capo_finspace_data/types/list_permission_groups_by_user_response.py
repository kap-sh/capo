"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListPermissionGroupsByUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.pagination_token
    import capo_finspace_data.types.permission_group_by_user_list


class ListPermissionGroupsByUserResponse(TypedDict, closed=True):
    permission_groups: NotRequired[
        "capo_finspace_data.types.permission_group_by_user_list.PermissionGroupByUserList"
    ]
    """<p>A list of returned permission groups.</p>"""
    next_token: NotRequired["capo_finspace_data.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionGroupsByUserResponse) -> dict:
    out: dict = {}
    if "permission_groups" in value:
        import capo_finspace_data.types.permission_group_by_user_list

        out["permissionGroups"] = (
            capo_finspace_data.types.permission_group_by_user_list.serialize_json(
                value["permission_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPermissionGroupsByUserResponse:
    out: ListPermissionGroupsByUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("permissionGroups") is not None:
        import capo_finspace_data.types.permission_group_by_user_list

        out["permission_groups"] = (
            capo_finspace_data.types.permission_group_by_user_list.deserialize_json(
                data["permissionGroups"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListPermissionGroupsByUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "permission_groups" in value:
        import capo_finspace_data.types.permission_group_by_user_list

        out["permission_groups"] = (
            capo_finspace_data.types.permission_group_by_user_list.redact_sensitive(
                value["permission_groups"]
            )
        )
    return out
