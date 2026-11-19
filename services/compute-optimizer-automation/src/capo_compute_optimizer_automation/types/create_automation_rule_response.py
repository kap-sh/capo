"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#CreateAutomationRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.criteria
    import capo_compute_optimizer_automation.types.organization_configuration
    import capo_compute_optimizer_automation.types.recommended_action_type_list
    import capo_compute_optimizer_automation.types.rule_arn
    import capo_compute_optimizer_automation.types.rule_id
    import capo_compute_optimizer_automation.types.rule_name
    import capo_compute_optimizer_automation.types.rule_status
    import capo_compute_optimizer_automation.types.rule_type
    import capo_compute_optimizer_automation.types.schedule
    import capo_compute_optimizer_automation.types.tag_list


class CreateAutomationRuleResponse(TypedDict, closed=True):
    rule_arn: NotRequired["capo_compute_optimizer_automation.types.rule_arn.RuleArn"]
    """<p> The Amazon Resource Name (ARN) of the created rule. </p>"""
    rule_id: NotRequired["capo_compute_optimizer_automation.types.rule_id.RuleId"]
    """<p> The unique identifier of the created rule. </p>"""
    name: NotRequired["capo_compute_optimizer_automation.types.rule_name.RuleName"]
    """<p>The name of the automation rule. Must be 1-128 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""
    description: NotRequired["str"]
    """<p>A description of the automation rule. Can be up to 1024 characters long and contain alphanumeric characters, underscores, hyphens, spaces, and certain special characters.</p>"""
    rule_type: NotRequired["capo_compute_optimizer_automation.types.rule_type.RuleType"]
    """<p>The type of automation rule. Can be either OrganizationRule for organization-wide rules or AccountRule for account-specific rules.</p>"""
    rule_revision: NotRequired["int"]
    """<p>The revision number of the automation rule. This is incremented each time the rule is updated.</p>"""
    organization_configuration: NotRequired[
        "capo_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>Configuration settings for organization-wide rules, including rule application order and target account IDs.</p>"""
    priority: NotRequired["str"]
    """<p>The priority level of the automation rule, used to determine execution order when multiple rules apply to the same resource.</p>"""
    recommended_action_types: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    ]
    """<p>List of recommended action types that this rule can execute, such as SnapshotAndDeleteUnattachedEbsVolume or UpgradeEbsVolumeType.</p>"""
    criteria: NotRequired["capo_compute_optimizer_automation.types.criteria.Criteria"]
    schedule: NotRequired["capo_compute_optimizer_automation.types.schedule.Schedule"]
    """<p>The schedule configuration for when the automation rule should execute, including cron expression, timezone, and execution window.</p>"""
    status: NotRequired[
        "capo_compute_optimizer_automation.types.rule_status.RuleStatus"
    ]
    """<p>The current status of the automation rule. Can be Active or Inactive.</p>"""
    tags: NotRequired["capo_compute_optimizer_automation.types.tag_list.TagList"]
    """<p>A list of key-value pairs used to categorize and organize the automation rule. Maximum of 200 tags allowed.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutomationRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
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
    if "rule_revision" in value:
        out["ruleRevision"] = value["rule_revision"]
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
    if "tags" in value:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            capo_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "created_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutomationRuleResponse:
    out: CreateAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
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
    if data.get("ruleRevision") is not None:
        out["rule_revision"] = data["ruleRevision"]
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
    if data.get("tags") is not None:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            capo_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if data.get("createdTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAutomationRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "rule_type" in value:
        import capo_compute_optimizer_automation.types.rule_type

        out["ruleType"] = (
            capo_compute_optimizer_automation.types.rule_type.serialize_cbor(
                value["rule_type"]
            )
        )
    if "rule_revision" in value:
        out["ruleRevision"] = value["rule_revision"]
    if "organization_configuration" in value:
        import capo_compute_optimizer_automation.types.organization_configuration

        out["organizationConfiguration"] = (
            capo_compute_optimizer_automation.types.organization_configuration.serialize_cbor(
                value["organization_configuration"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "recommended_action_types" in value:
        import capo_compute_optimizer_automation.types.recommended_action_type_list

        out["recommendedActionTypes"] = (
            capo_compute_optimizer_automation.types.recommended_action_type_list.serialize_cbor(
                value["recommended_action_types"]
            )
        )
    if "criteria" in value:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.serialize_cbor(
                value["criteria"]
            )
        )
    if "schedule" in value:
        import capo_compute_optimizer_automation.types.schedule

        out["schedule"] = (
            capo_compute_optimizer_automation.types.schedule.serialize_cbor(
                value["schedule"]
            )
        )
    if "status" in value:
        import capo_compute_optimizer_automation.types.rule_status

        out["status"] = (
            capo_compute_optimizer_automation.types.rule_status.serialize_cbor(
                value["status"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = capo_compute_optimizer_automation.types.tag_list.serialize_cbor(
            value["tags"]
        )
    if "created_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateAutomationRuleResponse:
    out: CreateAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ruleType") is not None:
        import capo_compute_optimizer_automation.types.rule_type

        out["rule_type"] = (
            capo_compute_optimizer_automation.types.rule_type.deserialize_cbor(
                data["ruleType"]
            )
        )
    if data.get("ruleRevision") is not None:
        out["rule_revision"] = data["ruleRevision"]
    if data.get("organizationConfiguration") is not None:
        import capo_compute_optimizer_automation.types.organization_configuration

        out["organization_configuration"] = (
            capo_compute_optimizer_automation.types.organization_configuration.deserialize_cbor(
                data["organizationConfiguration"]
            )
        )
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("recommendedActionTypes") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_type_list

        out["recommended_action_types"] = (
            capo_compute_optimizer_automation.types.recommended_action_type_list.deserialize_cbor(
                data["recommendedActionTypes"]
            )
        )
    if data.get("criteria") is not None:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.deserialize_cbor(
                data["criteria"]
            )
        )
    if data.get("schedule") is not None:
        import capo_compute_optimizer_automation.types.schedule

        out["schedule"] = (
            capo_compute_optimizer_automation.types.schedule.deserialize_cbor(
                data["schedule"]
            )
        )
    if data.get("status") is not None:
        import capo_compute_optimizer_automation.types.rule_status

        out["status"] = (
            capo_compute_optimizer_automation.types.rule_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = capo_compute_optimizer_automation.types.tag_list.deserialize_cbor(
            data["tags"]
        )
    if data.get("createdTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["createdTimestamp"]
            )
        )
    return out
