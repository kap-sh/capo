"""Generated from Smithy shape ``com.amazonaws.ram#ListPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.max_results
    import capo_ram.types.permission_status
    import capo_ram.types.permission_type_filter
    import capo_ram.types.resource_owner
    import capo_ram.types.string


class ListPermissionsRequest(TypedDict, closed=True):
    resource_type: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to list only those permissions that apply to the specified resource type. This parameter is not case sensitive.</p> <p>For example, to list only permissions that apply to Amazon EC2 subnets, specify <code>ec2:subnet</code>. You can use the <a>ListResourceTypes</a> operation to get the specific string required.</p>"""
    resource_owner: NotRequired["capo_ram.types.resource_owner.ResourceOwner"]
    """<p>Specifies that you want to list only permissions owned by a specific entity:</p> <ul> <li> <p> <code>SELF</code> – returns only permissions owned by the calling account.</p> </li> <li> <p> <code>OTHER-ACCOUNTS</code> – returns only permissions shared with the calling account by other accounts.</p> </li> </ul>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    permission_type: NotRequired[
        "capo_ram.types.permission_type_filter.PermissionTypeFilter"
    ]
    """<p>Specifies that you want to list only permissions of this type:</p> <ul> <li> <p> <code>AWS</code> – returns only Amazon Web Services managed permissions.</p> </li> <li> <p> <code>LOCAL</code> – returns only customer managed permissions</p> </li> <li> <p> <code>ALL</code> – returns both Amazon Web Services managed permissions and customer managed permissions.</p> </li> </ul> <p>If you don't specify this parameter, the default is <code>All</code>.</p>"""
    permission_status: NotRequired["capo_ram.types.permission_status.PermissionStatus"]
    """<p>Specifies that you want to filter the results to include only permissions with the specified status. For example, use <code>ATTACHABLE</code> to list only permissions that can be associated with resource shares, or <code>DEPRECATED</code> to list only deprecated permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionsRequest) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "resource_owner" in value:
        import capo_ram.types.resource_owner

        out["resourceOwner"] = capo_ram.types.resource_owner.serialize_json(
            value["resource_owner"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "permission_type" in value:
        import capo_ram.types.permission_type_filter

        out["permissionType"] = capo_ram.types.permission_type_filter.serialize_json(
            value["permission_type"]
        )
    if "permission_status" in value:
        import capo_ram.types.permission_status

        out["permissionStatus"] = capo_ram.types.permission_status.serialize_json(
            value["permission_status"]
        )
    return out


def deserialize_json(data: dict) -> ListPermissionsRequest:
    out: ListPermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("resourceOwner") is not None:
        import capo_ram.types.resource_owner

        out["resource_owner"] = capo_ram.types.resource_owner.deserialize_json(
            data["resourceOwner"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("permissionType") is not None:
        import capo_ram.types.permission_type_filter

        out["permission_type"] = capo_ram.types.permission_type_filter.deserialize_json(
            data["permissionType"]
        )
    if data.get("permissionStatus") is not None:
        import capo_ram.types.permission_status

        out["permission_status"] = capo_ram.types.permission_status.deserialize_json(
            data["permissionStatus"]
        )
    return out
