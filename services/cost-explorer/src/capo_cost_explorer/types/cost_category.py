"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.cost_category_name
    import capo_cost_explorer.types.cost_category_processing_status_list
    import capo_cost_explorer.types.cost_category_rule_version
    import capo_cost_explorer.types.cost_category_rules_list
    import capo_cost_explorer.types.cost_category_split_charge_rules_list
    import capo_cost_explorer.types.cost_category_value
    import capo_cost_explorer.types.zoned_date_time


class CostCategory(TypedDict, closed=True):
    cost_category_arn: "capo_cost_explorer.types.arn.Arn"
    """<p>The unique identifier for your cost category. </p>"""
    effective_start: "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    """<p>The effective start date of your cost category.</p>"""
    effective_end: NotRequired["capo_cost_explorer.types.zoned_date_time.ZonedDateTime"]
    """<p>The effective end date of your cost category.</p>"""
    name: "capo_cost_explorer.types.cost_category_name.CostCategoryName"
    rule_version: (
        "capo_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion"
    )
    rules: "capo_cost_explorer.types.cost_category_rules_list.CostCategoryRulesList"
    """<p>The rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that cost category value. </p>"""
    split_charge_rules: NotRequired[
        "capo_cost_explorer.types.cost_category_split_charge_rules_list.CostCategorySplitChargeRulesList"
    ]
    """<p> The split charge rules that are used to allocate your charges between your cost category values. </p>"""
    processing_status: NotRequired[
        "capo_cost_explorer.types.cost_category_processing_status_list.CostCategoryProcessingStatusList"
    ]
    """<p>The list of processing statuses for Cost Management products for a specific cost category. </p>"""
    default_value: NotRequired[
        "capo_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategory) -> dict:
    out: dict = {}
    out["CostCategoryArn"] = value["cost_category_arn"]
    out["EffectiveStart"] = value["effective_start"]
    if "effective_end" in value:
        out["EffectiveEnd"] = value["effective_end"]
    out["Name"] = value["name"]
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
    if "split_charge_rules" in value:
        import capo_cost_explorer.types.cost_category_split_charge_rules_list

        out["SplitChargeRules"] = (
            capo_cost_explorer.types.cost_category_split_charge_rules_list.serialize_aws_json_1_1(
                value["split_charge_rules"]
            )
        )
    if "processing_status" in value:
        import capo_cost_explorer.types.cost_category_processing_status_list

        out["ProcessingStatus"] = (
            capo_cost_explorer.types.cost_category_processing_status_list.serialize_aws_json_1_1(
                value["processing_status"]
            )
        )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategory:
    out: CostCategory = {}  # type: ignore[typeddict-item]
    if data.get("CostCategoryArn") is not None:
        out["cost_category_arn"] = data["CostCategoryArn"]
    else:
        out["cost_category_arn"] = ""
    if data.get("EffectiveStart") is not None:
        out["effective_start"] = data["EffectiveStart"]
    else:
        out["effective_start"] = ""
    if data.get("EffectiveEnd") is not None:
        out["effective_end"] = data["EffectiveEnd"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RuleVersion") is not None:
        import capo_cost_explorer.types.cost_category_rule_version

        out["rule_version"] = (
            capo_cost_explorer.types.cost_category_rule_version.deserialize_aws_json_1_1(
                data["RuleVersion"]
            )
        )
    else:
        import typing

        out["rule_version"] = typing.cast(
            "capo_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion",
            "",
        )
    if data.get("Rules") is not None:
        import capo_cost_explorer.types.cost_category_rules_list

        out["rules"] = (
            capo_cost_explorer.types.cost_category_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        out["rules"] = []
    if data.get("SplitChargeRules") is not None:
        import capo_cost_explorer.types.cost_category_split_charge_rules_list

        out["split_charge_rules"] = (
            capo_cost_explorer.types.cost_category_split_charge_rules_list.deserialize_aws_json_1_1(
                data["SplitChargeRules"]
            )
        )
    if data.get("ProcessingStatus") is not None:
        import capo_cost_explorer.types.cost_category_processing_status_list

        out["processing_status"] = (
            capo_cost_explorer.types.cost_category_processing_status_list.deserialize_aws_json_1_1(
                data["ProcessingStatus"]
            )
        )
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    return out
