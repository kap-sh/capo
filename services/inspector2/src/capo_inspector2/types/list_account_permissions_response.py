"""Generated from Smithy shape ``com.amazonaws.inspector2#ListAccountPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.next_token
    import capo_inspector2.types.permissions


class ListAccountPermissionsResponse(TypedDict, closed=True):
    permissions: "capo_inspector2.types.permissions.Permissions"
    """<p>Contains details on the permissions an account has to configure Amazon Inspector.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountPermissionsResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.permissions

    out["permissions"] = capo_inspector2.types.permissions.serialize_json(
        value["permissions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountPermissionsResponse:
    out: ListAccountPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("permissions") is not None:
        import capo_inspector2.types.permissions

        out["permissions"] = capo_inspector2.types.permissions.deserialize_json(
            data["permissions"]
        )
    else:
        out["permissions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
