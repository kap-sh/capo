"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeRangeFilterValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.rolling_date_configuration
    import capo_quicksight.types.timestamp


class TimeRangeFilterValue(TypedDict, closed=True):
    static_value: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The static input value.</p>"""
    rolling_date: NotRequired[
        "capo_quicksight.types.rolling_date_configuration.RollingDateConfiguration"
    ]
    """<p>The rolling date input value.</p>"""
    parameter: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter type input value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        import capo_quicksight.types.timestamp

        out["StaticValue"] = capo_quicksight.types.timestamp.serialize_json(
            value["static_value"]
        )
    if "rolling_date" in value:
        import capo_quicksight.types.rolling_date_configuration

        out["RollingDate"] = (
            capo_quicksight.types.rolling_date_configuration.serialize_json(
                value["rolling_date"]
            )
        )
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    return out


def deserialize_json(data: dict) -> TimeRangeFilterValue:
    out: TimeRangeFilterValue = {}  # type: ignore[typeddict-item]
    if data.get("StaticValue") is not None:
        import capo_quicksight.types.timestamp

        out["static_value"] = capo_quicksight.types.timestamp.deserialize_json(
            data["StaticValue"]
        )
    if data.get("RollingDate") is not None:
        import capo_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            capo_quicksight.types.rolling_date_configuration.deserialize_json(
                data["RollingDate"]
            )
        )
    if data.get("Parameter") is not None:
        out["parameter"] = data["Parameter"]
    return out


def redact_sensitive(value: TimeRangeFilterValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rolling_date" in value:
        import capo_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            capo_quicksight.types.rolling_date_configuration.redact_sensitive(
                value["rolling_date"]
            )
        )
    return out
