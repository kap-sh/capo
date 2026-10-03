"""Generated from Smithy shape ``com.amazonaws.iam#ListServiceSpecificCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.all_users
    import capo_iam.types.marker_type
    import capo_iam.types.max_items_type
    import capo_iam.types.service_name
    import capo_iam.types.user_name_type


class ListServiceSpecificCredentialsRequest(TypedDict, closed=True):
    user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>The name of the user whose service-specific credentials you want information about. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    service_name: NotRequired["capo_iam.types.service_name.serviceName"]
    """<p>Filters the returned results to only those for the specified Amazon Web Services service. If not specified, then Amazon Web Services returns service-specific credentials for all services.</p>"""
    all_users: NotRequired["capo_iam.types.all_users.allUsers"]
    """<p>A flag indicating whether to list service specific credentials for all users. This parameter cannot be specified together with UserName. When true, returns all credentials associated with the specified service.</p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker from the response that you received to indicate where the next call should start.</p>"""
    max_items: NotRequired["capo_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListServiceSpecificCredentialsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "service_name" in value:
        pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    if "all_users" in value:
        pairs.append(
            (f"{key_prefix}AllUsers", "true" if value["all_users"] else "false")
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_items" in value:
        pairs.append((f"{key_prefix}MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListServiceSpecificCredentialsRequest:
    out: ListServiceSpecificCredentialsRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    child_all_users = el.find("AllUsers")
    if child_all_users is not None:
        out["all_users"] = (child_all_users.text or "").lower() == "true"
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
