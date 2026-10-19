"""Generated from Smithy shape ``com.amazonaws.quicksight#DateDimensionField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.date_time_format_configuration
    import capo_quicksight.types.field_id
    import capo_quicksight.types.hierarchy_id
    import capo_quicksight.types.time_granularity


class DateDimensionField(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>DateDimensionField</code>.</p>"""
    date_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The date granularity of the <code>DateDimensionField</code>. Choose one of the following options:</p> <ul> <li> <p> <code>YEAR</code> </p> </li> <li> <p> <code>QUARTER</code> </p> </li> <li> <p> <code>MONTH</code> </p> </li> <li> <p> <code>WEEK</code> </p> </li> <li> <p> <code>DAY</code> </p> </li> <li> <p> <code>HOUR</code> </p> </li> <li> <p> <code>MINUTE</code> </p> </li> <li> <p> <code>SECOND</code> </p> </li> <li> <p> <code>MILLISECOND</code> </p> </li> </ul>"""
    hierarchy_id: NotRequired["capo_quicksight.types.hierarchy_id.HierarchyId"]
    """<p>The custom hierarchy ID.</p>"""
    format_configuration: NotRequired[
        "capo_quicksight.types.date_time_format_configuration.DateTimeFormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateDimensionField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "date_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["DateGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["date_granularity"]
        )
    if "hierarchy_id" in value:
        out["HierarchyId"] = value["hierarchy_id"]
    if "format_configuration" in value:
        import capo_quicksight.types.date_time_format_configuration

        out["FormatConfiguration"] = (
            capo_quicksight.types.date_time_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateDimensionField:
    out: DateDimensionField = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("DateDimensionField.column required")
    if data.get("DateGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["date_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["DateGranularity"]
            )
        )
    if data.get("HierarchyId") is not None:
        out["hierarchy_id"] = data["HierarchyId"]
    if data.get("FormatConfiguration") is not None:
        import capo_quicksight.types.date_time_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.date_time_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out


def redact_sensitive(value: DateDimensionField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "format_configuration" in value:
        import capo_quicksight.types.date_time_format_configuration

        out["format_configuration"] = (
            capo_quicksight.types.date_time_format_configuration.redact_sensitive(
                value["format_configuration"]
            )
        )
    return out
