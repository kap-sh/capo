"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeRangeFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.exclude_period_configuration
    import capo_quicksight.types.filter_null_option
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.time_granularity
    import capo_quicksight.types.time_range_filter_value


class TimeRangeFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    include_minimum: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the minimum value in the filter value range should be included in the filtered results.</p>"""
    include_maximum: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the maximum value in the filter value range should be included in the filtered results.</p>"""
    range_minimum_value: NotRequired[
        "capo_quicksight.types.time_range_filter_value.TimeRangeFilterValue"
    ]
    """<p>The minimum value for the filter value range.</p>"""
    range_maximum_value: NotRequired[
        "capo_quicksight.types.time_range_filter_value.TimeRangeFilterValue"
    ]
    """<p>The maximum value for the filter value range.</p>"""
    null_option: "capo_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    exclude_period_configuration: NotRequired[
        "capo_quicksight.types.exclude_period_configuration.ExcludePeriodConfiguration"
    ]
    """<p>The exclude period of the time range filter.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "include_minimum" in value:
        out["IncludeMinimum"] = value["include_minimum"]
    if "include_maximum" in value:
        out["IncludeMaximum"] = value["include_maximum"]
    if "range_minimum_value" in value:
        import capo_quicksight.types.time_range_filter_value

        out["RangeMinimumValue"] = (
            capo_quicksight.types.time_range_filter_value.serialize_json(
                value["range_minimum_value"]
            )
        )
    if "range_maximum_value" in value:
        import capo_quicksight.types.time_range_filter_value

        out["RangeMaximumValue"] = (
            capo_quicksight.types.time_range_filter_value.serialize_json(
                value["range_maximum_value"]
            )
        )
    import capo_quicksight.types.filter_null_option

    out["NullOption"] = capo_quicksight.types.filter_null_option.serialize_json(
        value["null_option"]
    )
    if "exclude_period_configuration" in value:
        import capo_quicksight.types.exclude_period_configuration

        out["ExcludePeriodConfiguration"] = (
            capo_quicksight.types.exclude_period_configuration.serialize_json(
                value["exclude_period_configuration"]
            )
        )
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    if "default_filter_control_configuration" in value:
        import capo_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            capo_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimeRangeFilter:
    out: TimeRangeFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterId") is not None:
        out["filter_id"] = data["FilterId"]
    else:
        out["filter_id"] = ""
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("TimeRangeFilter.column required")
    if data.get("IncludeMinimum") is not None:
        out["include_minimum"] = data["IncludeMinimum"]
    if data.get("IncludeMaximum") is not None:
        out["include_maximum"] = data["IncludeMaximum"]
    if data.get("RangeMinimumValue") is not None:
        import capo_quicksight.types.time_range_filter_value

        out["range_minimum_value"] = (
            capo_quicksight.types.time_range_filter_value.deserialize_json(
                data["RangeMinimumValue"]
            )
        )
    if data.get("RangeMaximumValue") is not None:
        import capo_quicksight.types.time_range_filter_value

        out["range_maximum_value"] = (
            capo_quicksight.types.time_range_filter_value.deserialize_json(
                data["RangeMaximumValue"]
            )
        )
    if data.get("NullOption") is not None:
        import capo_quicksight.types.filter_null_option

        out["null_option"] = capo_quicksight.types.filter_null_option.deserialize_json(
            data["NullOption"]
        )
    else:
        import typing

        out["null_option"] = typing.cast(
            "capo_quicksight.types.filter_null_option.FilterNullOption", ""
        )
    if data.get("ExcludePeriodConfiguration") is not None:
        import capo_quicksight.types.exclude_period_configuration

        out["exclude_period_configuration"] = (
            capo_quicksight.types.exclude_period_configuration.deserialize_json(
                data["ExcludePeriodConfiguration"]
            )
        )
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("DefaultFilterControlConfiguration") is not None:
        import capo_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            capo_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out


def redact_sensitive(value: TimeRangeFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "range_minimum_value" in value:
        import capo_quicksight.types.time_range_filter_value

        out["range_minimum_value"] = (
            capo_quicksight.types.time_range_filter_value.redact_sensitive(
                value["range_minimum_value"]
            )
        )
    if "range_maximum_value" in value:
        import capo_quicksight.types.time_range_filter_value

        out["range_maximum_value"] = (
            capo_quicksight.types.time_range_filter_value.redact_sensitive(
                value["range_maximum_value"]
            )
        )
    return out
