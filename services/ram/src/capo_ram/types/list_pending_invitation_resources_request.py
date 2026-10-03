"""Generated from Smithy shape ``com.amazonaws.ram#ListPendingInvitationResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.max_results
    import capo_ram.types.resource_region_scope_filter
    import capo_ram.types.string


class ListPendingInvitationResourcesRequest(TypedDict, closed=True):
    resource_share_invitation_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the invitation. You can use <a>GetResourceShareInvitations</a> to find the ARN of the invitation.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    resource_region_scope: NotRequired[
        "capo_ram.types.resource_region_scope_filter.ResourceRegionScopeFilter"
    ]
    """<p>Specifies that you want the results to include only resources that have the specified scope.</p> <ul> <li> <p> <code>ALL</code> – the results include both global and regional resources or resource types.</p> </li> <li> <p> <code>GLOBAL</code> – the results include only global resources or resource types.</p> </li> <li> <p> <code>REGIONAL</code> – the results include only regional resources or resource types.</p> </li> </ul> <p>The default value is <code>ALL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingInvitationResourcesRequest) -> dict:
    out: dict = {}
    out["resourceShareInvitationArn"] = value["resource_share_invitation_arn"]
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


def deserialize_json(data: dict) -> ListPendingInvitationResourcesRequest:
    out: ListPendingInvitationResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareInvitationArn") is not None:
        out["resource_share_invitation_arn"] = data["resourceShareInvitationArn"]
    else:
        raise DeserializationError(
            "ListPendingInvitationResourcesRequest.resource_share_invitation_arn required"
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
