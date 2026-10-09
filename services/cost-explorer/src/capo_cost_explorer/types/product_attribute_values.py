"""Generated from Smithy shape ``com.amazonaws.costexplorer#ProductAttributeValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.match_options
    import capo_cost_explorer.types.product_attribute_name
    import capo_cost_explorer.types.product_attribute_value_list


class ProductAttributeValues(TypedDict, closed=True):
    key: "capo_cost_explorer.types.product_attribute_name.ProductAttributeName"
    """<p>The name of the product attribute, such as <code>model</code>. The keys that are available depend on the service. For the keys of each supported service, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ProductAttributeValues.html"> <code>ProductAttributeValues</code> </a>.</p> <p>Keys are case-sensitive. A key that doesn't exist doesn't return an error: <code>EQUALS</code> matches no costs, and <code>ABSENT</code> matches all costs of supported services.</p>"""
    values: NotRequired[
        "capo_cost_explorer.types.product_attribute_value_list.ProductAttributeValueList"
    ]
    """<p>The specific values of the product attribute, such as <code>Claude Sonnet 5</code> for the <code>model</code> key. Values are matched exactly, including case. To list the values of a key, use <code>GetDimensionValues</code> with <code>Dimension</code> set to <code>PRODUCT_ATTRIBUTE</code> and <code>DimensionKey</code> set to the key.</p> <p>To match costs that have no value for the key, set <code>MatchOptions</code> to <code>ABSENT</code> and omit <code>Values</code>. Otherwise, <code>Values</code> is required.</p>"""
    match_options: NotRequired["capo_cost_explorer.types.match_options.MatchOptions"]
    """<p>The match options that you can use to filter your results. Valid values:</p> <ul> <li> <p> <code>EQUALS</code> - Matches the values that you specify.</p> </li> <li> <p> <code>ABSENT</code> - Matches costs that have no value for the key. Omit <code>Values</code>.</p> </li> <li> <p> <code>CASE_SENSITIVE</code> - Use only with <code>EQUALS</code>. Values are always matched case-sensitively.</p> </li> </ul> <p>Default values are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductAttributeValues) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "values" in value:
        import capo_cost_explorer.types.product_attribute_value_list

        out["Values"] = (
            capo_cost_explorer.types.product_attribute_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    if "match_options" in value:
        import capo_cost_explorer.types.match_options

        out["MatchOptions"] = (
            capo_cost_explorer.types.match_options.serialize_aws_json_1_1(
                value["match_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductAttributeValues:
    out: ProductAttributeValues = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ProductAttributeValues.key required")
    if data.get("Values") is not None:
        import capo_cost_explorer.types.product_attribute_value_list

        out["values"] = (
            capo_cost_explorer.types.product_attribute_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    if data.get("MatchOptions") is not None:
        import capo_cost_explorer.types.match_options

        out["match_options"] = (
            capo_cost_explorer.types.match_options.deserialize_aws_json_1_1(
                data["MatchOptions"]
            )
        )
    return out
