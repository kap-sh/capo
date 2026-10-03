"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.attributes
    import capo_directory_service_data.types.distinguished_name
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.group_scope
    import capo_directory_service_data.types.group_type
    import capo_directory_service_data.types.sid


class Group(TypedDict, closed=True):
    sid: NotRequired["capo_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the group. </p>"""
    sam_account_name: "capo_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    distinguished_name: NotRequired[
        "capo_directory_service_data.types.distinguished_name.DistinguishedName"
    ]
    """<p>The <a href="https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name">distinguished name</a> of the object. </p>"""
    group_type: NotRequired["capo_directory_service_data.types.group_type.GroupType"]
    """<p> The AD group type. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work">Active Directory security group type</a>. </p>"""
    group_scope: NotRequired["capo_directory_service_data.types.group_scope.GroupScope"]
    """<p> The scope of the AD group. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope">Active Directory security groups</a> </p>"""
    other_attributes: NotRequired[
        "capo_directory_service_data.types.attributes.Attributes"
    ]
    """<p> An expression of one or more attributes, data types, and the values of a group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    if "sid" in value:
        out["SID"] = value["sid"]
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


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("Group.sam_account_name required")
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
