"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_sort_configuration_list
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.integer
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.time_granularity


class TopBottomFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    limit: NotRequired["capo_quicksight.types.integer.Integer"]
    """<p>The number of items to include in the top bottom filter results.</p>"""
    aggregation_sort_configurations: "capo_quicksight.types.aggregation_sort_configuration_list.AggregationSortConfigurationList"
    """<p>The aggregation and sort configuration of the top bottom filter.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    parameter_name: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "limit" in value:
        out["Limit"] = value["limit"]
    import capo_quicksight.types.aggregation_sort_configuration_list

    out["AggregationSortConfigurations"] = (
        capo_quicksight.types.aggregation_sort_configuration_list.serialize_json(
            value["aggregation_sort_configurations"]
        )
    )
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "default_filter_control_configuration" in value:
        import capo_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            capo_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopBottomFilter:
    out: TopBottomFilter = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("TopBottomFilter.column required")
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("AggregationSortConfigurations") is not None:
        import capo_quicksight.types.aggregation_sort_configuration_list

        out["aggregation_sort_configurations"] = (
            capo_quicksight.types.aggregation_sort_configuration_list.deserialize_json(
                data["AggregationSortConfigurations"]
            )
        )
    else:
        out["aggregation_sort_configurations"] = []
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
    if data.get("DefaultFilterControlConfiguration") is not None:
        import capo_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            capo_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
