"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingGradientColor``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.expression
    import capo_quicksight.types.gradient_color


class ConditionalFormattingGradientColor(TypedDict, closed=True):
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The expression that determines the formatting configuration for gradient color.</p>"""
    color: "capo_quicksight.types.gradient_color.GradientColor"
    """<p>Determines the color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingGradientColor) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    import capo_quicksight.types.gradient_color

    out["Color"] = capo_quicksight.types.gradient_color.serialize_json(value["color"])
    return out


def deserialize_json(data: dict) -> ConditionalFormattingGradientColor:
    out: ConditionalFormattingGradientColor = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError(
            "ConditionalFormattingGradientColor.expression required"
        )
    if data.get("Color") is not None:
        import capo_quicksight.types.gradient_color

        out["color"] = capo_quicksight.types.gradient_color.deserialize_json(
            data["Color"]
        )
    else:
        raise DeserializationError("ConditionalFormattingGradientColor.color required")
    return out


def redact_sensitive(value: ConditionalFormattingGradientColor) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
