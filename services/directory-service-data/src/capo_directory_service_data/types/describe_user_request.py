"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DescribeUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.ldap_display_name_list
    import capo_directory_service_data.types.realm
    import capo_directory_service_data.types.user_name


class DescribeUserRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the user. </p>"""
    sam_account_name: "capo_directory_service_data.types.user_name.UserName"
    """<p> The name of the user. </p>"""
    other_attributes: NotRequired[
        "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList"
    ]
    """<p> One or more attribute names to be returned for the user. A key is an attribute name, and the value is a list of maps. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the user. </p> <note> <p> This parameter is optional, so you can return users outside your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD users are returned. </p> <p> This value is case insensitive. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserRequest) -> dict:
    out: dict = {}
    out["SAMAccountName"] = value["sam_account_name"]
    if "other_attributes" in value:
        import capo_directory_service_data.types.ldap_display_name_list

        out["OtherAttributes"] = (
            capo_directory_service_data.types.ldap_display_name_list.serialize_json(
                value["other_attributes"]
            )
        )
    if "realm" in value:
        out["Realm"] = value["realm"]
    return out


def deserialize_json(data: dict) -> DescribeUserRequest:
    out: DescribeUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("DescribeUserRequest.sam_account_name required")
    if data.get("OtherAttributes") is not None:
        import capo_directory_service_data.types.ldap_display_name_list

        out["other_attributes"] = (
            capo_directory_service_data.types.ldap_display_name_list.deserialize_json(
                data["OtherAttributes"]
            )
        )
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    return out
