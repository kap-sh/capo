"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCategoryFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.category_filter_function
    import capo_quicksight.types.category_filter_type
    import capo_quicksight.types.null_filter_type
    import capo_quicksight.types.topic_category_filter_constant


class TopicCategoryFilter(TypedDict, closed=True):
    category_filter_function: NotRequired[
        "capo_quicksight.types.category_filter_function.CategoryFilterFunction"
    ]
    """<p>The category filter function. Valid values for this structure are <code>EXACT</code> and <code>CONTAINS</code>.</p>"""
    category_filter_type: NotRequired[
        "capo_quicksight.types.category_filter_type.CategoryFilterType"
    ]
    """<p>The category filter type. This element is used to specify whether a filter is a simple category filter or an inverse category filter.</p>"""
    constant: NotRequired[
        "capo_quicksight.types.topic_category_filter_constant.TopicCategoryFilterConstant"
    ]
    """<p>The constant used in a category filter.</p>"""
    inverse: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates if the filter is inverse.</p>"""
    null_filter: NotRequired["capo_quicksight.types.null_filter_type.NullFilterType"]
    """<p>The <code>null</code> filter that is applied to the category filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicCategoryFilter) -> dict:
    out: dict = {}
    if "category_filter_function" in value:
        import capo_quicksight.types.category_filter_function

        out["CategoryFilterFunction"] = (
            capo_quicksight.types.category_filter_function.serialize_json(
                value["category_filter_function"]
            )
        )
    if "category_filter_type" in value:
        import capo_quicksight.types.category_filter_type

        out["CategoryFilterType"] = (
            capo_quicksight.types.category_filter_type.serialize_json(
                value["category_filter_type"]
            )
        )
    if "constant" in value:
        import capo_quicksight.types.topic_category_filter_constant

        out["Constant"] = (
            capo_quicksight.types.topic_category_filter_constant.serialize_json(
                value["constant"]
            )
        )
    out["Inverse"] = value.get("inverse", False)
    if "null_filter" in value:
        import capo_quicksight.types.null_filter_type

        out["NullFilter"] = capo_quicksight.types.null_filter_type.serialize_json(
            value["null_filter"]
        )
    return out


def deserialize_json(data: dict) -> TopicCategoryFilter:
    out: TopicCategoryFilter = {}  # type: ignore[typeddict-item]
    if data.get("CategoryFilterFunction") is not None:
        import capo_quicksight.types.category_filter_function

        out["category_filter_function"] = (
            capo_quicksight.types.category_filter_function.deserialize_json(
                data["CategoryFilterFunction"]
            )
        )
    if data.get("CategoryFilterType") is not None:
        import capo_quicksight.types.category_filter_type

        out["category_filter_type"] = (
            capo_quicksight.types.category_filter_type.deserialize_json(
                data["CategoryFilterType"]
            )
        )
    if data.get("Constant") is not None:
        import capo_quicksight.types.topic_category_filter_constant

        out["constant"] = (
            capo_quicksight.types.topic_category_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if data.get("Inverse") is not None:
        out["inverse"] = data["Inverse"]
    else:
        out["inverse"] = False
    if data.get("NullFilter") is not None:
        import capo_quicksight.types.null_filter_type

        out["null_filter"] = capo_quicksight.types.null_filter_type.deserialize_json(
            data["NullFilter"]
        )
    return out


def redact_sensitive(value: TopicCategoryFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "constant" in value:
        out["constant"] = "*** Sensitive Data Redacted ***"
    return out
