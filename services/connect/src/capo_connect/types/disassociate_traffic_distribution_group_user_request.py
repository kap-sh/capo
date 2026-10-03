"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateTrafficDistributionGroupUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.traffic_distribution_group_id_or_arn
    import capo_connect.types.user_id


class DisassociateTrafficDistributionGroupUserRequest(TypedDict, closed=True):
    traffic_distribution_group_id: "capo_connect.types.traffic_distribution_group_id_or_arn.TrafficDistributionGroupIdOrArn"
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN of the traffic distribution group.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier for the user. This can be the ID or the ARN of the user.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateTrafficDistributionGroupUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateTrafficDistributionGroupUserRequest:
    out: DisassociateTrafficDistributionGroupUserRequest = {}  # type: ignore[typeddict-item]
    return out
