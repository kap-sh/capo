"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_split_charge_method
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameters_list
    import capo_cost_explorer.types.cost_category_split_charge_rule_targets_list
    import capo_cost_explorer.types.generic_string


class CostCategorySplitChargeRule(TypedDict, closed=True):
    source: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The cost category value that you want to split. That value can't be used as a source or a target in other split charge rules. To indicate uncategorized costs, you can use an empty string as the source.</p>"""
    targets: "capo_cost_explorer.types.cost_category_split_charge_rule_targets_list.CostCategorySplitChargeRuleTargetsList"
    """<p>The cost category values that you want to split costs across. These values can't be used as a source in other split charge rules. </p>"""
    method: "capo_cost_explorer.types.cost_category_split_charge_method.CostCategorySplitChargeMethod"
    """<p>The method that's used to define how to split your source costs across your targets. </p> <p> <code>Proportional</code> - Allocates charges across your targets based on the proportional weighted cost of each target.</p> <p> <code>Fixed</code> - Allocates charges across your targets based on your defined allocation percentage.</p> <p>><code>Even</code> - Allocates costs evenly across all targets.</p>"""
    parameters: NotRequired[
        "capo_cost_explorer.types.cost_category_split_charge_rule_parameters_list.CostCategorySplitChargeRuleParametersList"
    ]
    """<p>The parameters for a split charge method. This is only required for the <code>FIXED</code> method. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRule) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    import capo_cost_explorer.types.cost_category_split_charge_rule_targets_list

    out["Targets"] = (
        capo_cost_explorer.types.cost_category_split_charge_rule_targets_list.serialize_aws_json_1_1(
            value["targets"]
        )
    )
    import capo_cost_explorer.types.cost_category_split_charge_method

    out["Method"] = (
        capo_cost_explorer.types.cost_category_split_charge_method.serialize_aws_json_1_1(
            value["method"]
        )
    )
    if "parameters" in value:
        import capo_cost_explorer.types.cost_category_split_charge_rule_parameters_list

        out["Parameters"] = (
            capo_cost_explorer.types.cost_category_split_charge_rule_parameters_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategorySplitChargeRule:
    out: CostCategorySplitChargeRule = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        out["source"] = ""
    if data.get("Targets") is not None:
        import capo_cost_explorer.types.cost_category_split_charge_rule_targets_list

        out["targets"] = (
            capo_cost_explorer.types.cost_category_split_charge_rule_targets_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    else:
        out["targets"] = []
    if data.get("Method") is not None:
        import capo_cost_explorer.types.cost_category_split_charge_method

        out["method"] = (
            capo_cost_explorer.types.cost_category_split_charge_method.deserialize_aws_json_1_1(
                data["Method"]
            )
        )
    else:
        import typing

        out["method"] = typing.cast(
            "capo_cost_explorer.types.cost_category_split_charge_method.CostCategorySplitChargeMethod",
            "",
        )
    if data.get("Parameters") is not None:
        import capo_cost_explorer.types.cost_category_split_charge_rule_parameters_list

        out["parameters"] = (
            capo_cost_explorer.types.cost_category_split_charge_rule_parameters_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
