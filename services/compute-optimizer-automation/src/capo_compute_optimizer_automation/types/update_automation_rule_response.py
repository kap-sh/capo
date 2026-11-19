"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UpdateAutomationRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.criteria
    import capo_compute_optimizer_automation.types.organization_configuration
    import capo_compute_optimizer_automation.types.recommended_action_type_list
    import capo_compute_optimizer_automation.types.rule_arn
    import capo_compute_optimizer_automation.types.rule_name
    import capo_compute_optimizer_automation.types.rule_status
    import capo_compute_optimizer_automation.types.rule_type
    import capo_compute_optimizer_automation.types.schedule


class UpdateAutomationRuleResponse(TypedDict, closed=True):
    rule_arn: NotRequired["capo_compute_optimizer_automation.types.rule_arn.RuleArn"]
    """<p> The ARN of the updated rule. </p>"""
    rule_revision: NotRequired["int"]
    """<p> The new revision number of the updated rule. </p>"""
    name: NotRequired["capo_compute_optimizer_automation.types.rule_name.RuleName"]
    """<p>The updated name of the automation rule.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the automation rule.</p>"""
    rule_type: NotRequired["capo_compute_optimizer_automation.types.rule_type.RuleType"]
    """<p>The updated type of automation rule.</p>"""
    organization_configuration: NotRequired[
        "capo_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>The updated organization configuration settings.</p>"""
    priority: NotRequired["str"]
    """<p>The updated priority level of the automation rule.</p>"""
    recommended_action_types: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    ]
    """<p>The updated list of recommended action types.</p>"""
    criteria: NotRequired["capo_compute_optimizer_automation.types.criteria.Criteria"]
    schedule: NotRequired["capo_compute_optimizer_automation.types.schedule.Schedule"]
    """<p>The updated schedule configuration.</p>"""
    status: NotRequired[
        "capo_compute_optimizer_automation.types.rule_status.RuleStatus"
    ]
    """<p>The updated status of the automation rule.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was originally created.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutomationRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule_revision" in value:
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
    if "created_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAutomationRuleResponse:
    out: UpdateAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    if data.get("ruleRevision") is not None:
        out["rule_revision"] = data["ruleRevision"]
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
    if data.get("createdTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdTimestamp"]
            )
        )
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateAutomationRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule_revision" in value:
        out["ruleRevision"] = value["rule_revision"]
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
    if "created_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateAutomationRuleResponse:
    out: UpdateAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    if data.get("ruleRevision") is not None:
        out["rule_revision"] = data["ruleRevision"]
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
    if data.get("createdTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["createdTimestamp"]
            )
        )
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["lastUpdatedTimestamp"]
            )
        )
    return out
