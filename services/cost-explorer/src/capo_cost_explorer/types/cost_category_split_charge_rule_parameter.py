"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRuleParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameter_type
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list


class CostCategorySplitChargeRuleParameter(TypedDict, closed=True):
    type: "capo_cost_explorer.types.cost_category_split_charge_rule_parameter_type.CostCategorySplitChargeRuleParameterType"
    """<p>The parameter type. </p>"""
    values: "capo_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list.CostCategorySplitChargeRuleParameterValuesList"
    """<p>The parameter values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRuleParameter) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameter_type

    out["Type"] = (
        capo_cost_explorer.types.cost_category_split_charge_rule_parameter_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list

    out["Values"] = (
        capo_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategorySplitChargeRuleParameter:
    out: CostCategorySplitChargeRuleParameter = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_cost_explorer.types.cost_category_split_charge_rule_parameter_type

        out["type"] = (
            capo_cost_explorer.types.cost_category_split_charge_rule_parameter_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cost_explorer.types.cost_category_split_charge_rule_parameter_type.CostCategorySplitChargeRuleParameterType",
            "",
        )
    if data.get("Values") is not None:
        import capo_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list

        out["values"] = (
            capo_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
