"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.action_list
    import capo_securityhub.types.automation_rules_finding_filters
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.rule_order_value
    import capo_securityhub.types.rule_status
    import capo_securityhub.types.timestamp


class AutomationRulesConfig(TypedDict, closed=True):
    rule_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of a rule. </p>"""
    rule_status: NotRequired["capo_securityhub.types.rule_status.RuleStatus"]
    """<p> Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created. </p>"""
    rule_order: NotRequired["capo_securityhub.types.rule_order_value.RuleOrderValue"]
    """<p> An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first. </p>"""
    rule_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the rule. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> A description of the rule. </p>"""
    is_terminal: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal. </p>"""
    criteria: NotRequired[
        "capo_securityhub.types.automation_rules_finding_filters.AutomationRulesFindingFilters"
    ]
    """<p> A set of <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html">Amazon Web Services Security Finding Format</a> finding field attributes and corresponding expected values that Security Hub CSPM uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub CSPM applies the rule action to the finding. </p>"""
    actions: NotRequired["capo_securityhub.types.action_list.ActionList"]
    """<p> One or more actions to update finding fields if a finding matches the defined criteria of the rule. </p>"""
    created_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> A timestamp that indicates when the rule was created. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> A timestamp that indicates when the rule was most recently updated. </p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    created_by: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The principal that created a rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesConfig) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "rule_status" in value:
        import capo_securityhub.types.rule_status

        out["RuleStatus"] = capo_securityhub.types.rule_status.serialize_json(
            value["rule_status"]
        )
    if "rule_order" in value:
        out["RuleOrder"] = value["rule_order"]
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "is_terminal" in value:
        out["IsTerminal"] = value["is_terminal"]
    if "criteria" in value:
        import capo_securityhub.types.automation_rules_finding_filters

        out["Criteria"] = (
            capo_securityhub.types.automation_rules_finding_filters.serialize_json(
                value["criteria"]
            )
        )
    if "actions" in value:
        import capo_securityhub.types.action_list

        out["Actions"] = capo_securityhub.types.action_list.serialize_json(
            value["actions"]
        )
    if "created_at" in value:
        import capo_securityhub.types.timestamp

        out["CreatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> AutomationRulesConfig:
    out: AutomationRulesConfig = {}  # type: ignore[typeddict-item]
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    if data.get("RuleStatus") is not None:
        import capo_securityhub.types.rule_status

        out["rule_status"] = capo_securityhub.types.rule_status.deserialize_json(
            data["RuleStatus"]
        )
    if data.get("RuleOrder") is not None:
        out["rule_order"] = data["RuleOrder"]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IsTerminal") is not None:
        out["is_terminal"] = data["IsTerminal"]
    if data.get("Criteria") is not None:
        import capo_securityhub.types.automation_rules_finding_filters

        out["criteria"] = (
            capo_securityhub.types.automation_rules_finding_filters.deserialize_json(
                data["Criteria"]
            )
        )
    if data.get("Actions") is not None:
        import capo_securityhub.types.action_list

        out["actions"] = capo_securityhub.types.action_list.deserialize_json(
            data["Actions"]
        )
    if data.get("CreatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["created_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    return out
