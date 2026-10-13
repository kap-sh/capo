"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathLabelType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.field_value
    import capo_quicksight.types.visibility


class DataPathLabelType(TypedDict, closed=True):
    field_id: NotRequired["capo_quicksight.types.field_id.FieldId"]
    """<p>The field ID of the field that the data label needs to be applied to.</p>"""
    field_value: NotRequired["capo_quicksight.types.field_value.FieldValue"]
    """<p>The actual value of the field that is labeled.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the data label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPathLabelType) -> dict:
    out: dict = {}
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> DataPathLabelType:
    out: DataPathLabelType = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    if data.get("FieldValue") is not None:
        out["field_value"] = data["FieldValue"]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out


def redact_sensitive(value: DataPathLabelType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_value" in value:
        out["field_value"] = "*** Sensitive Data Redacted ***"
    return out
