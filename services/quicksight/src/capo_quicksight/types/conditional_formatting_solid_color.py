"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingSolidColor``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.expression
    import capo_quicksight.types.hex_color


class ConditionalFormattingSolidColor(TypedDict, closed=True):
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The expression that determines the formatting configuration for solid color.</p>"""
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingSolidColor) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    if "color" in value:
        out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> ConditionalFormattingSolidColor:
    out: ConditionalFormattingSolidColor = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    return out


def redact_sensitive(value: ConditionalFormattingSolidColor) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
