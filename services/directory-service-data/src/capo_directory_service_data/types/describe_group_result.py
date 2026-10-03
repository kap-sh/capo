"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DescribeGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.attributes
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.distinguished_name
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.group_scope
    import capo_directory_service_data.types.group_type
    import capo_directory_service_data.types.realm
    import capo_directory_service_data.types.sid


class DescribeGroupResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "capo_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p>"""
    sid: NotRequired["capo_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the group. </p>"""
    sam_account_name: NotRequired[
        "capo_directory_service_data.types.group_name.GroupName"
    ]
    """<p> The name of the group. </p>"""
    distinguished_name: NotRequired[
        "capo_directory_service_data.types.distinguished_name.DistinguishedName"
    ]
    """<p> The <a href="https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name">distinguished name</a> of the object. </p>"""
    group_type: NotRequired["capo_directory_service_data.types.group_type.GroupType"]
    """<p> The AD group type. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work">Active Directory security group type</a>. </p>"""
    group_scope: NotRequired["capo_directory_service_data.types.group_scope.GroupScope"]
    """<p> The scope of the AD group. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope">Active Directory security groups</a>. </p>"""
    other_attributes: NotRequired[
        "capo_directory_service_data.types.attributes.Attributes"
    ]
    """<p> The attribute values that are returned for the attribute names that are included in the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGroupResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "sid" in value:
        out["SID"] = value["sid"]
    if "sam_account_name" in value:
        out["SAMAccountName"] = value["sam_account_name"]
    if "distinguished_name" in value:
        out["DistinguishedName"] = value["distinguished_name"]
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
    return out


def deserialize_json(data: dict) -> DescribeGroupResult:
    out: DescribeGroupResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    if data.get("DistinguishedName") is not None:
        out["distinguished_name"] = data["DistinguishedName"]
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
    return out
