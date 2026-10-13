"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomParameterValues``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_default_value_list
    import capo_quicksight.types.decimal_default_value_list
    import capo_quicksight.types.integer_default_value_list
    import capo_quicksight.types.string_default_value_list


class CustomParameterValues(TypedDict, closed=True):
    string_values: NotRequired[
        "capo_quicksight.types.string_default_value_list.StringDefaultValueList"
    ]
    """<p>A list of string-type parameter values.</p>"""
    integer_values: NotRequired[
        "capo_quicksight.types.integer_default_value_list.IntegerDefaultValueList"
    ]
    """<p>A list of integer-type parameter values.</p>"""
    decimal_values: NotRequired[
        "capo_quicksight.types.decimal_default_value_list.DecimalDefaultValueList"
    ]
    """<p>A list of decimal-type parameter values.</p>"""
    date_time_values: NotRequired[
        "capo_quicksight.types.date_time_default_value_list.DateTimeDefaultValueList"
    ]
    """<p>A list of datetime-type parameter values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomParameterValues) -> dict:
    out: dict = {}
    if "string_values" in value:
        import capo_quicksight.types.string_default_value_list

        out["StringValues"] = (
            capo_quicksight.types.string_default_value_list.serialize_json(
                value["string_values"]
            )
        )
    if "integer_values" in value:
        import capo_quicksight.types.integer_default_value_list

        out["IntegerValues"] = (
            capo_quicksight.types.integer_default_value_list.serialize_json(
                value["integer_values"]
            )
        )
    if "decimal_values" in value:
        import capo_quicksight.types.decimal_default_value_list

        out["DecimalValues"] = (
            capo_quicksight.types.decimal_default_value_list.serialize_json(
                value["decimal_values"]
            )
        )
    if "date_time_values" in value:
        import capo_quicksight.types.date_time_default_value_list

        out["DateTimeValues"] = (
            capo_quicksight.types.date_time_default_value_list.serialize_json(
                value["date_time_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomParameterValues:
    out: CustomParameterValues = {}  # type: ignore[typeddict-item]
    if data.get("StringValues") is not None:
        import capo_quicksight.types.string_default_value_list

        out["string_values"] = (
            capo_quicksight.types.string_default_value_list.deserialize_json(
                data["StringValues"]
            )
        )
    if data.get("IntegerValues") is not None:
        import capo_quicksight.types.integer_default_value_list

        out["integer_values"] = (
            capo_quicksight.types.integer_default_value_list.deserialize_json(
                data["IntegerValues"]
            )
        )
    if data.get("DecimalValues") is not None:
        import capo_quicksight.types.decimal_default_value_list

        out["decimal_values"] = (
            capo_quicksight.types.decimal_default_value_list.deserialize_json(
                data["DecimalValues"]
            )
        )
    if data.get("DateTimeValues") is not None:
        import capo_quicksight.types.date_time_default_value_list

        out["date_time_values"] = (
            capo_quicksight.types.date_time_default_value_list.deserialize_json(
                data["DateTimeValues"]
            )
        )
    return out


def redact_sensitive(value: CustomParameterValues) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "string_values" in value:
        import capo_quicksight.types.string_default_value_list

        out["string_values"] = (
            capo_quicksight.types.string_default_value_list.redact_sensitive(
                value["string_values"]
            )
        )
    if "integer_values" in value:
        import capo_quicksight.types.integer_default_value_list

        out["integer_values"] = (
            capo_quicksight.types.integer_default_value_list.redact_sensitive(
                value["integer_values"]
            )
        )
    if "decimal_values" in value:
        import capo_quicksight.types.decimal_default_value_list

        out["decimal_values"] = (
            capo_quicksight.types.decimal_default_value_list.redact_sensitive(
                value["decimal_values"]
            )
        )
    if "date_time_values" in value:
        import capo_quicksight.types.date_time_default_value_list

        out["date_time_values"] = (
            capo_quicksight.types.date_time_default_value_list.redact_sensitive(
                value["date_time_values"]
            )
        )
    return out
