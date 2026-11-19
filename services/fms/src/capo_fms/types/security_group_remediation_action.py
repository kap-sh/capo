"""Generated from Smithy shape ``com.amazonaws.fms#SecurityGroupRemediationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.remediation_action_description
    import capo_fms.types.remediation_action_type
    import capo_fms.types.security_group_rule_description


class SecurityGroupRemediationAction(TypedDict, closed=True):
    remediation_action_type: NotRequired[
        "capo_fms.types.remediation_action_type.RemediationActionType"
    ]
    """<p>The remediation action that will be performed.</p>"""
    description: NotRequired[
        "capo_fms.types.remediation_action_description.RemediationActionDescription"
    ]
    """<p>Brief description of the action that will be performed.</p>"""
    remediation_result: NotRequired[
        "capo_fms.types.security_group_rule_description.SecurityGroupRuleDescription"
    ]
    """<p>The final state of the rule specified in the <code>ViolationTarget</code> after it is remediated.</p>"""
    is_default_action: "capo_fms.types.boolean.Boolean"
    """<p>Indicates if the current action is the default action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupRemediationAction) -> dict:
    out: dict = {}
    if "remediation_action_type" in value:
        import capo_fms.types.remediation_action_type

        out["RemediationActionType"] = (
            capo_fms.types.remediation_action_type.serialize_aws_json_1_1(
                value["remediation_action_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "remediation_result" in value:
        import capo_fms.types.security_group_rule_description

        out["RemediationResult"] = (
            capo_fms.types.security_group_rule_description.serialize_aws_json_1_1(
                value["remediation_result"]
            )
        )
    out["IsDefaultAction"] = value.get("is_default_action", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityGroupRemediationAction:
    out: SecurityGroupRemediationAction = {}  # type: ignore[typeddict-item]
    if data.get("RemediationActionType") is not None:
        import capo_fms.types.remediation_action_type

        out["remediation_action_type"] = (
            capo_fms.types.remediation_action_type.deserialize_aws_json_1_1(
                data["RemediationActionType"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RemediationResult") is not None:
        import capo_fms.types.security_group_rule_description

        out["remediation_result"] = (
            capo_fms.types.security_group_rule_description.deserialize_aws_json_1_1(
                data["RemediationResult"]
            )
        )
    if data.get("IsDefaultAction") is not None:
        out["is_default_action"] = data["IsDefaultAction"]
    else:
        out["is_default_action"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupRemediationAction) -> dict:
    out: dict = {}
    if "remediation_action_type" in value:
        import capo_fms.types.remediation_action_type

        out["RemediationActionType"] = (
            capo_fms.types.remediation_action_type.serialize_cbor(
                value["remediation_action_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "remediation_result" in value:
        import capo_fms.types.security_group_rule_description

        out["RemediationResult"] = (
            capo_fms.types.security_group_rule_description.serialize_cbor(
                value["remediation_result"]
            )
        )
    out["IsDefaultAction"] = value.get("is_default_action", False)
    return out


def deserialize_cbor(data: dict) -> SecurityGroupRemediationAction:
    out: SecurityGroupRemediationAction = {}  # type: ignore[typeddict-item]
    if data.get("RemediationActionType") is not None:
        import capo_fms.types.remediation_action_type

        out["remediation_action_type"] = (
            capo_fms.types.remediation_action_type.deserialize_cbor(
                data["RemediationActionType"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RemediationResult") is not None:
        import capo_fms.types.security_group_rule_description

        out["remediation_result"] = (
            capo_fms.types.security_group_rule_description.deserialize_cbor(
                data["RemediationResult"]
            )
        )
    if data.get("IsDefaultAction") is not None:
        out["is_default_action"] = data["IsDefaultAction"]
    else:
        out["is_default_action"] = False
    return out
