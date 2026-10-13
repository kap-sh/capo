"""Generated from Smithy shape ``com.amazonaws.quicksight#PercentageDisplayFormatConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.decimal_places_configuration
    import capo_quicksight.types.negative_value_configuration
    import capo_quicksight.types.null_value_format_configuration
    import capo_quicksight.types.numeric_separator_configuration
    import capo_quicksight.types.prefix
    import capo_quicksight.types.suffix


class PercentageDisplayFormatConfiguration(TypedDict, closed=True):
    prefix: NotRequired["capo_quicksight.types.prefix.Prefix"]
    """<p>Determines the prefix value of the percentage format.</p>"""
    suffix: NotRequired["capo_quicksight.types.suffix.Suffix"]
    """<p>Determines the suffix value of the percentage format.</p>"""
    separator_configuration: NotRequired[
        "capo_quicksight.types.numeric_separator_configuration.NumericSeparatorConfiguration"
    ]
    """<p>The options that determine the numeric separator configuration.</p>"""
    decimal_places_configuration: NotRequired[
        "capo_quicksight.types.decimal_places_configuration.DecimalPlacesConfiguration"
    ]
    """<p>The option that determines the decimal places configuration.</p>"""
    negative_value_configuration: NotRequired[
        "capo_quicksight.types.negative_value_configuration.NegativeValueConfiguration"
    ]
    """<p>The options that determine the negative value configuration.</p>"""
    null_value_format_configuration: NotRequired[
        "capo_quicksight.types.null_value_format_configuration.NullValueFormatConfiguration"
    ]
    """<p>The options that determine the null value format configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PercentageDisplayFormatConfiguration) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "suffix" in value:
        out["Suffix"] = value["suffix"]
    if "separator_configuration" in value:
        import capo_quicksight.types.numeric_separator_configuration

        out["SeparatorConfiguration"] = (
            capo_quicksight.types.numeric_separator_configuration.serialize_json(
                value["separator_configuration"]
            )
        )
    if "decimal_places_configuration" in value:
        import capo_quicksight.types.decimal_places_configuration

        out["DecimalPlacesConfiguration"] = (
            capo_quicksight.types.decimal_places_configuration.serialize_json(
                value["decimal_places_configuration"]
            )
        )
    if "negative_value_configuration" in value:
        import capo_quicksight.types.negative_value_configuration

        out["NegativeValueConfiguration"] = (
            capo_quicksight.types.negative_value_configuration.serialize_json(
                value["negative_value_configuration"]
            )
        )
    if "null_value_format_configuration" in value:
        import capo_quicksight.types.null_value_format_configuration

        out["NullValueFormatConfiguration"] = (
            capo_quicksight.types.null_value_format_configuration.serialize_json(
                value["null_value_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PercentageDisplayFormatConfiguration:
    out: PercentageDisplayFormatConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("Suffix") is not None:
        out["suffix"] = data["Suffix"]
    if data.get("SeparatorConfiguration") is not None:
        import capo_quicksight.types.numeric_separator_configuration

        out["separator_configuration"] = (
            capo_quicksight.types.numeric_separator_configuration.deserialize_json(
                data["SeparatorConfiguration"]
            )
        )
    if data.get("DecimalPlacesConfiguration") is not None:
        import capo_quicksight.types.decimal_places_configuration

        out["decimal_places_configuration"] = (
            capo_quicksight.types.decimal_places_configuration.deserialize_json(
                data["DecimalPlacesConfiguration"]
            )
        )
    if data.get("NegativeValueConfiguration") is not None:
        import capo_quicksight.types.negative_value_configuration

        out["negative_value_configuration"] = (
            capo_quicksight.types.negative_value_configuration.deserialize_json(
                data["NegativeValueConfiguration"]
            )
        )
    if data.get("NullValueFormatConfiguration") is not None:
        import capo_quicksight.types.null_value_format_configuration

        out["null_value_format_configuration"] = (
            capo_quicksight.types.null_value_format_configuration.deserialize_json(
                data["NullValueFormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: PercentageDisplayFormatConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "prefix" in value:
        out["prefix"] = "*** Sensitive Data Redacted ***"
    if "suffix" in value:
        out["suffix"] = "*** Sensitive Data Redacted ***"
    if "null_value_format_configuration" in value:
        import capo_quicksight.types.null_value_format_configuration

        out["null_value_format_configuration"] = (
            capo_quicksight.types.null_value_format_configuration.redact_sensitive(
                value["null_value_format_configuration"]
            )
        )
    return out
