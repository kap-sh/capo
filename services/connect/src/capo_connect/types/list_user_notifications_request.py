"""Generated from Smithy shape ``com.amazonaws.connect#ListUserNotificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result1000
    import capo_connect.types.next_token
    import capo_connect.types.user_id


class ListUserNotificationsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of results to return per page. Valid range is 1-1000.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserNotificationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUserNotificationsRequest:
    out: ListUserNotificationsRequest = {}  # type: ignore[typeddict-item]
    return out
