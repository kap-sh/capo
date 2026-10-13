"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ListGroupsForMemberRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.max_results
    import capo_directory_service_data.types.member_name
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm


class ListGroupsForMemberRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the member. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive and defaults to your Managed Microsoft AD domain. </p> </note>"""
    member_realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group member. </p> <note> <p> This parameter is optional, so you can limit your results to the group members in a specific domain. </p> <p> This parameter is case insensitive and defaults to <code>Realm</code> </p> </note>"""
    sam_account_name: "capo_directory_service_data.types.member_name.MemberName"
    """<p> The <code>SAMAccountName</code> of the user, group, or computer that's a member of the group. </p>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""
    max_results: NotRequired["capo_directory_service_data.types.max_results.MaxResults"]
    """<p> The maximum number of results to be returned per request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsForMemberRequest) -> dict:
    out: dict = {}
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "member_realm" in value:
        out["MemberRealm"] = value["member_realm"]
    out["SAMAccountName"] = value["sam_account_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListGroupsForMemberRequest:
    out: ListGroupsForMemberRequest = {}  # type: ignore[typeddict-item]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("MemberRealm") is not None:
        out["member_realm"] = data["MemberRealm"]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError(
            "ListGroupsForMemberRequest.sam_account_name required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


def redact_sensitive(value: ListGroupsForMemberRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
