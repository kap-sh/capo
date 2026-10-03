"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UpdateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.attributes
    import capo_directory_service_data.types.client_token
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.group_scope
    import capo_directory_service_data.types.group_type
    import capo_directory_service_data.types.update_type


class UpdateGroupRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    sam_account_name: "capo_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    group_type: NotRequired["capo_directory_service_data.types.group_type.GroupType"]
    """<p> The AD group type. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work">Active Directory security group type</a>. </p>"""
    group_scope: NotRequired["capo_directory_service_data.types.group_scope.GroupScope"]
    """<p> The scope of the AD group. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope">Active Directory security groups</a>. </p>"""
    other_attributes: NotRequired[
        "capo_directory_service_data.types.attributes.Attributes"
    ]
    """<p> An expression that defines one or more attributes with the data type and the value of each attribute. </p>"""
    update_type: NotRequired["capo_directory_service_data.types.update_type.UpdateType"]
    """<p> The type of update to be performed. If no value exists for the attribute, use <code>ADD</code>. Otherwise, use <code>REPLACE</code> to change an attribute value or <code>REMOVE</code> to clear the attribute value. </p>"""
    client_token: NotRequired[
        "capo_directory_service_data.types.client_token.ClientToken"
    ]
    """<p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupRequest) -> dict:
    out: dict = {}
    out["SAMAccountName"] = value["sam_account_name"]
    if "group_type" in value:
        import capo_directory_service_data.types.group_type

        out["GroupType"] = capo_directory_service_data.types.group_type.serialize_json(
            value["group_type"]
        )
    if "group_scope" in value:
        import capo_directory_service_data.types.group_scope

        out["GroupScope"] = (
            capo_directory_service_data.types.group_scope.serialize_json(
                value["group_scope"]
            )
        )
    if "other_attributes" in value:
        import capo_directory_service_data.types.attributes

        out["OtherAttributes"] = (
            capo_directory_service_data.types.attributes.serialize_json(
                value["other_attributes"]
            )
        )
    if "update_type" in value:
        import capo_directory_service_data.types.update_type

        out["UpdateType"] = (
            capo_directory_service_data.types.update_type.serialize_json(
                value["update_type"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateGroupRequest:
    out: UpdateGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("UpdateGroupRequest.sam_account_name required")
    if data.get("GroupType") is not None:
        import capo_directory_service_data.types.group_type

        out["group_type"] = (
            capo_directory_service_data.types.group_type.deserialize_json(
                data["GroupType"]
            )
        )
    if data.get("GroupScope") is not None:
        import capo_directory_service_data.types.group_scope

        out["group_scope"] = (
            capo_directory_service_data.types.group_scope.deserialize_json(
                data["GroupScope"]
            )
        )
    if data.get("OtherAttributes") is not None:
        import capo_directory_service_data.types.attributes

        out["other_attributes"] = (
            capo_directory_service_data.types.attributes.deserialize_json(
                data["OtherAttributes"]
            )
        )
    if data.get("UpdateType") is not None:
        import capo_directory_service_data.types.update_type

        out["update_type"] = (
            capo_directory_service_data.types.update_type.deserialize_json(
                data["UpdateType"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
