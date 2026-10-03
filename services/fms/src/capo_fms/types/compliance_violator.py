"""Generated from Smithy shape ``com.amazonaws.fms#ComplianceViolator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.compliance_violator_metadata
    import capo_fms.types.resource_id
    import capo_fms.types.resource_type
    import capo_fms.types.violation_reason


class ComplianceViolator(TypedDict, closed=True):
    resource_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID.</p>"""
    violation_reason: NotRequired["capo_fms.types.violation_reason.ViolationReason"]
    """<p>The reason that the resource is not protected by the policy.</p>"""
    resource_type: NotRequired["capo_fms.types.resource_type.ResourceType"]
    """<p>The resource type. This is in the format shown in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services Resource Types Reference</a>. For example: <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code>, <code>AWS::CloudFront::Distribution</code>, or <code>AWS::NetworkFirewall::FirewallPolicy</code>.</p>"""
    metadata: NotRequired[
        "capo_fms.types.compliance_violator_metadata.ComplianceViolatorMetadata"
    ]
    """<p>Metadata about the resource that doesn't comply with the policy scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceViolator) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "violation_reason" in value:
        import capo_fms.types.violation_reason

        out["ViolationReason"] = capo_fms.types.violation_reason.serialize_aws_json_1_1(
            value["violation_reason"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "metadata" in value:
        import capo_fms.types.compliance_violator_metadata

        out["Metadata"] = (
            capo_fms.types.compliance_violator_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceViolator:
    out: ComplianceViolator = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ViolationReason") is not None:
        import capo_fms.types.violation_reason

        out["violation_reason"] = (
            capo_fms.types.violation_reason.deserialize_aws_json_1_1(
                data["ViolationReason"]
            )
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Metadata") is not None:
        import capo_fms.types.compliance_violator_metadata

        out["metadata"] = (
            capo_fms.types.compliance_violator_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    return out
