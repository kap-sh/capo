"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleRuntimePlatforms``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_ec2_requirements
    import capo_guardduty.types.detection_rule_ecs_fargate_requirements
    import capo_guardduty.types.detection_rule_eks_requirements


class DetectionRuleRuntimePlatforms(TypedDict, closed=True):
    eks: NotRequired[
        "capo_guardduty.types.detection_rule_eks_requirements.DetectionRuleEksRequirements"
    ]
    """<p>The requirements for running the rule on Amazon EKS.</p>"""
    ec2: NotRequired[
        "capo_guardduty.types.detection_rule_ec2_requirements.DetectionRuleEc2Requirements"
    ]
    """<p>The requirements for running the rule on Amazon EC2.</p>"""
    ecs_fargate: NotRequired[
        "capo_guardduty.types.detection_rule_ecs_fargate_requirements.DetectionRuleEcsFargateRequirements"
    ]
    """<p>The requirements for running the rule on Amazon ECS with the Fargate launch type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleRuntimePlatforms) -> dict:
    out: dict = {}
    if "eks" in value:
        import capo_guardduty.types.detection_rule_eks_requirements

        out["eks"] = (
            capo_guardduty.types.detection_rule_eks_requirements.serialize_json(
                value["eks"]
            )
        )
    if "ec2" in value:
        import capo_guardduty.types.detection_rule_ec2_requirements

        out["ec2"] = (
            capo_guardduty.types.detection_rule_ec2_requirements.serialize_json(
                value["ec2"]
            )
        )
    if "ecs_fargate" in value:
        import capo_guardduty.types.detection_rule_ecs_fargate_requirements

        out["ecsFargate"] = (
            capo_guardduty.types.detection_rule_ecs_fargate_requirements.serialize_json(
                value["ecs_fargate"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectionRuleRuntimePlatforms:
    out: DetectionRuleRuntimePlatforms = {}  # type: ignore[typeddict-item]
    if data.get("eks") is not None:
        import capo_guardduty.types.detection_rule_eks_requirements

        out["eks"] = (
            capo_guardduty.types.detection_rule_eks_requirements.deserialize_json(
                data["eks"]
            )
        )
    if data.get("ec2") is not None:
        import capo_guardduty.types.detection_rule_ec2_requirements

        out["ec2"] = (
            capo_guardduty.types.detection_rule_ec2_requirements.deserialize_json(
                data["ec2"]
            )
        )
    if data.get("ecsFargate") is not None:
        import capo_guardduty.types.detection_rule_ecs_fargate_requirements

        out["ecs_fargate"] = (
            capo_guardduty.types.detection_rule_ecs_fargate_requirements.deserialize_json(
                data["ecsFargate"]
            )
        )
    return out
