"""Generated from Smithy shape ``com.amazonaws.quicksight#UnaggregatedField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.field_id
    import capo_quicksight.types.format_configuration


class UnaggregatedField(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>UnaggregatedField</code>.</p>"""
    format_configuration: NotRequired[
        "capo_quicksight.types.format_configuration.FormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnaggregatedField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "format_configuration" in value:
        import capo_quicksight.types.format_configuration

        out["FormatConfiguration"] = (
            capo_quicksight.types.format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UnaggregatedField:
    out: UnaggregatedField = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("UnaggregatedField.field_id required")
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("UnaggregatedField.column required")
    if data.get("FormatConfiguration") is not None:
        import capo_quicksight.types.format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UnaggregatedField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "format_configuration" in value:
        import capo_quicksight.types.format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.format_configuration.redact_sensitive(
                value["format_configuration"]
            )
        )
    return out
