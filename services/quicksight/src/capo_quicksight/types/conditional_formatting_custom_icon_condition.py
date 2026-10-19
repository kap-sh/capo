"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingCustomIconCondition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_custom_icon_options
    import capo_quicksight.types.conditional_formatting_icon_display_configuration
    import capo_quicksight.types.expression
    import capo_quicksight.types.hex_color


class ConditionalFormattingCustomIconCondition(TypedDict, closed=True):
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The expression that determines the condition of the icon set.</p>"""
    icon_options: "capo_quicksight.types.conditional_formatting_custom_icon_options.ConditionalFormattingCustomIconOptions"
    """<p>Custom icon options for an icon set.</p>"""
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color of the icon.</p>"""
    display_configuration: NotRequired[
        "capo_quicksight.types.conditional_formatting_icon_display_configuration.ConditionalFormattingIconDisplayConfiguration"
    ]
    """<p>Determines the icon display configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingCustomIconCondition) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    import capo_quicksight.types.conditional_formatting_custom_icon_options

    out["IconOptions"] = (
        capo_quicksight.types.conditional_formatting_custom_icon_options.serialize_json(
            value["icon_options"]
        )
    )
    if "color" in value:
        out["Color"] = value["color"]
    if "display_configuration" in value:
        import capo_quicksight.types.conditional_formatting_icon_display_configuration

        out["DisplayConfiguration"] = (
            capo_quicksight.types.conditional_formatting_icon_display_configuration.serialize_json(
                value["display_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingCustomIconCondition:
    out: ConditionalFormattingCustomIconCondition = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    if data.get("IconOptions") is not None:
        import capo_quicksight.types.conditional_formatting_custom_icon_options

        out["icon_options"] = (
            capo_quicksight.types.conditional_formatting_custom_icon_options.deserialize_json(
                data["IconOptions"]
            )
        )
    else:
        raise DeserializationError(
            "ConditionalFormattingCustomIconCondition.icon_options required"
        )
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    if data.get("DisplayConfiguration") is not None:
        import capo_quicksight.types.conditional_formatting_icon_display_configuration

        out["display_configuration"] = (
            capo_quicksight.types.conditional_formatting_icon_display_configuration.deserialize_json(
                data["DisplayConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ConditionalFormattingCustomIconCondition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
