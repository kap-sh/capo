"""Generated from Smithy shape ``com.amazonaws.glue#SearchAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.search_attribute
    import capo_glue.types.search_filter_operator
    import capo_glue.types.search_filter_value


class SearchAttributeFilter(TypedDict, closed=True):
    attribute: "capo_glue.types.search_attribute.SearchAttribute"
    """<p>The attribute name to filter on.</p>"""
    operator: "capo_glue.types.search_filter_operator.SearchFilterOperator"
    """<p>The comparison operator. Valid values are <code>equals</code>, <code>greaterThan</code>, <code>greaterThanOrEquals</code>, <code>lessThan</code>, <code>lessThanOrEquals</code>, and <code>notExists</code>.</p>"""
    value: NotRequired["capo_glue.types.search_filter_value.SearchFilterValue"]
    """<p>The value to compare against.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchAttributeFilter) -> dict:
    out: dict = {}
    out["Attribute"] = value["attribute"]
    import capo_glue.types.search_filter_operator

    out["Operator"] = capo_glue.types.search_filter_operator.serialize_aws_json_1_1(
        value["operator"]
    )
    if "value" in value:
        import capo_glue.types.search_filter_value

        out["Value"] = capo_glue.types.search_filter_value.serialize_aws_json_1_1(
            value["value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchAttributeFilter:
    out: SearchAttributeFilter = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        out["attribute"] = data["Attribute"]
    else:
        out["attribute"] = ""
    if data.get("Operator") is not None:
        import capo_glue.types.search_filter_operator

        out["operator"] = (
            capo_glue.types.search_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_glue.types.search_filter_operator.SearchFilterOperator", ""
        )
    if data.get("Value") is not None:
        import capo_glue.types.search_filter_value

        out["value"] = capo_glue.types.search_filter_value.deserialize_aws_json_1_1(
            data["Value"]
        )
    return out
