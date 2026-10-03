"""Generated from Smithy shape ``com.amazonaws.connect#GetCrossRegionRoutingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.acgr_instance_id_or_arn


class GetCrossRegionRoutingRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.acgr_instance_id_or_arn.ACGRInstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCrossRegionRoutingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCrossRegionRoutingRequest:
    out: GetCrossRegionRoutingRequest = {}  # type: ignore[typeddict-item]
    return out
