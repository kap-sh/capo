"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactFlowAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.resource_id


class DescribeContactFlowAliasRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_id: "capo_connect.types.arn.ARN"
    """<p>The identifier of the flow.</p>"""
    alias_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The identifier of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactFlowAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeContactFlowAliasRequest:
    out: DescribeContactFlowAliasRequest = {}  # type: ignore[typeddict-item]
    return out
