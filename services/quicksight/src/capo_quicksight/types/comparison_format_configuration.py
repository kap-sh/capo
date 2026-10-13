"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonFormatConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.number_display_format_configuration
    import capo_quicksight.types.percentage_display_format_configuration


class ComparisonFormatConfiguration(TypedDict, closed=True):
    number_display_format_configuration: NotRequired[
        "capo_quicksight.types.number_display_format_configuration.NumberDisplayFormatConfiguration"
    ]
    """<p>The number display format.</p>"""
    percentage_display_format_configuration: NotRequired[
        "capo_quicksight.types.percentage_display_format_configuration.PercentageDisplayFormatConfiguration"
    ]
    """<p>The percentage display format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonFormatConfiguration) -> dict:
    out: dict = {}
    if "number_display_format_configuration" in value:
        import capo_quicksight.types.number_display_format_configuration

        out["NumberDisplayFormatConfiguration"] = (
            capo_quicksight.types.number_display_format_configuration.serialize_json(
                value["number_display_format_configuration"]
            )
        )
    if "percentage_display_format_configuration" in value:
        import capo_quicksight.types.percentage_display_format_configuration

        out["PercentageDisplayFormatConfiguration"] = (
            capo_quicksight.types.percentage_display_format_configuration.serialize_json(
                value["percentage_display_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComparisonFormatConfiguration:
    out: ComparisonFormatConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("NumberDisplayFormatConfiguration") is not None:
        import capo_quicksight.types.number_display_format_configuration

        out["number_display_format_configuration"] = (
            capo_quicksight.types.number_display_format_configuration.deserialize_json(
                data["NumberDisplayFormatConfiguration"]
            )
        )
    if data.get("PercentageDisplayFormatConfiguration") is not None:
        import capo_quicksight.types.percentage_display_format_configuration

        out["percentage_display_format_configuration"] = (
            capo_quicksight.types.percentage_display_format_configuration.deserialize_json(
                data["PercentageDisplayFormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ComparisonFormatConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "number_display_format_configuration" in value:
        import capo_quicksight.types.number_display_format_configuration

        out["number_display_format_configuration"] = (
            capo_quicksight.types.number_display_format_configuration.redact_sensitive(
                value["number_display_format_configuration"]
            )
        )
    if "percentage_display_format_configuration" in value:
        import capo_quicksight.types.percentage_display_format_configuration

        out["percentage_display_format_configuration"] = (
            capo_quicksight.types.percentage_display_format_configuration.redact_sensitive(
                value["percentage_display_format_configuration"]
            )
        )
    return out
