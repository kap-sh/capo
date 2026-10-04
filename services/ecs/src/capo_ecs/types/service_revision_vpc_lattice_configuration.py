"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionVpcLatticeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class ServiceRevisionVpcLatticeConfiguration(TypedDict, closed=True):
    target_group_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target group associated with the service revision.</p>"""
    production_listener_rule: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the production listener rule or listener that directs traffic to the target group associated with the service revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisionVpcLatticeConfiguration) -> dict:
    out: dict = {}
    if "target_group_arn" in value:
        out["targetGroupArn"] = value["target_group_arn"]
    if "production_listener_rule" in value:
        out["productionListenerRule"] = value["production_listener_rule"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceRevisionVpcLatticeConfiguration:
    out: ServiceRevisionVpcLatticeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("targetGroupArn") is not None:
        out["target_group_arn"] = data["targetGroupArn"]
    if data.get("productionListenerRule") is not None:
        out["production_listener_rule"] = data["productionListenerRule"]
    return out
