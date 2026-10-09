"""Generated from Smithy shape ``com.amazonaws.budgets#ProductAttributeValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.match_options
    import capo_budgets.types.product_attribute_name
    import capo_budgets.types.values


class ProductAttributeValues(TypedDict, closed=True):
    key: "capo_budgets.types.product_attribute_name.ProductAttributeName"
    """<p>The name of the product attribute to filter on. Valid values are the following:</p> <ul> <li> <p> <code>feature</code> – The feature that was used, such as <code>On-demand Inference</code>.</p> </li> <li> <p> <code>inferenceType</code> – The type of inference usage, such as <code>Input tokens</code> or <code>Output tokens</code>.</p> </li> <li> <p> <code>model</code> – The model, such as <code>Claude Sonnet 5</code> or <code>Claude Haiku 4.5</code>.</p> </li> <li> <p> <code>provider</code> – The model provider, such as <code>Anthropic</code>, <code>Cohere</code>, or <code>Amazon</code>.</p> </li> </ul> <p>Keys are case-sensitive.</p>"""
    values: NotRequired["capo_budgets.types.values.Values"]
    """<p>The specific values of the product attribute, such as <code>Claude Sonnet 5</code> for the <code>model</code> key. Values are matched exactly.</p> <p> <code>Values</code> is required unless <code>MatchOptions</code> is <code>ABSENT</code>. To match costs that have no value for the key, set <code>MatchOptions</code> to <code>ABSENT</code> and omit <code>Values</code>.</p>"""
    match_options: NotRequired["capo_budgets.types.match_options.MatchOptions"]
    """<p>The match options for the <code>ProductAttributes</code> filter. Valid values:</p> <ul> <li> <p> <code>ABSENT</code> – Matches costs that have no value for the attribute.</p> </li> <li> <p> <code>CASE_SENSITIVE</code> – Requires an exact case match.</p> </li> <li> <p> <code>EQUALS</code> – Matches costs where the attribute equals the specified value.</p> </li> </ul> <p>Specify either <code>EQUALS</code> or <code>ABSENT</code>. You can add <code>CASE_SENSITIVE</code> to <code>EQUALS</code>, but you can't use it by itself or with <code>ABSENT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductAttributeValues) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "values" in value:
        import capo_budgets.types.values

        out["Values"] = capo_budgets.types.values.serialize_aws_json_1_1(
            value["values"]
        )
    if "match_options" in value:
        import capo_budgets.types.match_options

        out["MatchOptions"] = capo_budgets.types.match_options.serialize_aws_json_1_1(
            value["match_options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductAttributeValues:
    out: ProductAttributeValues = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ProductAttributeValues.key required")
    if data.get("Values") is not None:
        import capo_budgets.types.values

        out["values"] = capo_budgets.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    if data.get("MatchOptions") is not None:
        import capo_budgets.types.match_options

        out["match_options"] = (
            capo_budgets.types.match_options.deserialize_aws_json_1_1(
                data["MatchOptions"]
            )
        )
    return out
