"""Generated from Smithy shape ``com.amazonaws.connect#ListRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.event_source_name
    import capo_connect.types.instance_id
    import capo_connect.types.max_result200
    import capo_connect.types.next_token
    import capo_connect.types.rule_publish_status


class ListRulesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    publish_status: NotRequired[
        "capo_connect.types.rule_publish_status.RulePublishStatus"
    ]
    """<p>The publish status of the rule.</p>"""
    event_source_name: NotRequired[
        "capo_connect.types.event_source_name.EventSourceName"
    ]
    """<p>The name of the event source.</p>"""
    max_results: NotRequired["capo_connect.types.max_result200.MaxResult200"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRulesRequest:
    out: ListRulesRequest = {}  # type: ignore[typeddict-item]
    return out
