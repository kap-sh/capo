"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.organization_user_list
    import capo_workdocs.types.page_marker_type
    import capo_workdocs.types.size_type


class DescribeUsersResponse(TypedDict, closed=True):
    users: NotRequired[
        "capo_workdocs.types.organization_user_list.OrganizationUserList"
    ]
    """<p>The users.</p>"""
    total_number_of_users: NotRequired["capo_workdocs.types.size_type.SizeType"]
    """<p>The total number of users included in the results.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_workdocs.types.organization_user_list

        out["Users"] = capo_workdocs.types.organization_user_list.serialize_json(
            value["users"]
        )
    if "total_number_of_users" in value:
        out["TotalNumberOfUsers"] = value["total_number_of_users"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeUsersResponse:
    out: DescribeUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_workdocs.types.organization_user_list

        out["users"] = capo_workdocs.types.organization_user_list.deserialize_json(
            data["Users"]
        )
    if data.get("TotalNumberOfUsers") is not None:
        out["total_number_of_users"] = data["TotalNumberOfUsers"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out


def redact_sensitive(value: DescribeUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_workdocs.types.organization_user_list

        out["users"] = capo_workdocs.types.organization_user_list.redact_sensitive(
            value["users"]
        )
    return out
