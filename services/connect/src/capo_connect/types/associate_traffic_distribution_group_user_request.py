"""Generated from Smithy shape ``com.amazonaws.connect#AssociateTrafficDistributionGroupUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.traffic_distribution_group_id_or_arn
    import capo_connect.types.user_id


class AssociateTrafficDistributionGroupUserRequest(TypedDict, closed=True):
    traffic_distribution_group_id: "capo_connect.types.traffic_distribution_group_id_or_arn.TrafficDistributionGroupIdOrArn"
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN of the traffic distribution group.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user account. This can be the ID or the ARN of the user. </p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTrafficDistributionGroupUserRequest) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    out["InstanceId"] = value["instance_id"]
    return out


def deserialize_json(data: dict) -> AssociateTrafficDistributionGroupUserRequest:
    out: AssociateTrafficDistributionGroupUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError(
            "AssociateTrafficDistributionGroupUserRequest.user_id required"
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "AssociateTrafficDistributionGroupUserRequest.instance_id required"
        )
    return out
