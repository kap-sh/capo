"""Generated from Smithy shape ``com.amazonaws.fms#AwsVPCSecurityGroupViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.partial_matches
    import capo_fms.types.security_group_remediation_actions
    import capo_fms.types.violation_target


class AwsVPCSecurityGroupViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>The security group rule that is being evaluated.</p>"""
    violation_target_description: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the security group that violates the policy.</p>"""
    partial_matches: NotRequired["capo_fms.types.partial_matches.PartialMatches"]
    """<p>List of rules specified in the security group of the Firewall Manager policy that partially match the <code>ViolationTarget</code> rule.</p>"""
    possible_security_group_remediation_actions: NotRequired[
        "capo_fms.types.security_group_remediation_actions.SecurityGroupRemediationActions"
    ]
    """<p>Remediation options for the rule specified in the <code>ViolationTarget</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsVPCSecurityGroupViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violation_target_description" in value:
        out["ViolationTargetDescription"] = value["violation_target_description"]
    if "partial_matches" in value:
        import capo_fms.types.partial_matches

        out["PartialMatches"] = capo_fms.types.partial_matches.serialize_aws_json_1_1(
            value["partial_matches"]
        )
    if "possible_security_group_remediation_actions" in value:
        import capo_fms.types.security_group_remediation_actions

        out["PossibleSecurityGroupRemediationActions"] = (
            capo_fms.types.security_group_remediation_actions.serialize_aws_json_1_1(
                value["possible_security_group_remediation_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsVPCSecurityGroupViolation:
    out: AwsVPCSecurityGroupViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("ViolationTargetDescription") is not None:
        out["violation_target_description"] = data["ViolationTargetDescription"]
    if data.get("PartialMatches") is not None:
        import capo_fms.types.partial_matches

        out["partial_matches"] = (
            capo_fms.types.partial_matches.deserialize_aws_json_1_1(
                data["PartialMatches"]
            )
        )
    if data.get("PossibleSecurityGroupRemediationActions") is not None:
        import capo_fms.types.security_group_remediation_actions

        out["possible_security_group_remediation_actions"] = (
            capo_fms.types.security_group_remediation_actions.deserialize_aws_json_1_1(
                data["PossibleSecurityGroupRemediationActions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsVPCSecurityGroupViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "violation_target_description" in value:
        out["ViolationTargetDescription"] = value["violation_target_description"]
    if "partial_matches" in value:
        import capo_fms.types.partial_matches

        out["PartialMatches"] = capo_fms.types.partial_matches.serialize_cbor(
            value["partial_matches"]
        )
    if "possible_security_group_remediation_actions" in value:
        import capo_fms.types.security_group_remediation_actions

        out["PossibleSecurityGroupRemediationActions"] = (
            capo_fms.types.security_group_remediation_actions.serialize_cbor(
                value["possible_security_group_remediation_actions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AwsVPCSecurityGroupViolation:
    out: AwsVPCSecurityGroupViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("ViolationTargetDescription") is not None:
        out["violation_target_description"] = data["ViolationTargetDescription"]
    if data.get("PartialMatches") is not None:
        import capo_fms.types.partial_matches

        out["partial_matches"] = capo_fms.types.partial_matches.deserialize_cbor(
            data["PartialMatches"]
        )
    if data.get("PossibleSecurityGroupRemediationActions") is not None:
        import capo_fms.types.security_group_remediation_actions

        out["possible_security_group_remediation_actions"] = (
            capo_fms.types.security_group_remediation_actions.deserialize_cbor(
                data["PossibleSecurityGroupRemediationActions"]
            )
        )
    return out
