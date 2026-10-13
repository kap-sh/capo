"""Generated from Smithy shape ``com.amazonaws.quicksight#NumberFormatConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.numeric_format_configuration


class NumberFormatConfiguration(TypedDict, closed=True):
    format_configuration: NotRequired[
        "capo_quicksight.types.numeric_format_configuration.NumericFormatConfiguration"
    ]
    """<p>The options that determine the numeric format configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberFormatConfiguration) -> dict:
    out: dict = {}
    if "format_configuration" in value:
        import capo_quicksight.types.numeric_format_configuration

        out["FormatConfiguration"] = (
            capo_quicksight.types.numeric_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumberFormatConfiguration:
    out: NumberFormatConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FormatConfiguration") is not None:
        import capo_quicksight.types.numeric_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.numeric_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: NumberFormatConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "format_configuration" in value:
        import capo_quicksight.types.numeric_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.numeric_format_configuration.redact_sensitive(
                value["format_configuration"]
            )
        )
    return out
