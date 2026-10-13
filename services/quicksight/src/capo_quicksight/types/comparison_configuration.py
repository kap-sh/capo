"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.comparison_format_configuration
    import capo_quicksight.types.comparison_method


class ComparisonConfiguration(TypedDict, closed=True):
    comparison_method: NotRequired[
        "capo_quicksight.types.comparison_method.ComparisonMethod"
    ]
    """<p>The method of the comparison. Choose from the following options:</p> <ul> <li> <p> <code>DIFFERENCE</code> </p> </li> <li> <p> <code>PERCENT_DIFFERENCE</code> </p> </li> <li> <p> <code>PERCENT</code> </p> </li> </ul>"""
    comparison_format: NotRequired[
        "capo_quicksight.types.comparison_format_configuration.ComparisonFormatConfiguration"
    ]
    """<p>The format of the comparison.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonConfiguration) -> dict:
    out: dict = {}
    if "comparison_method" in value:
        import capo_quicksight.types.comparison_method

        out["ComparisonMethod"] = (
            capo_quicksight.types.comparison_method.serialize_json(
                value["comparison_method"]
            )
        )
    if "comparison_format" in value:
        import capo_quicksight.types.comparison_format_configuration

        out["ComparisonFormat"] = (
            capo_quicksight.types.comparison_format_configuration.serialize_json(
                value["comparison_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComparisonConfiguration:
    out: ComparisonConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ComparisonMethod") is not None:
        import capo_quicksight.types.comparison_method

        out["comparison_method"] = (
            capo_quicksight.types.comparison_method.deserialize_json(
                data["ComparisonMethod"]
            )
        )
    if data.get("ComparisonFormat") is not None:
        import capo_quicksight.types.comparison_format_configuration

        out["comparison_format"] = (
            capo_quicksight.types.comparison_format_configuration.deserialize_json(
                data["ComparisonFormat"]
            )
        )
    return out


def redact_sensitive(value: ComparisonConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comparison_format" in value:
        import capo_quicksight.types.comparison_format_configuration

        out["comparison_format"] = (
            capo_quicksight.types.comparison_format_configuration.redact_sensitive(
                value["comparison_format"]
            )
        )
    return out
