"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#SearchGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.ldap_display_name_list
    import capo_directory_service_data.types.max_results
    import capo_directory_service_data.types.next_token
    import capo_directory_service_data.types.realm
    import capo_directory_service_data.types.search_string


class SearchGroupsRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    search_string: "capo_directory_service_data.types.search_string.SearchString"
    """<p> The attribute value that you want to search for. </p> <note> <p> Wildcard <code>(*)</code> searches aren't supported. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p> </note>"""
    search_attributes: (
        "capo_directory_service_data.types.ldap_display_name_list.LdapDisplayNameList"
    )
    """<p> One or more data attributes that are used to search for a group. For a list of supported attributes, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html">Directory Service Data Attributes</a>. </p>"""
    realm: NotRequired["capo_directory_service_data.types.realm.Realm"]
    """<p> The domain name that's associated with the group. </p> <note> <p> This parameter is optional, so you can return groups outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD groups are returned. </p> <p> This value is case insensitive. </p> </note>"""
    next_token: NotRequired["capo_directory_service_data.types.next_token.NextToken"]
    """<p> An encoded paging token for paginated calls that can be passed back to retrieve the next page. </p>"""
    max_results: NotRequired["capo_directory_service_data.types.max_results.MaxResults"]
    """<p> The maximum number of results to be returned per request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupsRequest) -> dict:
    out: dict = {}
    out["SearchString"] = value["search_string"]
    import capo_directory_service_data.types.ldap_display_name_list

    out["SearchAttributes"] = (
        capo_directory_service_data.types.ldap_display_name_list.serialize_json(
            value["search_attributes"]
        )
    )
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchGroupsRequest:
    out: SearchGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SearchString") is not None:
        out["search_string"] = data["SearchString"]
    else:
        raise DeserializationError("SearchGroupsRequest.search_string required")
    if data.get("SearchAttributes") is not None:
        import capo_directory_service_data.types.ldap_display_name_list

        out["search_attributes"] = (
            capo_directory_service_data.types.ldap_display_name_list.deserialize_json(
                data["SearchAttributes"]
            )
        )
    else:
        raise DeserializationError("SearchGroupsRequest.search_attributes required")
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
