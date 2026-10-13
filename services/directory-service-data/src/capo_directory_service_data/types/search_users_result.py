"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#SearchUsersResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm
    import capo_directory_service_data.types.user_list


class SearchUsersResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "capo_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory where the address block is added. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain that's associated with the user. </p>"""
    users: NotRequired["capo_directory_service_data.types.user_list.UserList"]
    """<p> The user information that the request returns. </p>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchUsersResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "users" in value:
        import capo_directory_service_data.types.user_list

        out["Users"] = capo_directory_service_data.types.user_list.serialize_json(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchUsersResult:
    out: SearchUsersResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("Users") is not None:
        import capo_directory_service_data.types.user_list

        out["users"] = capo_directory_service_data.types.user_list.deserialize_json(
            data["Users"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: SearchUsersResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_directory_service_data.types.user_list

        out["users"] = capo_directory_service_data.types.user_list.redact_sensitive(
            value["users"]
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
