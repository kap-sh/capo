"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListGroupMembersResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.member_list
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm


class ListGroupMembersResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "capo_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p>Identifier (ID) of the directory associated with the group.</p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p>"""
    member_realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the member. </p>"""
    members: NotRequired["capo_directory_service_data.types.member_list.MemberList"]
    """<p> The member information that the request returns. </p>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupMembersResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "member_realm" in value:
        out["MemberRealm"] = value["member_realm"]
    if "members" in value:
        import capo_directory_service_data.types.member_list

        out["Members"] = capo_directory_service_data.types.member_list.serialize_json(
            value["members"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupMembersResult:
    out: ListGroupMembersResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("MemberRealm") is not None:
        out["member_realm"] = data["MemberRealm"]
    if data.get("Members") is not None:
        import capo_directory_service_data.types.member_list

        out["members"] = capo_directory_service_data.types.member_list.deserialize_json(
            data["Members"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListGroupMembersResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
