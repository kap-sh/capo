"""Generated from Smithy shape ``com.amazonaws.quicksight#StringFormatConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.null_value_format_configuration
    import capo_quicksight.types.numeric_format_configuration


class StringFormatConfiguration(TypedDict, closed=True):
    null_value_format_configuration: NotRequired[
        "capo_quicksight.types.null_value_format_configuration.NullValueFormatConfiguration"
    ]
    """<p>The options that determine the null value format configuration.</p>"""
    numeric_format_configuration: NotRequired[
        "capo_quicksight.types.numeric_format_configuration.NumericFormatConfiguration"
    ]
    """<p>The formatting configuration for numeric strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringFormatConfiguration) -> dict:
    out: dict = {}
    if "null_value_format_configuration" in value:
        import capo_quicksight.types.null_value_format_configuration

        out["NullValueFormatConfiguration"] = (
            capo_quicksight.types.null_value_format_configuration.serialize_json(
                value["null_value_format_configuration"]
            )
        )
    if "numeric_format_configuration" in value:
        import capo_quicksight.types.numeric_format_configuration

        out["NumericFormatConfiguration"] = (
            capo_quicksight.types.numeric_format_configuration.serialize_json(
                value["numeric_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StringFormatConfiguration:
    out: StringFormatConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("NullValueFormatConfiguration") is not None:
        import capo_quicksight.types.null_value_format_configuration

        out["null_value_format_configuration"] = (
            capo_quicksight.types.null_value_format_configuration.deserialize_json(
                data["NullValueFormatConfiguration"]
            )
        )
    if data.get("NumericFormatConfiguration") is not None:
        import capo_quicksight.types.numeric_format_configuration

        out["numeric_format_configuration"] = (
            capo_quicksight.types.numeric_format_configuration.deserialize_json(
                data["NumericFormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: StringFormatConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "null_value_format_configuration" in value:
        import capo_quicksight.types.null_value_format_configuration

        out["null_value_format_configuration"] = (
            capo_quicksight.types.null_value_format_configuration.redact_sensitive(
                value["null_value_format_configuration"]
            )
        )
    if "numeric_format_configuration" in value:
        import capo_quicksight.types.numeric_format_configuration

        out["numeric_format_configuration"] = (
            capo_quicksight.types.numeric_format_configuration.redact_sensitive(
                value["numeric_format_configuration"]
            )
        )
    return out
