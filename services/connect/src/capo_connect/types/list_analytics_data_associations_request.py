"""Generated from Smithy shape ``com.amazonaws.connect#ListAnalyticsDataAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_set_id
    import capo_connect.types.instance_id
    import capo_connect.types.max_result1000
    import capo_connect.types.next_token


class ListAnalyticsDataAssociationsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    data_set_id: NotRequired["capo_connect.types.data_set_id.DataSetId"]
    """<p>The identifier of the dataset to get the association status.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyticsDataAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAnalyticsDataAssociationsRequest:
    out: ListAnalyticsDataAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
