"""Generated from Smithy shape ``com.amazonaws.quicksight#RelativeDatesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.anchor_date_configuration
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.exclude_period_configuration
    import capo_quicksight.types.filter_null_option
    import capo_quicksight.types.integer
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.relative_date_type
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.time_granularity


class RelativeDatesFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    anchor_date_configuration: (
        "capo_quicksight.types.anchor_date_configuration.AnchorDateConfiguration"
    )
    """<p>The date configuration of the filter.</p>"""
    minimum_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The minimum granularity (period granularity) of the relative dates filter.</p>"""
    time_granularity: "capo_quicksight.types.time_granularity.TimeGranularity"
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    relative_date_type: "capo_quicksight.types.relative_date_type.RelativeDateType"
    """<p>The range date type of the filter. Choose one of the options below:</p> <ul> <li> <p> <code>PREVIOUS</code> </p> </li> <li> <p> <code>THIS</code> </p> </li> <li> <p> <code>LAST</code> </p> </li> <li> <p> <code>NOW</code> </p> </li> <li> <p> <code>NEXT</code> </p> </li> </ul>"""
    relative_date_value: NotRequired["capo_quicksight.types.integer.Integer"]
    """<p>The date value of the filter.</p>"""
    parameter_name: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p>"""
    null_option: "capo_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    exclude_period_configuration: NotRequired[
        "capo_quicksight.types.exclude_period_configuration.ExcludePeriodConfiguration"
    ]
    """<p>The configuration for the exclude period of the filter.</p>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelativeDatesFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import capo_quicksight.types.anchor_date_configuration

    out["AnchorDateConfiguration"] = (
        capo_quicksight.types.anchor_date_configuration.serialize_json(
            value["anchor_date_configuration"]
        )
    )
    if "minimum_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["MinimumGranularity"] = (
            capo_quicksight.types.time_granularity.serialize_json(
                value["minimum_granularity"]
            )
        )
    import capo_quicksight.types.time_granularity

    out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
        value["time_granularity"]
    )
    import capo_quicksight.types.relative_date_type

    out["RelativeDateType"] = capo_quicksight.types.relative_date_type.serialize_json(
        value["relative_date_type"]
    )
    if "relative_date_value" in value:
        out["RelativeDateValue"] = value["relative_date_value"]
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
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
    if "default_filter_control_configuration" in value:
        import capo_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            capo_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RelativeDatesFilter:
    out: RelativeDatesFilter = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("RelativeDatesFilter.column required")
    if data.get("AnchorDateConfiguration") is not None:
        import capo_quicksight.types.anchor_date_configuration

        out["anchor_date_configuration"] = (
            capo_quicksight.types.anchor_date_configuration.deserialize_json(
                data["AnchorDateConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RelativeDatesFilter.anchor_date_configuration required"
        )
    if data.get("MinimumGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["minimum_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["MinimumGranularity"]
            )
        )
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    else:
        import typing

        out["time_granularity"] = typing.cast(
            "capo_quicksight.types.time_granularity.TimeGranularity", ""
        )
    if data.get("RelativeDateType") is not None:
        import capo_quicksight.types.relative_date_type

        out["relative_date_type"] = (
            capo_quicksight.types.relative_date_type.deserialize_json(
                data["RelativeDateType"]
            )
        )
    else:
        import typing

        out["relative_date_type"] = typing.cast(
            "capo_quicksight.types.relative_date_type.RelativeDateType", ""
        )
    if data.get("RelativeDateValue") is not None:
        out["relative_date_value"] = data["RelativeDateValue"]
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
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
    if data.get("DefaultFilterControlConfiguration") is not None:
        import capo_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            capo_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
