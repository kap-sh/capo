"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualHighlightOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visual_highlight_trigger


class VisualHighlightOperation(TypedDict, closed=True):
    trigger: "capo_quicksight.types.visual_highlight_trigger.VisualHighlightTrigger"
    """<p>Specifies whether a highlight operation is initiated by a click or hover, or whether it's disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualHighlightOperation) -> dict:
    out: dict = {}
    import capo_quicksight.types.visual_highlight_trigger

    out["Trigger"] = capo_quicksight.types.visual_highlight_trigger.serialize_json(
        value["trigger"]
    )
    return out


def deserialize_json(data: dict) -> VisualHighlightOperation:
    out: VisualHighlightOperation = {}  # type: ignore[typeddict-item]
    if data.get("Trigger") is not None:
        import capo_quicksight.types.visual_highlight_trigger

        out["trigger"] = (
            capo_quicksight.types.visual_highlight_trigger.deserialize_json(
                data["Trigger"]
            )
        )
    else:
        import typing

        out["trigger"] = typing.cast(
            "capo_quicksight.types.visual_highlight_trigger.VisualHighlightTrigger", ""
        )
    return out
