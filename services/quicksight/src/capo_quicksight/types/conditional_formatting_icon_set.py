"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIconSet``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_icon_set_type
    import capo_quicksight.types.expression


class ConditionalFormattingIconSet(TypedDict, closed=True):
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The expression that determines the formatting configuration for the icon set.</p>"""
    icon_set_type: NotRequired[
        "capo_quicksight.types.conditional_formatting_icon_set_type.ConditionalFormattingIconSetType"
    ]
    """<p>Determines the icon set type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingIconSet) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    if "icon_set_type" in value:
        import capo_quicksight.types.conditional_formatting_icon_set_type

        out["IconSetType"] = (
            capo_quicksight.types.conditional_formatting_icon_set_type.serialize_json(
                value["icon_set_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingIconSet:
    out: ConditionalFormattingIconSet = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    if data.get("IconSetType") is not None:
        import capo_quicksight.types.conditional_formatting_icon_set_type

        out["icon_set_type"] = (
            capo_quicksight.types.conditional_formatting_icon_set_type.deserialize_json(
                data["IconSetType"]
            )
        )
    return out


def redact_sensitive(value: ConditionalFormattingIconSet) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
