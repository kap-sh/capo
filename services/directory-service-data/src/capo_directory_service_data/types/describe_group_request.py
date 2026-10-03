"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DescribeGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.ldap_display_name_list
    import capo_directory_service_data.types.realm


class DescribeGroupRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service_data.types.directory_id.DirectoryId"
    """<p>The Identifier (ID) of the directory associated with the group.</p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>"""
    sam_account_name: "capo_directory_service_data.types.group_name.GroupName"
    """<p> The name of the group. </p>"""
    other_attributes: NotRequired[
        "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList"
    ]
    """<p> One or more attributes to be returned for the group. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGroupRequest) -> dict:
    out: dict = {}
    if "realm" in value:
        out["Realm"] = value["realm"]
    out["SAMAccountName"] = value["sam_account_name"]
    if "other_attributes" in value:
        import capo_directory_service_data.types.ldap_display_name_list

        out["OtherAttributes"] = (
            capo_directory_service_data.types.ldap_display_name_list.serialize_json(
                value["other_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeGroupRequest:
    out: DescribeGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("DescribeGroupRequest.sam_account_name required")
    if data.get("OtherAttributes") is not None:
        import capo_directory_service_data.types.ldap_display_name_list

        out["other_attributes"] = (
            capo_directory_service_data.types.ldap_display_name_list.deserialize_json(
                data["OtherAttributes"]
            )
        )
    return out
