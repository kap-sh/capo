"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.aws_region
    import capo_resiliencehubv2.types.entity_id
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.resource_type_filter_list


class ListResourcesRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    service_function_id: NotRequired["capo_resiliencehubv2.types.entity_id.EntityId"]
    """<p>Filter resources by service function identifier.</p>"""
    aws_region: NotRequired["capo_resiliencehubv2.types.aws_region.AwsRegion"]
    """<p>Filter resources by AWS Region.</p>"""
    resource_types: NotRequired[
        "capo_resiliencehubv2.types.resource_type_filter_list.ResourceTypeFilterList"
    ]
    """<p>The CloudFormation resource types to include in the response.</p>"""
    billable: NotRequired["bool"]
    """<p>Specifies whether to filter non-billable resources. When true (the default), the operation returns only billable resources.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourcesRequest:
    out: ListResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
