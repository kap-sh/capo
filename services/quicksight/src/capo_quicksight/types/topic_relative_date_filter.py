"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRelativeDateFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.null_filter_type
    import capo_quicksight.types.topic_relative_date_filter_function
    import capo_quicksight.types.topic_singular_filter_constant
    import capo_quicksight.types.topic_time_granularity


class TopicRelativeDateFilter(TypedDict, closed=True):
    time_granularity: NotRequired[
        "capo_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    relative_date_filter_function: NotRequired[
        "capo_quicksight.types.topic_relative_date_filter_function.TopicRelativeDateFilterFunction"
    ]
    """<p>The function to be used in a relative date filter to determine the range of dates to include in the results. Valid values for this structure are <code>BEFORE</code>, <code>AFTER</code>, and <code>BETWEEN</code>.</p>"""
    constant: NotRequired[
        "capo_quicksight.types.topic_singular_filter_constant.TopicSingularFilterConstant"
    ]
    """<p>The constant used in a relative date filter.</p>"""
    null_filter: NotRequired["capo_quicksight.types.null_filter_type.NullFilterType"]
    """<p>The <code>null</code> filter that is applied to the relative date filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRelativeDateFilter) -> dict:
    out: dict = {}
    if "time_granularity" in value:
        import capo_quicksight.types.topic_time_granularity

        out["TimeGranularity"] = (
            capo_quicksight.types.topic_time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "relative_date_filter_function" in value:
        import capo_quicksight.types.topic_relative_date_filter_function

        out["RelativeDateFilterFunction"] = (
            capo_quicksight.types.topic_relative_date_filter_function.serialize_json(
                value["relative_date_filter_function"]
            )
        )
    if "constant" in value:
        import capo_quicksight.types.topic_singular_filter_constant

        out["Constant"] = (
            capo_quicksight.types.topic_singular_filter_constant.serialize_json(
                value["constant"]
            )
        )
    if "null_filter" in value:
        import capo_quicksight.types.null_filter_type

        out["NullFilter"] = capo_quicksight.types.null_filter_type.serialize_json(
            value["null_filter"]
        )
    return out


def deserialize_json(data: dict) -> TopicRelativeDateFilter:
    out: TopicRelativeDateFilter = {}  # type: ignore[typeddict-item]
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.topic_time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.topic_time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("RelativeDateFilterFunction") is not None:
        import capo_quicksight.types.topic_relative_date_filter_function

        out["relative_date_filter_function"] = (
            capo_quicksight.types.topic_relative_date_filter_function.deserialize_json(
                data["RelativeDateFilterFunction"]
            )
        )
    if data.get("Constant") is not None:
        import capo_quicksight.types.topic_singular_filter_constant

        out["constant"] = (
            capo_quicksight.types.topic_singular_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if data.get("NullFilter") is not None:
        import capo_quicksight.types.null_filter_type

        out["null_filter"] = capo_quicksight.types.null_filter_type.deserialize_json(
            data["NullFilter"]
        )
    return out


def redact_sensitive(value: TopicRelativeDateFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "constant" in value:
        out["constant"] = "*** Sensitive Data Redacted ***"
    return out
