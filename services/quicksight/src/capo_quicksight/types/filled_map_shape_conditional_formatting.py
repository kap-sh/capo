"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapShapeConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.shape_conditional_format


class FilledMapShapeConditionalFormatting(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID of the filled map shape.</p>"""
    format: NotRequired[
        "capo_quicksight.types.shape_conditional_format.ShapeConditionalFormat"
    ]
    """<p>The conditional formatting that determines the background color of a filled map's shape.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapShapeConditionalFormatting) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "format" in value:
        import capo_quicksight.types.shape_conditional_format

        out["Format"] = capo_quicksight.types.shape_conditional_format.serialize_json(
            value["format"]
        )
    return out


def deserialize_json(data: dict) -> FilledMapShapeConditionalFormatting:
    out: FilledMapShapeConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError(
            "FilledMapShapeConditionalFormatting.field_id required"
        )
    if data.get("Format") is not None:
        import capo_quicksight.types.shape_conditional_format

        out["format"] = capo_quicksight.types.shape_conditional_format.deserialize_json(
            data["Format"]
        )
    return out


def redact_sensitive(value: FilledMapShapeConditionalFormatting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "format" in value:
        import capo_quicksight.types.shape_conditional_format

        out["format"] = capo_quicksight.types.shape_conditional_format.redact_sensitive(
            value["format"]
        )
    return out
