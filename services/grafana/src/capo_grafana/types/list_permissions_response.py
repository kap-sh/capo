"""Generated from Smithy shape ``com.amazonaws.grafana#ListPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.pagination_token
    import capo_grafana.types.permission_entry_list


class ListPermissionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use in a subsequent <code>ListPermissions</code> operation to return the next set of results.</p>"""
    permissions: "capo_grafana.types.permission_entry_list.PermissionEntryList"
    """<p>The permissions returned by the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_grafana.types.permission_entry_list

    out["permissions"] = capo_grafana.types.permission_entry_list.serialize_json(
        value["permissions"]
    )
    return out


def deserialize_json(data: dict) -> ListPermissionsResponse:
    out: ListPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("permissions") is not None:
        import capo_grafana.types.permission_entry_list

        out["permissions"] = capo_grafana.types.permission_entry_list.deserialize_json(
            data["permissions"]
        )
    else:
        out["permissions"] = []
    return out
