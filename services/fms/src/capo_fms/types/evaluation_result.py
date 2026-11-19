"""Generated from Smithy shape ``com.amazonaws.fms#EvaluationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.policy_compliance_status_type
    import capo_fms.types.resource_count


class EvaluationResult(TypedDict, closed=True):
    compliance_status: NotRequired[
        "capo_fms.types.policy_compliance_status_type.PolicyComplianceStatusType"
    ]
    """<p>Describes an Amazon Web Services account's compliance with the Firewall Manager policy.</p>"""
    violator_count: "capo_fms.types.resource_count.ResourceCount"
    """<p>The number of resources that are noncompliant with the specified policy. For WAF and Shield Advanced policies, a resource is considered noncompliant if it is not associated with the policy. For security group policies, a resource is considered noncompliant if it doesn't comply with the rules of the policy and remediation is disabled or not possible.</p>"""
    evaluation_limit_exceeded: "capo_fms.types.boolean.Boolean"
    """<p>Indicates that over 100 resources are noncompliant with the Firewall Manager policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResult) -> dict:
    out: dict = {}
    if "compliance_status" in value:
        import capo_fms.types.policy_compliance_status_type

        out["ComplianceStatus"] = (
            capo_fms.types.policy_compliance_status_type.serialize_aws_json_1_1(
                value["compliance_status"]
            )
        )
    out["ViolatorCount"] = value.get("violator_count", 0)
    out["EvaluationLimitExceeded"] = value.get("evaluation_limit_exceeded", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationResult:
    out: EvaluationResult = {}  # type: ignore[typeddict-item]
    if data.get("ComplianceStatus") is not None:
        import capo_fms.types.policy_compliance_status_type

        out["compliance_status"] = (
            capo_fms.types.policy_compliance_status_type.deserialize_aws_json_1_1(
                data["ComplianceStatus"]
            )
        )
    if data.get("ViolatorCount") is not None:
        out["violator_count"] = data["ViolatorCount"]
    else:
        out["violator_count"] = 0
    if data.get("EvaluationLimitExceeded") is not None:
        out["evaluation_limit_exceeded"] = data["EvaluationLimitExceeded"]
    else:
        out["evaluation_limit_exceeded"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EvaluationResult) -> dict:
    out: dict = {}
    if "compliance_status" in value:
        import capo_fms.types.policy_compliance_status_type

        out["ComplianceStatus"] = (
            capo_fms.types.policy_compliance_status_type.serialize_cbor(
                value["compliance_status"]
            )
        )
    out["ViolatorCount"] = value.get("violator_count", 0)
    out["EvaluationLimitExceeded"] = value.get("evaluation_limit_exceeded", False)
    return out


def deserialize_cbor(data: dict) -> EvaluationResult:
    out: EvaluationResult = {}  # type: ignore[typeddict-item]
    if data.get("ComplianceStatus") is not None:
        import capo_fms.types.policy_compliance_status_type

        out["compliance_status"] = (
            capo_fms.types.policy_compliance_status_type.deserialize_cbor(
                data["ComplianceStatus"]
            )
        )
    if data.get("ViolatorCount") is not None:
        out["violator_count"] = data["ViolatorCount"]
    else:
        out["violator_count"] = 0
    if data.get("EvaluationLimitExceeded") is not None:
        out["evaluation_limit_exceeded"] = data["EvaluationLimitExceeded"]
    else:
        out["evaluation_limit_exceeded"] = False
    return out
