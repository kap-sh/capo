"""Generated from Smithy shape ``com.amazonaws.costexplorer#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_values
    import capo_cost_explorer.types.dimension_values
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.expressions
    import capo_cost_explorer.types.product_attribute_values
    import capo_cost_explorer.types.tag_values

Expression = TypedDict(
    "Expression",
    {
        "or": NotRequired["capo_cost_explorer.types.expressions.Expressions"],
        "and": NotRequired["capo_cost_explorer.types.expressions.Expressions"],
        "not": NotRequired["capo_cost_explorer.types.expression.Expression"],
        "dimensions": NotRequired[
            "capo_cost_explorer.types.dimension_values.DimensionValues"
        ],
        "tags": NotRequired["capo_cost_explorer.types.tag_values.TagValues"],
        "cost_categories": NotRequired[
            "capo_cost_explorer.types.cost_category_values.CostCategoryValues"
        ],
        "product_attributes": NotRequired[
            "capo_cost_explorer.types.product_attribute_values.ProductAttributeValues"
        ],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Expression) -> dict:
    out: dict = {}
    if "or" in value:
        import capo_cost_explorer.types.expressions

        out["Or"] = capo_cost_explorer.types.expressions.serialize_aws_json_1_1(
            value["or"]
        )
    if "and" in value:
        import capo_cost_explorer.types.expressions

        out["And"] = capo_cost_explorer.types.expressions.serialize_aws_json_1_1(
            value["and"]
        )
    if "not" in value:
        import capo_cost_explorer.types.expression

        out["Not"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["not"]
        )
    if "dimensions" in value:
        import capo_cost_explorer.types.dimension_values

        out["Dimensions"] = (
            capo_cost_explorer.types.dimension_values.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "tags" in value:
        import capo_cost_explorer.types.tag_values

        out["Tags"] = capo_cost_explorer.types.tag_values.serialize_aws_json_1_1(
            value["tags"]
        )
    if "cost_categories" in value:
        import capo_cost_explorer.types.cost_category_values

        out["CostCategories"] = (
            capo_cost_explorer.types.cost_category_values.serialize_aws_json_1_1(
                value["cost_categories"]
            )
        )
    if "product_attributes" in value:
        import capo_cost_explorer.types.product_attribute_values

        out["ProductAttributes"] = (
            capo_cost_explorer.types.product_attribute_values.serialize_aws_json_1_1(
                value["product_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if data.get("Or") is not None:
        import capo_cost_explorer.types.expressions

        out["or"] = capo_cost_explorer.types.expressions.deserialize_aws_json_1_1(
            data["Or"]
        )
    if data.get("And") is not None:
        import capo_cost_explorer.types.expressions

        out["and"] = capo_cost_explorer.types.expressions.deserialize_aws_json_1_1(
            data["And"]
        )
    if data.get("Not") is not None:
        import capo_cost_explorer.types.expression

        out["not"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Not"]
        )
    if data.get("Dimensions") is not None:
        import capo_cost_explorer.types.dimension_values

        out["dimensions"] = (
            capo_cost_explorer.types.dimension_values.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_cost_explorer.types.tag_values

        out["tags"] = capo_cost_explorer.types.tag_values.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("CostCategories") is not None:
        import capo_cost_explorer.types.cost_category_values

        out["cost_categories"] = (
            capo_cost_explorer.types.cost_category_values.deserialize_aws_json_1_1(
                data["CostCategories"]
            )
        )
    if data.get("ProductAttributes") is not None:
        import capo_cost_explorer.types.product_attribute_values

        out["product_attributes"] = (
            capo_cost_explorer.types.product_attribute_values.deserialize_aws_json_1_1(
                data["ProductAttributes"]
            )
        )
    return out
