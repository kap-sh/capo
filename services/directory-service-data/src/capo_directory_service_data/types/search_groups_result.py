"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#SearchGroupsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.group_list
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm


class SearchGroupsResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "capo_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain that's associated with the group. </p>"""
    groups: NotRequired["capo_directory_service_data.types.group_list.GroupList"]
    """<p> The group information that the request returns. </p>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupsResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "groups" in value:
        import capo_directory_service_data.types.group_list

        out["Groups"] = capo_directory_service_data.types.group_list.serialize_json(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchGroupsResult:
    out: SearchGroupsResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("Groups") is not None:
        import capo_directory_service_data.types.group_list

        out["groups"] = capo_directory_service_data.types.group_list.deserialize_json(
            data["Groups"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: SearchGroupsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "groups" in value:
        import capo_directory_service_data.types.group_list

        out["groups"] = capo_directory_service_data.types.group_list.redact_sensitive(
            value["groups"]
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
