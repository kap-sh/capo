"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDefaultValues``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_default_value_list
    import capo_quicksight.types.dynamic_default_value
    import capo_quicksight.types.rolling_date_configuration


class DateTimeDefaultValues(TypedDict, closed=True):
    dynamic_value: NotRequired[
        "capo_quicksight.types.dynamic_default_value.DynamicDefaultValue"
    ]
    """<p>The dynamic value of the <code>DataTimeDefaultValues</code>. Different defaults are displayed according to users, groups, and values mapping.</p>"""
    static_values: NotRequired[
        "capo_quicksight.types.date_time_default_value_list.DateTimeDefaultValueList"
    ]
    """<p>The static values of the <code>DataTimeDefaultValues</code>.</p>"""
    rolling_date: NotRequired[
        "capo_quicksight.types.rolling_date_configuration.RollingDateConfiguration"
    ]
    """<p>The rolling date of the <code>DataTimeDefaultValues</code>. The date is determined from the dataset based on input expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDefaultValues) -> dict:
    out: dict = {}
    if "dynamic_value" in value:
        import capo_quicksight.types.dynamic_default_value

        out["DynamicValue"] = (
            capo_quicksight.types.dynamic_default_value.serialize_json(
                value["dynamic_value"]
            )
        )
    if "static_values" in value:
        import capo_quicksight.types.date_time_default_value_list

        out["StaticValues"] = (
            capo_quicksight.types.date_time_default_value_list.serialize_json(
                value["static_values"]
            )
        )
    if "rolling_date" in value:
        import capo_quicksight.types.rolling_date_configuration

        out["RollingDate"] = (
            capo_quicksight.types.rolling_date_configuration.serialize_json(
                value["rolling_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateTimeDefaultValues:
    out: DateTimeDefaultValues = {}  # type: ignore[typeddict-item]
    if data.get("DynamicValue") is not None:
        import capo_quicksight.types.dynamic_default_value

        out["dynamic_value"] = (
            capo_quicksight.types.dynamic_default_value.deserialize_json(
                data["DynamicValue"]
            )
        )
    if data.get("StaticValues") is not None:
        import capo_quicksight.types.date_time_default_value_list

        out["static_values"] = (
            capo_quicksight.types.date_time_default_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    if data.get("RollingDate") is not None:
        import capo_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            capo_quicksight.types.rolling_date_configuration.deserialize_json(
                data["RollingDate"]
            )
        )
    return out


def redact_sensitive(value: DateTimeDefaultValues) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "static_values" in value:
        import capo_quicksight.types.date_time_default_value_list

        out["static_values"] = (
            capo_quicksight.types.date_time_default_value_list.redact_sensitive(
                value["static_values"]
            )
        )
    if "rolling_date" in value:
        import capo_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            capo_quicksight.types.rolling_date_configuration.redact_sensitive(
                value["rolling_date"]
            )
        )
    return out
