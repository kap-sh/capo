"""Generated from Smithy shape ``com.amazonaws.connect#ListReplicationFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.large_next_token
    import capo_connect.types.max_result100
    import capo_connect.types.replication_finding_resource_type


class ListReplicationFindingsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can provide either the instance ID or the full instance ARN. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    resource_type: "capo_connect.types.replication_finding_resource_type.ReplicationFindingResourceType"
    """<p>The type of resource to list replication findings for. The following values are currently supported: <code>AGENT</code>, <code>AGENT_GROUP</code>, <code>AGENT_GROUP_LEVEL</code>, <code>AGENT_STATE</code>, <code>ATTRIBUTE</code>, <code>CONTACT_FLOW</code>, <code>DATA_TABLE</code>, <code>DATA_TABLE_ATTRIBUTE</code>, <code>DATA_TABLE_RECORD</code>, <code>DATA_TABLE_VALUE</code>, <code>FLOW_MODULE</code>, <code>FLOW_MODULE_ALIAS</code>, <code>FLOW_MODULE_VERSION</code>, <code>METRIC</code>, <code>NOTIFICATION</code>, <code>OPERATING_HOURS</code>, <code>PHONE_NUMBER</code>, <code>PROMPT</code>, <code>QUEUE</code>, <code>REPORT</code>, <code>ROUTING_PROFILE</code>, <code>SECURITY_PROFILE</code>, <code>TASK_TEMPLATE</code>, <code>TEST_CASE</code>, <code>TRANSFER_DESTINATION</code>, <code>VIEW</code>, and <code>WORKSPACE</code>. Additional resource types can be supported over time. Specifying a value that is not currently supported returns an <code>InvalidRequestException</code>.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplicationFindingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReplicationFindingsRequest:
    out: ListReplicationFindingsRequest = {}  # type: ignore[typeddict-item]
    return out
