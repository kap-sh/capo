"""Generated from Smithy shape ``com.amazonaws.ram#ListResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.max_results
    import capo_ram.types.resource_arn_list
    import capo_ram.types.resource_owner
    import capo_ram.types.resource_region_scope_filter
    import capo_ram.types.resource_share_arn_list
    import capo_ram.types.string


class ListResourcesRequest(TypedDict, closed=True):
    resource_owner: "capo_ram.types.resource_owner.ResourceOwner"
    """<p>Specifies that you want to list only the resource shares that match the following:</p> <ul> <li> <p> <b> <code>SELF</code> </b> – resources that your account shares with other accounts</p> </li> <li> <p> <b> <code>OTHER-ACCOUNTS</code> </b> – resources that other accounts share with your account</p> </li> </ul>"""
    principal: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to list only the resource shares that are associated with the specified principal.</p>"""
    resource_type: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to list only the resource shares that include resources of the specified resource type.</p> <p>For valid values, query the <a>ListResourceTypes</a> operation.</p>"""
    resource_arns: NotRequired["capo_ram.types.resource_arn_list.ResourceArnList"]
    """<p>Specifies that you want to list only the resource shares that include resources with the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""
    resource_share_arns: NotRequired[
        "capo_ram.types.resource_share_arn_list.ResourceShareArnList"
    ]
    """<p>Specifies that you want to list only resources in the resource shares identified by the specified <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    resource_region_scope: NotRequired[
        "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
    ]
    """<p>Specifies that you want the results to include only resources that have the specified scope.</p> <ul> <li> <p> <code>ALL</code> – the results include both global and regional resources or resource types.</p> </li> <li> <p> <code>GLOBAL</code> – the results include only global resources or resource types.</p> </li> <li> <p> <code>REGIONAL</code> – the results include only regional resources or resource types.</p> </li> </ul> <p>The default value is <code>ALL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesRequest) -> dict:
    out: dict = {}
    import capo_ram.types.resource_owner

    out["resourceOwner"] = capo_ram.types.resource_owner.serialize_json(
        value["resource_owner"]
    )
    if "principal" in value:
        out["principal"] = value["principal"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "resource_arns" in value:
        import capo_ram.types.resource_arn_list

        out["resourceArns"] = capo_ram.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    if "resource_share_arns" in value:
        import capo_ram.types.resource_share_arn_list

        out["resourceShareArns"] = (
            capo_ram.types.resource_share_arn_list.serialize_json(
                value["resource_share_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "resource_region_scope" in value:
        import capo_ram.types.resource_region_scope_filter

        out["resourceRegionScope"] = (
            capo_ram.types.resource_region_scope_filter.serialize_json(
                value["resource_region_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListResourcesRequest:
    out: ListResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceOwner") is not None:
        import capo_ram.types.resource_owner

        out["resource_owner"] = capo_ram.types.resource_owner.deserialize_json(
            data["resourceOwner"]
        )
    else:
        raise DeserializationError("ListResourcesRequest.resource_owner required")
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("resourceArns") is not None:
        import capo_ram.types.resource_arn_list

        out["resource_arns"] = capo_ram.types.resource_arn_list.deserialize_json(
            data["resourceArns"]
        )
    if data.get("resourceShareArns") is not None:
        import capo_ram.types.resource_share_arn_list

        out["resource_share_arns"] = (
            capo_ram.types.resource_share_arn_list.deserialize_json(
                data["resourceShareArns"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("resourceRegionScope") is not None:
        import capo_ram.types.resource_region_scope_filter

        out["resource_region_scope"] = (
            capo_ram.types.resource_region_scope_filter.deserialize_json(
                data["resourceRegionScope"]
            )
        )
    return out
