"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateCostCategoryDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.cost_category_rule_version
    import capo_cost_explorer.types.cost_category_rules_list
    import capo_cost_explorer.types.cost_category_split_charge_rules_list
    import capo_cost_explorer.types.cost_category_value
    import capo_cost_explorer.types.zoned_date_time


class UpdateCostCategoryDefinitionRequest(TypedDict, closed=True):
    cost_category_arn: "capo_cost_explorer.types.arn.Arn"
    """<p>The unique identifier for your cost category.</p>"""
    effective_start: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The cost category's effective start date. It can only be a billing start date (first day of the month). If the date isn't provided, it's the first day of the current month. Dates can't be before the previous twelve months, or in the future.</p>"""
    rule_version: (
        "capo_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion"
    )
    rules: "capo_cost_explorer.types.cost_category_rules_list.CostCategoryRulesList"
    """<p>The <code>Expression</code> object used to categorize costs. For more information, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html">CostCategoryRule </a>. </p>"""
    default_value: NotRequired[
        "capo_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]
    split_charge_rules: NotRequired[
        "capo_cost_explorer.types.cost_category_split_charge_rules_list.CostCategorySplitChargeRulesList"
    ]
    """<p> The split charge rules used to allocate your charges between your cost category values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCostCategoryDefinitionRequest) -> dict:
    out: dict = {}
    out["CostCategoryArn"] = value["cost_category_arn"]
    if "effective_start" in value:
        out["EffectiveStart"] = value["effective_start"]
    import capo_cost_explorer.types.cost_category_rule_version

    out["RuleVersion"] = (
        capo_cost_explorer.types.cost_category_rule_version.serialize_aws_json_1_1(
            value["rule_version"]
        )
    )
    import capo_cost_explorer.types.cost_category_rules_list

    out["Rules"] = (
        capo_cost_explorer.types.cost_category_rules_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "split_charge_rules" in value:
        import capo_cost_explorer.types.cost_category_split_charge_rules_list

        out["SplitChargeRules"] = (
            capo_cost_explorer.types.cost_category_split_charge_rules_list.serialize_aws_json_1_1(
                value["split_charge_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCostCategoryDefinitionRequest:
    out: UpdateCostCategoryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CostCategoryArn") is not None:
        out["cost_category_arn"] = data["CostCategoryArn"]
    else:
        raise DeserializationError(
            "UpdateCostCategoryDefinitionRequest.cost_category_arn required"
        )
    if data.get("EffectiveStart") is not None:
        out["effective_start"] = data["EffectiveStart"]
    if data.get("RuleVersion") is not None:
        import capo_cost_explorer.types.cost_category_rule_version

        out["rule_version"] = (
            capo_cost_explorer.types.cost_category_rule_version.deserialize_aws_json_1_1(
                data["RuleVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCostCategoryDefinitionRequest.rule_version required"
        )
    if data.get("Rules") is not None:
        import capo_cost_explorer.types.cost_category_rules_list

        out["rules"] = (
            capo_cost_explorer.types.cost_category_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("UpdateCostCategoryDefinitionRequest.rules required")
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("SplitChargeRules") is not None:
        import capo_cost_explorer.types.cost_category_split_charge_rules_list

        out["split_charge_rules"] = (
            capo_cost_explorer.types.cost_category_split_charge_rules_list.deserialize_aws_json_1_1(
                data["SplitChargeRules"]
            )
        )
    return out
