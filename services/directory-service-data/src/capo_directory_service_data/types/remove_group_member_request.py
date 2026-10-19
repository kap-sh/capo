"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#RemoveGroupMemberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.client_token
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.member_name
    import capo_directory_service_data.types.realm


class RemoveGroupMemberRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the member. </p>"""
    group_name: "capo_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    member_name: "capo_directory_service_data.types.member_name.MemberName"
    """<p> The <code>SAMAccountName</code> of the user, group, or computer to remove from the group. </p>"""
    member_realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group member. This parameter defaults to the Managed Microsoft AD domain. </p> <note> <p> This parameter is optional and case insensitive. </p> </note>"""
    client_token: NotRequired[
        "capo_directory_service_data.types.client_token.ClientToken"
    ]
    """<p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveGroupMemberRequest) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    out["MemberName"] = value["member_name"]
    if "member_realm" in value:
        out["MemberRealm"] = value["member_realm"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RemoveGroupMemberRequest:
    out: RemoveGroupMemberRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("MemberName") is not None:
        out["member_name"] = data["MemberName"]
    else:
        out["member_name"] = ""
    if data.get("MemberRealm") is not None:
        out["member_realm"] = data["MemberRealm"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
