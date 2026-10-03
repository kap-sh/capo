"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_inherited_value_dimension
    import capo_cost_explorer.types.cost_category_rule_type
    import capo_cost_explorer.types.cost_category_value
    import capo_cost_explorer.types.expression


class CostCategoryRule(TypedDict, closed=True):
    value: NotRequired["capo_cost_explorer.types.cost_category_value.CostCategoryValue"]
    rule: NotRequired["capo_cost_explorer.types.expression.Expression"]
    """<p>An <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object used to categorize costs. This supports dimensions, tags, and nested expressions. Currently the only dimensions supported are <code>LINKED_ACCOUNT</code>, <code>SERVICE_CODE</code>, <code>RECORD_TYPE</code>, <code>LINKED_ACCOUNT_NAME</code>, <code>REGION</code>, and <code>USAGE_TYPE</code>.</p> <p> <code>RECORD_TYPE</code> is a dimension used for Cost Explorer APIs, and is also supported for cost category expressions. This dimension uses different terms, depending on whether you're using the console or API/JSON editor. For a detailed comparison, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html#cost-categories-terms">Term Comparisons</a> in the <i>Billing and Cost Management User Guide</i>.</p>"""
    inherited_value: NotRequired[
        "capo_cost_explorer.types.cost_category_inherited_value_dimension.CostCategoryInheritedValueDimension"
    ]
    """<p>The value the line item is categorized as if the line item contains the matched dimension.</p>"""
    type: NotRequired[
        "capo_cost_explorer.types.cost_category_rule_type.CostCategoryRuleType"
    ]
    """<p>You can define the <code>CostCategoryRule</code> rule type as either <code>REGULAR</code> or <code>INHERITED_VALUE</code>. The <code>INHERITED_VALUE</code> rule type adds the flexibility to define a rule that dynamically inherits the cost category value. This value is from the dimension value that's defined by <code>CostCategoryInheritedValueDimension</code>. For example, suppose that you want to costs to be dynamically grouped based on the value of a specific tag key. First, choose an inherited value rule type, and then choose the tag dimension and specify the tag key to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryRule) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "rule" in value:
        import capo_cost_explorer.types.expression

        out["Rule"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["rule"]
        )
    if "inherited_value" in value:
        import capo_cost_explorer.types.cost_category_inherited_value_dimension

        out["InheritedValue"] = (
            capo_cost_explorer.types.cost_category_inherited_value_dimension.serialize_aws_json_1_1(
                value["inherited_value"]
            )
        )
    if "type" in value:
        import capo_cost_explorer.types.cost_category_rule_type

        out["Type"] = (
            capo_cost_explorer.types.cost_category_rule_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategoryRule:
    out: CostCategoryRule = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Rule") is not None:
        import capo_cost_explorer.types.expression

        out["rule"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Rule"]
        )
    if data.get("InheritedValue") is not None:
        import capo_cost_explorer.types.cost_category_inherited_value_dimension

        out["inherited_value"] = (
            capo_cost_explorer.types.cost_category_inherited_value_dimension.deserialize_aws_json_1_1(
                data["InheritedValue"]
            )
        )
    if data.get("Type") is not None:
        import capo_cost_explorer.types.cost_category_rule_type

        out["type"] = (
            capo_cost_explorer.types.cost_category_rule_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
