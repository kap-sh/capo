"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeEqualityFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.rolling_date_configuration
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.time_granularity
    import capo_quicksight.types.timestamp


class TimeEqualityFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    value: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The value of a <code>TimeEquality</code> filter.</p> <p>This field is mutually exclusive to <code>RollingDate</code> and <code>ParameterName</code>.</p>"""
    parameter_name: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p> <p>This field is mutually exclusive to <code>Value</code> and <code>RollingDate</code>.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    rolling_date: NotRequired[
        "capo_quicksight.types.rolling_date_configuration.RollingDateConfiguration"
    ]
    """<p>The rolling date input for the <code>TimeEquality</code> filter.</p> <p>This field is mutually exclusive to <code>Value</code> and <code>ParameterName</code>.</p>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeEqualityFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "value" in value:
        import capo_quicksight.types.timestamp

        out["Value"] = capo_quicksight.types.timestamp.serialize_json(value["value"])
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    if "rolling_date" in value:
        import capo_quicksight.types.rolling_date_configuration

        out["RollingDate"] = (
            capo_quicksight.types.rolling_date_configuration.serialize_json(
                value["rolling_date"]
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


def deserialize_json(data: dict) -> TimeEqualityFilter:
    out: TimeEqualityFilter = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("TimeEqualityFilter.column required")
    if data.get("Value") is not None:
        import capo_quicksight.types.timestamp

        out["value"] = capo_quicksight.types.timestamp.deserialize_json(data["Value"])
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("RollingDate") is not None:
        import capo_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            capo_quicksight.types.rolling_date_configuration.deserialize_json(
                data["RollingDate"]
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


def redact_sensitive(value: TimeEqualityFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rolling_date" in value:
        import capo_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            capo_quicksight.types.rolling_date_configuration.redact_sensitive(
                value["rolling_date"]
            )
        )
    return out
