"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#CreateAutomationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.criteria
    import capo_compute_optimizer_automation.types.organization_configuration
    import capo_compute_optimizer_automation.types.recommended_action_type_list
    import capo_compute_optimizer_automation.types.rule_description
    import capo_compute_optimizer_automation.types.rule_name
    import capo_compute_optimizer_automation.types.rule_status
    import capo_compute_optimizer_automation.types.rule_type
    import capo_compute_optimizer_automation.types.schedule
    import capo_compute_optimizer_automation.types.tag_list


class CreateAutomationRuleRequest(TypedDict, closed=True):
    name: "capo_compute_optimizer_automation.types.rule_name.RuleName"
    """<p> The name of the automation rule. </p>"""
    description: NotRequired[
        "capo_compute_optimizer_automation.types.rule_description.RuleDescription"
    ]
    """<p> A description of the automation rule. </p>"""
    rule_type: "capo_compute_optimizer_automation.types.rule_type.RuleType"
    """<p> The type of rule. </p> <note> <p>Only the management account or a delegated administrator can set the ruleType to be OrganizationRule.</p> </note>"""
    organization_configuration: NotRequired[
        "capo_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p> Configuration for organization-level rules. Required for OrganizationRule type. </p>"""
    priority: NotRequired["str"]
    """<p>A string representation of a decimal number between 0 and 1 (having up to 30 digits after the decimal point) that determines the priority of the rule. When multiple rules match the same recommended action, Compute Optimizer assigns the action to the rule with the lowest priority value (highest priority), even if that rule is scheduled to run later than other matching rules. </p>"""
    recommended_action_types: "capo_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    """<p> The types of recommended actions this rule will automate. </p>"""
    criteria: NotRequired["capo_compute_optimizer_automation.types.criteria.Criteria"]
    """<p>A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. </p>"""
    schedule: "capo_compute_optimizer_automation.types.schedule.Schedule"
    """<p> The schedule for when the rule should run. </p>"""
    status: "capo_compute_optimizer_automation.types.rule_status.RuleStatus"
    """<p>The status of the rule </p>"""
    tags: NotRequired["capo_compute_optimizer_automation.types.tag_list.TagList"]
    """<p> The tags to associate with the rule. </p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p> A unique identifier to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutomationRuleRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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
    import capo_compute_optimizer_automation.types.schedule

    out["schedule"] = (
        capo_compute_optimizer_automation.types.schedule.serialize_aws_json_1_0(
            value["schedule"]
        )
    )
    import capo_compute_optimizer_automation.types.rule_status

    out["status"] = (
        capo_compute_optimizer_automation.types.rule_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "tags" in value:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            capo_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutomationRuleRequest:
    out: CreateAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ruleType") is not None:
        import capo_compute_optimizer_automation.types.rule_type

        out["rule_type"] = (
            capo_compute_optimizer_automation.types.rule_type.deserialize_aws_json_1_0(
                data["ruleType"]
            )
        )
    else:
        import typing

        out["rule_type"] = typing.cast(
            "capo_compute_optimizer_automation.types.rule_type.RuleType", ""
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
    else:
        out["recommended_action_types"] = []
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
    else:
        raise DeserializationError("CreateAutomationRuleRequest.schedule required")
    if data.get("status") is not None:
        import capo_compute_optimizer_automation.types.rule_status

        out["status"] = (
            capo_compute_optimizer_automation.types.rule_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_compute_optimizer_automation.types.rule_status.RuleStatus", ""
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            capo_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
