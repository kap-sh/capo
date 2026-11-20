"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#ListRolesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access_runtime.types.access_details_list


class ListRolesResponse(TypedDict, closed=True):
    roles: "capo_account_access_runtime.types.access_details_list.AccessDetailsList"
    """<p>The list of roles that you can access in the tenant. Each entry describes an Amazon Web Services account and a role.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to include in a subsequent <code>ListRoles</code> request to retrieve the next page of results. This value is absent when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRolesResponse) -> dict:
    out: dict = {}
    import capo_account_access_runtime.types.access_details_list

    out["roles"] = capo_account_access_runtime.types.access_details_list.serialize_json(
        value["roles"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRolesResponse:
    out: ListRolesResponse = {}  # type: ignore[typeddict-item]
    if data.get("roles") is not None:
        import capo_account_access_runtime.types.access_details_list

        out["roles"] = (
            capo_account_access_runtime.types.access_details_list.deserialize_json(
                data["roles"]
            )
        )
    else:
        out["roles"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
