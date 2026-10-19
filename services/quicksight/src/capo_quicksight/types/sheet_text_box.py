"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetTextBox``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_text_box_content
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.text_box_interaction_options


class SheetTextBox(TypedDict, closed=True):
    sheet_text_box_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier for a text box. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have text boxes that share identifiers.</p>"""
    content: NotRequired[
        "capo_quicksight.types.sheet_text_box_content.SheetTextBoxContent"
    ]
    """<p>The content that is displayed in the text box.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.text_box_interaction_options.TextBoxInteractionOptions"
    ]
    """<p>The general textbox interactions setup for a textbox.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetTextBox) -> dict:
    out: dict = {}
    out["SheetTextBoxId"] = value["sheet_text_box_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "interactions" in value:
        import capo_quicksight.types.text_box_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.text_box_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetTextBox:
    out: SheetTextBox = {}  # type: ignore[typeddict-item]
    if data.get("SheetTextBoxId") is not None:
        out["sheet_text_box_id"] = data["SheetTextBoxId"]
    else:
        out["sheet_text_box_id"] = ""
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Interactions") is not None:
        import capo_quicksight.types.text_box_interaction_options

        out["interactions"] = (
            capo_quicksight.types.text_box_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
