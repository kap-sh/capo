"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNumericEqualityFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.named_filter_agg_type
    import capo_quicksight.types.null_filter_type
    import capo_quicksight.types.topic_singular_filter_constant


class TopicNumericEqualityFilter(TypedDict, closed=True):
    constant: NotRequired[
        "capo_quicksight.types.topic_singular_filter_constant.TopicSingularFilterConstant"
    ]
    """<p>The constant used in a numeric equality filter.</p>"""
    aggregation: NotRequired[
        "capo_quicksight.types.named_filter_agg_type.NamedFilterAggType"
    ]
    """<p>An aggregation function that specifies how to calculate the value of a numeric field for a topic. Valid values for this structure are <code>NO_AGGREGATION</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>MIN</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, and <code>VARP</code>.</p>"""
    inverse: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates if the filter is inverse.</p>"""
    null_filter: NotRequired["capo_quicksight.types.null_filter_type.NullFilterType"]
    """<p>The <code>null</code> filter that is applied to the numeric equality filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNumericEqualityFilter) -> dict:
    out: dict = {}
    if "constant" in value:
        import capo_quicksight.types.topic_singular_filter_constant

        out["Constant"] = (
            capo_quicksight.types.topic_singular_filter_constant.serialize_json(
                value["constant"]
            )
        )
    if "aggregation" in value:
        import capo_quicksight.types.named_filter_agg_type

        out["Aggregation"] = capo_quicksight.types.named_filter_agg_type.serialize_json(
            value["aggregation"]
        )
    out["Inverse"] = value.get("inverse", False)
    if "null_filter" in value:
        import capo_quicksight.types.null_filter_type

        out["NullFilter"] = capo_quicksight.types.null_filter_type.serialize_json(
            value["null_filter"]
        )
    return out


def deserialize_json(data: dict) -> TopicNumericEqualityFilter:
    out: TopicNumericEqualityFilter = {}  # type: ignore[typeddict-item]
    if data.get("Constant") is not None:
        import capo_quicksight.types.topic_singular_filter_constant

        out["constant"] = (
            capo_quicksight.types.topic_singular_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if data.get("Aggregation") is not None:
        import capo_quicksight.types.named_filter_agg_type

        out["aggregation"] = (
            capo_quicksight.types.named_filter_agg_type.deserialize_json(
                data["Aggregation"]
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


def redact_sensitive(value: TopicNumericEqualityFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "constant" in value:
        out["constant"] = "*** Sensitive Data Redacted ***"
    return out
