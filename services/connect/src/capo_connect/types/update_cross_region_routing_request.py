"""Generated from Smithy shape ``com.amazonaws.connect#UpdateCrossRegionRoutingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.acgr_instance_id_or_arn
    import capo_connect.types.boolean


class UpdateCrossRegionRoutingRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.acgr_instance_id_or_arn.ACGRInstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    isolated_all: "capo_connect.types.boolean.Boolean"
    """<p>Set to <code>true</code> to disable cross-region routing for all Regions associated with this instance. Set to <code>false</code> to re-enable cross-region routing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCrossRegionRoutingRequest) -> dict:
    out: dict = {}
    out["IsolatedAll"] = value.get("isolated_all", False)
    return out


def deserialize_json(data: dict) -> UpdateCrossRegionRoutingRequest:
    out: UpdateCrossRegionRoutingRequest = {}  # type: ignore[typeddict-item]
    if data.get("IsolatedAll") is not None:
        out["isolated_all"] = data["IsolatedAll"]
    else:
        out["isolated_all"] = False
    return out
