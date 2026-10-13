"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIcon``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_custom_icon_condition
    import capo_quicksight.types.conditional_formatting_icon_set


class ConditionalFormattingIcon(TypedDict, closed=True):
    icon_set: NotRequired[
        "capo_quicksight.types.conditional_formatting_icon_set.ConditionalFormattingIconSet"
    ]
    """<p>Formatting configuration for icon set.</p>"""
    custom_condition: NotRequired[
        "capo_quicksight.types.conditional_formatting_custom_icon_condition.ConditionalFormattingCustomIconCondition"
    ]
    """<p>Determines the custom condition for an icon set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingIcon) -> dict:
    out: dict = {}
    if "icon_set" in value:
        import capo_quicksight.types.conditional_formatting_icon_set

        out["IconSet"] = (
            capo_quicksight.types.conditional_formatting_icon_set.serialize_json(
                value["icon_set"]
            )
        )
    if "custom_condition" in value:
        import capo_quicksight.types.conditional_formatting_custom_icon_condition

        out["CustomCondition"] = (
            capo_quicksight.types.conditional_formatting_custom_icon_condition.serialize_json(
                value["custom_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingIcon:
    out: ConditionalFormattingIcon = {}  # type: ignore[typeddict-item]
    if data.get("IconSet") is not None:
        import capo_quicksight.types.conditional_formatting_icon_set

        out["icon_set"] = (
            capo_quicksight.types.conditional_formatting_icon_set.deserialize_json(
                data["IconSet"]
            )
        )
    if data.get("CustomCondition") is not None:
        import capo_quicksight.types.conditional_formatting_custom_icon_condition

        out["custom_condition"] = (
            capo_quicksight.types.conditional_formatting_custom_icon_condition.deserialize_json(
                data["CustomCondition"]
            )
        )
    return out


def redact_sensitive(value: ConditionalFormattingIcon) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "icon_set" in value:
        import capo_quicksight.types.conditional_formatting_icon_set

        out["icon_set"] = (
            capo_quicksight.types.conditional_formatting_icon_set.redact_sensitive(
                value["icon_set"]
            )
        )
    if "custom_condition" in value:
        import capo_quicksight.types.conditional_formatting_custom_icon_condition

        out["custom_condition"] = (
            capo_quicksight.types.conditional_formatting_custom_icon_condition.redact_sensitive(
                value["custom_condition"]
            )
        )
    return out
