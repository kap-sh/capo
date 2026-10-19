"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UpdateAutomationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.criteria
    import capo_compute_optimizer_automation.types.organization_configuration
    import capo_compute_optimizer_automation.types.recommended_action_type_list
    import capo_compute_optimizer_automation.types.rule_arn
    import capo_compute_optimizer_automation.types.rule_description
    import capo_compute_optimizer_automation.types.rule_name
    import capo_compute_optimizer_automation.types.rule_status
    import capo_compute_optimizer_automation.types.rule_type
    import capo_compute_optimizer_automation.types.schedule


class UpdateAutomationRuleRequest(TypedDict, closed=True):
    rule_arn: "capo_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the rule to update. </p>"""
    rule_revision: "int"
    """<p> The revision number of the rule to update. </p>"""
    name: NotRequired["capo_compute_optimizer_automation.types.rule_name.RuleName"]
    """<p>The updated name of the automation rule. Must be 1-128 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""
    description: NotRequired[
        "capo_compute_optimizer_automation.types.rule_description.RuleDescription"
    ]
    """<p>The updated description of the automation rule. Can be up to 1024 characters long and contain alphanumeric characters, underscores, hyphens, spaces, and certain special characters.</p>"""
    rule_type: NotRequired["capo_compute_optimizer_automation.types.rule_type.RuleType"]
    """<p>The updated type of automation rule. Can be either OrganizationRule for organization-wide rules or AccountRule for account-specific rules.</p>"""
    organization_configuration: NotRequired[
        "capo_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>Updated configuration settings for organization-wide rules, including rule application order and target account IDs.</p>"""
    priority: NotRequired["str"]
    """<p>The updated priority level of the automation rule, used to determine execution order when multiple rules apply to the same resource.</p>"""
    recommended_action_types: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    ]
    """<p>Updated list of recommended action types that this rule can execute, such as SnapshotAndDeleteUnattachedEbsVolume or UpgradeEbsVolumeType.</p>"""
    criteria: NotRequired["capo_compute_optimizer_automation.types.criteria.Criteria"]
    schedule: NotRequired["capo_compute_optimizer_automation.types.schedule.Schedule"]
    """<p>The updated schedule configuration for when the automation rule should execute, including cron expression, timezone, and execution window.</p>"""
    status: NotRequired[
        "capo_compute_optimizer_automation.types.rule_status.RuleStatus"
    ]
    """<p>The updated status of the automation rule. Can be Active or Inactive.</p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutomationRuleRequest) -> dict:
    out: dict = {}
    out["ruleArn"] = value["rule_arn"]
    out["ruleRevision"] = value["rule_revision"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "rule_type" in value:
        import capo_compute_optimizer_automation.types.rule_type

        out["ruleType"] = (
            capo_compute_optimizer_automation.types.rule_type.serialize_aws_json_1_0(
                value["rule_type"]
            )
        )
    if "organization_configuration" in value:
        import capo_compute_optimizer_automation.types.organization_configuration

        out["organizationConfiguration"] = (
            capo_compute_optimizer_automation.types.organization_configuration.serialize_aws_json_1_0(
                value["organization_configuration"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "recommended_action_types" in value:
        import capo_compute_optimizer_automation.types.recommended_action_type_list

        out["recommendedActionTypes"] = (
            capo_compute_optimizer_automation.types.recommended_action_type_list.serialize_aws_json_1_0(
                value["recommended_action_types"]
            )
        )
    if "criteria" in value:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.serialize_aws_json_1_0(
                value["criteria"]
            )
        )
    if "schedule" in value:
        import capo_compute_optimizer_automation.types.schedule

        out["schedule"] = (
            capo_compute_optimizer_automation.types.schedule.serialize_aws_json_1_0(
                value["schedule"]
            )
        )
    if "status" in value:
        import capo_compute_optimizer_automation.types.rule_status

        out["status"] = (
            capo_compute_optimizer_automation.types.rule_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAutomationRuleRequest:
    out: UpdateAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    else:
        out["rule_arn"] = ""
    if data.get("ruleRevision") is not None:
        out["rule_revision"] = data["ruleRevision"]
    else:
        out["rule_revision"] = 0
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ruleType") is not None:
        import capo_compute_optimizer_automation.types.rule_type

        out["rule_type"] = (
            capo_compute_optimizer_automation.types.rule_type.deserialize_aws_json_1_0(
                data["ruleType"]
            )
        )
    if data.get("organizationConfiguration") is not None:
        import capo_compute_optimizer_automation.types.organization_configuration

        out["organization_configuration"] = (
            capo_compute_optimizer_automation.types.organization_configuration.deserialize_aws_json_1_0(
                data["organizationConfiguration"]
            )
        )
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("recommendedActionTypes") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_type_list

        out["recommended_action_types"] = (
            capo_compute_optimizer_automation.types.recommended_action_type_list.deserialize_aws_json_1_0(
                data["recommendedActionTypes"]
            )
        )
    if data.get("criteria") is not None:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.deserialize_aws_json_1_0(
                data["criteria"]
            )
        )
    if data.get("schedule") is not None:
        import capo_compute_optimizer_automation.types.schedule

        out["schedule"] = (
            capo_compute_optimizer_automation.types.schedule.deserialize_aws_json_1_0(
                data["schedule"]
            )
        )
    if data.get("status") is not None:
        import capo_compute_optimizer_automation.types.rule_status

        out["status"] = (
            capo_compute_optimizer_automation.types.rule_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
