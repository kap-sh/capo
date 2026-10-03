"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalableTargetAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.resource_capacity


class ScalableTargetAction(TypedDict, closed=True):
    min_capacity: NotRequired[
        "capo_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The minimum capacity.</p> <p>When the scheduled action runs, the resource will have at least this much capacity, but it might have more depending on other settings, such as the target utilization level of a target tracking scaling policy.</p>"""
    max_capacity: NotRequired[
        "capo_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The maximum capacity.</p> <p>Although you can specify a large maximum capacity, note that service quotas may impose lower limits. Each service has its own default quotas for the maximum capacity of the resource. If you want to specify a higher limit, you can request an increase. For more information, consult the documentation for that service. For information about the default quotas for each service, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html">Service endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalableTargetAction) -> dict:
    out: dict = {}
    if "min_capacity" in value:
        out["MinCapacity"] = value["min_capacity"]
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalableTargetAction:
    out: ScalableTargetAction = {}  # type: ignore[typeddict-item]
    if data.get("MinCapacity") is not None:
        out["min_capacity"] = data["MinCapacity"]
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = data["MaxCapacity"]
    return out
