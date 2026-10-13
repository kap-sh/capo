"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapConditionalFormattingOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.filled_map_shape_conditional_formatting


class FilledMapConditionalFormattingOption(TypedDict, closed=True):
    shape: "capo_quicksight.types.filled_map_shape_conditional_formatting.FilledMapShapeConditionalFormatting"
    """<p>The conditional formatting that determines the shape of the filled map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapConditionalFormattingOption) -> dict:
    out: dict = {}
    import capo_quicksight.types.filled_map_shape_conditional_formatting

    out["Shape"] = (
        capo_quicksight.types.filled_map_shape_conditional_formatting.serialize_json(
            value["shape"]
        )
    )
    return out


def deserialize_json(data: dict) -> FilledMapConditionalFormattingOption:
    out: FilledMapConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if data.get("Shape") is not None:
        import capo_quicksight.types.filled_map_shape_conditional_formatting

        out["shape"] = (
            capo_quicksight.types.filled_map_shape_conditional_formatting.deserialize_json(
                data["Shape"]
            )
        )
    else:
        raise DeserializationError(
            "FilledMapConditionalFormattingOption.shape required"
        )
    return out


def redact_sensitive(value: FilledMapConditionalFormattingOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "shape" in value:
        import capo_quicksight.types.filled_map_shape_conditional_formatting

        out["shape"] = (
            capo_quicksight.types.filled_map_shape_conditional_formatting.redact_sensitive(
                value["shape"]
            )
        )
    return out
