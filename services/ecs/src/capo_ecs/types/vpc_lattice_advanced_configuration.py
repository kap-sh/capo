"""Generated from Smithy shape ``com.amazonaws.ecs#VpcLatticeAdvancedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class VpcLatticeAdvancedConfiguration(TypedDict, closed=True):
    alternate_target_group_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the alternate target group associated with the VPC Lattice Configuration for Amazon ECS blue/green deployments.</p>"""
    production_listener_rule: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the production listener rule or listener for routing production traffic.</p>"""
    test_listener_rule: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the test listener rule or listener for routing test traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcLatticeAdvancedConfiguration) -> dict:
    out: dict = {}
    if "alternate_target_group_arn" in value:
        out["alternateTargetGroupArn"] = value["alternate_target_group_arn"]
    if "production_listener_rule" in value:
        out["productionListenerRule"] = value["production_listener_rule"]
    if "test_listener_rule" in value:
        out["testListenerRule"] = value["test_listener_rule"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcLatticeAdvancedConfiguration:
    out: VpcLatticeAdvancedConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("alternateTargetGroupArn") is not None:
        out["alternate_target_group_arn"] = data["alternateTargetGroupArn"]
    if data.get("productionListenerRule") is not None:
        out["production_listener_rule"] = data["productionListenerRule"]
    if data.get("testListenerRule") is not None:
        out["test_listener_rule"] = data["testListenerRule"]
    return out
