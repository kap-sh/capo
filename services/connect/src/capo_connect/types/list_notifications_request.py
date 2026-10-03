"""Generated from Smithy shape ``com.amazonaws.connect#ListNotificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token


class ListNotificationsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page. Valid range is 1-100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotificationsRequest:
    out: ListNotificationsRequest = {}  # type: ignore[typeddict-item]
    return out
