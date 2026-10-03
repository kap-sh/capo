"""Generated from Smithy shape ``com.amazonaws.connect#ListTrafficDistributionGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.acgr_instance_id_or_arn
    import capo_connect.types.max_result10
    import capo_connect.types.next_token


class ListTrafficDistributionGroupsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_connect.types.max_result10.MaxResult10"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    instance_id: NotRequired[
        "capo_connect.types.acgr_instance_id_or_arn.ACGRInstanceIdOrArn"
    ]
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrafficDistributionGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTrafficDistributionGroupsRequest:
    out: ListTrafficDistributionGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
