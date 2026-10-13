"""Generated from Smithy shape ``com.amazonaws.quicksight#FormatConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_format_configuration
    import capo_quicksight.types.number_format_configuration
    import capo_quicksight.types.string_format_configuration


class FormatConfiguration(TypedDict, closed=True):
    string_format_configuration: NotRequired[
        "capo_quicksight.types.string_format_configuration.StringFormatConfiguration"
    ]
    """<p>Formatting configuration for string fields.</p>"""
    number_format_configuration: NotRequired[
        "capo_quicksight.types.number_format_configuration.NumberFormatConfiguration"
    ]
    """<p>Formatting configuration for number fields.</p>"""
    date_time_format_configuration: NotRequired[
        "capo_quicksight.types.date_time_format_configuration.DateTimeFormatConfiguration"
    ]
    """<p>Formatting configuration for <code>DateTime</code> fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormatConfiguration) -> dict:
    out: dict = {}
    if "string_format_configuration" in value:
        import capo_quicksight.types.string_format_configuration

        out["StringFormatConfiguration"] = (
            capo_quicksight.types.string_format_configuration.serialize_json(
                value["string_format_configuration"]
            )
        )
    if "number_format_configuration" in value:
        import capo_quicksight.types.number_format_configuration

        out["NumberFormatConfiguration"] = (
            capo_quicksight.types.number_format_configuration.serialize_json(
                value["number_format_configuration"]
            )
        )
    if "date_time_format_configuration" in value:
        import capo_quicksight.types.date_time_format_configuration

        out["DateTimeFormatConfiguration"] = (
            capo_quicksight.types.date_time_format_configuration.serialize_json(
                value["date_time_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FormatConfiguration:
    out: FormatConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StringFormatConfiguration") is not None:
        import capo_quicksight.types.string_format_configuration

        out["string_format_configuration"] = (
            capo_quicksight.types.string_format_configuration.deserialize_json(
                data["StringFormatConfiguration"]
            )
        )
    if data.get("NumberFormatConfiguration") is not None:
        import capo_quicksight.types.number_format_configuration

        out["number_format_configuration"] = (
            capo_quicksight.types.number_format_configuration.deserialize_json(
                data["NumberFormatConfiguration"]
            )
        )
    if data.get("DateTimeFormatConfiguration") is not None:
        import capo_quicksight.types.date_time_format_configuration

        out["date_time_format_configuration"] = (
            capo_quicksight.types.date_time_format_configuration.deserialize_json(
                data["DateTimeFormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: FormatConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "string_format_configuration" in value:
        import capo_quicksight.types.string_format_configuration

        out["string_format_configuration"] = (
            capo_quicksight.types.string_format_configuration.redact_sensitive(
                value["string_format_configuration"]
            )
        )
    if "number_format_configuration" in value:
        import capo_quicksight.types.number_format_configuration

        out["number_format_configuration"] = (
            capo_quicksight.types.number_format_configuration.redact_sensitive(
                value["number_format_configuration"]
            )
        )
    if "date_time_format_configuration" in value:
        import capo_quicksight.types.date_time_format_configuration

        out["date_time_format_configuration"] = (
            capo_quicksight.types.date_time_format_configuration.redact_sensitive(
                value["date_time_format_configuration"]
            )
        )
    return out
