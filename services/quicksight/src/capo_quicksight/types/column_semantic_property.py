"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSemanticProperty``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.additional_notes
    import capo_quicksight.types.column_description
    import capo_quicksight.types.column_semantic_type


class ColumnSemanticProperty(TypedDict, closed=True):
    description: NotRequired[
        "capo_quicksight.types.column_description.ColumnDescription"
    ]
    """<p>A description of the column.</p>"""
    additional_notes: NotRequired[
        "capo_quicksight.types.additional_notes.AdditionalNotes"
    ]
    """<p>Additional notes for the column.</p>"""
    semantic_type: NotRequired[
        "capo_quicksight.types.column_semantic_type.ColumnSemanticType"
    ]
    """<p>The semantic type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSemanticProperty) -> dict:
    out: dict = {}
    if "description" in value:
        import capo_quicksight.types.column_description

        out["Description"] = capo_quicksight.types.column_description.serialize_json(
            value["description"]
        )
    if "additional_notes" in value:
        import capo_quicksight.types.additional_notes

        out["AdditionalNotes"] = capo_quicksight.types.additional_notes.serialize_json(
            value["additional_notes"]
        )
    if "semantic_type" in value:
        import capo_quicksight.types.column_semantic_type

        out["SemanticType"] = capo_quicksight.types.column_semantic_type.serialize_json(
            value["semantic_type"]
        )
    return out


def deserialize_json(data: dict) -> ColumnSemanticProperty:
    out: ColumnSemanticProperty = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        import capo_quicksight.types.column_description

        out["description"] = capo_quicksight.types.column_description.deserialize_json(
            data["Description"]
        )
    if data.get("AdditionalNotes") is not None:
        import capo_quicksight.types.additional_notes

        out["additional_notes"] = (
            capo_quicksight.types.additional_notes.deserialize_json(
                data["AdditionalNotes"]
            )
        )
    if data.get("SemanticType") is not None:
        import capo_quicksight.types.column_semantic_type

        out["semantic_type"] = (
            capo_quicksight.types.column_semantic_type.deserialize_json(
                data["SemanticType"]
            )
        )
    return out


def redact_sensitive(value: ColumnSemanticProperty) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        import capo_quicksight.types.column_description

        out["description"] = capo_quicksight.types.column_description.redact_sensitive(
            value["description"]
        )
    if "additional_notes" in value:
        import capo_quicksight.types.additional_notes

        out["additional_notes"] = (
            capo_quicksight.types.additional_notes.redact_sensitive(
                value["additional_notes"]
            )
        )
    return out
