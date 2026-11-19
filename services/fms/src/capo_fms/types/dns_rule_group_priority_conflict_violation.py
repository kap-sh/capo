"""Generated from Smithy shape ``com.amazonaws.fms#DnsRuleGroupPriorityConflictViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.dns_rule_group_priorities
    import capo_fms.types.dns_rule_group_priority
    import capo_fms.types.length_bounded_string
    import capo_fms.types.policy_id
    import capo_fms.types.violation_target


class DnsRuleGroupPriorityConflictViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>Information about the VPC ID. </p>"""
    violation_target_description: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the violation that specifies the VPC and the rule group that's already associated with it.</p>"""
    conflicting_priority: "capo_fms.types.dns_rule_group_priority.DnsRuleGroupPriority"
    """<p>The priority setting of the two conflicting rule groups.</p>"""
    conflicting_policy_id: NotRequired["capo_fms.types.policy_id.PolicyId"]
    """<p>The ID of the Firewall Manager DNS Firewall policy that was already applied to the VPC. This policy contains the rule group that's already associated with the VPC. </p>"""
    unavailable_priorities: NotRequired[
        "capo_fms.types.dns_rule_group_priorities.DnsRuleGroupPriorities"
    ]
    """<p>The priorities of rule groups that are already associated with the VPC. To retry your operation, choose priority settings that aren't in this list for the rule groups in your new DNS Firewall policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRuleGroupPriorityConflictViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violation_target_description" in value:
        out["ViolationTargetDescription"] = value["violation_target_description"]
    out["ConflictingPriority"] = value.get("conflicting_priority", 0)
    if "conflicting_policy_id" in value:
        out["ConflictingPolicyId"] = value["conflicting_policy_id"]
    if "unavailable_priorities" in value:
        import capo_fms.types.dns_rule_group_priorities

        out["UnavailablePriorities"] = (
            capo_fms.types.dns_rule_group_priorities.serialize_aws_json_1_1(
                value["unavailable_priorities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsRuleGroupPriorityConflictViolation:
    out: DnsRuleGroupPriorityConflictViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("ViolationTargetDescription") is not None:
        out["violation_target_description"] = data["ViolationTargetDescription"]
    if data.get("ConflictingPriority") is not None:
        out["conflicting_priority"] = data["ConflictingPriority"]
    else:
        out["conflicting_priority"] = 0
    if data.get("ConflictingPolicyId") is not None:
        out["conflicting_policy_id"] = data["ConflictingPolicyId"]
    if data.get("UnavailablePriorities") is not None:
        import capo_fms.types.dns_rule_group_priorities

        out["unavailable_priorities"] = (
            capo_fms.types.dns_rule_group_priorities.deserialize_aws_json_1_1(
                data["UnavailablePriorities"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DnsRuleGroupPriorityConflictViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violation_target_description" in value:
        out["ViolationTargetDescription"] = value["violation_target_description"]
    out["ConflictingPriority"] = value.get("conflicting_priority", 0)
    if "conflicting_policy_id" in value:
        out["ConflictingPolicyId"] = value["conflicting_policy_id"]
    if "unavailable_priorities" in value:
        import capo_fms.types.dns_rule_group_priorities

        out["UnavailablePriorities"] = (
            capo_fms.types.dns_rule_group_priorities.serialize_cbor(
                value["unavailable_priorities"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DnsRuleGroupPriorityConflictViolation:
    out: DnsRuleGroupPriorityConflictViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("ViolationTargetDescription") is not None:
        out["violation_target_description"] = data["ViolationTargetDescription"]
    if data.get("ConflictingPriority") is not None:
        out["conflicting_priority"] = data["ConflictingPriority"]
    else:
        out["conflicting_priority"] = 0
    if data.get("ConflictingPolicyId") is not None:
        out["conflicting_policy_id"] = data["ConflictingPolicyId"]
    if data.get("UnavailablePriorities") is not None:
        import capo_fms.types.dns_rule_group_priorities

        out["unavailable_priorities"] = (
            capo_fms.types.dns_rule_group_priorities.deserialize_cbor(
                data["UnavailablePriorities"]
            )
        )
    return out
