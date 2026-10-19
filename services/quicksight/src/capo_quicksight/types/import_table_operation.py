"""Generated from Smithy shape ``com.amazonaws.quicksight#ImportTableOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.import_table_operation_source
    import capo_quicksight.types.transform_operation_alias


class ImportTableOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: (
        "capo_quicksight.types.import_table_operation_source.ImportTableOperationSource"
    )
    """<p>The source configuration that specifies which source table to import and any column mappings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTableOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.import_table_operation_source

    out["Source"] = capo_quicksight.types.import_table_operation_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> ImportTableOperation:
    out: ImportTableOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("Source") is not None:
        import capo_quicksight.types.import_table_operation_source

        out["source"] = (
            capo_quicksight.types.import_table_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("ImportTableOperation.source required")
    return out
