"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicDateRangeFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.null_filter_type
    import capo_quicksight.types.topic_range_filter_constant


class TopicDateRangeFilter(TypedDict, closed=True):
    inclusive: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the date range filter should include the boundary values. If set to true, the filter includes the start and end dates. If set to false, the filter excludes them.</p>"""
    constant: NotRequired[
        "capo_quicksight.types.topic_range_filter_constant.TopicRangeFilterConstant"
    ]
    """<p>The constant used in a date range filter.</p>"""
    null_filter: NotRequired["capo_quicksight.types.null_filter_type.NullFilterType"]
    """<p>The <code>null</code> filter that is applied to the date range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicDateRangeFilter) -> dict:
    out: dict = {}
    out["Inclusive"] = value.get("inclusive", False)
    if "constant" in value:
        import capo_quicksight.types.topic_range_filter_constant

        out["Constant"] = (
            capo_quicksight.types.topic_range_filter_constant.serialize_json(
                value["constant"]
            )
        )
    if "null_filter" in value:
        import capo_quicksight.types.null_filter_type

        out["NullFilter"] = capo_quicksight.types.null_filter_type.serialize_json(
            value["null_filter"]
        )
    return out


def deserialize_json(data: dict) -> TopicDateRangeFilter:
    out: TopicDateRangeFilter = {}  # type: ignore[typeddict-item]
    if data.get("Inclusive") is not None:
        out["inclusive"] = data["Inclusive"]
    else:
        out["inclusive"] = False
    if data.get("Constant") is not None:
        import capo_quicksight.types.topic_range_filter_constant

        out["constant"] = (
            capo_quicksight.types.topic_range_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if data.get("NullFilter") is not None:
        import capo_quicksight.types.null_filter_type

        out["null_filter"] = capo_quicksight.types.null_filter_type.deserialize_json(
            data["NullFilter"]
        )
    return out


def redact_sensitive(value: TopicDateRangeFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "constant" in value:
        out["constant"] = "*** Sensitive Data Redacted ***"
    return out
