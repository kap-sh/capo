"""Generated from Smithy shape ``com.amazonaws.quicksight#Parameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_parameter_list
    import capo_quicksight.types.decimal_parameter_list
    import capo_quicksight.types.integer_parameter_list
    import capo_quicksight.types.string_parameter_list


class Parameters(TypedDict, closed=True):
    string_parameters: NotRequired[
        "capo_quicksight.types.string_parameter_list.StringParameterList"
    ]
    """<p>The parameters that have a data type of string.</p>"""
    integer_parameters: NotRequired[
        "capo_quicksight.types.integer_parameter_list.IntegerParameterList"
    ]
    """<p>The parameters that have a data type of integer.</p>"""
    decimal_parameters: NotRequired[
        "capo_quicksight.types.decimal_parameter_list.DecimalParameterList"
    ]
    """<p>The parameters that have a data type of decimal.</p>"""
    date_time_parameters: NotRequired[
        "capo_quicksight.types.date_time_parameter_list.DateTimeParameterList"
    ]
    """<p>The parameters that have a data type of date-time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Parameters) -> dict:
    out: dict = {}
    if "string_parameters" in value:
        import capo_quicksight.types.string_parameter_list

        out["StringParameters"] = (
            capo_quicksight.types.string_parameter_list.serialize_json(
                value["string_parameters"]
            )
        )
    if "integer_parameters" in value:
        import capo_quicksight.types.integer_parameter_list

        out["IntegerParameters"] = (
            capo_quicksight.types.integer_parameter_list.serialize_json(
                value["integer_parameters"]
            )
        )
    if "decimal_parameters" in value:
        import capo_quicksight.types.decimal_parameter_list

        out["DecimalParameters"] = (
            capo_quicksight.types.decimal_parameter_list.serialize_json(
                value["decimal_parameters"]
            )
        )
    if "date_time_parameters" in value:
        import capo_quicksight.types.date_time_parameter_list

        out["DateTimeParameters"] = (
            capo_quicksight.types.date_time_parameter_list.serialize_json(
                value["date_time_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Parameters:
    out: Parameters = {}  # type: ignore[typeddict-item]
    if data.get("StringParameters") is not None:
        import capo_quicksight.types.string_parameter_list

        out["string_parameters"] = (
            capo_quicksight.types.string_parameter_list.deserialize_json(
                data["StringParameters"]
            )
        )
    if data.get("IntegerParameters") is not None:
        import capo_quicksight.types.integer_parameter_list

        out["integer_parameters"] = (
            capo_quicksight.types.integer_parameter_list.deserialize_json(
                data["IntegerParameters"]
            )
        )
    if data.get("DecimalParameters") is not None:
        import capo_quicksight.types.decimal_parameter_list

        out["decimal_parameters"] = (
            capo_quicksight.types.decimal_parameter_list.deserialize_json(
                data["DecimalParameters"]
            )
        )
    if data.get("DateTimeParameters") is not None:
        import capo_quicksight.types.date_time_parameter_list

        out["date_time_parameters"] = (
            capo_quicksight.types.date_time_parameter_list.deserialize_json(
                data["DateTimeParameters"]
            )
        )
    return out


def redact_sensitive(value: Parameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "string_parameters" in value:
        import capo_quicksight.types.string_parameter_list

        out["string_parameters"] = (
            capo_quicksight.types.string_parameter_list.redact_sensitive(
                value["string_parameters"]
            )
        )
    if "integer_parameters" in value:
        import capo_quicksight.types.integer_parameter_list

        out["integer_parameters"] = (
            capo_quicksight.types.integer_parameter_list.redact_sensitive(
                value["integer_parameters"]
            )
        )
    if "decimal_parameters" in value:
        import capo_quicksight.types.decimal_parameter_list

        out["decimal_parameters"] = (
            capo_quicksight.types.decimal_parameter_list.redact_sensitive(
                value["decimal_parameters"]
            )
        )
    if "date_time_parameters" in value:
        import capo_quicksight.types.date_time_parameter_list

        out["date_time_parameters"] = (
            capo_quicksight.types.date_time_parameter_list.redact_sensitive(
                value["date_time_parameters"]
            )
        )
    return out
