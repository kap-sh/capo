"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filled_map_conditional_formatting_option_list


class FilledMapConditionalFormatting(TypedDict, closed=True):
    conditional_formatting_options: "capo_quicksight.types.filled_map_conditional_formatting_option_list.FilledMapConditionalFormattingOptionList"
    """<p>Conditional formatting options of a <code>FilledMapVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapConditionalFormatting) -> dict:
    out: dict = {}
    import capo_quicksight.types.filled_map_conditional_formatting_option_list

    out["ConditionalFormattingOptions"] = (
        capo_quicksight.types.filled_map_conditional_formatting_option_list.serialize_json(
            value["conditional_formatting_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> FilledMapConditionalFormatting:
    out: FilledMapConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("ConditionalFormattingOptions") is not None:
        import capo_quicksight.types.filled_map_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            capo_quicksight.types.filled_map_conditional_formatting_option_list.deserialize_json(
                data["ConditionalFormattingOptions"]
            )
        )
    else:
        out["conditional_formatting_options"] = []
    return out


def redact_sensitive(value: FilledMapConditionalFormatting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conditional_formatting_options" in value:
        import capo_quicksight.types.filled_map_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            capo_quicksight.types.filled_map_conditional_formatting_option_list.redact_sensitive(
                value["conditional_formatting_options"]
            )
        )
    return out
